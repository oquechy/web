import cv2
import os.path
from pathlib import Path


def cv2_size(got, min_r, min_c):
    prefix = os.path.join("test", "out")

    r, c, _ = got.shape
    if r > min_r and c > min_c:
        return

    path = os.path.join(prefix, "small" + str(hash(str(got))) + ".jpg")
    Path(prefix).mkdir(parents=True, exist_ok=True)

    cv2.imwrite(path, got)
    assert r > min_r and c > min_c, "too small: " + path


def cv2_eq(got, want):
    prefix = os.path.join("test", "out")

    if got.shape != want.shape:
        Path(prefix).mkdir(parents=True, exist_ok=True)
        pathgot = os.path.join(prefix, "got" + str(hash(str(got))) + ".jpg")
        cv2.imwrite(pathgot, got)
        pathwant = os.path.join(prefix, "want" + str(hash(str(want))) + ".jpg")
        cv2.imwrite(pathwant, want)
        assert got.shape == want.shape, "got: " + pathgot + ", " \
            + "want: " + pathwant

    difference = cv2.subtract(got, want)

    conv_hsv_gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(conv_hsv_gray, 0, 255,
                            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    difference[mask != 255] = [0, 0, 255]

    similarity = 1 - (difference.sum(axis=-1) > 0).mean()

    if similarity > 0.6:
        return

    out = cv2.vconcat([got, want, difference])
    path = os.path.join(prefix, "diff" + str(hash(str(out))) + ".jpg")

    Path(prefix).mkdir(parents=True, exist_ok=True)
    cv2.imwrite(path, out)
    assert similarity > 0.6, "diff: " + path

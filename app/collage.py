import cv2
import numpy as np
import os
from pathlib import Path


def same_w(im_list, interpolation=cv2.INTER_LINEAR_EXACT):
    w_max = max(im.shape[1] for im in im_list)
    return [cv2.resize(im,
                       (w_max, int(im.shape[0]
                                   * w_max / im.shape[1])),
                       interpolation=interpolation)
            for im in im_list]


def same_h(im_list, interpolation=cv2.INTER_LINEAR_EXACT):
    h_max = max(im.shape[0] for im in im_list)
    return [cv2.resize(im,
                       (int(im.shape[1] * h_max / im.shape[0]),
                        h_max),
                       interpolation=interpolation)
            for im in im_list]


def remove_alpha(pic):
    image = cv2.imread(pic, cv2.IMREAD_UNCHANGED)
    if image.shape[2] < 4:
        return image
    trans_mask = image[:, :, 3] == 0
    image[trans_mask] = [255, 255, 255, 255]
    return cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)


def img_hash(img):
    hash(str(img))


def make_collage(pics):
    im_list = [remove_alpha(p) for p in pics]
    im_list_grid = np.array_split(im_list,
                                  (len(im_list) + 2) // 3)
    im_cols = [cv2.vconcat(same_w(col)) for col in im_list_grid]
    return cv2.hconcat(same_h(im_cols))


def save_collage(pic, prefix):
    Path(prefix).mkdir(parents=True, exist_ok=True)
    path = os.path.join(prefix, str(hash(str(pic))) + ".jpg")
    cv2.imwrite(path, pic)
    return path

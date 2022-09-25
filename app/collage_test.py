import cv2

import random

from os.path import join

from . import db
from . import helper

from .collage import same_w, same_h, remove_alpha, make_collage, save_collage


def test_same_w():
    im_list = [cv2.imread(im) for im in db.shoes()[:4]]
    got = same_w(im_list)

    prefix = join("test", "canonic")
    want = [
        join(prefix, "same_w1.jpg"),
        join(prefix, "same_w2.jpg"),
        join(prefix, "same_w3.jpg"),
        join(prefix, "same_w4.jpg"),
    ]
    assert len(got) == len(want)
    for i in range(len(got)):
        helper.cv2_eq(got[i], cv2.imread(want[i]))


def test_same_h():
    im_list = [cv2.imread(im) for im in db.shoes()[:4]]
    got = same_h(im_list)

    prefix = join("test", "canonic")
    want = [
        join(prefix, "same_h1.jpg"),
        join(prefix, "same_h2.jpg"),
        join(prefix, "same_h3.jpg"),
        join(prefix, "same_h4.jpg"),
    ]

    assert len(got) == len(want)
    for i in range(len(got)):
        helper.cv2_eq(got[i], cv2.imread(want[i]))


def test_remove_alpha_has_alpha():
    got = remove_alpha(join("images", "top", "3.png"))
    want = cv2.imread(join("test", "canonic", "has_alpha.jpg"))
    helper.cv2_eq(got, want)


def test_remove_alpha_no_alpha():
    got = remove_alpha(join("images", "top", "4.webp"))
    want = cv2.imread(join("images", "top", "4.webp"))
    helper.cv2_eq(got, want)


def test_make_collage_1_pic():
    got = make_collage([db.top()[0]])
    want = cv2.imread(join("images", "top", "1.png"))
    helper.cv2_eq(got, want)


def test_make_collage_4_pics():
    got = make_collage(db.shoes()[:4])
    want = cv2.imread(join("test", "canonic", "make_collage_4.jpg"))
    helper.cv2_eq(got, want)


def test_save_collage_dir_doesnt_exist():
    want = cv2.imread(join("images", "top", "1.png"))
    got = save_collage(want, join(
        "test", "out", str(random.randrange(2**64)),
        str(random.randrange(2**64))))
    helper.cv2_eq(cv2.imread(got), want)


def test_save_collage_dir_exists():
    want = cv2.imread(join("images", "top", "1.png"))
    got = save_collage(want, join("test", "out"))
    helper.cv2_eq(cv2.imread(got), want)

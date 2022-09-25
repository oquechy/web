import os
from itertools import chain


def summer_looks():
    return len(top()) * len(bottom()) * len(shoes())


def winter_looks():
    return summer_looks() * len(outwear()) * len(hats())


def closet():
    return list(chain(top(),
                      bottom(),
                      hats(),
                      bags(),
                      shoes(),
                      accessories(),
                      outwear(),
                      ))


def pics(dir):
    exts = ("jpg", "jpeg", "png", "webp")
    files = os.listdir(os.path.join("images", dir))
    ps = [os.path.join("images", dir, f)
          for f in files if f.lower().endswith(exts)]
    ps.sort()
    return ps


def top():
    return pics("top")


def bottom():
    return pics("bottom")


def outwear():
    return pics("outwear")


def hats():
    return pics("hats")


def bags():
    return pics("bags")


def shoes():
    return pics("shoes")


def accessories():
    return pics("accessories")

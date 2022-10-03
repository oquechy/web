import os
from itertools import chain


def summer_looks() -> int:
    """Counts the number of summer looks in the wardrobe.

    Returns:
        int: Number of tops * number of bottoms * number of pairs of shoes.
    """
    return len(top()) * len(bottom()) * len(shoes())


def winter_looks() -> int:
    """Counts the number of summer looks in the wardrobe.

    Returns:
        int: Number of tops * number of bottoms * number of pairs of shoes 
            * number of outwear pieces * number of hats.
    """
    return summer_looks() * len(outwear()) * len(hats())


def closet() -> list[str]:
    """Returns the list of items in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return list(chain(top(),
                      bottom(),
                      hats(),
                      bags(),
                      shoes(),
                      accessories(),
                      outwear(),
                      ))


def pics(dir: str) -> list[str]:
    """Returns image files in a specified subdirectory of "images" folder.

    Args:
        dir (str): Subdirectory name.

    Returns:
        list[str]: List of files in "images/<dir>" that end in ".jpg", ".jpeg",
         ".png", or ".webp".
    """
    exts = (".jpg", ".jpeg", ".png", ".webp")
    files = os.listdir(os.path.join("images", dir))
    ps = [os.path.join("images", dir, f)
          for f in files if f.lower().endswith(exts)]
    ps.sort()
    return ps


def top() -> list[str]:
    """Returns list of tops in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return pics("top")


def bottom() -> list[str]:
    """Returns list of bottoms in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return pics("bottom")


def outwear() -> list[str]:
    """Returns list of outwear pieces in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return pics("outwear")


def hats() -> list[str]:
    """Returns list of hats in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return pics("hats")


def bags() -> list[str]:
    """Returns list of bags in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return pics("bags")


def shoes() -> list[str]:
    """Returns list of pairs of shoes in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return pics("shoes")


def accessories() -> list[str]:
    """Returns list of accessories in the wardrobe.

    Returns:
        list[str]: Image file paths.
    """
    return pics("accessories")

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from enum import Enum


import app.db as db

from app.log import Level, log

router = APIRouter()


class ItemType(str, Enum):
    top = "top"
    bottom = "bottom"
    shoes = "shoes"
    hats = "hats"
    bags = "bags"
    outwear = "outwear"
    accessories = "accessories"


def at_index(items: list[str], item_id: int) -> FileResponse:
    """Performs checked indexing of the list of images.

    Args:
        items (list[str]): List of image files.
        item_id (int): Index.

    Raises:
        HTTPException: Status 422. List out of bounds error.

    Returns:
        FileResponse: Image.
    """
    n = len(items)
    if not (0 <= item_id < n):
        raise HTTPException(status_code=422,
                            detail="Expected 0 <= item_id < " + str(n)
                            + ", got: " + str(item_id))
    return FileResponse(items[item_id])


@router.get("/show/{type}/{item_id}")
async def show(type: ItemType, item_id: int) -> FileResponse:
    """Returns a wardrobe item by its type and index position.

    Args:
        type (ItemType): Can be "top", "bottom", "shoes", "hats", "bags", 
        "outwear", or "accessories".
        item_id (int): Serial number.

    Returns:
        FileResponse: Image.
    """
    log(Level.INFO, "fetch item")
    match type:
        case ItemType.top:
            return at_index(db.top(), item_id)
        case ItemType.bottom:
            return at_index(db.bottom(), item_id)
        case ItemType.shoes:
            return at_index(db.shoes(), item_id)
        case ItemType.hats:
            return at_index(db.hats(), item_id)
        case ItemType.bags:
            return at_index(db.bags(), item_id)
        case ItemType.outwear:
            return at_index(db.outwear(), item_id)
        case ItemType.accessories:
            return at_index(db.accessories(), item_id)
        case _:
            return {"unknown type": type}

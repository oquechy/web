from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from enum import Enum


import app.db as db

router = APIRouter()


class ItemType(str, Enum):
    top = "top"
    bottom = "bottom"
    shoes = "shoes"
    hats = "hats"
    bags = "bags"
    outwear = "outwear"
    accessories = "accessories"


def at_index(items, item_id):
    n = len(items)
    if not (0 <= item_id < n):
        raise HTTPException(status_code=422,
                            detail="Expected 0 <= item_id < " + str(n)
                            + ", got: " + str(item_id))
    return FileResponse(items[item_id])


@router.get("/show/{type}/{item_id}")
async def show(type: ItemType, item_id: int):
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

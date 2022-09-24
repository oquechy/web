from fastapi.responses import FileResponse

from enum import Enum

import random

import os
from pathlib import Path

from collage import make_collage, save_collage
import db

from main import app


class ItemType(str, Enum):
    top = "top"
    bottom = "bottom"
    shoes = "shoes"
    hats = "hats"
    bags = "bags"
    outwear = "outwear"
    accessories = "accessories"


@app.get("/show/{type}/{item_id}")
async def show(type: ItemType, item_id: int):
    match type:
        case ItemType.top:
            return FileResponse(db.top()[item_id])
        case ItemType.bottom:
            return FileResponse(db.bottom()[item_id])
        case ItemType.shoes:
            return FileResponse(db.shoes()[item_id])
        case ItemType.hats:
            return FileResponse(db.hats()[item_id])
        case ItemType.bags:
            return FileResponse(db.bags()[item_id])
        case ItemType.outwear:
            return FileResponse(db.outwear()[item_id])
        case _:
            return {"unknown type": type}


class Season(str, Enum):
    summer = "summer"
    winter = "winter"


@app.get("/randomize/")
async def randomize(season: Season):
    imgs = []
    match season:
        case Season.summer:
            imgs.append(random.choice(db.top()))
            imgs.append(random.choice(db.bottom()))
            imgs.append(random.choice(db.shoes()))
            imgs.extend(random.sample(db.accessories(), 2))
            imgs.append(random.choice(db.bags()))
        case Season.winter:
            imgs.append(random.choice(db.top()))
            imgs.append(random.choice(db.bottom()))
            imgs.append(random.choice(db.shoes()))
            imgs.extend(random.sample(db.accessories(), 3))
            imgs.append(random.choice(db.outwear()))
            imgs.append(random.choice(db.bags()))

        case _:
            return {"unknown season": season}

    pic = make_collage(imgs)

    prefix = os.path.join("out", "randomize")
    Path(prefix).mkdir(parents=True, exist_ok=True)

    path = save_collage(pic, prefix)
    return FileResponse(path)

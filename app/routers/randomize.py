from fastapi import APIRouter
from fastapi.responses import FileResponse

from enum import Enum

import random

import os

from app.collage import make_collage, save_collage
import app.db as db

from app.log import Level, log

router = APIRouter()


class Season(str, Enum):
    summer = "summer"
    winter = "winter"


@router.get("/randomize/")
async def randomize(season: Season) -> FileResponse:
    """Generates a random outfit for the chosen season.

    Args:
        season (Season): Can be "summer" or "winter".

    Returns:
        FileResponse: Image of the outfit.
    """
    imgs = []
    log(Level.INFO, "randomize outfit")
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
            log(Level.ERRO, "unknown season", str(season))
            return {"unknown season": season}

    pic = make_collage(imgs)

    prefix = os.path.join("out", "randomize")
    path = save_collage(pic, prefix)
    return FileResponse(path)

from fastapi.responses import FileResponse

from enum import Enum

import random

import os
from pathlib import Path

from collage import make_collage, save_collage
import db

from main import app


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

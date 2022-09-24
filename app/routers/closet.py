from fastapi import APIRouter
from fastapi.responses import FileResponse

import os
from pathlib import Path

from app.collage import make_collage, save_collage
import app.db as db

router = APIRouter()


@router.get("/closet")
async def closet():
    pic = make_collage(db.closet())

    prefix = os.path.join("out", "closet")
    Path(prefix).mkdir(parents=True, exist_ok=True)

    path = save_collage(pic, prefix)
    return FileResponse(path)

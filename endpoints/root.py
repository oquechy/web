from typing import Union

from pydantic import BaseModel

import db

from main import app


class Closet(BaseModel):
    description: Union[str, None] = None
    closet_size: int
    winter_looks: int
    summer_looks: int


@app.get("/")
async def main():
    resp = Closet(
        description="Welcome to my web closet!! (^o^)/",
        closet_size=len(db.closet()),
        summer_looks=db.summer_looks(),
        winter_looks=db.winter_looks(),
    )
    return resp

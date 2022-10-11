from fastapi import FastAPI

import app.routers as routers


app = FastAPI()

app.include_router(routers.closet.router)
app.include_router(routers.favicon.router)
app.include_router(routers.randomize.router)
app.include_router(routers.root.router)
app.include_router(routers.show.router)

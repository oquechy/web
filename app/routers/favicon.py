from fastapi import APIRouter
from fastapi.responses import FileResponse

import os.path

router = APIRouter()

favicon_path = 'favicon.ico'


@router.get('/favicon.ico')
async def favicon():
    print('get favicon', os.path.isfile(favicon_path))
    return FileResponse(favicon_path)

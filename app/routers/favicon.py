from fastapi import APIRouter
from fastapi.responses import FileResponse

import os.path

router = APIRouter()

favicon_path = 'favicon.ico'


@router.get('/favicon.ico')
async def favicon() -> FileResponse:
    """Returns the favicon.

    Returns:
        FileResponse: Image.
    """
    print('get favicon', os.path.isfile(favicon_path))
    return FileResponse(favicon_path)

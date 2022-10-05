from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.log import Level, log


router = APIRouter()

favicon_path = 'favicon.ico'


@router.get('/favicon.ico')
async def favicon() -> FileResponse:
    """Returns the favicon.

    Returns:
        FileResponse: Image.
    """
    log(Level.INFO, "fetch favicon")
    return FileResponse(favicon_path)

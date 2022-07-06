from fastapi import APIRouter, UploadFile, File, Request
from package.handlers.storage import create_archive, get_archive, get_all_archives, delete_archive
from starlette.responses import JSONResponse

files = APIRouter()

@files.post("/file")
async def create_file(req: Request , file: UploadFile = File(...)):
    archive = create_archive(file=file, uid=req.state.uid)
    return JSONResponse(archive)

@files.get("/file")
async def get_all_files(req: Request ):
    archives = get_all_archives()
    return JSONResponse(archives)

@files.get("/file/{id}")
async def get_file(req:Request, id: str):
    archive = get_archive(id)
    return JSONResponse(archive)
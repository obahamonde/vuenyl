from dotenv import load_dotenv
from os import environ
environ.clear()
load_dotenv()


from package.handlers.auth import get_token, get_user, update_avatar
from package.handlers.storage import create_archive
from package.services.fauna import Q
from fastapi import APIRouter, UploadFile, File, Request, Response, status, HTTPException
from starlette.responses import JSONResponse, RedirectResponse

user = APIRouter()

@user.get("/public/auth/")
async def auth(code:str):
    token = get_token(code)
    if token:
        return RedirectResponse(f"{environ.get('FRONT_END_URL')}/auth?token={token}")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

@user.post("/public/auth/")
async def auth(req: Request):
    user = get_user(req.headers.get("Authorization").split(" ")[1])
    if user:
        return JSONResponse(user)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

@user.post("/user/avatar")
async def updateAvatar(req:Request, file: UploadFile = File(...)):
    archive = create_archive(file=file, uid=req.state.uid)
    update_avatar(uid=req.state.uid, avatar=archive.url)
    user = Q.read("users", "uid", req.state.uid)
    return JSONResponse(user)
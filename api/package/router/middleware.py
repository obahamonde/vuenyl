from package.handlers.auth import get_uid
from fastapi import FastAPI, Request, Response, status, HTTPException
from typing import Callable

def AuthMiddleware(app: FastAPI)->FastAPI:
    @app.middleware("http")
    async def auth_middleware(request: Request, call_next: Callable)->Response:
        if "public" in request.url.path:
            return await call_next(request)
        else:
            uid = get_uid(request.headers.get("Authorization").split(" ")[1])
            if uid:
                request.state.uid = uid
                return await call_next(request)
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return app

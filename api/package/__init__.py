from fastapi import FastAPI
from package.router.contact import contact
from package.router.user import user
from package.router.file import files
from package.router.middleware import AuthMiddleware


def main():
    app = AuthMiddleware(FastAPI(
        title="E-commerce API",
        description="This is a cloud native e-commerce API",
        version="0.0.1",
        openapi_url="/public/openapi.json",
        docs_url="/public/docs",
        redoc_url="/public/redoc"
    ))
    app.include_router(contact, tags=["contact"])
    app.include_router(user, tags=["user"])
    app.include_router(files, tags=["file"])
    return app
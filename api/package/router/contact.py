from package.handlers.auth import create_contact, get_contacts, delete_contact, send_email
from package.services.fauna import Q
from package.models.schemas import Contact
from fastapi import APIRouter, Request, status, HTTPException
from starlette.responses import JSONResponse

contact = APIRouter()

@contact.post("/public")
async def send_mail(contact: Contact):
    try:
        send_email(contact)
        create_contact(contact.name, contact.email, contact.message)
        return JSONResponse({"message": "Email sent"}, status_code=status.HTTP_201_CREATED)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")

@contact.get("/contact")
async def get_all_contacts(req: Request ):
    try:
        res = Q.read("users", "uid", req.state.uid)
        if res.isAdmin:
            response = get_contacts()
            return JSONResponse(status_code=status.HTTP_200_OK, content=response)
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

@contact.delete("/contact/{email}")
async def delete_contact(req: Request, email: str ):
    try:
        res = Q.read("users", "uid", req.state.uid)
        if res.isAdmin:
            delete_contact(email)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Contact deleted"})
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
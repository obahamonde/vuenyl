from dotenv import load_dotenv
from os import environ
environ.clear()
load_dotenv()

from pydantic import HttpUrl, EmailStr

from package.services.aws import cognito, ses
from package.services.fauna import Q

from package.models.schemas import User, Contact

from requests import post

def get_token(code:str)->str:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': environ.get('COGNITO_CLIENT_ID'),
        'client_secret': environ.get('COGNITO_CLIENT_SECRET'),
        'code': code,
        'redirect_uri': environ.get('COGNITO_REDIRECT_URI')
    }
    response = post(f"{environ.get('COGNITO_URL')}/oauth2/token", headers=headers, data=data)
    return response.json()['access_token']

def get_user(token:str)->User:
    response = cognito.get_user(AccessToken=token)
    user = User(
        uid=response['UserAttributes'][0]['Value'],
        email=response['UserAttributes'][2]['Value'],
        name=response['Username'])
    try:
        res = Q.read("user", "uid", user.uid)
        return res
    except Exception:
        if user.email.endswith("@oscarbahamonde.cloud"):
            user.isAdmin = True
        res = Q.create(user)
        print(res)
        return user


def get_uid(token:str)->str:
    res = get_user(token)
    return res['uid']

def update_avatar(uid:str, avatar:HttpUrl):
    try:
        user = Q.read("users", "uid", uid)
        user.avatar = avatar
        res = Q.update("users", "uid", user.uid, user)
        return res
    except Exception:
        return None

def create_contact(name:str, email:EmailStr, message:str):
    contact = Contact(name=name, email=email, message=message)
    try:
        res = Q.read("contacts", "email", contact.email)
        if res:
            Q.update("contacts", "email", contact.email, contact)
            return contact
        else:
            res = Q.create(contact)
            return contact
    except Exception:
        return None

def get_contacts():
    try:
        res = Q.read_all("contacts",20)
        return res
    except Exception:
        return None

def get_contact(email:EmailStr):
    try:
        res = Q.read("contacts", "email", email)
        return res
    except Exception:
        return None

def delete_contact(email:EmailStr):
    try:
        res = Q.delete("contacts", "email", email)
        return res
    except Exception:
        return None

def send_email(contact:Contact):
    try:
        res = ses.send_email(
            Source=environ.get('SES_FROM_EMAIL'),
            Destination={
                'ToAddresses': ['vuenyl@oscarbahamonde.cloud','dev@oscarbahamonde.cloud'],
                'CcAddresses': [contact.email]
            },
            Message={
                'Subject': {
                    'Data': f"{contact.name}<{contact.email}> sent you a message"
                },
                'Body': {
                    'Text': {
                        'Data': contact.message
                    }
                }
            })
        return res
    except Exception:
        raise Exception("Error sending email")
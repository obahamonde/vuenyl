from dotenv import load_dotenv
from os import environ
load_dotenv()

from package.services.aws import s3
from package.services.fauna import Q
from package.models.schemas import Archive
from fastapi import UploadFile, File

from typing import List

def create_archive(uid:str, file: UploadFile = File(...)) -> Archive:
    archive = Archive(uid=uid, content_type=file.content_type, name=file.filename)
    archive.url = s3.generate_presigned_url(Bucket=environ.get("S3_BUCKET"), Key=f"{archive.uid}/{archive.mid}/{archive.name}", ExpiresIn=31536000)
    s3.put_object(Bucket=environ.get("S3_BUCKET"), Key=f"{archive.uid}/{archive.mid}/{archive.name}", Body=file.file.read(), ACL = "public-read", ContentType=archive.content_type)
    
    Q.create(archive)
    return archive

def get_archive(mid: str = ...) -> Archive:
    return Q.read("archives", "mid", id)

def get_all_archives() -> List[Archive]:
    return Q.read_all("archives", 20)

def delete_archive(mid: str = ...) -> Archive:
    return Q.delete("archives", "mid", id)
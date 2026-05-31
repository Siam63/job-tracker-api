import os
import shutil

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models import Document

UPLOAD_DIR = "storage/uploads"


def save_document(
    file: UploadFile,
    db: Session
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_type = file.filename.split(".")[-1].lower()

    document = Document(
        filename=file.filename,
        file_path=file_path,
        file_type=file_type,
        status="uploaded"
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document
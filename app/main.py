from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import Document
from app.schemas import DocumentResponse
from fastapi import UploadFile, File
from app.document_service import save_document

Base.metadata.create_all(bind=engine)

app = FastAPI(title="VectorFlow AI")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "VectorFlow AI API is running"}


@app.get("/documents", response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    return db.query(Document).all()


@app.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )

    return document


@app.put("/documents/{document_id}/status", response_model=DocumentResponse)
def update_document_status(
    document_id: int,
    new_status: str,
    db: Session = Depends(get_db)
):
    allowed_statuses = {"uploaded", "queued", "processing", "completed", "failed"}

    if new_status not in allowed_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid document status"
        )

    document = db.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )

    document.status = new_status
    db.commit()
    db.refresh(document)

    return document


@app.post(
    "/documents/upload",
    response_model=DocumentResponse
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return save_document(file, db)
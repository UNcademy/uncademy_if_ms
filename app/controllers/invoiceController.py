from sqlalchemy.orm import Session
from models.model import InvoiceDetail
from models.schemas.invoiceDetailSchema import InvoiceDetailSchema



def get_invoice_detail(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InvoiceDetail).offset(skip).limit(limit).all()

def get_invoice_detail_by_id(db: Session, invoice_detail_id: int):
    return db.query(InvoiceDetail).filter(InvoiceDetail.id == invoice_detail_id).first() 

def create_invoice_detail()

def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InvoiceDetail).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(InvoiceDetail).filter(InvoiceDetail.id == book_id).first()


def create_book(db: Session, book: InvoiceDetailSchema):
    _book = InvoiceDetail(reason=book.reason, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()


def update_book(db: Session, book_id: int, title: str, description: str):
    _book = get_book_by_id(db=db, book_id=book_id)

    _book.title = title
    _book.description = description

    db.commit()
    db.refresh(_book)
    return _book
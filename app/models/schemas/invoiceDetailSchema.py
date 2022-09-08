from cgitb import text
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class InvoiceDetailSchema(BaseModel):

    id: Optional[int] = None
    ut_payment_value: Optional[float] = None
    ut_payment_date: Optional[str] = None
    t_payment_value: Optional[float] = None
    t_payment_date: Optional[str] = None
    reason: Optional[str] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestInvoiceDetail(BaseModel):
    parameter: InvoiceDetailSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
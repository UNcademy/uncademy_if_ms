from operator import imod
from sqlalchemy import Column, Integer, Text, Float, Date
from config.config import Base

class InvoiceDetail(Base): 
    __tablename__ = 'invoice_detail'

    id=Column(Integer, primary_key=True)
    ut_payment_value=Column(Float)
    ut_payment_date=Column(Date)
    t_payment_value=Column(Float)
    t_payment_date=Column(Date)
    reason=Column(Text)
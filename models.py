from sqlalchemy import Column, Integer, String

from emp.db import Base

# model/table
class  emp(Base):
    __tablename__ = "empdetails"

    # fields 
    fname = Column(String(20),primary_key=True, index=True)
    lname = Column(String(20))
    empid = Column(String)
    city = Column(String)
    age = Column(Integer)
    contanctno = Column(Integer)
    experience = Column(Integer)



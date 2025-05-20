from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    payday = Column(Date, nullable=False)
    admin_id = Column(Integer, ForeignKey("admins.id"))
    admin = relationship("Admin", back_populates="companies")

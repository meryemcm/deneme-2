from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Staff(Base):
    __tablename__ = 'staff'
 
    id = Column(Integer, primary_key=True)
    isim = Column(String(250), nullable=False)
 
class Client(Base):
    __tablename__ = 'client'
 
    id = Column(Integer, primary_key=True)
    isim = Column(String(250), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    staff = relationship(Staff, backref='client')
 
 
# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///worksystem.db')
 
# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)
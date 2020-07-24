from decleration import Staff, Client, Base
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
engine = create_engine('sqlite:///worksystem.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
staffs = session.query(Staff).all()
print(["{} ile {} calismaktadir".format(client.isim, staff.isim) for staff in staffs for client in staff.client])
 
hasan = session.query(Staff).filter(Staff.isim=='Hasan').first()
clients = session.query(Client).filter(Client.staff==hasan).all()
ayse = session.query(Staff).filter(Staff.isim=='Ayşe').first()
clients = session.query(Client).filter(Client.staff==ayse).all()
print("Hasan çalışanına ait musteriler")
print([client.isim for client in clients])
print("Ayşe çalışanına ait musteriler")
print([client.isim for client in clients])
print(["çalışanlar:{}".format(staff.isim) for staff in staffs])

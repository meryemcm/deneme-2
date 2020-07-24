from decleration import Staff, Client, Base
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
engine = create_engine('sqlite:///worksystem.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
hasan = Staff(isim='Hasan')
session.add(hasan)
ayse = Staff(isim='Ayşe')
session.add(ayse)
session.commit()
 
client1 = Client(isim='client1', staff=hasan)
client2 = Client(isim='client2', staff=hasan)
client3 = Client(isim='client3', staff=ayse)
client4 = Client(isim='client4', staff=ayse)
 
session.add_all([client1, client2, client3,client4])
session.commit()
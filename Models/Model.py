
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship 

engine = create_engine("postgresql://devops:4linux@127.0.0.1/dexter") 
Session = sessionmaker() 
Session.configure(bind=engine) 
session = Session() 
Base = declarative_base() 

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cpf = Column(String)
    segment = Column(String)
    service = relationship("Service")

    def __init__(self,name="",cpf="",segment=""): 
        self.name = name
        self.cpf = cpf
        self.segment = segment


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)

    def __init__(self,name="",description="",image=""):
        self.name = name
        self.description = description
        self.image = image

class Service(Base):
    __tablename__ = "service"
    id = Column(Integer,primary_key=True)
    request_date = Column(String)
    cancel_date = Column(String)
    client_id = Column(Integer,ForeignKey("client.id"))
    product_id = Column(Integer,ForeignKey("product.id"))
    client = relationship("Client")
    product = relationship("Product")

    def __init__(self,request_date="",cancel_date=""):
        self.request_date = request_date
        self.cancel_date = cancel_date

    
if __name__ == '__main__':
    try:
        cliente = Client('Erick','000.000.000-01','TI')
        session.add(cliente)
        produto = Product('WebServer','WebServer for test','WebServerTest')
        session.add(produto)
        servico = Service('03/26','03/31')
        cliente.service.append(servico)
        servico.product = produto
        session.add(servico)
        session.commit()
        Base.metadata.create_all(engine) 
    except Exception as e:
        print "Erro: %s"%e
        session.rollback()

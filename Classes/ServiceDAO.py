from Models.Model import session,Service as ServiceModel,Client,Product
from Classes.Client import Client as ClientClass
from Classes.Product import Product as ProductClass
from Classes.Service import Service as ServiceClass

class ServiceDAO:
    def __init__(self,service=""):
        self.service = service

    def get(self):
        try:
            service = session.query(ServiceModel,Client,Product).join(Client,Product).filter(ServiceModel.id==self.service.id).first()
            if service is None:
                return None
        
            c = ClientClass(service.Client.name,service.Client.cpf,service.Client.segment)
            c.id = service.Client.id

            p = ProductClass(service.Product.name,service.Product.description,service.Product.image)
            p.id = service.Product.id

            s = ServiceClass(service.Service.request_date,service.Service.cancel_date)
            s.id = service.Service.id

            s.client = c
            s.product = p

            return s
        except Exception as e:
            print "Algum erro aconteceu %s"%e

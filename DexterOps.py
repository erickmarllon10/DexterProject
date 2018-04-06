from Modules.MongoOps import MongoOps
from Modules.ProvisionOps import ProvisionOps

def Start():
    mongo = MongoOps()
    print "Existem %s servicos na fila"%(mongo.getQueue().count())
    for service in mongo.getServiceToInstall():
        prov = ProvisionOps(service["_id"])
        prov.InstallService()

if __name__ == '__main__':
    Start()

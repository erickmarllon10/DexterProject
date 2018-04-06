from pymongo import MongoClient
class MongoOps:
    def __init__(self):
        self.client = MongoClient("127.0.0.1")
        self.db = self.client["dexter"]

    def getQueue(self):
        return self.db.queue.find()

    def getServiceToInstall(self):
        return self.db.queue.find({"status":0})

    def insertQueue(self):
        self.db.queue.insert({"_id":1,"status":0})

if __name__ == '__main__':
    m = MongoOps()
    m.insertQueue()

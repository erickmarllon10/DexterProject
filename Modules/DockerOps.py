from Modules.SSHOps import SSHOps

class DockerOps:
    def createContainer(self,id,image):
        command = "docker run -d -ti --name %s %s /bin/bash"%("%s_%s"%(image,id),"webservercloud")
        ssh = SSHOps()
        res = ssh.executarComandoRemoto(command)
        if res['status'] == 1:
            print res['message']

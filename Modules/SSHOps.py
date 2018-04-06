from paramiko.client import SSHClient
import paramiko

class SSHOps:
    def __init__(self):
        self.servidor = "192.168.0.2"
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.servidor, username='root', password='4linux')

    def executarComandoRemoto(self,com):
        try:
            stdin,stdout,stderr = self.ssh.exec_command(com)
            if stderr.channel.recv_exit_status() != 0:
                return {"status":1,"message":stderr.read()}
            else:
                return {"status":0,"message":stdout.read()}
        except Exception as e:
            print "Nao conseguiu se conectar ao servidor\n%s"%e

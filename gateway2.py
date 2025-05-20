#container 1:
import socket
import threading
import time
from roteamento import ler_json_bloqueado, apenasLer
from menorCaminho import dijkstra    

class ClientThread(threading.Thread):

    def __init__(self, nome, conexao, clienteAddress):

        super().__init__()
        self.nome = nome
        self.conexao = conexao
        self.clienteAddress = clienteAddress
        print(self.nome, ' conectado')
        ler_json_bloqueado('172.19.0.2', nome, 0)
        self.startEnd = threading.Event()
    
    def enviaSolicitacaoMsg(self, address, msg):
        address.send(msg.encode)

    def ajeitaMsg(self, destinos):

        dest = eval(destinos[3])
        listaDestinos = list(dest)
        del listaDestinos[0]
        return listaDestinos[0], str(destinos[0] + '-' + destinos[1] + '-' + 
                                     destinos[2] + '-' + str(tuple(listaDestinos)) + '-' + destinos[4])


    def run(self):

        while not self.startEnd.is_set():
            
            recebe = self.conexao.recv(1024)
            print('mensagem from ' + self.nome +': '+ recebe.decode())
            if recebe.decode() == 'diconnect' or recebe.decode() == '':

                self.conexao.close()
                self.startEnd.set()
                print(self.nome + ' disconnected')
                ler_json_bloqueado('172.19.0.2', self.nome, 1)
                print('Ureia')
                break
            destinos = recebe.decode().split('-')
            print(destinos)

            address, mensagemEnvio = self.ajeitaMsg(destinos)
            try:
                print('\n\n',address, mensagemEnvio,'\n\n')
                self.enviaSolicitacaoMsg(address, mensagemEnvio)
                print('Enviado')
            except:
                print('Caminho inexistente!')
            

host  = ''   #se eu deixar em branco eu vou poder aceitar conexao de qualquer lugar

port = 9002 # valores menores que 1024 sao utilizadas pelo sistema o ideial e rodar em um porta maior que > 24

addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor (deixar aberta a conexao)
serv_socket.listen(10) #define o limite de conexoes

#precisa do ip, e da porta para os computadores se comunicar

while(True):

    try:

        print('aguardando conexao...')
        con, cliente = serv_socket.accept() #servidor aguardando conexao
        print(con)
        #recebe = con.recv(1024) #define que os pacotes recebidos sao ate 1024 bytes
        #print(cliente[0])
        cliente = ClientThread(cliente[0], con, cliente)
        cliente.start()
        #enviaSolicitacaoMsg()
        #enviar = input('digite uma mensagem para enviar ao cliente: ')
        #con.send(enviar.encode()) #enviar uma mensagem para o cliente
    except:
        con, cliente = serv_socket.accept() #servidor aguardando conexao

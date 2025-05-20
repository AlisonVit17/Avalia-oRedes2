#container 1:
import socket
import threading
from roteamento import ler_json_bloqueado, apenasLer
from menorCaminho import dijkstra
from time import sleep
def receber_dados(cliente_socket):

    while(True):
        receberMsg = client_socket.recv(1024).decode()
        print('Mensagens recebidas: ', receberMsg, '\n')
        flush=True

#ip = input('digite )
ip = '172.19.0.2' #ip do servidor (ip da maquina)

#Ip da minha máquina: 192.168.1.13
#10.180.44.143
port = 9002
#port = 7001
addr = ((ip, port)) #deefine a tupla de endereco
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
client_socket.connect(addr) #realiza a conexao
sleep(2)
ip_address = client_socket.getsockname()
ler_json_bloqueado(ip_address[0], '172.19.0.2', 0)
print(ip_address[0], '\n')
mensagem = ip_address[0] 

print('A conexão funcionou :)')

lista_hosts = ['172.18.0.4', '172.18.0.3', '172.19.0.4', '172.18.0.3']
#$ fazer a desconexxao do servidor, o servidor vai aguardar uma nova conexao esperando um novo cliente

# Criação da thread
thread = threading.Thread(target=receber_dados, args=[client_socket,])

# Início da thread
thread.start()

print("Thread iniciada")
while(True):
    try:
        
        msg = input('Insira a mensagem que será propagada: ')
        if msg == 'disconnect':
            client_socket.close()
            print('cliente desconectado')
            ler_json_bloqueado(ip_address[0], '172.19.0.2', 1)
            break    
        #print('mensagem recebida: ' +client_socket.recv(1024).decode())

        host = input('Insira o número do host para qual você enviará essa mensagem\n'
        '0 - host 1;\n1 - host 2; \n2 - host 3; \n3 - host 4.\n' \
        'Insira a sua opção\n: ')
        if(lista_hosts[int(host)] != ip_address[0]):
            caminho_a_seguir = dijkstra(apenasLer(), ip_address[0], lista_hosts[int(host)])
            print(caminho_a_seguir,'\n\n')
            print(ip_address[0], lista_hosts[int(host)])
            auxMsg = str(mensagem +'-30-' + str(caminho_a_seguir) + '-')
            print('Aqui1')
            auxsequenceNumber = len(auxMsg)
            print('Aqui2')
            sequenceNumber = str(int(auxsequenceNumber + len(str(auxsequenceNumber)) + 1))
            print('aqui3')
            msg = str(mensagem + '-' + sequenceNumber + '-30-' + str(caminho_a_seguir) + '-' + msg)
            client_socket.send(msg.encode()) #enviar a mensagem
            print('mensagem enviada')
        else:
            print('Não pode enviar mensagem para si mesmo!')
    except:
        client_socket.close() #fecha conexao


'''
Implementar a comunicação em rede e a multithread
OBS: Colocar o aquire e o realise
'''

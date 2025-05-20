import json
import fcntl

def escreverArquivo(novoDicio):
    with open('tabelaRoteamento.json', 'w') as arquivo:
        # Converte o dicionário para JSON e escreve no arquivo
        json.dump(novoDicio, arquivo)  # indent=4 para formatação
        arquivo.close()
            

def ler_json_bloqueado(ipServidor, ipCliente, opcao):

    try:
        print('Acerto')
        with open('tabelaRoteamento.json', 'r') as file:
            data = json.load(file)
            fcntl.flock(file, fcntl.LOCK_SH)# Bloqueio de leitura
            if opcao == 0:
                if ipServidor in data:
                    print('servidor está em data')
                    if ipCliente not in data[ipServidor]:
                        tupla = [ipCliente, 1]
                        print('Adicionado o cliente')
                        data[ipServidor].append(tupla)
                        print(data)
                else:
                    print('Servidor não estava em data. Foi adicionado ele e o cliente')
                    data[ipServidor] = []
                    tupla = [ipCliente, 1]
                    data[ipServidor].append(tupla)

            else:
                print(data, ' em remoção')
                for i in data[ipServidor]:
                    if ipCliente in i:
                        lista_principal = data[ipServidor]
                        lista_principal.remove(i)

                        # Remova a lista da lista principal
                print(data, 'depois de remover')
            escreverArquivo(data)
            fcntl.flock(file, fcntl.LOCK_UN) # Liberação do bloqueio
            file.close()
            return data

    except:
        data = {}
        data[ipServidor] = []
        tupla = [ipCliente, 1]
        data[ipServidor].append(tupla)
        escreverArquivo(data)
        print(data, ' em except')
        return data

def apenasLer():
    with open('tabelaRoteamento.json', 'r') as file:
        data = json.load(file)
        file.close()
        return data

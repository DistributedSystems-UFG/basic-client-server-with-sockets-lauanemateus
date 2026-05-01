from socket import *
from constCS import *
import json

def enviar_operacao(socket, operacao, valor1, valor2):
    """
    Envia uma requisição de operação para o servidor e recebe o resultado.
    Formato: operacao|valor1|valor2
    """
    requisicao = f"{operacao}|{valor1}|{valor2}"
    print(f"Enviando: {requisicao}")
    socket.send(str.encode(requisicao))  # send some data
    
    data = socket.recv(1024) # receive the response
    resposta = json.loads(bytes.decode(data))
    
    # print the result
    if "erro" in resposta:
        print(f"❌ Erro: {resposta['erro']}")
    else:
        print(f"✓ Resultado: {resposta['valor1']} {resposta['operacao']} {resposta['valor2']} = {resposta['resultado']}")
    
    return resposta

s = socket(AF_INET, SOCK_STREAM)
print(f"Conectando ao servidor {HOST}:{PORT}...")
s.connect((HOST, PORT)) # connect to server (block until accepted)
print("Conectado!\n")

# Testando múltiplas operações
operacoes_teste = [
    ("add", 10, 5),
    ("subtract", 20, 8),
    ("multiply", 7, 6),
    ("divide", 100, 4)
]

for operacao, v1, v2 in operacoes_teste:
    print(f"--- Operação {v1} {operacao} {v2} ---")
    enviar_operacao(s, operacao, v1, v2)
    print()

print("Encerrando conexão...")
s.close() # close the connection
print("Desconectado!")

from socket import *
from constCS import *
import json

def processar_operacao(operacao, valor1, valor2):
    """
    Processa uma operação matemática e retorna o resultado.
    Operações suportadas: add, subtract, multiply, divide
    """
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
        
        if operacao == "add":
            resultado = valor1 + valor2
        elif operacao == "subtract":
            resultado = valor1 - valor2
        elif operacao == "multiply":
            resultado = valor1 * valor2
        elif operacao == "divide":
            if valor2 == 0:
                return {"erro": "Divisão por zero não permitida"}
            resultado = valor1 / valor2
        else:
            return {"erro": f"Operação '{operacao}' não reconhecida"}
        
        return {"resultado": resultado, "operacao": operacao, "valor1": valor1, "valor2": valor2}
    except ValueError:
        return {"erro": "Valores devem ser numéricos"}
    except Exception as e:
        return {"erro": str(e)}

def processar_requisicao(dados):
    """
    Processa requisição do cliente no formato: operacao|valor1|valor2
    """
    try:
        partes = dados.strip().split("|")
        if len(partes) != 3:
            return {"erro": "Formato inválido. Use: operacao|valor1|valor2"}
        
        operacao, valor1, valor2 = partes
        return processar_operacao(operacao, valor1, valor2)
    except Exception as e:
        return {"erro": f"Erro ao processar requisição: {str(e)}"}

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f"Servidor iniciado em {HOST}:{PORT}")
print("Aguardando conexões...\n")

(conn, addr) = s.accept()  # returns new socket and addr. client 
print(f"Conexão estabelecida com {addr}")

while True: # forever
    data = conn.recv(1024) # receive data from client
    if not data: break # stop if client stopped
    
    requisicao = bytes.decode(data)
    print(f"Requisição recebida: {requisicao}")
    
    resposta = processar_requisicao(requisicao)
    resposta_json = json.dumps(resposta, ensure_ascii=False)
    
    print(f"Resposta enviada: {resposta_json}\n")
    conn.send(str.encode(resposta_json)) # return sent data plus an "*"

print("Cliente desconectado")
conn.close()
s.close()

# Calculadora Remota com Sockets

Um sistema cliente-servidor básico que implementa uma **calculadora remota** utilizando sockets TCP em Python.

## Descrição

Este projeto demonstra a comunicação entre cliente e servidor usando sockets. O servidor executa operações matemáticas simples e envia os resultados para o cliente.

## Funcionalidades

O servidor suporta as seguintes operações matemáticas:

- **add**: Adição de dois números
- **subtract**: Subtração de dois números
- **multiply**: Multiplicação de dois números
- **divide**: Divisão de dois números (com validação para divisão por zero)

## Estrutura do Projeto

- **server.py** - Servidor que recebe requisições e executa operações matemáticas
- **client.py** - Cliente que envia requisições e exibe os resultados
- **constCS.py** - Constantes de configuração (HOST e PORT)
- **README.md** - Este arquivo

### Execução

1. **Inicie o servidor:**
   ```bash
   python server.py
   ```

2. **Em outro terminal, execute o cliente:**
   ```bash
   python client.py
   ```

## Protocolo de Comunicação

O cliente envia requisições no formato:
```
operacao|valor1|valor2
```

Exemplos:
- `add|10|5`
- `subtract|20|8`
- `multiply|7|6`
- `divide|100|4`

O servidor responde com um JSON contendo o resultado ou mensagem de erro:
```json
{"resultado": 15, "operacao": "add", "valor1": 10, "valor2": 5}
```

## Configuração

Edite o arquivo `constCS.py` para mudar o ip do seu HOST e PORT escolhida:
```python
HOST = '192.168.1.10'
PORT = 5678
```

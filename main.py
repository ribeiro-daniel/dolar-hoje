import requests
import time
from datetime import datetime
import json
import os

now = datetime.now()
while True:
    try:
        req = requests.get('https://economia.awesomeapi.com.br/json/all/USD-BRL')
        resp = json.loads(req.text)
        moeda = resp['USD']['code']
        alta = resp['USD']['high']
        baixa = resp['USD']['low']
        tipo = resp['USD']['name']
        data = now.now()
        print("=== Programinha que verifica a cotação do Dólar em Real em tempo real 1.0 ===")
        print("=== Atualizado a cada 30 segundos ===")
        print("Moeda:\t ", moeda,
              "\nAlta do dólar:\t R$", round(float(alta), 2),
              "\nBaixa do dólar:\t R$", round(float(baixa), 2),
              "\nTipo de dólar:\t ", tipo,
              "\nData:\t ", data)
        time.sleep(30)
        os.system("cls")
    except:
        print("Erro de conexão. Tentando reconectar... ")





import requests
import json
import time

achados = []
municipios = []

def acharGabriel(municipio): #a funcao recebe um dicionario com o nome e id do municipio e procura o nome Gabriel no top 10
    resposta = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade={municipio['id']}')
    time.sleep(0.5) # evita bloqueio por muitas requisições
    
    if resposta.status_code == 200:
        print(f"{municipio['nome']} - OK")
        resposta_json = resposta.json()
        nomes = resposta_json[0]['res']
        for item in nomes[:10]:  
            if item['nome'] == 'GABRIEL':
                print(f"Encontrado Gabriel em {municipio['nome']} com ranking {item['ranking']}")
                achados.append({municipio['nome']: item['frequencia']})
                break
    else:
        print(f"Erro ao acessar dados para {municipio['nome']}")
    
#requisição para pegar os municipios de SP
resposta = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios')
resposta_json = resposta.json()

if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
    for municipio in resposta_json:
        #para cada municipio, adiciona o nome e id em um dicionario e adiciona esse dicionario na lista municipios
        municipios.append({'nome':municipio['nome'], 'id': municipio['id']})    
    
         #faz o arquivo.json e adiciona os municipios com gabriel no top 10
    try:
        for municipio in municipios:
            acharGabriel(municipio)
        
    except Exception as e:
        print(f"Erro ao processar um município: {e}")
    finally:
        # Ordena a lista de achados pela frequência
        achados.sort(key=lambda x: list(x.values())[0])
        achados.reverse()
            # Salva os achados em um arquivo JSON
    with open('resultado.json', 'w') as arquivo:
        arquivo.write(json.dumps(achados, ensure_ascii=False))
       
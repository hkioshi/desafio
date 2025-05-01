# Gabriel no Top 10 de Nomes - Municípios de SP

Este script em Python consulta a API do IBGE para verificar se o nome **"Gabriel"** está entre os 10 nomes mais frequentes em cada município do estado de São Paulo. O resultado é salvo em um arquivo `resultado.json`, contendo os municípios onde o nome foi encontrado e a frequência correspondente.

## 📋 Requisitos

- Python 3.6 ou superior
- Bibliotecas:
  - `requests`
  - `json` (módulo padrão do Python)
  - `time` (módulo padrão do Python)

Você pode instalar as dependências com:

```bash
pip install requests
```

## 🚀 Como usar

1. Baixe o script
2. Execute o script no terminal:

```bash
python Desafio_Henrique_kioshi.py
```

3. Aguarde a execução (pode levar alguns minutos, pois há um `sleep(0.5)` entre as requisições para evitar bloqueios).
4. Ao final, será gerado o arquivo `resultado.json` com os municípios onde "Gabriel" aparece no top 10.

## 🧾 Estrutura do resultado

O arquivo `resultado.json` é uma lista de dicionários no formato:

```json
[
  {
    "NomeDoMunicipio": frequência
  },
  ...
]
```

Ordenado da maior para a menor frequência.

## 💡 Observações

- A API consultada é pública e fornecida pelo IBGE.
- O nome é procurado em caixa alta: `"GABRIEL"`.
- Apenas os **10 primeiros nomes mais frequentes** de cada município são considerados.
- Há uma pausa de 0.5 segundos entre as requisições para evitar bloqueios por excesso de chamadas.



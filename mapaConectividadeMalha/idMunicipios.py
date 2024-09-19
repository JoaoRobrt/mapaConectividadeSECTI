from typing import List, Any
import requests
import pandas as pd


df_municipios = pd.read_csv('parahybaCities.csv', engine='python')

df_municipios['CD_MUN'] = df_municipios['CD_MUN'].astype(str)


malhas: List[Any] = []

for cd_num in df_municipios['CD_MUN']:

    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/{cd_num}"

    try:

        response = requests.get(url)
        response.raise_for_status()


        malhas.append(response.json())

    except requests.exceptions.HTTPError:
        print(f"Erro para o código de município {cd_num}.")
        malhas.append(None)

    except Exception as e:
        print(f"Ocorreu um erro para o código {cd_num}: {e}. Adicionando valor vazio.")
        malhas.append(None)

df_malhas = pd.DataFrame(malhas)


print(df_malhas.head())

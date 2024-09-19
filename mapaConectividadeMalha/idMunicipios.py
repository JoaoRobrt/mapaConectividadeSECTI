import requests
from typing import Dict, Optional

def obter_malha(codigo_municipio: str) -> Optional[Dict]:
    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/municipios/{codigo_municipio}?formato=application/vnd.geo+json"
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.headers.get('Content-Type') == 'application/vnd.geo+json':
            return response.json()
        else:
            print(f"Formato de resposta inesperado para o código {codigo_municipio}.")
            return None

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP para o código {codigo_municipio}: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro para o código {codigo_municipio}: {e}")
        return None

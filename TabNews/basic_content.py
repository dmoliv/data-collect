# %%
import requests
import pandas as pd
import datetime
import json
import time

# %%

# funcao para passar parametros da API
def get_response(**kawargs): 
    url = 'https://www.tabnews.com.br/api/v1/contents/'
    resp = requests.get(url, params=kawargs)
    return resp


# funcao para salvar varios retornos da API em json ou parquet
def save_data(data, option='json'):

    #aqui tomar cuidado no windows ele não aceita :
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f')

    if option == 'json':
        with open(f'data/contents/json/{now}.json', 'w') as open_file:
            json.dump(data, open_file, indent=4)

    elif option == 'parquet':
        df = pd.DataFrame(data)
        df.to_parquet(f'data/contents/json/{now}.parquet', index=False)


# %%
page = 1
while True:
    print(page)
    resp = get_response(page=page, per_page=100, strategy='new')
    if resp.status_code == 200:
         data = resp.json()
         save_data(data)

         if len(data) < 100:
             break
         page += 1
         time.sleep(5)
    else:
        print(resp.status_code)
        print('tente novamente mais tarde')
        break
        

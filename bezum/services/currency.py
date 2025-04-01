
import aiohttp
import asyncio
import random
import json 
from bezum.db.schemas.currency import CurrencySchema

class CurrencyService:
    async def get_all_currencies(self) -> CurrencySchema:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://currate.ru/api/?get=rates&pairs=USDRUB,EURRUB,THBRUB,RSDRUB,JPYRUB,LKRRUB,MDLRUB,MMKRUB,GELRUB,GBPRUB,BYNRUB,CADRUB,CHFRUB,CNYRUB,ETHRUB,BCHRUB,BTCRUB,BYNRUB&key=d0f096c77d6302528ed02df44ef86f93') as response:
                if response.status == 200:
                    data_bait = await response.read()
                    data_json = json.loads(data_bait.decode('utf-8'))
                    status = data_json['status']
                    data = data_json['data']
                    #print(data, type(data))
                    list_data = []
                    for key, value in data.items():
                        list_data.append(CurrencySchema(key=key, value=value))
                    #print(list_data)
                    return list_data
                else:
                    raise Exception(f'Error fetching data: {response.status}')
    
    
    async def get_random_currency(self):
        currencies = 'USDRUB','EURRUB','THBRUB','RSDRUB','JPYRUB','LKRRUB','MDLRUB','MMKRUB','GELRUB','GBPRUB','BYNRUB','CADRUB','CHFRUB','CNYRUB','ETHRUB','BCHRUB','BTCRUB','BYNRUB'
        rand_cur = random.choice(currencies)
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://currate.ru/api/?get=rates&pairs={rand_cur}&key=d0f096c77d6302528ed02df44ef86f93') as response:
                if response.status == 200:
                    data_bait = await response.read()
                    data_json = json.loads(data_bait.decode('utf-8'))
                    status = data_json['status']
                    data = data_json['data']
                    #print(data, type(data))
                    res = CurrencySchema(key=rand_cur, value=data[rand_cur])
                    return data
                else:
                    raise Exception(f'Error fetching data: {response.status}')
                
                

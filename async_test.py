#asynctest
import asyncio

import aiohttp
from aiohttp import request
from aiomultiprocess import Pool
from aiofile import AIOFile, Writer

from builtins import set

import bs4
import re
import os 
from time import time

async def write_ids(world: str, data: set):
    async with AIOFile(f"{world}.txt", 'w') as afp:
        await afp.write(str(data))


async def write_err_html(sth: str):
    async with AIOFile("err.html", 'w') as err:
        await err.write(str(sth))


async def get(world: str, page: int) -> str:
    url = f'https://new.margonem.pl/ladder/players,{world}'
    
    while True:
        try:
            async with request("GET", url, params={'page': page}) as response:
                return await response.text("utf-8")
            break
        except aiohttp.client_exceptions.ClientConnectorError:
            continue



async def get_max_page(world) -> int:
    MAX_PAGE_SELECTOR = ('body > div.background-logged-wrapper > div'
    ' > div.body-container > div > div.pagination > div.total-pages > a')
    result = 0
    while not (result > 0 and result < 1000):
        try:
            html = bs4.BeautifulSoup(await get(world, 0), features='html.parser')
            result = int(html.select_one(MAX_PAGE_SELECTOR).text.strip())
        except:
            result = 0
    return result


async def get_profiles(world, max_page, modulo, ratio):
    PROFILES_URL_SELECTOR = ('body > div.background-logged-wrapper > div'
    ' > div.body-container > div > div.light-brown-box'
    ' > div.ranking-body.player-ranking > table > tbody')
    ID_REGEX = 'view,([0-9]*)'

    accounts = set()
    for page in range(modulo, max_page, ratio):
        html = bs4.BeautifulSoup(await get(world, page), features='html.parser')
        accounts.update(
            set(re.search(ID_REGEX, acc.attrs['href']).group(1) for acc in html
                .select_one(PROFILES_URL_SELECTOR)
                .find_all('a')))

    return accounts




async def get_all_profiles_from_world(world: str) -> set:
    max_page = await get_max_page(world) + 1
    ratio = max_page#max(max_page % 10, 1)
    print(f'Rozpoczynam pobieranie {max_page} stron z rankingu {world}.')
    
    all_result = await asyncio.gather(*[
        get_profiles(world, max_page, i, ratio) 
        for i in range(ratio)
    ])
    final_result = set()
    for result in all_result:
        final_result.update(result)
    print(world)
    # print(final_result)
    await write_ids(world, final_result)
    return final_result

async def main():
    worlds = \
    [
    "Aldous", "Berufs", "Brutal", "Classic", "Fobos", "Gefion",
    "Hutena", "Jaruna", "Katahha", "Lelwani", "Majuna", "Nomada", "Perkun",
    "Tarhuna", "Telawel", "Tempest", "Zemyna", "Zorza", "Aequus",  "Elizjum", "Erebos"
    #  "Asylum", "Ataentsic", "Avalon", "Badzior", "Dionizos", "Dream", "Ertill", "Experimental", "Febris", "Helios", "Inferno", 
    #  "Infinity", "Legion", "Majorka", "Mordor", "Narwhals", "Nerthus",
    #  "Odysea", "Orchidea", "Orvidia", "Pandora", "Regros", "Riventia", 
    #  "Stark", "Stoners", "Syberia", "Thantos", "Unia", "Virtus", "Zefira"
     ]
    # worlds = ['Nubes','Hypnos']
    # world = 'Fobos's
    async with Pool() as pool:
        await pool.map(get_all_profiles_from_world, worlds)
        
if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    t1 = time()
    asyncio.run(main())
    t2 = time()
    print(f"Czas operacji: {t2-t1}")
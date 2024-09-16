import asyncio
import aiohttp
import os
import json


lock = asyncio.Lock()

async def get_data(page):
    async with aiohttp.ClientSession() as session:
        data = await session.get(f'https://jsonplaceholder.typicode.com/posts/{page}')
        data = await data.json()
        async with lock:
            if os.path.exists("data.json"):
                with open("data.json", 'a') as f:
                    f.write(",\n")
                    json.dump(data, f, indent=2)
            else:
                with open("data.json", 'w') as f:
                    f.write("[\n")
                    json.dump(data, f, indent=2)


async def main():
    await asyncio.gather(*(get_data(i) for i in range(1,78)))

if __name__ == '__main__':
    asyncio.run(main())
    with open("data.json", 'a') as f:
        f.write("\n]")

import asyncio

semapore = asyncio.Semaphore(2)

async def res(id:int):
    async with semapore:
        print (f"tasks started and running {id}")
        await asyncio.sleep(2)
        print(f"tasks stopped {id}")


async def main():
    tasks = [res(i) for i in range(0,6)]
    await asyncio.gather(*tasks)

asyncio.run(main())
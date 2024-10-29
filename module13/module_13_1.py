import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1,6):
        print(f'Силач {name} поднял {i} шар' )
        await asyncio.sleep(10/power)
    print(f'Силач {name} закончил соревнования')


async def main():
    task = asyncio.create_task(start_strongman("Denis", 5))
    task1 = asyncio.create_task(start_strongman("Anton", 10))
    task2 = asyncio.create_task(start_strongman("Egor", 3))
    await task
    await task1
    await task2



start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Соревнование закончено за {round(finish - start, 2)} минут')

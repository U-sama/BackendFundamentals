import asyncio
import aiofiles

async def print_trace():
    print("1")
    await asyncio.sleep(3)
    print("2")
    return "done"

async def read_file_async(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        await asyncio.sleep(6)
        data = await file.read()
    print(data)
    return "Done reading file"
    

async def main():
    task1 = asyncio.create_task(print_trace())
    task2 = asyncio.create_task(read_file_async("file.txt"))

    print(await task1)
    print(await task2)
    print("finished")

asyncio.run(main())


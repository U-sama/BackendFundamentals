import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8080') as websocket:
        await websocket.send("Hello! I'm client")
        async for message in websocket:
            print(f"Received: {message}")

asyncio.get_event_loop().run_until_complete(hello())
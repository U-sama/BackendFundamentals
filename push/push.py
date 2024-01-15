import asyncio
import websockets

connections = set()

async def server(websocket):
    connections.add(websocket)
    try:
        async for message in websocket:
            for connection in connections:
                if connection != websocket:
                    await connection.send(f"User {websocket.remote_address[1]} says: {message}")
        for connection in connections:
            if connection != websocket:
                await connection.send(f"User {websocket.remote_address[1]} just connected.")
    finally:
        connections.remove(websocket)

start_server = websockets.serve(server, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
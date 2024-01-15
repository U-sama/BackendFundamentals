import asyncio
import websockets

connections = set()
fastest_time = 0

async def buzzer_game_server(websocket, path):
    global connections
    global fastest_time

    await websocket.send("Welcome to the buzzer game! Please enter your name.")
            
    if websocket not in connections:
        connections.add(websocket)
        print(f"User {websocket.remote_address[1]} just connected.")
        for connection in connections:
            if connection.open and connection.remote_address[1] != websocket.remote_address[1]:
                await connection.send(f"User {connection.remote_address[1]} just connected.")
    message = await websocket.recv()

    if message == "buzz":
        response_time = asyncio.get_event_loop().time()
        if len(connections) == 1:
            await websocket.send("Firs Place!")
            fastest_time = response_time
        else:
            t = round(response_time - fastest_time, 2)
            await websocket.send(f"Your time was {t} seconds slower.")  
            for connection in connections:
                if connection.open and connection.remote_address[1] != websocket.remote_address[1]:
                    await connection.send(f"User response time was {t} seconds slower.")  

async def main():
    async with websockets.serve(buzzer_game_server, "localhost", 8080):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

    
    

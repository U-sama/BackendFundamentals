import asyncio
import websockets
import keyboard
async def play_buzzer_game():
    async with websockets.connect('ws://localhost:8080') as websocket:
        message = await websocket.recv()
        print(message)
        done = False
        while not done:
            if keyboard.is_pressed('q'):
                await websocket.send("buzz")
                message = await websocket.recv()
                print(message)
                done = True          

        while True:
            message = await websocket.recv()
            print(message)      

if __name__ == "__main__":
    asyncio.run(play_buzzer_game())
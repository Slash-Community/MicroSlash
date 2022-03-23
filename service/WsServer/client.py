import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.send("123")
        print(await websocket.recv())

asyncio.run(hello("ws://localhost:8889"))

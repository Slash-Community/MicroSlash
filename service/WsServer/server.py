import os
import asyncio
import websockets

JSON_FILE_PATH = os.path.dirname(os.path.dirname(__file__)) + "/data.json"

async def message_handler(websocket, *args):
    async for message in websocket:
        while True:
            try:
                with open(JSON_FILE_PATH, "r") as file_:
                    send_data = file_.read()
                    await websocket.send(send_data)
                    await asyncio.sleep(10)
            except:
                pass


async def main():
    print("WsServer started...")
    async with websockets.serve(message_handler, "localhost", 8889):
        await asyncio.Future()

asyncio.run(main())
import socketio
from aiohttp import web

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ):
    print(f"{sid} connected")

@sio.event
async def join(sid, data):
    room = data.get("room")
    await sio.enter_room(sid, room)
    print(f"{sid} joined room: {room}")
    await sio.emit("system", f"{sid} joined the chat", room=room)

@sio.event
async def message(sid, data):
    room = data.get("room")
    msg = data.get("msg")
    await sio.emit("message", {"sid": sid, "msg": msg}, room=room)

@sio.event
async def disconnect(sid):
    print(f"{sid} disconnected")

if __name__ == '__main__':
    web.run_app(app, port=8000)

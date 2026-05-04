import socketio
from aiohttp import web

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ):
    # Por seguridad, podríamos unirlo a una sala 'global' por defecto
    await sio.enter_room(sid, "global")
    print(f"Conectado: {sid}")

@sio.event
async def join(sid, data):
    room = data.get("room")
    if room:
        await sio.enter_room(sid, room)
        print(f"{sid} se unió a: {room}")
        # Notificar a la sala
        await sio.emit("system", f"Usuario {sid[-4:]} entró al canal", room=room)

@sio.event
async def leave(sid, data):
    room = data.get("room")
    if room:
        await sio.leave_room(sid, room)
        print(f"{sid} salió de: {room}")
        await sio.emit("system", f"Usuario {sid[-4:]} salió del canal", room=room)

@sio.event
async def message(sid, data):
    # IMPORTANTE: El cliente debe enviar 'room' y 'msg'
    room = data.get("room", "global") # Si no hay sala, va a la global
    msg = data.get("msg")
    
    if msg:
        # Retransmitir SOLO a los miembros de esa sala
        await sio.emit("message", {"sid": sid, "msg": msg}, room=room)

@sio.event
async def disconnect(sid):
    print(f"Desconectado: {sid}")

if __name__ == '__main__':
    web.run_app(app, port=8000)
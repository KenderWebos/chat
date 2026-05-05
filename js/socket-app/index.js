const { Server } = require("socket.io");
const http = require("http");

const httpServer = http.createServer();
const io = new Server(httpServer, {
  cors: {
    origin: "*",
  },
});

io.on("connection", (socket) => {
  // Por seguridad, unir a sala 'global' por defecto
  socket.join("global");
  console.log(`Conectado: ${socket.id}`);

  // Evento Join
  socket.on("join", (data) => {
    const room = data?.room;
    if (room) {
      socket.join(room);
      console.log(`${socket.id} se unió a: ${room}`);
      // Notificar a la sala
      io.to(room).emit("system", `Usuario ${socket.id.slice(-4)} entró al canal`);
    }
  });

  // Evento Leave
  socket.on("leave", (data) => {
    const room = data?.room;
    if (room) {
      socket.leave(room);
      console.log(`${socket.id} salió de: ${room}`);
      io.to(room).emit("system", `Usuario ${socket.id.slice(-4)} salió del canal`);
    }
  });

  // Evento Message
  socket.on("message", (data) => {
    const room = data?.room || "global";
    const msg = data?.msg;

    if (msg) {
      // Retransmitir SOLO a los miembros de esa sala
      io.to(room).emit("message", { sid: socket.id, msg: msg });
    }
  });

  socket.on("disconnect", () => {
    console.log(`Desconectado: ${socket.id}`);
  });
});

const PORT = 8000;
httpServer.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
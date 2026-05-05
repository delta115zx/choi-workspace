const express = require("express");
const app = express();

// 학원 패턴 그대로: io.listen(포트) + io.sockets.on("connection")
// Dec08_3: emit/on 기초 / Dec08_4: 채팅(객체전달) / Dec08_5: 드로잉(xy좌표) / Dec09_1: 게임(host/guestX)
const io = require("socket.io")();
io.listen(process.env.PORT || 4000, {
  cors: { origin: "*" },
});

let visitors = 0;

io.sockets.on("connection", (socket) => {
  visitors++;
  io.sockets.emit("visitor_count", visitors);

  // Dec08_5 드로잉 패턴: xy좌표 수신 → 브로드캐스트
  socket.on("xy", (xy) => {
    io.sockets.emit("xy2", xy);
  });

  // 전체 지우기 브로드캐스트
  socket.on("draw_clear", () => {
    io.sockets.emit("draw_clear");
  });

  socket.on("disconnect", () => {
    visitors--;
    io.sockets.emit("visitor_count", visitors);
  });
});

module.exports = app;

var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");

var indexRouter = require("./routes/index");
var usersRouter = require("./routes/users");

var app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "jade");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

// express Dec08_3_WebSocketSrv
// cd Dec08_3_WebSocketSrv
// npm install
// npm install socket.io@2
// nodemon app.js

// Node.js : 웹소켓서버 구현에 특화
//    JS파일제공 -> 웹 환경에서 사용 편리
//    문법 간단
//    실시간통신 -> 동시에 여러작업 -> 멀티쓰레드 관련 작업
//      non-blocking I/O에 특화된 JS -> 멀티쓰레드 신경안써도

var io = require("socket.io")();
io.listen(7777); // 웹소켓서버 포트 지정
// 웹소켓서버 시작 -> 자동으로 만들어짐
// http://주소:포트/socket.io/socket.io.js

// io.sockets : 연결된 모든 소켓들
// socket : 소켓 하나

// emit("제목", 내용) : 보낼때
// on("제목", 콜백함수) : 받을때
io.sockets.on("connection", function (socket) {
   console.log("연결");
   socket.on("abcd", function (zxcv) {
      io.sockets.emit("efgh", zxcv);
   });
});

// catch 404 and forward to error handler
app.use(function (req, res, next) {
   next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
   // set locals, only providing error in development
   res.locals.message = err.message;
   res.locals.error = req.app.get("env") === "development" ? err : {};

   // render the error page
   res.status(err.status || 500);
   res.render("error");
});

module.exports = app;

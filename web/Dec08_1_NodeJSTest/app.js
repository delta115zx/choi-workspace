var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.listen(9999); // Node.js express WAS 포트번호

// app.post();
// app.get("주소" function (요청객체, 응답객체) {
// });
app.get("/te.st", function (reqqq, resss) {
  resss.send("abcd")
});

app.get("/html.test", function (req, res) {
  var html = "<html><head><meta charset=\"utf-8\"><head><body>"
  html += "<marquee>ㅋㅋ</marquee>"
  html += "</body></html>"
  res.send(html)
});

// 클래식웹 : html을 만들어서 응답
// http://195.168.9.200:9999/param.test?a=10&b=20
app.get("/param.test", function (req, res) {
  var aa = req.query.a * 1; // req.query.파라메터변수명
  var bb = req.query.b * 1;
  var cc = aa + bb;
  var html = "<html><head><meta charset=\"utf-8\"><head><body>"
  html += "<h1>" + cc + "</h1>";
  html += "</body></html>"
  res.send(html)
});

// 신형웹 : xml/json을 만들어서 응답 + Front-end에서...
app.get("/json.test", function (req, res) {
  var aa = req.query.a * 1;
  var bb = req.query.b * 1;
  var cc = aa + bb;
  var dd = {"result": cc};
  res.setHeader("Access-Control-Allow-Origin", "*")
  res.send(dd);
});

// @app.get("/html.test")
// def htmlTest():
//     html = "<html><head><meta charset=\"utf-8\"><head><body>"
//     html += "<marquee>ㅋㅋ</marquee>"
//     html += "</body></html>"
//     return html


// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;

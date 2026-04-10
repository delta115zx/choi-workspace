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

// Node.js : JS 백엔드
// MongoDB : JS로 DB제어(Node.js사의 제품)
// mongojs : MongoDB명령어 그대로 사용하게 해주는 lib
//    npm install mongojs

app.listen(8888);

// http://195.168.9.200:8888/snack.reg?n=양파링&p=3000
app.get("/snack.reg", function (req, res) {
  // var mjs = require("mongojs");

  // "서버주소/DB명", ["테이블명", "테이블명", ...]
  // var db = mjs("195.168.9.232/dec08", ["dec08_snack"])
  var db = require("mongojs")("195.168.9.232/dec08", ["dec08_snack"])

  var name = req.query.n;
  var price = req.query.p * 1;
  var snack = { "s_name": name, "s_price": price }

  db.dec08_snack.insertOne(snack, function(errr, resulttt){
    res.setHeader("Access-Control-Allow-Origin", "*")
    res.send(resulttt);
  });

});

app.get("/snack.get", function (req, res) {
  var db = require("mongojs")("195.168.9.232/dec08", ["dec08_snack"])

  db.dec08_snack.find(function(errr, resulttt){
    res.setHeader("Access-Control-Allow-Origin", "*")
    res.send(resulttt);
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
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;

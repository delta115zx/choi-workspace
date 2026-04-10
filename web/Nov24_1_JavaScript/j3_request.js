// form없이
// button클릭하면
// input에 쓴 내용 받아서
// reqParam만들어서
// 요청
function doReq() {
    // document : 이 HTML
    var nInput = document.getElementById("nameInput");
    var aInput = document.getElementById("ageInput");
    var n = nInput.value;
    var a = aInput.value;

    // GET방식 요청
    location.href = "http://195.168.9.200/te.st?name=" + n + "&age=" + a;

    // POST방식 요청 : JS로 form을 만들어서...
}
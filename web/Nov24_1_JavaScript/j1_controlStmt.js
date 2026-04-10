function test() {
    alert("테스트");
}

function forTest() {
    // for (변수초기화(1); 조건식(2, 5); 증감(4, 7)) {
    //      내용(3, 6)
    // }
    for (var a = 1; a < 5; a++) {
        alert(a);
    }
}

function whileTest() {
    while (true) {
        var r = Math.random(); // 0.0 ~ 0.999...
        alert(r);
        if (r > 0.9) {
            break;
        }
    }
}
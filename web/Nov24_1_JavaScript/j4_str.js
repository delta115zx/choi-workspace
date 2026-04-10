function strTest() {
    var s = "일단 여기다 연습좀";
    alert(s);
    alert(s.length); // 글자수
    alert(s[1]); // 두번째글자
    alert(s.indexOf("단")); // '단'은 몇번째 위치에
    alert(s.indexOf("습") != -1); // '습'이 있나
}
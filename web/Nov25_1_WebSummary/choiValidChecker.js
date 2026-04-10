// JavaScript 유효성검사 라이브러리
//      - 다양한 상황에 대응가능하게 최대한 일반적으로
//      - 부정적

// <input> 넣었을때 
// 안썼으면 true, 썼으면 false
function isEmpty(input) {
    return !input.value;
}

// <input>, 글자수 넣었을때
// 그 글자수보다 짧으면 true, 아니면 false
function lessThen(input, len) {
    return input.value.length < len;
}

// <input> 넣었을때
// 한글 들어있으면 true, 아니면 false
function containsHangul(input) {
    var okSet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@._-1234567890";
    for (var i = 0; i < input.value.length; i++) {
        if (okSet.indexOf(input.value[i]) == -1) {
            return ture;
        }
    }
    return false;
}

// <input> x 2 넣었을때
// 내용이 다르면 true, 같으면 false
function notEqual(input1, input2) {
    return input1.value != input2.value;
}

// <input>, 문자열세트 넣었을때
// 그게 안들어있으면 true, 들어있으면 false
function notContains(input, set) {
    var okSet = set
    for (var i = 0; i < set.length; i++)
        if (input.value.indexOf(set[i]) != -1) {
            return false;
        }
    return true;
}

// <input> 넣었을때
// 숫자가 아니면 true, 정상적인 숫자면 false
function isNotNum(input) {
    return isNaN(input.value) || (input.value.indexOf(" ") != -1)
}

// 양수

// 정수

// input.value
//      다른거 : 입력한 내용
//      파일타입 : 선택한 파일명이 문자열로

// 파일명만 체크?
//      1) vanilla JS에서 정확하게 파일체크가 불가
//      2) 유효성검사 자체가 사용자를 배려한
//          굳이 zip -> png로 바꿔가면서까지? 본인만 프사 안나올뿐

// <input>, 확장자 넣었을때
// 그 파일이 아니면 true
function isNotType(input, type){
    type = "." + type
    return input.value.toLowerCase().indexOf(type) == -1;
}
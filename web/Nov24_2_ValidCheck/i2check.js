// 이 사이트 js소스
function i2check() {
    var idField = document.i2joinForm.id;
    var pwField = document.i2joinForm.pw;
    var pwChkField = document.i2joinForm.pwChk;
    var ageField = document.i2joinForm.age;
    var photoField = document.i2joinForm.photo;

    if (isEmpty(idField) || lessThen(idField, 4) || containsHangul(idField)) {
        alert("ID?");
        idField.value = "";
        idField.focus();
        return false;
    }

    if (isEmpty(pwField)
        || lessThen(pwField, 5)
        || notEqual(pwField, pwChkField)
        || notContains(pwField, "qwertyuiopasdfghjklzxcvbnm")
        || notContains(pwField, "0123456789")
    ) {
        alert("PW?");
        pwField.value = "";
        pwChkField.value = "";
        pwField.focus();
        return false;
    }

    if (isEmpty(ageField) || isNotNum(ageField)) {
        alert("나이?");
        ageField.value = "";
        ageField.focus();
        return false;
    }

    if (isEmpty(photoField) || isNotType(photoField, "png")) {
        alert("프사?")
        return false;
    }

    return true;
}

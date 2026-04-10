function vCheck() {
    var nameField = document.joinForm.name;
    var heightField = document.joinForm.height;
    var weightField = document.joinForm.weight;
    var photoField = document.joinForm.photo;

    if (isEmpty(nameField)) {
        alert("이름 필수");
        nameField.focus();
        return false;
    }

    if (isEmpty(heightField) || isNotNum(heightField)) {
        alert("키 필수");
        heightField.value = "";
        heightField.focus();
        return false;
    }

    if (isEmpty(weightField) || isNotNum(weightField)) {
        alert("몸무게 필수");
        weightField.value = "";
        weightField.focus();
        return false;
    }

    if (isEmpty(photoField) || (isNotType(photoField, "png") && isNotType(photoField, "jpg")
        && isNotType(photoField, "gif") && isNotType(photoField, "bmp"))) {
        alert("사진 필수");
        return false;
    }

    return true;
}
function arrayTest() {
    var a = [234, 5, 123, 111, 333, 444];
    // alert(a.length); // 내용물 갯수
    // alert(a[0]); // index는 0부터
    // alert(a[0:3]); // Python에만 있음
    // for (var i = 0; i < a.length; i++) {
    //     alert(a[i]);
    // }
    for (var v of a) {
        alert(v);
    }
}

function objectTest() {
    // class를 써서 하는 정통 OOP -> React때
    // class안쓰고
    var d = {
        name: "후추",
        age: 2,
        bark: function () {
            alert("멍")
        }
    };
    alert(d);
    alert(d.name);
    alert(d.age);
    alert(JSON.stringify(d)); // 객체 -> 문자열
}

function aoTest() {
    var dogs = [
        { name: "후추", age: 2 },
        { name: "호초", age: 3 },
        { name: "하차", age: 1 }
    ];

    for (var i = 0; i < dogs.length; i++) {
        alert(dogs[i].name + " : " + dogs[i].age);
    }

    for (var d of dogs) {
        alert(d.name + " : " + d.age);
    }

}
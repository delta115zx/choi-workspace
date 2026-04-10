function connectRegBtnClickEvent() {
    $("#regBtn").click(function () {
        var pname = $("#nameInput").val()
        var pprice = $("#priceInput").val()
        $.ajax({
            url: "http://195.168.9.200:7777/product.reg",
            data: { "name": pname, "price": pprice },
            success: function (regResult) {
                alert(regResult.result)
            }
        })
        $("#nameInput").val("")
        $("#priceInput").val("")
    })
}
// var ntd = $("<td></td>").append($("#nameInput").val())
// var ptd = $("<td></td>").append($("#priceInput").val())
// var tr = $("<tr></tr>").append(ntd, ptd)
// $("#playerTbl").append(tr)

$(function () {
    connectRegBtnClickEvent();
})
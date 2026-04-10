function connectSellerRegBtnClickEvent() {
    $("#sellerRegBtn").click(function () {
        var name = $("#sellerNameInput").val();
        var bd = $("#sellerBDInput").val();
        var addr = $("#sellerAddrInput").val();

        $.ajax({
            url: "http://195.168.9.200:7777/seller.reg",
            data: { "namee": name, "bdd": bd, "addrr": addr },
            success: function (regResult) {
                alert(regResult.result);
                getSeller(1);
            }
        });

        $("#sellerNameInput").val("");
        $("#sellerBDInput").val("");
        $("#sellerAddrInput").val("");
    });
}

function connectProductRegBtnClickEvent() {
    $("#productRegBtn").click(function () {
        var name = $("#productNameInput").val();
        var price = $("#productPriceInput").val();
        var stock = $("#productStockInput").val();
        var p_s_no = $("#p_s_noInput").val();

        $.ajax({
            url: "http://195.168.9.200:7777/product.reg",
            data: {
                "namee": name, "pricee": price, "stockk": stock,
                "p_s_noo": p_s_no
            },
            success: function (regResult) {
                alert(regResult.result)
                getProduct(1);
            }
        });

        $("#productNameInput").val("");
        $("#productPriceInput").val("");
        $("#productStockInput").val("");
        $("#p_s_noInput").val("");

    });
}
function getSeller(p) {
    $.ajax({
        url: "http://195.168.9.200:7777/seller.get",
        data: { "page": p },
        success: function (sellersResult) {
            $("#sellerBBS").empty();
            $.each(sellersResult.sellers, function (i, s) {
                var br1 = $("<br>");
                var br2 = $("<br>");
                var li = $("<li></li>").append(s.name, br1, s.bd, br2, s.addr);
                $("#sellerBBS").append(li);
            });
            $("#sellerPageControlTbl td").empty();
            for (var i = 1; i <= sellersResult.pageCount; i++) {
                var a = $("<a></a>").attr("onclick", "getSeller(" + i + ");").text(i);
                $("#sellerPageControlTbl td").append(a);
            }
            $("#sellerBBS").listview("refresh"); // 동적으로 추가한거 디자인 부여
            ///////////////////////////////////////
            // alert(sellerResult.pageCount);
        }
    });
}

function connectGoSellerPageAEvent() {
    $("#goSellerPageA").click(function () {
        getSeller(1);
    })
}

function connectGoProductPageAEvnet() {
    $("#goProdcutPageA").click(function () {
        getProduct(1);
    })
}

function getProduct(p) {
    $.ajax({
        url: "http://195.168.9.200:7777/product.get",
        data: { "page": p },
        success: function (productsResult) {
            $("#productBBS").empty();
            $.each(productsResult.products, function (i, p) {
                var br1 = $("<br>");
                var br2 = $("<br>");
                var br3 = $("<br>");
                var li = $("<li></li").append(p.name, br1, p.price, br2, p.stock, br3, p.p_s_no)
                $("#productBBS").append(li)
            });
            $("#productPageControlTbl td").empty();
            for (var i = 1; i <= productsResult.pageCount; i++) {
                var a = $("<a></a>").attr("onclick", "getProduct(" + i + ");").text(i);
                $("#productPageControlTbl td").append(a);
            }
            $("#productBBS").listview("refresh");

        }
    });
}


$(function () {
    connectSellerRegBtnClickEvent();
    connectProductRegBtnClickEvent();
    getSeller(1);
    getProduct(1);
});
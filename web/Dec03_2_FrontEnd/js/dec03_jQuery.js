var sellerBBSPage = false;
var sellerBBSPageNo = 1;

var productBBSPage = false;
var productBBSPageNo = 1;

function connectProductUpdateEvent() {
    $("#productUpdateBtn").click(function () {
        $.ajax({
            url: "http://195.168.9.200:7777/product.detail.update",
            data: {
                "no": $("#productNo").val(), "na": $("#productName").val(),
                "price": $("#productPrice").val(), "stock": $("#productStock").val()
            },
            success(updateResult) {
                alert(updateResult.result)
                productBBSPageNo = 1;
                getProduct();
                $.mobile.changePage("#productpage");
            }
        });
    });
}

function connectSellerUpdateEvent() {
    $("#sellerUpdateBtn").click(function () {
        $.ajax({
            url: "http://195.168.9.200:7777/seller.update",
            data: {
                "no": $("#sellerNo").val(), "name": $("#sellerName").val(),
                "addr": $("#sellerAddr").val()
            },
            success(updateResult) {
                alert(updateResult.result)
                getSellerDetail($("#sellerNo").val());
            }
        });
    });
}

function connectSellerDeleteEvent() {
    $("#sellerDeleteBtn").click(function () {
        if (confirm("진짜?")) {
            $.ajax({
                url: "http://195.168.9.200:7777/seller.delete",
                data: { "no": $("#sellerNo").val() },
                success: function (deleteResult) {
                    alert(deleteResult.result);
                    sellerBBSPageNo = 1;
                    getSeller();
                    $.mobile.changePage("#sellerpage");
                }
            });
        }
    });
}

function connectProductDeleteEvent() {
    $("#productDeleteBtn").click(function () {
        if (confirm("진짜?")) {
            $.ajax({
                url: "http://195.168.9.200:7777/product.detail.delete",
                data: { "no": $("#productNo").val() },
                success: function (deleteResult) {
                    alert(deleteResult.result);
                    productBBSPageNo = 1;
                    getProduct();
                    $.mobile.changePage("#productpage");
                }
            });
        }
    });
}

function connectSellerSearchEvent() {
    $("#sellerSearchInput").keyup(function (e) {
        sellerBBSPageNo = 1;
        getSeller();
    });
}

function connectProductSearchEvent() {
    $("#productSearchInput").keyup(function (e) {
        productBBSPageNo = 1;
        getProduct();
    })
}

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
                getSeller();
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
                getProduct();
            }
        });

        $("#productNameInput").val("");
        $("#productPriceInput").val("");
        $("#productStockInput").val("");
        $("#p_s_noInput").val("");

    });
}
function getSeller() {
    var searchTxt = $("#sellerSearchInput").val();
    $.ajax({
        url: "http://195.168.9.200:7777/seller.get",
        data: { "page": sellerBBSPageNo, "search": searchTxt },
        success: function (sellersResult) {
            if (sellerBBSPageNo == 1) {
                $("#sellerBBS").empty();
            }
            $.each(sellersResult.sellers, function (i, s) {
                var br1 = $("<br>");
                var br2 = $("<br>");
                var a = $("<a></a>").attr("onclick", "getSellerDetail(" + s.no + ");").attr("href", "#sellerDetailPage").append(s.name, br1, s.bd, br2, s.addr);
                var li = $("<li></li").append(a);
                $("#sellerBBS").append(li);
            });
            $("#sellerBBS").listview("refresh"); // 동적으로 추가한거 디자인 부여
            ///////////////////////////////////////
            // alert(sellerResult.pageCount);
        }
    });
}

function getSellerDetail(no) {
    $.ajax({
        url: "http://195.168.9.200:7777/seller.get.detail",
        data: { "no": no },
        success: function (sellerResult) {
            $("#sellerNo").val(sellerResult.no)
            $("#sellerName").val(sellerResult.name)
            $("#sellerBirthday").val(sellerResult.bd)
            $("#sellerAddr").val(sellerResult.addr)
        }
    })
}


function connectScrollEvent() {
    $(window).scroll(function () {
        var htmlHeight = $(document).height();
        var browserHeight = $(window).height();
        var scrollTop = $(window).scrollTop();
        var scrollBottom = scrollTop + browserHeight;
        if (sellerBBSPage && scrollBottom >= htmlHeight - 10) {
            sellerBBSPageNo++;
            getSeller(sellerBBSPageNo);
        }
        if (productBBSPage && scrollBottom >= htmlHeight - 10) {
            productBBSPageNo++;
            getProduct(productBBSPageNo);
        }
    });
}

function connectGoSellerPageAEvent() {
    $("#goSellerPageA").click(function () {
        sellerBBSPage = true;
        sellerBBSPageNo = 0;
        getSeller();
    })
}
function connectGoMenuPageAEvent() {
    $(".goMenuPageA").click(function () {
        sellerBBSPage = false;
        productBBSPage = false
        $("#sellerSearchInput").val("");
        $("#productSearchInput").val("");
    })
}

function connectGoProductPageAEvent() {
    $("#goProdcutPageA").click(function () {
        productBBSPage = true;
        productBBSPageNo = 0;
        getProduct();
    })
}

function getProduct() {
    var searchTxt = $("#productSearchInput").val();
    $.ajax({
        url: "http://195.168.9.200:7777/product.get",
        data: { "page": productBBSPageNo, "search": searchTxt },
        success: function (productsResult) {
            if (productBBSPageNo == 1) {
                $("#productBBS").empty();
            }
            $.each(productsResult.products, function (i, p) {
                var br1 = $("<br>");
                var br2 = $("<br>");
                var br3 = $("<br>");
                var a = $("<a></a>").attr("onclick", "getProductDetail(" + p.no + ");").attr("href", "#productDetailPage").append(p.name, br1, p.price, br2, p.stock, br3, p.p_s_no);
                var li = $("<li></li").append(a);
                $("#productBBS").append(li)
            });
            $("#productBBS").listview("refresh");
        }
    });
}

function getProductDetail(no) {
    $.ajax({
        url: "http://195.168.9.200:7777/product.detail.get",
        data: { "no": no },
        success: function (productResult) {
            $("#productNo").val(productResult.no)
            $("#productName").val(productResult.name)
            $("#productPrice").val(productResult.price)
            $("#productStock").val(productResult.stock)
            $("#productp_s_no").val(productResult.p_s_no)
        }

    })
}


$(function () {
    connectScrollEvent();
    connectSellerSearchEvent();
    connectProductSearchEvent();
    connectGoMenuPageAEvent();
    connectGoSellerPageAEvent();
    connectGoProductPageAEvent();
    connectSellerRegBtnClickEvent();
    connectProductRegBtnClickEvent();
    connectProductDeleteEvent();
    connectSellerDeleteEvent();
    connectProductUpdateEvent();
    connectSellerUpdateEvent();
});
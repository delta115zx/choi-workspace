var playerPageNo = 1;

function connectPlayerRegEvent() {
    $("#playerRegBtn").click(function () {
        $.ajax({
            url: "http://195.168.9.200:7777/player.reg",
            data: {
                "pname": $("#playerNameInput").val(),
                "tname": $("#teamNameInput").val()
            },
            success: function (regResult) {
                alert(regResult.result);
            }
        });
        $("#playerNameInput").val("");
        $("#teamNameInput").val("");
        $("#playerTbl").empty();
        getPlayer();
    });
}

function connectPlayerDeleteEvent() {
    $("#playerDeleteBtn").click(function () {
        $.ajax({
            url: "http://195.168.9.200:7777/player.delete",
            data: {
                "no": $("#playerUDNoInput").val()
            },
            success: function (deleteResult) {
                alert(deleteResult.result)
                InputTableRefresh();
            }
        });
    })
}

function connectPlayerUpdateEvent() {
    $("#playerUpdateBtn").click(function () {
        $.ajax({
            url: "http://195.168.9.200:7777/player.update",
            data: {
                "no": $("#playerUDNoInput").val(), "pname": $("#playerUDNameInput").val(),
                "tname": $("#teamUDNameInput").val()
            },
            success: function (updateResult) {
                alert(updateResult.result);
                InputTableRefresh();
            }
        });
    });
}

function connectPlayerSearchEvent() {
    $("#searchPlayerInput").keyup(function () {
        playerPageNoPageNo = 1;
        getPlayer();
    })
}

function InputTableRefresh() {
    $("#playerNameInput").val("");
    $("#teamNameInput").val("");
    $("#playerUDNoInput").val("");
    $("#playerUDNameInput").val("");
    $("#teamUDNameInput").val("");
    $("#playerTbl").empty();
    getPlayer();
}

function getPlayer() {
    var searchTxt = $("#searchPlayerInput").val()
    $.ajax({
        url: "http://195.168.9.200:7777/player.get",
        data: {"pageNo":playerPageNo, "search":searchTxt},
        success: function (getResult) {
            if (playerPageNo == 1){
                $("#playerTbl").empty();
            }
            $.each(getResult.players, function (i, p) {
                var br1 = $("<br>");
                var br2 = $("<br>");
                var td = $("<td></td>").attr("onclick", "getPlayerUD(" + p.no + ");").append(p.no, br1, p.pname, br2, p.tname);
                var tr = $("<tr></tr>").append(td)
                $("#playerTbl").append(tr)
            })
        }
    })
}

function connectScrollEvent() {
    $(window).scroll(function () {
        var htmlHeight = $(document).height();
        var browserHeight = $(window).height();
        var scrollTop = $(window).scrollTop();
        var scrollBottom = scrollTop + browserHeight;
        if (scrollBottom >= htmlHeight - 10) {
            playerPageNo++;
            getPlayer(playerPageNo);
        }
    });
}

function getPlayerUD(no) {
    $.ajax({
        url: "http://195.168.9.200:7777/player.get.ud",
        data: { "no": no },
        success: function (playerResult) {
            $("#playerUDNoInput").val(playerResult.no);
            $("#playerUDNameInput").val(playerResult.pname);
            $("#teamUDNameInput").val(playerResult.tname);
        }
    });
}

$(function () {
    InputTableRefresh();
    connectPlayerRegEvent();
    connectPlayerDeleteEvent();
    connectPlayerUpdateEvent();
    connectPlayerSearchEvent();
    connectScrollEvent();
});

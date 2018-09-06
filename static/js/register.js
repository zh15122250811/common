$(function () {

    // 监听确认密码输入框的改变,验证两次输入密码是否一致
    $("#confirm_pwd").change(function () {
        pwd1 = $("#pwd").val()
        pwd2 = $("#confirm_pwd").val()

        if (pwd1 == pwd2){
            $("#message").html("两次密码输入一致").css("color","green")
        } else {
            $("#message").html("两次密码输入不一致,请重新输入").css("color","red")
        }
    })


    // 监听用户民输入框的改变, 验证用户名是否可用
    $("#username").change(function () {
        Username = $("#username").val()
        $.getJSON("/app/check_user",{"Username":Username},function (data) {
            if(data["code"] == "901"){
                $("#username_info").html(data[msg]).css("color","red")
            } else if (data["code"] == "200"){
                $("#username_info").html(data[msg]).css("color","green")
            }

        })
    })

})
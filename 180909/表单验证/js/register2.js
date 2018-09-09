$(function(){
    var flag_user = false
    var flag_allow = true  // 开，复选框默认是选中的状态
    // alert(1)
    // 当用户输入完成的时候验证 -- 失去焦点的时候 blur
    // 验证用户：当失去焦点：获取用户输入的数据，列正则  if 正则test合法通过否则报错
    // $('#user_name').blur(function(){})
    // oUser.onclick = function(){}
    var $user_name = $('#user_name')
    $user_name.blur(function(){
        fnCheckUser()
    })
    // 验证用户名的函数
    function fnCheckUser(){
        // alert(1)
        var vals = $user_name.val()
        var re = /^\w{6,20}$/;
        if(vals == '')
        {
            $user_name.next().show().html('用户名不能为空！')
            flag_user = false
            return
        }


        if(re.test(vals))
        {
            // 合法 -- 隐藏错误
            $user_name.next().hide()
            // 开关设置的是false
            flag_user = true
        }
        else
        {
            // 不合法 -- 报错
            $user_name.next().show().html('用户名是6-20位数字、字母和下划线！')
            flag_user = false
        }
    }
    

    // 验证协议：单击就能勾选或者取消勾选 ，验证发生在click：如果勾选隐藏错误信息，否则报错
    var $allow = $('#allow')
    $allow.click(function(){
        // 条件勾选代码怎么写

        fnCheckAllow()
    })
    // 验证协议的函数
    function fnCheckAllow(){
        // alert($allow.prop('checked'))
        var myCheck = $allow.prop('checked')
        if(myCheck)
        {
            // 隐藏错误
            $allow.next().next().hide()
            flag_allow = true
        }else{
            // 报错
            $allow.next().next().show().html('请同意协议')
            flag_allow = false
        }
    }
    // 提交验证
    var $myform = $('#myform')
    $myform.submit(function(){
        // 如果验证合法 可以提交，否则不合法  return false
        // 有两种情况不能提交：1直接刷新页面就单击注册按钮； 如果正则还在发生报错不能提交
        // 定义开关全局变量，以上上中情况不能提交，开关feng以上两种情况都是关闭的，表示不提交；只在正则验证合法的地方打开开关表示可以提交 -- 在submit事件里面写if，如果开关打开提交否则不能提交
        // 如果所有开关都是true提交
        if(flag_user && flag_allow)
        {
            alert('ok')
            return true
        }else{
            alert('报错不能提交')
            return false
        }
    })
})
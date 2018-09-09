$(function(){
    // 思路：当用户输入完成后 验证，即失去焦点的时候 blur
    // 失去焦点后 获取用户的输入数据 列正则 加if判断

    // 定义开关 合法后开关打开，用于最后判断是否可以注册
    var flag_user = false
    var flag_password = false
    var flag_cpassword = false
    var flag_email = false
    var flag_allow = true

    // 1.验证用户名
    $('#user_name').blur(function(){
        fnCheckUser()
    })
    $('#user_name').focus(function(){
        $(this).next().hide();
    })
    // 定义验证用户名的函数
    function fnCheckUser(){
        var vals = $('#user_name').val();
        var re = /^\w{6,20}$/;
        // 判断 是否输入为空
        if(vals == ''){
            $('#user_name').next().show().html("用户名不能为空！")
            flag_user = false
            return 
        }
        if(re.test(vals)){
            $('#user_name').next().hide();
            flag_user = true;
        }
        else{
            $('#user_name').next().show().html('用户名是6-20位数字、字母和下划线！');
            flag_user = false;
        }
    }

    // 2.验证密码
    $('#pwd').blur(function(){
        fnCheckPwd();
    })
    $('#pwd').focus(function(){
        $(this).next().hide();
    })
    
    // 验证密码的函数
    function fnCheckPwd(){
        var re = /^[\@A-Za-z0-9\!\#\$\%\^\&\*\.\~]{6,22}$/;
        var vals = $('#pwd').val();

        if(vals == ""){         
            $('#pwd').next().html('密码不能为空！');           
            $('#pwd').next().show()
            flag_password = false;
            return

        }
        if(re.test(vals)){
            $('#pwd').next().hide();
            flag_password = true;
        }
        else{
            $('#pwd').next().show().html('密码是6-15位字母、数字，还可以包括！@#$%^&*字符');
            flag_password = false;
        }
    }

    // 3.确认密码是否正确
    $('#cpwd').blur(function(){
        fnCheckCpwd();
    })
    $('#cpwd').focus(function(){
        $('#cpwd').next().hide();
    })
    // 判断密码是否正确的函数
    function fnCheckCpwd(){
        if($('#cpwd').val() != $('#pwd').val()){
            $('#cpwd').next().show().html('两次输入的密码不一致');
             flag_cpassword = false;
        }
        else{
            $('#cpwd').next().hide();
             flag_cpassword = true;
        }
    }

    // 4.验证邮箱
    $('#email').blur(function(){
        fnCheckEmail();
    })
    $('#email').focus(function(){
        $('#email').next().hide();
    })
    // 判断邮箱是否正确的函数
    function fnCheckEmail(){
        var vals = $('#email').val()
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+\.[a-z]{2,5}$/;

        if(vals == ''){
            $('#email').next().show().html('邮箱不能为空！');
            flag_email = false;
            return

        }
        if(re.test(vals)){
            $('#email').next().hide();
            flag_email = true;
        }
        else{
           $('#email').next().show().html('你输入的邮箱格式不正确！')
           flag_email = false; 
        }
    }

    // 5.判断是否点击同意
    
    
    $('#allow').click(function(){
        var vals = $('#allow').prop('checked')
        if(vals){
            $(this).siblings('span').hide();
            flag_allow = true;
        }
        else{
            $(this).siblings('span').show().html('请勾选同意')
            flag_allow = false;
        }
    })

    // 6.判断注册是否可以点击
    $('#myform').submit(function(){
        if(flag_user  && flag_password && flag_cpassword && flag_email &&
        flag_allow ){
            alert('验证通过，可以提交！')
            return true;
        }
        else{
            alert('以上输入有误！')
            return false;
        }
    })
})
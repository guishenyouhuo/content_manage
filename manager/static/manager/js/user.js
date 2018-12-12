// 打开修改用户窗体
function modifyUser(userId, userName) {
    $('#modify_user_pwd_title').html("修改用户：" + userName + " 密码");
    $('#modify_user_modal').modal('show');
    // 设置用户ID
    $('#modify_user_id').val(userId);
}

// 表单提交处理
$("#modify_user_pwd_form").submit(function () {
    event.preventDefault();
    var newPassword = $.trim($("#user_pwd_new").val());
    var confirmPassword = $.trim($("#user_pwd_confirm").val());
    if (newPassword === null || newPassword === '') {
        $.alert({title: '警告!', content: '输入密码为空！'});
        return;
    }
    if (newPassword !== confirmPassword) {
        $.alert({title: '警告!', content: '两次输入密码不一致！'});
        return;
    }
    $.ajax({
        url: modify_user_pwd,
        type: 'POST',
        data: $(this).serialize(),
        cache: false,
        success: function (data) {
            if (data['status'] === 'SUCCESS') {
                window.location.reload();
            } else {
                $.alert({title: '错误!', content: '更新密码出现错误！'});
            }
        }
    });
});

// 修改用户状态
function changeUser(userId, userName, status) {
    var btnText = '';
    if (status === 1) {
        btnText = '停用';
    } else {
        btnText = '启用';
    }
    $.confirm({
        title: '确认' + btnText,
        content: '确认' + btnText + '用户：' + userName + ' ?',
        buttons: {
            confirm: {
                text: "确认",
                btnClass: 'btn-primary',
                keys: ['enter'],
                action: function () {
                    $.ajax({
                        url: change_user,
                        type: 'GET',
                        data: {
                            user_id: userId,
                            user_status: status
                        },
                        cache: false,
                        success: function (data) {
                            console.log(data);
                            if (data['status'] === 'SUCCESS') {
                                window.location.reload();
                            } else {
                                $.alert('操作失败！');
                            }
                        },
                        error: function (xhr) {
                            console.log(xhr);
                        }
                    });
                },
            },
            cancel: {
                text: "取消",
                keys: ['esc'],
                action: function () {

                },
            }
        }
    });
}

// 删除用户
function deleteUser(userId, userName) {
    $.confirm({
        title: '确认删除',
        content: '确认删除用户：' + userName + ' ? 删除后，用户所属资源将会同时删除，如需保留请先转移！',
        buttons: {
            confirm: {
                text: "确认",
                btnClass: 'btn-primary',
                keys: ['enter'],
                action: function () {
                    $.ajax({
                        url: delete_user,
                        type: 'GET',
                        data: {
                            user_id: userId
                        },
                        cache: false,
                        success: function (data) {
                            console.log(data);
                            if (data['status'] === 'SUCCESS') {
                                window.location.reload();
                            } else {
                                $.alert('操作失败！');
                            }
                        },
                        error: function (xhr) {
                            console.log(xhr);
                        }
                    });
                },
            },
            cancel: {
                text: "取消",
                keys: ['esc'],
                action: function () {

                },
            }
        }
    });
}
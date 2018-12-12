function intentChange(obj, object_id) {
    var isIntented = obj.getElementsByClassName('active').length !== 0;
    var title = '确认添加意向？';
    var content = '添加意向之后，可到意向组查看！';
    if (isIntented) {
        title = '确认移除意向？';
        content = '移除意向之后，意向组中查看不到该条留言！';
    }
    $.confirm({
        title: title,
        content: content,
        buttons: {
            confirm: {
                text: "确认",
                btnClass: 'btn-primary',
                keys: ['enter'],
                action: function () {
                    $.ajax({
                        url: intent_change,
                        type: 'GET',
                        data: {
                            object_id: object_id,
                            is_intented: isIntented
                        },
                        cache: false,
                        success: function (data) {
                            console.log(data);
                            if (data['status'] === 'SUCCESS') {
                                // 更新意向状态，更新操作文字
                                /*
                                var element = $(obj.getElementsByClassName('glyphicon-star'));
                                var operateText = $(obj.getElementsByClassName('intent-operate-text'));
                                if (isIntented) {
                                    element.removeClass('active');
                                    operateText.text('添加意向');
                                    isIntented = false;
                                    var title = "message_title";
                                    if (title === '我的意向组') {
                                        // 如果是意向组页面，需要将移除意向组的那条隐藏
                                        var messagesBody = $(obj).parents('.panel-body')[0];
                                        var messageDiv = $(obj).parents('.message')[0];
                                        messagesBody.removeChild(messageDiv);
                                        var messageCount = parseInt($('.message-count').text());
                                        messageCount--;
                                        $('.message-count').text(messageCount);
                                    }
                                } else {
                                    element.addClass('active');
                                    operateText.text('移除意向');
                                    isIntented = true;
                                }
                                */
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

// 用户列表全局变量
var userList = new Array();

function transToOther(eleObj, msgId, curUser) {
    if (eleObj.getElementsByClassName('trans-select').length !== 0) {
        return;
    }
    if (userList.length === 0) {
        $.ajax({
            url: get_user_list,
            type: 'GET',
            cache: false,
            data: {},
            success: function (data) {
                userList = data['user_list'];
                doTransUser(eleObj, msgId, curUser);
            },
            error: function (xhr) {
                console.log(xhr);
            }
        });
    } else {
        doTransUser(eleObj, msgId, curUser);
    }
}

function doTransUser(eleObj, msgId, curUser) {
    if (userList.length === 0) {
        return;
    }
    // 隐藏文字
    var textElem = $(eleObj).children('.trans-to-text')[0];
    $(textElem).addClass('div-hide');

    var selectHtml = '<select class="trans-select" name="trans-select" onChange="selectTransUser(this ,&quot;' + msgId + '&quot;)";>' +
        '<option value="---">--请选择--</option>';
    for (var i = 0; i < userList.length; i++) {
        var user = userList[i];
        if (user['id'] === curUser) {
            continue;
        }
        selectHtml += '<option value=' + user['id'] + '>' + user['username'] + '</option>';
    }
    selectHtml += '</select>';
    $(eleObj).append(selectHtml);
}

function selectTransUser(selObj, msgId) {
    var selectVal = $(".trans-select").val();
    if (selectVal === '---') {
        return;
    }
    var transDiv = $(selObj).parent('.trans-to')[0];
    var transText = $(transDiv).children('.trans-to-text')[0];
    var selectName = $(".trans-select").find("option:selected").text();
    var selUserId = $(".trans-select").find("option:selected").val();
    // var messageDiv = $(selObj).parents('.message')[0];
    $.confirm({
        title: '确认转移留言？',
        content: '请确认是否转移给' + selectName + '?',
        buttons: {
            confirm: {
                text: "确认",
                btnClass: 'btn-primary',
                keys: ['enter'],
                action: function () {
                    // Ajax请求后台进行更新
                    $.ajax({
                        url: move_message,
                        type: 'GET',
                        cache: false,
                        data: {
                            message_id: msgId,
                            user_id: selUserId
                        },
                        success: function (data) {
                            /*
                            $(messageDiv).remove();
                            var messageCount = parseInt($('.message-count').text());
                            messageCount--;
                            $('.message-count').text(messageCount);
                            */
                            window.location.reload();
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
                    $(selObj).remove();
                    $(transText).removeClass('div-hide');
                },
            }
        }
    });
}

//删除资源(移入回收站)
function deleteMessage(cliObj, msgId, messageStatus) {
    var titleText = '确认删除留言？';
    var contentText = '请确认是否删除此条资源？ 删除之后可以到回收站查看或恢复！';
    if (messageStatus === 0) {
        titleText = '确认恢复留言？';
        contentText = '请确认是否恢复此条资源？ 恢复之后即可对其进行正常操纵！';
    }
    $.confirm({
        title: titleText,
        content: contentText,
        buttons: {
            confirm: {
                text: "确认",
                btnClass: 'btn-primary',
                keys: ['enter'],
                action: function () {
                    // Ajax请求后台进行更新
                    $.ajax({
                        url: change_status,
                        type: 'GET',
                        cache: false,
                        data: {
                            message_id: msgId,
                            message_status: messageStatus
                        },
                        success: function (data) {
                            window.location.reload();
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

// 从回收站删除（永久删除！）
function emptyMessage(cliObj, msgId) {
    $.confirm({
        title: '确认彻底删除资源？',
        content: '请确认彻底删除此条资源？ 彻底删除后再也无法恢复！ 请谨慎操作！！！',
        buttons: {
            confirm: {
                text: "确认",
                btnClass: 'btn-primary',
                keys: ['enter'],
                action: function () {
                    // Ajax请求后台进行更新
                    $.ajax({
                        url: del_message,
                        type: 'GET',
                        cache: false,
                        data: {
                            message_id: msgId,
                        },
                        success: function (data) {
                            window.location.reload();
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

function intentComplete(obj, object_id) {
    var isCompleted = obj.getElementsByClassName('active').length !== 0;
    var title = '提示';
    var content = '确认将该客户标记为已完成？';
    if (isCompleted) {
        content = '确认将该客户恢复至未完成？';
    }
    $.confirm({
        title: title,
        content: content,
        buttons: {
            confirm: {
                text: "确认",
                btnClass: 'btn-primary',
                keys: ['enter'],
                action: function () {
                    $.ajax({
                        url: complete_change,
                        type: 'GET',
                        data: {
                            object_id: object_id,
                            is_completed: isCompleted
                        },
                        cache: false,
                        success: function (data) {
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
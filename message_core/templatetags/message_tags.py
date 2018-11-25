from django import template

register = template.Library()


@register.simple_tag()
def get_message_status(obj):
    if obj.type == 2:
        return 'active'
    else:
        return ''


@register.simple_tag()
def get_intent_operate(obj):
    if obj.type == 2:
        return '移除意向'
    else:
        return '添加意向'


@register.simple_tag()
def get_del_operate(obj):
    if obj.message_status == 0:
        return '恢复资源'
    else:
        return '删除资源'


@register.simple_tag()
def get_del_icon(obj):
    if obj.message_status == 0:
        return 'glyphicon-refresh'
    else:
        return 'glyphicon-trash'


@register.simple_tag()
def get_complete_operate(obj):
    if obj.type == 3:
        return '未完成'
    else:
        return '完成'


@register.simple_tag()
def get_complete_status(obj):
    if obj.type == 3:
        return 'active'
    else:
        return ''

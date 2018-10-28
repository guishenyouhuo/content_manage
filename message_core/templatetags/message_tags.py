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

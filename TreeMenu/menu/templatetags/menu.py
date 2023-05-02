from django import template

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    request = context.get('request')

    itemmenulist = []
    """Формируем для меню список пунктов меню"""

    menu = MenuItem.objects.filter(
        menu__name=name
    )

    try:
        active_menu_item = menu.get(pk=request.path[1:])
    except:
        level = 1
        active_menu_item = None
    else:
        level = active_menu_item.level
    menuitem=[]
    for menu_item in menu:
        if menu_item.level <= level and menu_item.level!=1:
            menuitem.append(menu_item)
        if menu_item.level==1:
            menuitem.append(menu_item)
    if active_menu_item:
        menuitem += active_menu_item.children.all()
    menuitem = sorted(
        menuitem, key=lambda menu_item: ( menu_item.position)
    )
    itemmenulist += menuitem
    return {'active_menu_item': active_menu_item, 'menu': itemmenulist}


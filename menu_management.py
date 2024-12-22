def Manmenu(menu, add_item=None, remove_item=None):
    if add_item:
        menu.append(add_item)
    if remove_item and remove_item in menu:
        menu.remove(remove_item)
    return menu

def availability(menu, item):
    return f"{item} is {'available' if item in menu else 'not available'}"

menu = ["Pizza", "Burger", "Pasta", "Salad"]
menu = Manmenu(menu, add_item="Tacos", remove_item="Salad")
print(f"Updated menu: {menu}")
print(availability(menu, "Pizza"))

# -*- coding:utf-8 -*-
def addToInventory(inventory, addedItems): # 更新背包
    c1 = {}
    for add in addedItems:  # 为boss 物品创立字典
        c1.setdefault(add, 0)
        c1[add] += 1
    for k in c1:    # 为新增的种类创建进字典
        if k not in inventory:  # 种类不在 inventory 里，setdefault
            c1.setdefault(k, 0)

        if k in inventory:  # 种类在，加数量
            c1[k] = c1[k] + inventory[k]
    for k in inventory: # 谈论原来就有的情况
        if k not in c1.keys():
            c1.setdefault(k, 0)
            c1[k] += 1

    return c1

def displayInventory(inv):
    for k, v in inv.items():
        print(str(v) + ' ' + k)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dragger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print('背包物品：')
displayInventory(inv)

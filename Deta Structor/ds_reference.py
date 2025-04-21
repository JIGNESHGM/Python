print("Simple Arguments")

shopping_list = ['milk', 'eggs', 'bread', 'butter']

mylist = shopping_list

del shopping_list[0]

print("My shopping list is now", mylist)

print('Copy by making a full slice')
mylist = shopping_list[:]

del mylist[0]
print("My shopping list is now", mylist)
print("My shopping list is now", shopping_list)
# This Is my shoping list

shoplist = ['apple', 'banana', 'Mengo', 'Chiku']

print('I have {0} items to purchase'.format(len(shoplist)))

print('These items are :')
for item in shoplist:
    print(item)

print("I have also by a rice")
shoplist.append("rice")
print(shoplist)

print("I have a short my list now")
shoplist.sort()
print(shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print ('I bought the', olditem)
print ('My shopping list is now', shoplist)

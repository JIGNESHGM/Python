# Set Declaration

bri = set(['brazil', 'russia', 'india'])

print('india' in bri)  # True  
print('usa' in bri)  # False


bric = bri.copy()
bric.add('china')
bric.issubset(bri)  # False
print(bric.issuperset(bri))  # True

bri.remove('brazil')    
print(bri & bric)
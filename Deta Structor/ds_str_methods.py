name = 'jignesh'

if name.startswith('jig '):
    print("Yes, the string starts with 'jig'")
    
if 'a' in name:
    print("Yes, it contains the character 'a'")
    
if name.find('g') != -1:   
    print("Yes, it contains the character 'g'")

delmin = name.split('_*_')
mylist = ['apple', 'mango', 'carrot', 'banana']
print('_*_'.join(mylist))
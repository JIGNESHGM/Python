# Variabels Declaration

zoo = ('Python', ' Hipopotemus', 'Elephent')

print('Number of elephonts in zoo {0}'.format(len(zoo)))

new_zoo = 'Monkey', 'Camel', zoo

print("Number of cages in the new zoo is {0}".format(len(new_zoo)))

print ('All animals in new zoo are', new_zoo)
print ('Animals brought from old zoo are', new_zoo[2])
print ('Last animal brought from old zoo is', new_zoo[2][2])
print ('Number of animals in the new zoo is', \
 len(new_zoo)-1+len(new_zoo[2]))

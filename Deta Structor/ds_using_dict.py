# 'ab' is short for 'a'ddress'b'ook


students = {'Name' : 'Jignesh',
            'Age': 22,
            'Email-Id' : 'jigneshmevada87@gmail.com',
            'MobileNumber' : 9638137734
            }

print("Studnet Email Address is {0}".format(students['Email-Id']))

del(students['Age'])

for Student_key, Studnet_values in students.items():
    print(Student_key,' : ', Studnet_values)
    
students['Age'] = 25

if 'Age' in students:
    print(students['Age'])
#python

names : list[str] = ['hikmat' , 'ihsan' , 'sir zia']

for name in names[:2]: # to iterate from back of list [::-1]
    print(f'Names: {names}')

#tuple
#Note: tuple is imutable not changable

databse : list[tuple[str,str]] = [('hikmat' , '123'),
                                   'zia' , '123'] 

#unziping tuple

for row in databse:     # note in python we can use else with for (but for that break is necessary otherwise else block will be run at the end)
    user, password = row
    print(user , password)
    print("valid user")
    break
else:
    print('user invalid')

#enumerate() function returns the indexes or makes list tuple

#comprehensive 
"""
used to less the code or comress the lines of code 

syntax:

[loop_body for item in items_list]
"""
#Slicing is always a deep copy
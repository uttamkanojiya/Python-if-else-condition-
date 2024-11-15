#program to use random module
import random
dice=random.randint(1,6)
print(dice)
if dice == 1:
    print('you can move one step')
elif dice == 2:
    print('you can move two steps')
elif dice == 3:
    print('you can move three steps')
elif dice == 4:
    print('you can move four steps')
elif dice == 5:
    print('you can move five steps')
else:
    print('you can move six steps')

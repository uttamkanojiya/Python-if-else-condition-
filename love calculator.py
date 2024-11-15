#program for love calculator
name1=(input("what is your name ?"))
name2=(input("what is his/her name ?"))
name3=name1+name2
name3.lower()
t=name3.count('t')
r=name3.count('r')
u=name3.count('u')
e=name3.count('e')
true=t+r+u+e
l=name3.count('l')
o=name3.count('o')
v=name3.count('v')
e=name3.count('e')
love=l+o+v+e
inst=int(str(true)+str(love))
if inst >=40 and inst <=80:
    print("your love score is ",inst,"and you both are alright together")
elif inst>10 or inst <90:
    print("your love score is ",inst,"and you both are like coke and mentos")
else:
    print("your love score is ",inst)

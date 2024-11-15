#pizza ordering program
print("UTTAM PIZZA WORLD")
print('small pizza = 100')
print('medium pizza = 200')
print('large pizza = 500')
print('pepperoni for small pizza = 30')
print('pepperoni for medium pizza or large pizza = 50')
print('extra cheese for any size pizza = 20')
bill=0
size=(input('what size pizza do you want ?'))
if size =='small pizza':
    #bill=bill+100
    #print('you have to pay bill',bill,'enjoy your meal')
    #want_pepperroni = (input('do you want pepperoni for pizza say (Y/N)'))
    #if want_pepperroni == 'Y' or want_pepperroni == 'y':
        bill +=100
        print('you have to pay',bill,'enjoy your meal')
    #else:
        #bill=bill+100
        #print('you have to pay',bill,'enjoy your meal')
    #want_extracheese = (input('do you want extra cheese for pizza say (Y/N)'))
    #if want_extracheese == 'Y' or want_extracheese == 'y' :
        #bill=bill+20+100
        #print('you have to pay',bill,'enjoy meal')
    #else:
        #bill=bill+1100
        #print('you have to pay',bill,'enjoy meal')
elif size == 'medium pizza':
    #bill=bill+200
    #print('you have to pay',bill,'enjoy meal')
    #want_pepperroni = (input('do you want pepperoni for pizza say (Y/N)'))
    #if want_pepperroni == 'Y' or want_pepperroni == 'y':
        #bill=bill+50+200
        #print('you have to pay',bill,'enjoy your meal')
    #else:
        #bill=bill+200
        #print('you have to pay',bill,'enjoy your meal')
    #want_cheese =(input('do you want extra cheese for your pizza say(Y/N)'))
    #if want_cheese == 'Y' or want_cheese == 'y':
        #bill=bill+20+200
        #print('you have to pay',bill,'enjoy your meal')
    #else:
        bill+=200
        print('you have to pay',bill,'enjoy your meal')
elif size == 'large pizza':
    #bill=bill+500
    #print('you have to pay',bill,'enjoy your meal')
    #want_pepperroni = (input('do you want peperoni for your pizza say (Y/N)'))
    #if want_pepperroni == 'Y' or want_pepperroni == 'y':
        #bill=bill+500+20
        #print('you have to pay',bill,'enjoy your meal')
    #else:
        #bill=bill+500
        #print('you have to pay ',bill,'enjoy your meal')
    #want_extracheese = (input(" do you want extea cheese for your pizza say (Y/N)"))
    #if want_extracheese == 'Y' or want_extracheese == 'y':
        #bill=bill+500+20
        #print('you have to pay',bill,'enjoy your meal')
    #else:
        bill+=500
        print('you have to pay',bill,'enjoy your meal')
else:
    print("you have entry a wrong input ,\n which is not valid ,\n please give proper input")
    print("INPUTS LIKE 'S for small pizza','m for medium pizza','l for large pizza'")
want_pepperoni=(input('do you want to add pepperoni for your pizza say (Y/N)'))
if want_pepperoni == 'y' or want_pepperoni == 'Y':
    if size == 'small pizza':
        bill+=30
    else:
        bill+=50
elif want_pepperoni == 'n' or want_pepperoni == 'N':
    if size == 'small pizza':
        bill+=0
    else:
        bill+=0
else:
    print("wrong input', plaese try again with correct input")
want_extracheese=(input('do you want to add extra cheese to your pizza say (Y/N)'))
if want_extracheese == 'Y' or want_extracheese == 'y':
    bill+=20
elif want_extracheese == 'N' or want_extracheese == 'n':
    bill+=0
else:
    print("wrong input', plaese try again with correct input")
print(f"your final bill is {bill}")





        

    









        

import random

userpoints=0
computerpoints=0

def getcmpch():
    choices=['stone','paper','scissor']
    index=random.randrange(0,len(choices))
    return choices[index]
#print(getcmpch())   use only for uppercode


def selectwinner(user,comp): 
    global userpoints
    global computerpoints
    if user==comp:
        return
    elif user=="stone" and comp=="paper":
        computerpoints +=1
        return
    elif user=="paper" and comp=="stone":
        userpoints += 1
        return
    elif user =="scissor" and comp=="stone":
        computerpoints += 1
        return
    elif user=="stone" and comp=="scissor":
        userpoints += 1
        return
    elif user=="paper" and comp=="scissor":
        computerpoints += 1
        return
    elif user=="scissor" and comp=="paper":
        userpoints += 1
        return 

userpoints=0
computerpoints=0
while userpoints<5 and computerpoints<5:
    print()
    userchoice=input("enter user choice: ")
    userchoice=userchoice.lower()
    if userchoice not in ['stone','paper','scissor']:
        print("incorrect choice")
        break
    computerchoice=getcmpch()
    print("\nyour choice: {}             computer choice:{}".format(userchoice,computerchoice))
    selectwinner(userchoice, computerchoice)
    print("user points: {}             computer points: {}". format(userpoints,computerpoints))


if userpoints>computerpoints:
    print("you win")
else:
    print("you lose")

















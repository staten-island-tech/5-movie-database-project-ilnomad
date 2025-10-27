import random
def realgambling100percent():
    b=0
    a=False

    while a==False:
        x=random.randint(1,100)
        y=random.randint(1,100)
        z=random.randint(1,100)
        if x==y==z:
            print("you got 0.0001% chance")
            a=True
            print(b)
            print(x,y,z)
        else:
            print("you didnt get it")
            b+=1
            print(x,y,z)

realgambling100percent()
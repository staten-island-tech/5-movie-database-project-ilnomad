def brokemartha(q,a,b,c):
    p=0
    while q>=1:
        if q>0:
            q-=1
            p+=1
            a+=1
            if a>=35:
                a=0
                q+=30
        if q>0:
            q-=1
            p+=1
            b+=1
            if b>=100:
                b=0
                q+=60
        if q>0:
            q-=1
            p+=1
            c+=1
            if c>=10:
                c=0
                q+=9
        print(q,a,b,c)
    print(f"Martha plays {p} times before going broke.")
brokemartha(77,4,9,3)


# import random
# def realgambling100percent():
#     a=False
#     while a==False:
#         if random.randint(1,10)==random.randint(1,10)==random.randint(1,10):
#             print("you got 1% chance")
#             a==True
#         else:
#             print("you didnt get it")

# realgambling100percent()
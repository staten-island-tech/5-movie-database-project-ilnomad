import json
movies = open("./movies.json", encoding="utf8")
movielist = json.load(movies)

def title():
    i=0
    for h in movielist:
        i+=1
        print(movielist[i]["title"])
def yearafter():
    z=0
    x=input("What year ")
    x=int(x)
    for h in movielist:
        if x<=movielist[z]["year"]:
            print(movielist[z]["title"])
        z+=1
def yearrange():
    x=int(input("Min "))
    y=int(input("Max "))
    z=0
    for h in movielist:
        if x<=movielist[z]["year"]<=y:
            print(movielist[z]["title"])
        z+=1
def yeargiven():
    x=int(input("Year given "))
    z=0
    for h in movielist:
        if x==movielist[z]["year"]:
            print(movielist[z]["title"])
        z+=1
def specificmovie():
    a=1
def genresearch():
    genres=input("genres ")
    z=0
    for h in movielist:
        if genres==movielist[z]["genres"]:
            print(movielist[z]["genres"])
        z+=1
genresearch()
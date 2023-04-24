from fastapi import FastAPI, HTTPException

from models.models import Person, Friend


def find_person_by_id(id:int, person:list[Person]):
    finallist = list(filter(lambda x: x.id == id, person))
    if len(finallist) >= 1:
        raise HTTPException(status_code=400, detail="Id already exist")
    return finallist
def validate_person(id:int, person:list[Person]):
    finallist = list(filter(lambda x: x.id == id, person))
    print ('validate', finallist)
    if len(finallist) < 1:
        raise HTTPException(status_code=400, detail="Id already exist")
    return finallist


def find_friend_by_id(friend:Friend, friends:list[Friend]):
    friends= list(filter(lambda x: x.id == id, friend))
    if len(friends) >= 1:
        raise HTTPException(status_code=400, detail="Id already exist")
    return friends
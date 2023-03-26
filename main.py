from fastapi import FastAPI, HTTPException

from models import Person, Friend
from persons import find_person_by_id, validate_person

app = FastAPI()
friends=[]
persons_lists=[]
@app.post("/friends",status_code=204)
async def create_friend(friend: Friend):
    validate_person(friend.idfrom, persons_lists)
    validate_person(friend.idto, persons_lists)
    friend_list= list(filter(lambda x: (x.idfrom == friend.idfrom and friend.idto==x.idto)or (x.idfrom==friend.idto and x.idto==friend.idfrom), friends))
    if len(friend_list)<=0:
        friends.append(friend)
    else:
        raise HTTPException(status_code=400, detail="invitacion no valida")
    return None

@app.get("/friends",status_code=200)
async def get1():
    return friends

@app.get("/persons",status_code=200)
async def get1():
    return persons_lists

@app.post("/persons/add/massive",status_code=202)
async def create_multiplate_person(person:list[Person]):
    erorr_person=[]
    for i in person:
        person_lists= list(filter(lambda x: x.id == i.id, persons_lists))
        if len(person_lists)<1:
            persons_lists.append(i)
        else:
            erorr_person.append(i)
    return erorr_person
@app.post("/persons",status_code=204)
async def create_person(person: Person):
    find_person_by_id(person.id, persons_lists)
    persons_lists.append(person)
    return person
@app.put("/persons/{id}")
async def put1(id: int,person: Person):
    if id!=person.id:
        raise HTTPException(status_code=400, detail="id not match ")
    finallist = list(filter(lambda x: x.id == id, persons_lists))
    if len(finallist) >= 1:
        finallist[0].name=person.name
        return {"person": finallist[0]}
    raise HTTPException(status_code=400, detail="Id ")
@app.patch("/persons")
async def patch1():
    return {"message": "Hello World"}
@app.delete("/persons/{id}")
async def delete1 (id:int):
    finallist = list(filter(lambda x: x.id!= id, persons_lists))
    return finallist


from fastapi import APIRouter, HTTPException

from models.models import Person
from models.persons import find_person_by_id
from utils import persons_lists

router = APIRouter(
    prefix='/persons',
    tags=['persons']
)


@router.get("/", status_code=200)
async def get_all_person():
    return persons_lists


@router.get("/{id}")
async def get(id: int):
    print(id)
    try:
        idfind = list(filter(lambda x: x.id == id, persons_lists))
        print(idfind[0])
        return idfind[0]
    except IndexError:
        raise HTTPException(status_code=404, detail="person not found")


@router.post("/add/massive", status_code=202)
async def create_multiplate_person(person: list[Person]):
    erorr_person = []
    for i in person:
        person_lists = list(filter(lambda x: x.id == i.id, persons_lists))
        if len(person_lists) < 1:
            persons_lists.append(i)
        else:
            erorr_person.append(i)
    return erorr_person


@router.post("/", status_code=204)
async def create_person(person: Person):
    find_person_by_id(person.id, persons_lists)
    persons_lists.append(person)
    return person


@router.put("/{id}")
async def put_person_by_id(id: int, person: Person):
    if id != person.id:
        raise HTTPException(status_code=400, detail="id not match ")
    finallist = list(filter(lambda x: x.id == id, persons_lists))
    if len(finallist) >= 1:
        finallist[0].name = person.name
        return {"person": finallist[0]}
    raise HTTPException(status_code=400, detail="Id ")


@router.patch("/")
async def patch_person_by_id(person: Person):
    finallist = list(filter(lambda x: x.id == person.id, persons_lists))
    if len(finallist) >= 1:
        finallist[0].name = person.name
        return {"person": finallist[0]}
    raise HTTPException(status_code=400, detail="Id ")


@router.delete("/{id}")
async def delete_person_by_id(id: int):
    finallist = list(filter(lambda x: x.id != id, persons_lists))
    return finallist

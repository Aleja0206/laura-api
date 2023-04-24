from fastapi import APIRouter, HTTPException

from main import persons_lists, friends
from models.models import Friend
from models.persons import validate_person

router = APIRouter(
    prefix='/friends',
    tags=['persons']
)


@router.post("/", status_code=204)
async def create_friend(friend: Friend):
    validate_person(friend.idfrom, persons_lists)
    validate_person(friend.idto, persons_lists)
    friend_list = list(filter(lambda x: (x.idfrom == friend.idfrom and friend.idto == x.idto) or (
            x.idfrom == friend.idto and x.idto == friend.idfrom), friends))
    if len(friend_list) <= 0:
        friends.append(friend)
    else:
        raise HTTPException(status_code=400, detail="invitacion no valida")
    return None

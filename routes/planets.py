from fastapi import APIRouter
from pydantic.main import BaseModel

router = APIRouter(
    prefix='/planets',
    tags=['persons']
)
planets = []

class Planet(BaseModel):
    name: str
    orderFromSun: int
    hasRings: bool

@router.get('/')
def all_planets():
    return planets


@router.post('/')
def add_planet(planet: Planet):
    planets.append(planet)
    return planets


@router.get('/{planet_id}')
def get_planet(planet_id: int):
    return planets[planet_id]


@router.delete('/{planet_id}')
def delete_planet(planet_id: int):
    planets.pop(planet_id)
    return planets

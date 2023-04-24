import csv
import os
from typing import List

from bson import ObjectId
from pydantic import BaseModel
from pydantic_mongo import AbstractRepository, ObjectIdField
from pymongo import MongoClient


class Foo(BaseModel):
    count: int
    size: float = None


class SurfaceTemperatureC(BaseModel):
    min: int = None
    max: int = None
    mean: int = None


class Planet(BaseModel):
    id: ObjectIdField = None
    name: str
    orderFromSun: int
    hasRings: bool
    surfaceTemperatureC: SurfaceTemperatureC
    mainAtmosphere: List[str]

    class Config:
        # The ObjectIdField creates an bson ObjectId value, so its necessary to setup the json encoding
        json_encoders = {ObjectId: str}


class PlanetRepository(AbstractRepository[Planet]):
    class Meta:
        collection_name = 'planets'
class ExportCsv():
    def __init__(self, name):
        self.name = name
    def filexist(self):
        isexist = os.path.exists(self.name)
        if 'csv' not in self.name:
            self.name = self.name + '.csv'
        if isexist:
            raise TypeError('El archivo ya existe')
        return
    def writercsv(self):
        with open(self.name, 'w') as csvfile:
            fieldnames = ['name', 'orderFromSun']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in database.planets.find():
                writer.writerow({'name': i['name'], 'orderFromSun': i['orderFromSun']})
        return

client = MongoClient(
   "BASE_URI")
database = client['sample_guides']

planet_repository = PlanetRepository(database=database)

data = planet_repository.find_by({'hasRings': True})
#for item in data:
#    print(item)

for i in database.planets.find({'hasRings': False}):
    print(i)
name=input('Ingrese nombre del archivo: ')

#export = ExportCsv(name)
#export.filexist()
#export.writercsv()
def create():
    saver=[Planet(
        name='alpha',
        orderFromSun=9,
        hasRings=False,
        mainAtmosphere=['nitrogen', 'oxygen', 'argon'],
        surfaceTemperatureC=SurfaceTemperatureC(min=5, max=10, mean=20)),

        Planet(
            name='alpha',
            orderFromSun=9,
            hasRings=False,
            mainAtmosphere=['nitrogen', 'oxygen', 'argon'],
            surfaceTemperatureC=SurfaceTemperatureC(min=5, max=10, mean=20))
    ]
    for i in saver:
        planet_repository.save(i)
    return
def deleated():
   delete_result= database.planets.delete_many({})
   print(delete_result)
deleated()
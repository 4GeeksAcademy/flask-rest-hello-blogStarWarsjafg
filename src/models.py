from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,ForeignKey,DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True,nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250),nullable=False)
    fisrtName:Mapped[str] = mapped_column(String(120),nullable=True)
    lastName:Mapped[str] = mapped_column(String(120),nullable=True)
    suscription_date:Mapped[datetime] = mapped_column(DateTime(),default=DateTime)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstName":self.fisrtName,
            "lastName" : self.lastName,
            "suscription_date" : self.suscription_date
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(20),nullable=False,unique=True)
    population:Mapped[str] = mapped_column(String(1000),nullable=True)
    weather:Mapped[str] = mapped_column(String(120),nullable=True)
    galaxy:Mapped[str] = mapped_column(String(120),nullable=True)

    def serialize(self):
        return{
            "id" :self.id,
            "name" : self.name,
            "population" : self.population,
            "weather" : self.weather,
            "galaxy": self.galaxy
        }
    
class Characters(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(120),unique=True,nullable=False)
    gender:Mapped[str] = mapped_column(String(50),nullable=True)
    height:Mapped[str] = mapped_column(String(20),nullable=True)
    specie:Mapped[str] = mapped_column(String(20),nullable=True)
    weapon:Mapped[str] = mapped_column(String(20),nullable=True)

    def serialize(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "ender" : self.gender,
            "height" : self.height,
            "specie" : self.specie,
            "weapon" : self.weapon
        }
    
class Favoritos(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'),nullable=False)
    planets_id:Mapped[int] = mapped_column(ForeignKey('planets.id'), nullable=True)
    characters_id:Mapped[int] = mapped_column(ForeignKey('characters.id'),nullable=True)

    def serialize(self):
        return{
            "id" : self.id,
            "user_id" : self.user_id,
            "planets_id" : self.planets_id,
            "characters_id" : self.characters_id
        }



 
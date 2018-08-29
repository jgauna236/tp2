import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Samples(Base):
    __tablename__ = 'samples'
    id=Column(Integer, primary_key=True)
    temperature=Column('temperature', Integer, default=0)
    humidity=Column('humidity', Integer, default=0)
    pressure=Column('pressure', Integer, default=0)
    windspeed=Column('windspeed', Integer, default=0)

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'  : self.id,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'pressure': self.pressure,
            'windspeed' : self.windspeed
        }


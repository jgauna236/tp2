
from models import Samples

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import json
import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "samples"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()

    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session


    def get_last_ten(self):
        """Retorna el último Sample"""
        session = self.get_session()
        samples = session.query(Samples).order_by(Samples.id.desc())[:10]
        session.close()
        return  [sample.serialize() for sample in samples]

    def get_promedio(self):
        """Retorna el último Sample"""
        session = self.get_session()
        samples = session.query(Samples).order_by(Samples.id.desc())[:10]
        session.close()
        t = 0
        h = 0
        p = 0
        ws = 0
        for s in samples:
            t += s.temperature
            h += s.humidity
            p += s.pressure
            ws+= s.windspeed
        promedios = {
            'temperature': t/10,
            'humidity': h/10,
            'pressure': p/10,
            'windspeed': ws/10
        }
        return  promedios

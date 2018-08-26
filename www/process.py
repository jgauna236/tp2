
from database import Database
from models import Samples

import random
import time
import signal
import sys
import pbd



class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True



def main(sample, session):
    killer = GracefulKiller()
    while(1):
         sample.temperature = random.randint(0,9)
         sample.humidity = random.randint(0,9)
         sample.pressure = random.randint(0,9)
         sample.windspeed = random.randint(0,9)
         """ aca no funca"""
         logging.debug()
        session.commit()
        print("temperatura:%s, humedad:%s, presión:%s, velocidad de viento:%s", sample.temperature, sample.humidity, sample.pressure, sample.windspeed)
        time.sleep(1)
        if killer.k8080ill_now:
            session.close()
            break


if __name__ == '__main__':    
    db = Database()
    session = db.get_session()
    sample = session.query(Samples)
    main(sample, session)
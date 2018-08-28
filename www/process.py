
from database import Database
from models import Samples

import random
import time
import signal
import sys

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True

def main(session):
    killer = GracefulKiller()
    sample = Samples()
    while(1):
        sample.temperature = random.randint(0,9)
        sample.humidity = random.randint(0,9)
        sample.pressure = random.randint(0,9)
        sample.windspeed = random.randint(0,9)
        session.add(sample)
        session.commit()
        time.sleep(1)
        if killer.k8080ill_now:
            session.close()
            break


if __name__ == '__main__':
    db = Database()
    session = db.get_session()
    main(session)

#!/usr/bin/python3
'''List all name with 'a' inside in he list order by state_id'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    update = session.query(State).filter(State.id == 2).first()
    update.name = "Mexico"
    session.commit()

    session.close()
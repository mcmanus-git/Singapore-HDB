import pandas as pd
from sqlalchemy import create_engine
from MyCreds.mycreds import Capstone_AWS_SG


class DatabaseHelpers:
    engine = create_engine(f'postgresql+psycopg2://{Capstone_AWS_SG.username}:{Capstone_AWS_SG.password}@{Capstone_AWS_SG.host}/Capstone', echo=False)
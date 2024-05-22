import psycopg2
from configparser import ConfigParser
from app.resources import queries as queries


def load_config(filename='app/resources/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config


def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def select(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(queries.selectAllFromFoodTable)
                queryresults = cur.fetchall()
                print(queryresults)
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def insert(config, insertquery: str) -> None:
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        # query = queries.insert_query("Bread", 1, 140)
        print("insertquery: ", insertquery)
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(insertquery)
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

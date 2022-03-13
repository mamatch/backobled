from databases import Database


# Connect the db
from utils.consts import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


async def connect_db():
    db = Database("postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME))
    await db.connect()
    return db


# disconnect
async def disconnect(db):
    await db.disconnect()


# query = "insert into table values (:name, ...)"
# values = {"name": value}
# values = [{}, {}]
async def execute(query: str, is_many: bool, values=None):
    """
    A function to insert rows in db
    :param query: The query to execute
    :param is_many: If there are many rows to insert
    :param values: values to insert
    :return:
    """
    db = await connect_db()
    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query, values)

    await disconnect(db)


async def fetch(query, is_one, values=None):
    """
    A function to fetch data from the db
    :param query: The query to execute
    :param is_one: If the result is s only one row
    :param values: The parameters
    :return: The rows fetched
    """
    db = await connect_db()
    if is_one:
        result = await db.fetch_one(query, values)
        if result is None:
            out = None
        else:
            out = dict(result)
    else:
        result = await db.fetch_all(query, values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                out.append(dict(row))
    await disconnect(db)
    return out


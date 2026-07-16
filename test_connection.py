print("Program Started")

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from config import DB_CONFIG

print("Imports Successful")

try:

    print("Creating URL...")

    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"]
    )

    print("Creating Engine...")

    engine = create_engine(connection_url)

    print("Connecting...")

    with engine.connect():
        print("✅ Connected Successfully!")

except Exception as e:
    print("❌ Connection Failed")
    print(e)

print("Program Finished")
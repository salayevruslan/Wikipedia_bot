import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="ruslan",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="wikipedia.bot")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE BOT
          (ID BIGINT  PRIMARY KEY     NOT NULL,
            FULL_NAME   VARCHAR(100)   NOT NULL,
            USERNAME VARCHAR(100) NULL ); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


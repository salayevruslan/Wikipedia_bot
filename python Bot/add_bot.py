import psycopg2
from psycopg2 import Error


def add_bot(ID , FULL_NAME , USERNAME):

    try:
        connection = psycopg2.connect(user="postgres",
                                    password="ruslan",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="wikipedia.bot")

        cursor = connection.cursor()
       
        create_table_query = ''' INSERT INTO BOT (ID , FULL_NAME , USERNAME ) VALUES(%s , %s , %s)'''
        cursor.execute(create_table_query,(ID , FULL_NAME , USERNAME))
      
        connection.commit()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# add_teble(45456465, 'ruslan' ,'ruslan_s')
import psycopg2
        
def queryDatabase(limitParameter):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()

        postgreSQL_insert_Query =  """INSERT INTO public."BitExenLiveDemo" ("marketcode","lastprice",dailyaverage,buyerorderprice,sellerorderprice) VALUES (%s,%s,%s,%s,%s);"""

        sql_select_query_1 = """select lastprice as LP from public."BitExenLiveDemo" ORDER BY Id DESC LIMIT %s  """

        sql_select_query_2 = """select dailyaverage as DA from public."BitExenLiveDemo" ORDER BY Id DESC LIMIT %s  """

        sql_select_query_3 = """select logtime as lc from public."BitExenLiveDemo" ORDER BY Id DESC LIMIT %s  """
        
        cursor.execute(sql_select_query_1, (limitParameter,))
        record_list_1 = list(cursor.fetchall())
        
        cursor.execute(sql_select_query_2, (limitParameter,))
        record_list_2 = list(cursor.fetchall())

        cursor.execute(sql_select_query_3, (limitParameter,))
        record_list_3 = list(cursor.fetchall())
        
##        print(record[0][1])
##        print(record_list_1)
        
        return record_list_1,record_list_2,record_list_3

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
            
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed log printed successfully")
            # closing database connection.
                
            
             

import psycopg2

class Database:
    def __init__(self, marketcode ,lastprice,dailyaverage,buyerorderprice,sellerorderprice):
        
        self.marketcode = marketcode
        self.lastprice = lastprice
        self.dailyaverage = dailyaverage
        self.buyerorderprice = buyerorderprice
        self.sellerorderprice = sellerorderprice
        
        try:
            connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
            cursor = connection.cursor()

            postgreSQL_insert_Query =  """INSERT INTO public."DB_NAME" ("marketcode","lastprice",dailyaverage,buyerorderprice,sellerorderprice) VALUES (%s,%s,%s,%s,%s);"""
            record_to_insert = (self.marketcode, self.lastprice, self.dailyaverage,self.buyerorderprice,self.sellerorderprice)

            cursor.execute(postgreSQL_insert_Query,record_to_insert)
            
            connection.commit()

            print("DB updated Successfully!")
            
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        # closing database connection.
             


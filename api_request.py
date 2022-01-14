import requests
import json
import schedule
import time
import sqlite3
import psycopg2
import sys
import os

sys.path.append(".")
from sql_demo_1 import Database
from SQL_QUERY_DataBase import queryDatabase
from graphicdemo_3 import animate

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class JSONObject:
  def __init__( self, dict ):
      vars(self).update( dict )
  
def job():
    response = requests.get("API_REQUEST_URL")
    
    res = json.loads(response.text)

    asd = json.dumps(res)
            
    jsonobject = json.loads( asd, object_hook= JSONObject)
    
    me = Object()
    
    me.market = jsonobject.data.market_code
    me.last_price = jsonobject.data.ticker.last_price
    me.avg_24h = jsonobject.data.ticker.avg_24h
    
    me.buyers = jsonobject.data.buyers[1].orders_price
    me.sellers = jsonobject.data.sellers[1].orders_price


    print(me.market)
    print(float(me.last_price))
    print(float(me.avg_24h))
    print(float(me.buyers))
    print(float(me.sellers))
    
    p1 = Database(me.market,float(me.last_price),float(me.avg_24h),float(me.buyers),float(me.sellers))

    

schedule.every(4).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)








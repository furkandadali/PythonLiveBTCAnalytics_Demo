import requests
import json
import schedule
import time
import sqlite3
import psycopg2
import sys
import os
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

sys.path.append(".")
from SQL_QUERY_DataBase import queryDatabase

x = []
index = count()


def animate(i):
    data = queryDatabase(5)
    x = data[1]
    y1 = data[0]

    plt.cla()
    plt.plot(x, y1, label='LastPrice')
##    plt.plot(x, y2, label='Daily Average')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

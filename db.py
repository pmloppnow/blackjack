# imports needed modules
from decimal import Decimal
from decimal import ROUND_HALF_UP
import sqlite3
from contextlib import closing

conn = None


# connects the program to the database
def connect():
    global conn
    conn = sqlite3.connect("session_db.sqlite")
    return conn


# disconnects the program from the database
def close():
    if conn:
        conn.close()


# finds the most recent session and returns a session object
def getLastSession():
    lastSession = """SELECT * FROM Session ORDER BY sessionID DESC"""
    with closing(conn.cursor()) as c:
        c.execute(lastSession)
        row = c.fetchone()
    return row


# creates a table called Session and calls getLastSession
def createSession():
    global conn
    createTable = """CREATE TABLE IF NOT EXISTS Session (sessionID INTEGER PRIMARY KEY, startTime TEXT, startMoney
    REAL, stopTime TEXT, stopMoney REAL)"""
    default = """INSERT INTO Session(sessionID, startTime, startMoney, stopTime, stopMoney) VALUES(0, 'x', 199, 'y', 
    199)"""
    c = conn.cursor()
    c.execute(createTable)
    session = getLastSession()
    if session is None:
        c.execute(default)
        conn.commit()


# inserts the input session into the Session table of the database
def addSessions(s):
    insert = """INSERT INTO Session (startTime, startMoney, stopTime, stopMoney) VALUES (?, ?, ?, ?)"""
    with closing(conn.cursor()) as c:
        c.execute(insert, s)
        conn.commit()

import threading
import datetime
from time import sleep
import mysql.connector
from send_notify import send


class Test:
    def __init__(self):
        self.running = True
        self.hundred_closest = []

    def send_call(self, closest):
        print(closest)
        send(closest['UserID'], closest['NoteText'])

    def get_nearest(self):
        while self.running:

            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor(dictionary=True)
            cursor.execute('SELECT `UserID`, `NoteText`, `NoteDate` FROM `notifies` WHERE `NoteDate` > CURRENT_TIMESTAMP')
            results = cursor.fetchall()
            results.sort(key=lambda k: k['NoteDate'])
            hundred_closest = results[:100]
            print(hundred_closest)
            self.hundred_closest = hundred_closest
            sleep(10)

    def schedule_nearest(self):
        while self.running:

            a = self.hundred_closest[0]['NoteDate']

            if a - datetime.timedelta(seconds=1) < datetime.datetime.now() < a + datetime.timedelta(seconds=1):
                print('aaa')
                message = self.hundred_closest[0]
                self.hundred_closest.pop(0)
                self.send_call(message)

    def go(self):
        th1 = threading.Thread(target=self.get_nearest)
        th2 = threading.Thread(target=self.schedule_nearest)
        th1.start()
        sleep(1)
        th2.start()


config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'port': 8889,
  'database': 'shiburibot',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(dictionary=True)

t = Test()
t.go()

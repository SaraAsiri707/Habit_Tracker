#Habit-tracker
class To_do_list:
    def __init__(self,nam):
        self.val=False
        self.nam=nam
    def mark_done(self):
        ask=input(f'Did you complete {self.nam} today?')
        if ask.lower() =='yes' :
            self.val=True
            print(self.nam,'done')
        elif ask.lower() =='no' :
            self.val=False
            print(self.nam,'not complete')
        else:
            print('Please enter yes or no')

first_habit=To_do_list('python')
second_habit=To_do_list('English')
third_habit=To_do_list('Quran')

habits=[]
habits.append(first_habit)
habits.append(second_habit)
habits.append(third_habit)
for habit in habits:
    habit.mark_done()

#create date 
from datetime import date
today=date.today().isoformat()

#create DB to store prograss
import sqlite3
connection=sqlite3.connect('HabitDB')
cur=connection.cursor()
#1_CREATE HABIT TABLE:
cur.execute('CREATE TABLE IF NOT EXISTS Habit(id INTEGER PRIMARY KEY,name TEXT UNIQUE)')

#2_CREATE HABIT_LOG TABLE
cur.execute('CREATE TABLE IF NOT EXISTS Habit_log(Habit_id INTEGER,date DATE,completed INTEGER,PRIMARY KEY (Habit_id, date))')
for habit in habits:
    cur.execute('INSERT OR IGNORE INTO Habit(name) VALUES (?)',(habit.nam, ))
    cur.execute('SELECT id FROM Habit WHERE name =?',(habit.nam,))
    habit_id=cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Habit_log(Habit_id,date,completed) VALUES (?,?,?)',(habit_id,today,habit.val ))
connection.commit()
cur.execute('SELECT * FROM Habit_log')
print(cur.fetchall())
connection.close()

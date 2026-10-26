# Habit Tracker 

### Why I built it
I wanted a program to store my daily habits so I can look back later and see my progress. I decided to build it using the new concepts I learned in Python, especially OOP and SQLite.

### How it works
I chose three habits to track: Python, English, and Quran. The program asks me if I completed each habit today, then saves my answer with the date.

### What I used
- **OOP:** I created a class for my habits, with a name and a completion status. Then I created an object for each habit.
- **Lists and loops:** I stored my habits in a list and used a loop to go through them one by one.
- **Dates:** I used Python's `datetime` module to get today's date and save it with each record.
- **SQLite:** I created two tables: `Habit` to store habit names and IDs, and `Habit_log` to store the daily progress.
- **SQL:** I used `CREATE TABLE`, `INSERT`, and `SELECT` to create tables, save data, and retrieve records. I also used `INSERT OR IGNORE` to avoid duplicate habits and `INSERT OR REPLACE` to update a habit's status for the same day.

### What I learned
This project helped me understand how OOP and SQLite work together. I also learned how to keep records for different days instead of just storing the current status.

It's a simple project, but I enjoyed building something useful for myself and practicing the new concepts I learned. I'm happy with what I've learned so far, and I hope to improve it as I learn more. 

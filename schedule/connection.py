import psycopg2
from random import randint
connection = psycopg2.connect(
    dbname="dreamteam4",
    host="localhost",
    user="dtuser",
    password="qwerty123456"
)
cursor = connection.cursor()
week_days = (('Понедельник', 'danger'), ('Фторник', 'info'), ('Среда', 'warning'), ('Четверг', 'success'), ('Жума', 'primary'), ('Суббота', 'dark'))
class_names = ('Математика','Английский язык','Кыргыз тили','Русский язык','Биология','Химия','Физкультура')
teachers = ('Joomart', 'Daniyar', 'Ermek', 'Adinai', 'Atai', 'Aibek', 'Alymbek', 'Liazat', 'Salavat', 'Bolot', 'Aslan')
start_times = ('08:00','08:30','09:00','09:30','10:00')
room_numbers = ('105', '101', '102', '100', '107', '109', '104')
class_numbers = ('11 А', '11 Б', '1 Г', '10 М', '9 Е', '8 А', '5 В', '3 Г', '9 Н', '9 А', '7 Б')
for i in range(0,len(week_days)):
    days_query = f''' INSERT INTO week_days (day_name, css_background)
VALUES (
'{week_days[i][0]}',
'{week_days[i][1]}'
);'''
cursor.execute(days_query)
connection.commit()
for _ in range(24):
    lesson_query = f'''INSERT INTO lessons (
day_id,
class_name,
teacher_name,
class_start_time,
room_number,
class_number
)
VALUES (
'{randint(1,len(week_days))}',
'{class_names[randint(0,len(class_names) - 1)]}',
'{teachers[randint(0,len(teachers) - 1)]}',
'{start_times[randint(0,len(start_times) - 1)]}',
'{room_numbers[randint(0,len(room_numbers) - 1)]}',
'{class_numbers[randint(0,len(class_numbers) - 1)]}'
);'''
cursor.execute(lesson_query)
connection.commit()
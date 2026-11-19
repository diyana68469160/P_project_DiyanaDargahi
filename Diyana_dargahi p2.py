import sqlite3
db=sqlite3.connect('QuizGame.db')
cursor=db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER
)
''')
db.commit()




menu={
      '1':'Math Quiz',
      '2':'Geography Quiz',
      '3':'Exit'
      }

Math_Quiz={
    ' 100 - 1 =  ': '99',
    '24 + 24 = ': '48',
    '10 - 3 + 4 = ':'11'
   }


Geography_Quiz={  
    'Capital of Iran?':['Tehran','tehran'],
    'Capital of Freance?':['Paris','paris'],
    'Capital of japan?':['Tokyo','tokyo']
    }

print('Welcome to Quiz Game!')
name=input('Enter name please:')
print('Menu:')

for key in menu:
    print(key,'-',menu[key])


person=input('Select an option:').strip()
score=0

if person=='1':
    for question in Math_Quiz:
        answer=input(question)
        if answer==Math_Quiz[question]:
            print(' True')
            score+=34
        else:
            print('False!')
            
elif person=='2':
    for question in Geography_Quiz:
        answer=input(question)
        if answer in Geography_Quiz[question]:
            print('True')
            score+=34
        else: 
            print('False!')
elif person=='3':
    print('Exiting the Game....')
print('Your score:', score)
print(name,'tanks for play Game.')

cursor.execute(
    'INSERT INTO players (name,score) VALUES (?, ?)',
    (name,score)
)
db.commit()

cursor.execute('SELECT * FROM players')
result=cursor.fetchall()

for player in result:
    print(player)
 
db.close()
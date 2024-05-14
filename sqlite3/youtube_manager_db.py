import sqlite3

con=sqlite3.connect('youtube videos.db')

cursor=con.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY,
                   name NOT NULL,
                   time NOT NULL
               )
               ''')

def list_all_videos():
    cursor.execute('SELECT * FROM videos')
    print('\n')
    print('*'*70)
    print('\n')
    for row in cursor.fetchall():
        print(f'{row[0]}. {row[1]}, duration: {row[2]}')
    print('\n')
    print('*'*70)

def add_video():
    name=input('Enter the video name: ')
    time=input('Enter the video duration: ')
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)',(name, time))
    con.commit()
    print('\n')
    print('SUCCESS : Video added SuccessFully')

def update_video():
    video_id=input('Enter the video ID to update: ')
    new_name=input('Enter the video name to update: ')
    new_time=input('Enter the video duration to update: ')
    cursor.execute('UPDATE videos SET name=?, time=? WHERE id=?',(new_name,new_time,video_id))
    con.commit()
    print('\n')
    print('SUCCESS : Video updated SuccessFully')

def delete_video():
    video_id=input('Enter the video ID to update: ')
    cursor.execute('DELETE FROM videos WHERE id=?',(video_id,))
    con.commit()
    print('\n')
    print('SUCCESS : Video deleted SuccessFully')

def main():
    while True:
        print('\n')
        print('Youtube Videos Manager | Select the option')
        print('1. list all youtube videos')
        print('2. add youtube video')
        print('3. update youtube video')
        print('4. delete youtube video')
        print('5. Exit the program')
    
        choice=input('Enter your Choice: ')
    
        match choice:
          case '1':
                list_all_videos()
          case '2':
                add_video()
          case '3':
                update_video()
          case '4':
                delete_video()
          case '5':
               break
          case _:
                print('Invalid Choice')

    con.close()
    
if __name__=='__main__':
    main()
    
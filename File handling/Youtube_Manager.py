
import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('\n')
    print('*'*70)
    print('\n')
    for index,video in enumerate(videos, start=1):
        print(f'{index}. {video['name']}, Duration: {video['time']}')
    print('\n')
    print('*'*70)
        
    
def add_video(videos):
    name=input('Enter the video name: ')
    time= input('Enter the video duration: ')
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)
    print('\n')
    print('SUCCESS : Video added SuccessFully')

def update_video(videos):
    list_all_videos(videos)
    index=int(input('Enter the video number to update: '))
    if 1<=index<=len(videos):
        name=input('Enter the new video name: ')
        time=input('Enter the video duration: ')
        videos[index-1]={'name':name, 'time':time}
        save_data_helper(videos)
        print('\n')
        print('SUCCESS : Video updated SuccessFully')
    else:
        print('\n')
        print('Invalid video index selected')

def delete_video(videos):
    list_all_videos(videos)
    index=int(input('Enter the video number to be deleted: '))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print('\n')
        print('SUCCESS : Video deleted SuccessFully')
    else:
        print('\n')
        print('Invalid video index selected')

def main():
    videos=load_data()
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
                list_all_videos(videos)
          case '2':
                add_video(videos)
          case '3':
                update_video(videos)
          case '4':
                delete_video(videos)
          case '5':
               break
          case _:
                print('Invalid Choice')
    
if __name__=="__main__":
    main()
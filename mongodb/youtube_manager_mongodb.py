import pymongo # type: ignore
from bson import ObjectId

client=pymongo.MongoClient("mongodb+srv://<username>:<password>@projects.2bn8u5r.mongodb.net/", tlsAllowInvalidCertificates=True)

# print(client)
db=client['ytManager']
video_collection=db['videos']

def list_all_videos():
     for video in video_collection.find():
         print(f'id: {video['_id']}. name: {video['name']}, duration: {video['time']}')

def add_video():
    name=input('Enter the video name: ')
    time=input('Enter the video duration: ')
    video_collection.insert_one({'name':name, 'time':time})

def update_video():
    video_id=input('Enter the video id to update: ')
    new_name=input('Enter the new video name: ')
    new_time=input('Enter the updated video duration: ')
    video_collection.update_one({'_id':ObjectId(video_id)},{'$set':{'name':new_name, 'time':new_time}})

def delete_video():
    video_id=input('Enter the video id to delete: ')
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main():
    while True:
        print('\nYoutube Manager App | Enter your choice')
        print('1. List all videos')
        print('2. Add a new videos')
        print('3. Update a video')
        print('4. Delete a video')
        print('5. Exit the App')
        choice=input('Enter your choice: ')
        
        if choice=='1':
            list_all_videos()
            
        elif choice=='2':
            add_video()
        elif choice=='3':
            update_video()
        elif choice=='4':
            delete_video()
        elif choice=='5':
            break
        else:
            print('Invalid Choice | Try again')
        
if __name__=='__main__':
    main()

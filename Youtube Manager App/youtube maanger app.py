"""
1.Video list 
2.Add Video
3.Delete Video
4.Update Video
5.Exit video
"""
import json

file_name = "youtube.txt"

def load_data():
    try:
        with open(file_name) as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#? save , add , update data using this function
def save_data_helper(videos):
    with open (file_name, "w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
        print(f"{index} : {video["name"] , video["time"]}")

def add_videos(videos):
    videoName = input("Enter video Name : ")
    videoTime = input("Enter video Time : ")
    videos.append({"name" : videoName , "time" : videoTime })
    save_data_helper(videos)
    

def update_Videos(videos):
    index = int(input("choose which video to update from the list : "))-1
    updateData = input("Choose any one to update : name or time ? ")
    match updateData:
        case "name":
            videos[index][updateData] = input("Enter updated video name : ")
        case "time":
            videos[index][updateData] = input("Enter updated video time : ")
    save_data_helper(videos)

def delete_Video(videos):
    index = int(input("choose which video to delete from the list : "))
    videos.pop(index-1)
    save_data_helper(videos)


def main():
    videos = load_data()
    while True:
        print(f"\n Youtube Video Manager || Choose and Option ")
        print(f"1. List all youtube videos")
        print(f"2. Add a youtube video ")
        print(f"3. Update a youtube video details ")
        print(f"4. Delete a video ")
        print(f"5. Exit the app ")
        choose = input("Enter your choice  1-5 : ")

        match choose:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_Videos(videos)
            case '4':
                delete_Video(videos)
            case '5':
                break
            case _:
                print("Invalid choice!!!!!!!!!!!!")
#! Dunder 
if __name__ == "__main__":
    main()
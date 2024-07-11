import json

def load_data():
    try:
        with open("data.txt","r") as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open("data.txt","w") as file:
        json.dump(videos, file)
        
            
def list_all_videos(videos):
    print("\n")
    print("*-"*76)
    
    for index , video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]} duration = {video["time"]}")
    print("\n")
    print("*-"*76)    

def add_video(videos):
    name=input("enter the name of the video")
    time = input("enter the duration of the video")
    videos.append({"name":name ,"time":time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video no to update =>"))
    if 1<= index <= len(videos):
        name = input("enter the name of video")
        time = input("enter the duration of the video")
        videos[index-1] = {"name":name,"time":time}
        save_data(videos)
    else:
        print("invalid input")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video no to update =>"))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("invalid")



def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("inavali choice")
                
if __name__ == "__main__":
    main()
    
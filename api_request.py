import requests
import json

# def fetch_random_user_freeapi():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/"

#     response = requests.get(url)
#     data = response.json()

#     if data["success"] and "data" in data:
        
#         userData = data["data"]
#         userName = userData["data"][1]["login"]["username"]
#         country = userData["data"][1]["location"]["country"]
#         print("Request in process")
#         return (userName,country)
    
#     else:
#         raise Exception("Failed to fetch user data")

# def main():
#     try:
#         username , country = fetch_random_user_freeapi()
#         print(f"user name = {username} , country = {country}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()



url = "https://api.freeapi.app/api/v1/public/randomproducts"

response = requests.get(url)
data = response.json()

load_data = data["data"]["data"]

for i in load_data:
    # print(f"{i["title"]}")
    print(f"title : {i["title"]}")
    print(f"price : {i["price"]}")
    print(f"rating : {i["rating"]}")
    print(f"*"*70)






import json
# Create a program capable of displaying questions to the user like KBC



# with open("game_bank.txt") as file:
#     bank = json.load(file)
#     for i in bank:
#         print(i["question"])

def play_game(gameFile):
    win_amount = 0
    print("Who Wants to Be a Millionaire?")
    with open(gameFile) as file:
        bank = json.load(file)
        for i in bank:
            print(i["question"])
            print("Your Options are : ")
            print(i["options"])
            answer = input("Select A, B ,C , D : ")
            if answer.upper()== i["answer"]:
                win_amount += 5000
                print(f"Congratulations You have won ${win_amount}")
            else:
                print(f"Your take home winning amount is ${win_amount}")
                break
  
play_game("game_bank.txt")


            # match answer.upper():
            #     case "D":
            #         win_amount += 5000
            #         print(f"Congratulations You have won ${win_amount}")
            #     case "C":
            #         win_amount += 5000
            #         print(f"Congratulations You have won ${win_amount}")
            #     case "A":
            #         win_amount += 5000
            #         print(f"Congratulations You have won ${win_amount}")
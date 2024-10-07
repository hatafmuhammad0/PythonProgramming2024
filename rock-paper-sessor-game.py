import random



def game(rounds):
    BotScore = 0
    Player_Score = 0
    totalGames = 0
    Weapons = {
        1 : "rock",
        2 : "paper",
        3 : "sessor"
    }
    while ((totalGames < rounds) and (BotScore < 3) and (Player_Score <3)):

        BotPlay = Weapons[random.randint(1,3)]
        PlayerPlay = Weapons[int(input("Choice number 1 = Rock , 2 = Paper , 3 = Sessor : "))]
        
        if BotPlay=="rock" and PlayerPlay == "sessor":
            BotScore +=1
            print(f"Bot wins {BotPlay} and score of Bot is : {BotScore}")
            totalGames += 1
        elif BotPlay=="paper" and PlayerPlay == "rock":
            BotScore +=1
            print(f"Bot wins {BotPlay} and score of Bot is : {BotScore}")
            totalGames += 1
        elif BotPlay == PlayerPlay:
            print(f"Same Tool ====>  Bot : {BotPlay} and player 2 : {PlayerPlay}")
            totalGames += 1
        else:
            Player_Score +=1
            print(f"Player 2 wins and score of player 2 is : {Player_Score}")
            totalGames += 1
    print(f"Bot Score : {BotScore} , Player Score {Player_Score} and Game rounds : {totalGames}")


game(5)
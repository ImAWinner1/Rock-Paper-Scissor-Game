#this is a Game!.............
# Rock .....  Paper .......... Scissers ..... Game

print('rock...')
print('paper...')
print('scissers...')
player_1 = input('Enter player_1 : ')
player_2 = input('Enter player_2 : ')
if player_1 == "rock" and player_2 == "scissers":
    print("player_1 is wins...")
elif player_1 == "rock" and player_2 ==  "paper":
    print("player_1 is lost...") 
elif player_1 == "paper"  and player_2 == "rock":
    print("player_1 is wins...")
elif player_1 == "paper" and player_2 == "scissers":
    print("player_1 is wins...")
elif player_1 == "scissers" and player_2 == "rock":
    print("player_1 is lost...") 
elif player_1 == "scissers" and player_2 == "paper":
    print("player_1 is wins...")  
elif player_1 == player_2:
    print("you are tie...")
else:
    print(" somthing is wrong...")             

import random

choose = {
    1:"snake",
    2:"water",
    3:"gun"
}

while True:
    print("1.snake")
    print("2.water")
    print("3.gun")
    print("4.exit")

    user = int(input("enter your move: "))

    if user == 4:
        print("thanks for playing the game")
        break

    if user not in [1,2,3]:
        print("choose correct move")
        continue

    computer_move = random.choice([1,2,3])
    print("Computer chose:", computer_move)
    if user == computer_move:
        print("its a draw")
        continue

    if user == 1 and computer_move == 3:
        print("you lose")
    elif user == 2 and computer_move == 1:
        print("you lose")
    elif user == 3 and computer_move == 2:
        print("you lose")
    else:
        print("you won")







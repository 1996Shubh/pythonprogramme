import random
winning_number = random.randint(1,100)
n=int(input("enter a number btwn 1 and 100"))
game_over=False
guess=1
while not game_over:
    if n==winning_number:
        print(f"you win,and u win in {guess}  guess")
        game_over=True
    else:
        if winning_number>n:
            print("too low")
            guess+=1
            n=int(input('input again'))
        else:
            print('too high')
            guess+=1
            n=int(input('input again'))

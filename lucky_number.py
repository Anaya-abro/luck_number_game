import random

print("💫welcome to lucky number game💫")
while True:
 computer = random.randint(1,5)
 user_guess = int(input('Enter your lucky guess number🤞🍀:(1 to 5)'))

 if user_guess == computer:
    print(f'You win 🎉 | You chose {user_guess}, computer chose {computer}')
    

 else:
    print(f'you lose 😟 | You chose {user_guess}, computer chose {computer}|')
    continue

 play_again = input('Do you want to play again(Yes/No) ').lower()
 if play_again == 'no':
   print("Thank you for playing! ")
   break




















import random

number = random.randint(1, 100)

num_of_guesses = 0

while True:

   guess = int(input("1부터 100까지의 숫자를 입력하세요: "))

   num_of_guesses += 1

   if guess > number:
    print("입력한 숫자가 너무 큽니다.")

   elif guess < number:
      print("입력한 숫자가 너무 작습니다.")

   else:
     print(f"축하합니다! {num_of_guesses}회 만에 숫자를 맞췄습니다.")
     break 
   
   
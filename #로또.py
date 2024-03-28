#로또
import random

lotto = []
random_num = random.randint(1, 45)

for i in range(6):
   while random_num in lotto:
      random_num = random.randint(1, 45)
lotto.append(random_num)

lotto.sort()
print("로또번호: {}".format(lotto))
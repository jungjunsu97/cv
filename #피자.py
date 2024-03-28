#피자
print("파이썬 피자에 오신것을 환영합니다!")ㄴs
size = input("원하는 피자 사이즈가 무엇인가요? S,M, L >")
price = 0


if (size == 'S'):
      price = 15000
elif(size == 'M'):
      price = 20000
else:
      price= 30000            
pepperoni = input("페퍼로니 추가를 원하시나요? Y or N > ").upper()
cheese = input("치즈 추가를 원하시나요? Y or N > ").upper()

if(cheese == 'Y'):
      price += 3000
if(pepperoni == 'Y'):
      price += 2000

print(f'총 지불하실 금액은 {price}원 입니다.')
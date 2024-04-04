rate=0

def get_fixed_price(price):
    return int(price/(1-rate/100))


rate=int(input('할인율은? '))
price=int(input('A 상품의 할인된 가격은? '))
Aprice=get_fixed_price(price)
price=int(input('B 상품의 할인된 가격은? '))
Bprice=get_fixed_price(price)

print('A 상품의 정가는', Aprice,'원')
print('B 상품의 정가는', Bprice,'원')

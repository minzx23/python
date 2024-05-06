shopping_bag=[]
nums={}
while True:
    item=input('상품명? ')
    if item=='':
        break
    else:
        shopping_bag.append(item)
        num=int(input('수량은? '))
        nums[item]=num
        
        print(f'장바구니에 {item} {nums.get(item)}개가 담겼습니다.')
        print()

print(f'>>>장바구니 보기: {nums}')
print()

find_item=input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{find_item}은(는) {nums.get(find_item)}개 담겨 있습니다.')

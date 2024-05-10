def buy(dic):
    item=input('상품명? ')
    if item=='':
        return False
    
    num=int(input('수량은? '))
    dic[item]=num
    print(f'장바구니에 {item} {dic.get(item)}개가 담겼습니다.')
    print()

def show(dic):
    print(f'>>>장바구니 보기: {dic}')
    print()

def find(dic):
    find_item=input('장바구니에서 확인하고자 하는 상품은? ')
    if find_item in dic:
        print(f'{find_item}은(는) {dic.get(find_item)}개 담겨 있습니다.')
    else:
        print(f'{find_item}은(는) 없습니다.')

shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break
show(shopping_bag)
find(shopping_bag)

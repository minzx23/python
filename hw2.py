def exchange(money):
    w500=money//500
    money=money%500
    w100=money//100
    money=money%100
    w50=money//50
    money=money%50
    w10=money//10

    print('500원 동전의 개수:',w500)
    print('100원 동전의 개수:',w100)
    print('50원 동전의 개수:',w50)
    print('10원 동전의 개수:',w10)


def get_integer(prompt):
    return int(input(prompt))

money=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(money)

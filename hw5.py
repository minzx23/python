def read_single_digit(n):
    if n == 1:
        return '일'
    elif n == 2:
        return '이'
    elif n == 3:
        return '삼'
    elif n == 4:
        return '사'
    elif n == 5:
        return '오'
    elif n == 6:
        return '육'
    elif n == 7:
        return '칠'
    elif n == 8:
        return '팔'
    elif n == 9:
        return '구'
    else:
        return '영'

def read_number(num):
    hundred = num // 100
    ten = (num % 100) // 10
    one = num % 10

    result = ""
    
    if hundred > 0:
        result += read_single_digit(hundred)
    if ten > 0:
        result += read_single_digit(ten)
    else:
        result += "영"
    if one > 0:
        result += read_single_digit(one)
    else:
        result += "영"

    return result

num = int(input('세 자리 정수 입력: '))
if num < 10:
    print(read_single_digit(num))
else:
    print(read_number(num))

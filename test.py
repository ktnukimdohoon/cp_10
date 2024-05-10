import random

def generate_lotto_numbers():
    lotto_numbers = []
    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)
        if number not in lotto_numbers:
            lotto_numbers.append(number)
    lotto_numbers.sort()
    a = "생성된 로또번호는 "
    b = ' '.join(map(str, lotto_numbers))
    c = " 입니다."
    return a + b + c

print(generate_lotto_numbers())
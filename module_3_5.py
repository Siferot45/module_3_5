
def get_multiplied_digits(number):
    
    str_number = str(number)
    
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Проверка если последнее число 0 то заменяем его 1 
        # # Примечание: топорно зато быстро и работает по тз =)
        if first == 0:
            first = 1
        return first



result = get_multiplied_digits(400000200000003000000)
print(result)

     
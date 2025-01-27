from os.path import exists


def djmax_condition01(number_rate1, number_rate2):
    total_rate = format((number_rate1 + (number_rate2 / 100)) - 20, ".4f")
    return total_rate


def djmax_condition02(number_rate1, number_rate2):
    total_rate = number_rate1 + number_rate2
    total_rate_removezero = list(total_rate.replace("0",""))
    count = {}
    for i in total_rate_removezero:
        try:
            count[i] += 1
        except:
            count[i] = 1
    max_count = int(count.get(max(count, key=count.get)))
    if max_count == 4:
        return '100.0000'
    elif max_count == 3:
        return '75.0000'
    elif max_count == 2:
        return '50.0000'
    else:
        return '25.0000'

def djmax_condition03(number_rate1, number_rate2):
    total_rate = number_rate1 + number_rate2
    count = {}
    for i in total_rate:
        try:
            count[i] += 1
        except:
            count[i] = 1
    print(count)
    collection_count = 5 - int(count.get(max(count, key=count.get)))
    if total_rate == '10000':
        return '50.0000'
    else:
        if collection_count == 4:
            return '100.0000'
        elif collection_count == 3:
            return '75.0000'
        elif collection_count == 2:
            return '50.0000'
        else:
            return '25.0000'

def djmax_condition04(number_rate1, number_rate2):
    return format(abs(number_rate1 - number_rate2), ".4f")


def djmax_condition05(number_break):
    if number_break != 0:
        return '0.0000'
    else:
        return '100.0000'


def djmax_condition06(number_break, number_max90):
    if number_break >= 10:
        return '0.0000'
    else:
        result = number_break * number_max90
        if result >= 100:
            return '100.0000'
        else:
            return format(result, ".4f")

def djmax_condition07(number_keymode, number_max100, number_max90, number_max80, number_max70, number_max60, number_max50, number_max40, number_max30, number_max20, number_max10, number_max1, number_break):
    exists_number_max100 = 0 if number_max100 == 0 else 1
    exists_number_max90 = 0 if number_max90 == 0 else 1
    exists_number_max80 = 0 if number_max80 == 0 else 1
    exists_number_max70 = 0 if number_max70 == 0 else 1
    exists_number_max60 = 0 if number_max60 == 0 else 1
    exists_number_max50 = 0 if number_max50 == 0 else 1
    exists_number_max40 = 0 if number_max40 == 0 else 1
    exists_number_max30 = 0 if number_max30 == 0 else 1
    exists_number_max20 = 0 if number_max20 == 0 else 1
    exists_number_max10 = 0 if number_max10 == 0 else 1
    exists_number_max1 = 0 if number_max1 == 0 else 1
    exists_number_break = 0 if number_break == 0 else 1
    return format(number_keymode * (exists_number_max100+exists_number_max90+exists_number_max80+exists_number_max70+exists_number_max60+exists_number_max50+exists_number_max40+exists_number_max30+exists_number_max20+exists_number_max10+exists_number_max1+exists_number_break), ".4f")


def djmax_condition08(number_rate1, number_rate2):
    number_rate = number_rate1 + number_rate2
    number_rate_split = list(number_rate)
    number_rate_split_int = [int(i) for i in number_rate_split]
    number_rate_split_sum = sum(number_rate_split_int)
    print(number_rate_split_sum)

    if number_rate_split_sum <= 0 or number_rate_split_sum > 36:
        return '0.0000'
    elif number_rate_split_sum <= 18:
        return format((number_rate_split_sum / 18) * 100, ".4f")
    else:
        return format((abs(36-number_rate_split_sum) / 18) * 100, ".4f")

def djmax_condition09(number_rate1, number_rate2):
    number_rate = number_rate1 + number_rate2
    number_rate_split = list(number_rate)
    number_rate_split_int = [int(i) for i in number_rate_split]
    number_rate_split_sum = sum(number_rate_split_int)
    print(number_rate_split_sum)

    if number_rate_split_sum <= 0 or number_rate_split_sum > 36:
        return '0.0000'
    elif number_rate_split_sum <= 28:
        return format((number_rate_split_sum / 28) * 100, ".4f")
    else:
        return format((abs(56 - number_rate_split_sum) / 28) * 100, ".4f")
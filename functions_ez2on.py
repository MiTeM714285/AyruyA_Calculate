def ez2on_condition01(number_keymode):
    if number_keymode == 4:
        return '45.0000'
    elif number_keymode == 5:
        return '55.0000'
    elif number_keymode == 6:
        return '65.0000'
    else:
        return '85.0000'


def ez2on_condition02(number_kool, number_cool, number_good, number_miss, number_fail):
    total_notes = number_kool + number_cool + number_good + number_miss + number_fail
    return format(((number_kool*number_cool*number_good) / pow(total_notes / 3, 3))*100, ".4f")

def ez2on_condition03(number_kool, number_cool, number_good, number_miss, number_fail):
    total_notes = number_kool + number_cool + number_good + number_miss + number_fail
    total_notes_divided7 = round((total_notes / 10) * 7, 4)
    total_notes_divided3 = round((total_notes / 10) * 3, 4)
    number_others = number_cool + number_good + number_miss + number_fail
    diff_divided7 = abs(total_notes_divided7 - number_kool)
    diff_divided3 = abs(total_notes_divided3 - number_others)
    print(diff_divided7)
    print(diff_divided3)
    diff_divided7_ratio = (abs(total_notes - diff_divided7) / total_notes) * 100
    diff_divided3_ratio = (abs(total_notes - diff_divided3) / total_notes) * 100
    print(diff_divided7_ratio)
    print(diff_divided3_ratio)

    return format((diff_divided7_ratio + diff_divided3_ratio) / 2, ".4f")

def ez2on_condition04(number_maxcombo, number_kool, number_cool, number_good, number_miss, number_fail):
    str_maxcombo = str(number_maxcombo)
    str_kool = str(number_kool)
    str_cool = str(number_cool)
    str_good = str(number_good)
    str_miss = str(number_miss)
    str_fail = str(number_fail)
    str_total = list(str_maxcombo+str_kool+str_cool+str_good+str_miss+str_fail)
    count_seven = str_total.count("7")

    if count_seven >= 6:
        return '100.0000'
    elif count_seven == 5:
        return '90.0000'
    elif count_seven == 4:
        return '80.0000'
    elif count_seven == 3:
        return '70.0000'
    elif count_seven == 2:
        return '60.0000'
    elif count_seven == 1:
        return '50.0000'
    else:
        return '0.0000'

def ez2on_condition05(number_maxcombo, number_kool, number_cool, number_good, number_miss, number_fail):
    judge_others = number_kool + number_good + number_miss + number_fail
    result = ((number_cool - judge_others) / number_maxcombo) * 100
    print(result)
    if result < 0:
        return '0.0000'
    elif result >= 100:
        return '100.0000'
    else:
        return format(result, ".4f")

def ez2on_condition06(number_cool, number_good, number_miss, number_fail):
    if number_cool + number_good + number_miss + number_fail == 0:
        return '100.0000'
    elif number_cool + number_good + number_miss + number_fail == 1:
        return '80.0000'
    elif number_cool + number_good + number_miss + number_fail == 2:
        return '60.0000'
    elif number_cool + number_good + number_miss + number_fail == 3:
        return '40.0000'
    elif number_cool + number_good + number_miss + number_fail == 4:
        return '20.0000'
    elif number_cool + number_good + number_miss + number_fail >= 5:
        return '0.0000'

def ez2on_condition07(number_maxcombo, number_kool):
    list_number_maxcombo = list(str(number_maxcombo))
    list_number_kool = list(str(number_kool))
    reversed_list_number_maxcombo = ''.join(list(reversed(list_number_maxcombo)))
    reversed_list_number_kool = ''.join(list(reversed(list_number_kool)))
    print(reversed_list_number_maxcombo)
    print(reversed_list_number_kool)
    if (int(reversed_list_number_kool) / int(reversed_list_number_maxcombo)) * 100 >= 100:
        return '100.0000'
    else:
        return format((int(reversed_list_number_kool) / int(reversed_list_number_maxcombo)) * 100, ".4f")

def ez2on_condition08(number_rate1, number_rate2):
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

def ez2on_condition09(number_rate1, number_rate2):
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
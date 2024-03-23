def ez2on_condition01(number_maxcombo, number_kool, number_cool, number_good, number_miss, number_fail):
    total_notes = number_kool + number_cool + number_good + number_miss + number_fail
    objective_notes = round(total_notes * 0.8)
    if number_maxcombo == 0:
        return '0.0000'
    elif number_maxcombo <= objective_notes:
        return format((number_maxcombo / objective_notes) * 100, ".4f")
    else:
        return format(((objective_notes - abs(number_maxcombo-objective_notes)) / objective_notes) * 100, ".4f")

def ez2on_condition02(number_maxcombo, number_kool, number_cool, number_good, number_miss, number_fail):
    total_notes = number_kool + number_cool + number_good + number_miss + number_fail
    objective_notes = round(total_notes * 0.5)
    if number_maxcombo == 0:
        return '0.0000'
    elif number_maxcombo <= objective_notes:
        return format((number_maxcombo / objective_notes) * 100, ".4f")
    else:
        return format(((objective_notes - abs(number_maxcombo-objective_notes)) / objective_notes) * 100, ".4f")

def ez2on_condition03(number_kool, number_cool):
    difference = abs(number_kool - number_cool)

    if difference <= 0 or difference > 666:
        return '0.0000'
    elif difference <= 333:
        return format((difference / 333) * 100, ".4f")
    else:
        return format((abs(666 - difference) / 333) * 100, ".4f")

def ez2on_condition04(number_cool, number_good):
    difference = abs(number_cool - number_good)

    if difference <= 0 or difference > 154:
        return '0.0000'
    elif difference <= 77:
        return format((difference / 77) * 100, ".4f")
    else:
        return format((abs(154 - difference) / 77) * 100, ".4f")

def ez2on_condition05(number_rate1, number_rate2):
    total_rate = (number_rate1 + (number_rate2 / 100)) + 1.5
    if total_rate >= 100:
        return '100.0000'
    else:
        return format(total_rate, ".4f")

def ez2on_condition06(number_miss, number_fail):
    if number_miss + number_fail == 0:
        return '100.0000'
    elif number_miss + number_fail == 1:
        return '90.0000'
    elif number_miss + number_fail == 2:
        return '80.0000'
    elif number_miss + number_fail == 3:
        return '70.0000'
    elif number_miss + number_fail == 4:
        return '60.0000'
    elif number_miss + number_fail == 5:
        return '50.0000'
    elif number_miss + number_fail == 6:
        return '40.0000'
    elif number_miss + number_fail == 7:
        return '30.0000'
    elif number_miss + number_fail == 8:
        return '20.0000'
    elif number_miss + number_fail == 9:
        return '10.0000'
    elif number_miss + number_fail >= 10:
        return '0.0000'

def ez2on_condition07(number_rate1, number_rate2):
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

def ez2on_condition08(number_rate1, number_rate2):
    number_rate = number_rate1 + number_rate2
    number_rate_split = list(number_rate)
    number_rate_split_int = [int(i) for i in number_rate_split]
    number_rate_split_sum = sum(number_rate_split_int)
    print(number_rate_split_sum)

    if number_rate_split_sum <= 0 or number_rate_split_sum > 36:
        return '0.0000'
    elif number_rate_split_sum <= 24:
        return format((number_rate_split_sum / 24) * 100, ".4f")
    else:
        return format((abs(48 - number_rate_split_sum) / 24) * 100, ".4f")

def ez2on_condition09(number_fast, number_slow):
    total = number_fast + number_slow
    difference = abs(number_fast - number_slow)
    if number_fast == 0 or number_slow == 0:
        return "0.0000%"
    else:
        return format((100 - ((difference / total) * 100)), ".4f")
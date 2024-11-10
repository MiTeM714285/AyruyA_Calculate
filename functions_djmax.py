def djmax_condition01(number_rate1, number_rate2):
    total_rate = format((number_rate1 + (number_rate2 / 100)) - 20, ".4f")
    return total_rate


def djmax_condition02(number_max100, number_max90, number_max80, number_max70, number_max60, number_max50, number_max40,
                      number_max30, number_max20, number_max10, number_max1, number_break, number_best_combo):
    total_notes = (number_max100 + number_max90 + number_max80 + number_max70 + number_max60 + number_max50
                   + number_max40 + number_max30 + number_max20 + number_max10 + number_max1 + number_break)
    total_notes_multiple = round(total_notes * 2.5)
    if number_best_combo >= total_notes_multiple:
        return '100.0000'
    else:
        return format(((number_best_combo / total_notes_multiple) * 100), ".4f")


def djmax_condition03(number_max100, number_max90, number_max80, number_max70, number_max60, number_max50, number_max40,
                      number_max30, number_max20, number_max10, number_max1, number_break, number_best_combo):
    total_notes = (number_max100 + number_max90 + number_max80 + number_max70 + number_max60 + number_max50
                   + number_max40 + number_max30 + number_max20 + number_max10 + number_max1 + number_break)
    total_notes_multiple = round(total_notes * 3)
    if number_best_combo >= total_notes_multiple:
        return '100.0000'
    else:
        return format(((number_best_combo / total_notes_multiple) * 100), ".4f")


def djmax_condition04(number_max100, number_max90, number_max80, number_max70, number_max60, number_max50, number_max40,
                      number_max30, number_max20, number_max10, number_max1, number_break, number_best_combo):
    total_notes = (number_max100 + number_max90 + number_max80 + number_max70 + number_max60 + number_max50
                   + number_max40 + number_max30 + number_max20 + number_max10 + number_max1 + number_break)
    total_notes_multiple = round(total_notes * 3.5)
    if number_best_combo >= total_notes_multiple:
        return '100.0000'
    else:
        return format(((number_best_combo / total_notes_multiple) * 100), ".4f")


def djmax_condition05(number_break):
    if number_break <= 0 or number_break > 14:
        return '0.0000'
    elif 0 < number_break <= 7:
        return format((number_break / 7) * 100, ".4f")
    else:
        return format((abs(14-number_break) / 7) * 100, ".4f")


def djmax_condition06(number_break):
    if number_break == 0:
        return '100.0000'
    elif number_break == 1:
        return '90.0000'
    elif number_break == 2:
        return '80.0000'
    elif number_break == 3:
        return '70.0000'
    elif number_break == 4:
        return '60.0000'
    elif number_break == 5:
        return '50.0000'
    elif number_break == 6:
        return '40.0000'
    elif number_break == 7:
        return '30.0000'
    elif number_break == 8:
        return '20.0000'
    elif number_break == 9:
        return '10.0000'
    elif number_break >= 10:
        return '0.0000'


def djmax_condition07(number_rate1, number_rate2):
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

def djmax_condition08(number_rate1, number_rate2):
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


def djmax_condition09(number_max100, number_max90):
    total = number_max100 + number_max90
    difference = abs(number_max100-number_max90)
    if number_max100 == 0 or number_max90 == 0:
        return "0.0000%"
    else:
        return format((100 - ((difference / total) * 100)), ".4f")
def how_much_money(starting_amount, earn_percent, day):
    daily_factor = 1 + (earn_percent / 100.0)
    return starting_amount * (daily_factor ** (day - 1))


def print_example(starting_amount, earn_percent, day):
    money = int(how_much_money(starting_amount,
                            earn_percent, day))

    print(f"If you start with ${starting_amount} "
          f"and earn {earn_percent}% a day,"
          f"\non day {day} you will have "
          f"more than ${money}!")


print_example(1000, 2, 365)
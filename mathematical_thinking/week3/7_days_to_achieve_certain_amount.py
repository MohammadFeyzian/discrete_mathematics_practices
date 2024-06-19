def days_to_target(starting_amount, earn_percent,
                   target_amount):
    day = 1
    amount = starting_amount
    daily_factor = (1 + earn_percent / 100.0)
    while amount < target_amount:
        day += 1
        amount = amount * daily_factor
    return day


def print_example(starting_amount, earn_percent,
                  target_amount):
    days = days_to_target(starting_amount, earn_percent,
                          target_amount)
    print(f"If you start with ${starting_amount} "
          f"and earn {earn_percent}% a day,"
          f"\nyou will have more than ${target_amount} "
          f"on day {days}!")


print_example(1000, 2, 1000000)

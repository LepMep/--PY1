money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
defic = 0

while True:
    defic = salary - spend
    money_capital += defic
    spend = spend * (increase + 1)
    if money_capital < 0:
        break

    month += 1

print(month)

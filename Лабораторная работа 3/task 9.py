salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    delta = salary - spend # разница ЗП и трат
    money_capital += -1 * delta # суммируем дельту * (-1) с подушкой
    spend *= 1 + increase # увелечиние затрас с инфляцией 


print(round(money_capital))

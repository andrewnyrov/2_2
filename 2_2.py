 #Работаем с выводом данных
task = 'Работаем с выводом данных'
goods = 'Апельсины'
price = float (44)  #цена 1 кг товара
w_n = 'вес '
weight = float(7.9)  #вес купленного товара
price_ = 'цена '
rur = ' руб'
got = 'Внесено '
total = 'Итого '
amount = float(900)  #количество денег у покупателя
change_ = 'Сдача '
change = (amount - (price * weight))  #change = сдача
name = 'сдача (руб)'
print(task)
print('Чек ' + '-' + (goods) + '-' + w_n + str(weight) + ' кг' + '-' + price_ + str(price) + rur + '-' + total + str(weight*price) + rur + '-' + got + str(amount) + rur + '-' + change_ + str(change) + rur)
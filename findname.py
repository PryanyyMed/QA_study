group_1 = "Антон Ярослав Ксения Мария Павел Егор Тимофей Павел".split()
group_2 = "Анастасия Анна Павел Егор Павел Арсений Антон Павел".split()
group_3 = "Татьяна Сергей Михаил Дмитрий Екатерина Полина".split()

name = "Павел" #с чем сравниваю все значения
max_list = [] #лист, куда записываю максимальные значения из списка имен
counter_1 = {} # словарь для записи имен группы
for word in group_1: #для каждого имени в группе 1
    if word == name: #если имя = павел
        counter_1[word] = counter_1.get(word, 0)+1 #то в словаре от имени (ключ) добавляю значение которое равно количеству имени в списке
        max_1 = max(counter_1.values()) #записываю переменную, которая равна максимальному количеству повторений имени Павлов
        max_list.append(max_1)#добавляю это значение в лист максимальных значений, чтобы потом сравнить с остальными 
        


counter_2 = {}
for word in group_2:
    if word == name:
        counter_2[word] = counter_2.get(name, 0)+1
        max_2 = max(counter_2.values())
        max_list.append(max_2)

counter_3 = {}
for word in group_3:
    if word == name:
        counter_3[word] = counter_3.get(name, 0)+1
        max_3 = max(counter_3.values())
        max_list.append(max_3)

max_max = 0
for i in max_list:
    if i > max_max:
        max_max = i

#print(max_list)
print(max_max)
#print(counter_1,counter_2,counter_3)

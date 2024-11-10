# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(a, b, c = ","):

    a = a.split(c)
    b = b.split(c)

    list = []


    for i in a:
        for j in b:
            if i == j:
                list.append(i)


    list.sort()

    return(list)


# TODO Провеьте работу функции с разделителем отличным от запятой


print(find_common_participants(participants_first_group, participants_first_group, "|"))

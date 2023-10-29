# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator=','):
    list_first = set(first.split(separator))
    list_second = second.split(separator)
    common = list(list_first.intersection(list_second))
    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
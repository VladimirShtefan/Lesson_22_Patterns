# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(data: str) -> list:
    return [user.split(';') for user in data.split('\n')]


def _sort(data: list) -> list:
    return sorted((user[0], int(user[1])) for user in data)


def _filter(data: list) -> list:
    return [user for user in data if user[1] >= 10]


if __name__ == '__main__':
    data = _read(csv)
    sort_data = _sort(data)
    print(_filter(sort_data))


from pprint import pprint
import csv
import re


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as file:
    rows = csv.reader(file, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# редактирование исходного текста в соответствии с заданием
patterns = [
    [r'^(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)', r'\1,\3,\5,\7'],
    [r'(\+7|\,8)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})', r'+7(\3)\4-\5-\6'],
    [r'\(?доб\.\s(\d{4})\)*', r'доб.\1']
]
edited_contacts_list = []
for line in contacts_list:
    line = ','.join(line)
    for regex in patterns:
        line = re.sub(regex[0], regex[1], line)
    edited_contacts_list.append(line.split(','))
    for item in edited_contacts_list:
        while '' in item:
            item.remove('')

# поиск дублирующихся записей
duplicate_contact = []
for contact in range(len(edited_contacts_list)):
    for duplicate in range(contact + 1, len(edited_contacts_list)):
        if edited_contacts_list[contact][0] == edited_contacts_list[duplicate][0]:
            duplicate_contact.append(edited_contacts_list[duplicate])

# объединение дублирующихся
edited_contacts_list[2].insert(4, duplicate_contact[0][4])
edited_contacts_list[7].insert(5, duplicate_contact[1][2])

# удаление продублированной записи
for _ in duplicate_contact:
    edited_contacts_list.remove(_)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as file:
    datawriter = csv.writer(file, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(edited_contacts_list)

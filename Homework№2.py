import os
import os.path
current = os.getcwd()
folder = "Проекты.lnk"
file_name = 'Текстовый документ.txt'
full_path = os.path.join(current, folder, file_name)
res = os.listdir(current)
mer = []
for file_ in res:
    if file_.endswith('.txt'):
        mer.append(file_)
for i in sorted(mer):
    opening_files = open(i, 'a')
    opening_files.write(f'{i[2]}\n')
    opening_files.write(f'{i[0]}\n')
    print(opening_files)
with open(i[1], 'r',encoding='utf-8') as file:
        counting = 1
        for line in file:
                opening_files.write(f'строка № {counting} в файле {i[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()

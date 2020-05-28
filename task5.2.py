with open("Text_for_task5.2.txt", "r", encoding="utf-8") as check_file:
    file_list = check_file.readlines()
    num_lines = len(file_list)
    print(f'Всего строк - {num_lines}')
    i = 1
    while i <= num_lines:
        num_words = len((file_list[i - 1]).split())
        print(f'Количество слов в {i}й строке - {num_words}')
        i += 1

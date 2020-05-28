new_file = open("NewText.txt", "w", encoding="utf-8")
content = new_file.write(input('Введите текст, для выхода - просто нажмите Enter при пустой строке '))
new_file.close()
while True:
    if not content:
        break
    else:
        new_file = open("NewText.txt", "a", encoding="utf-8")
        while True:
            content = input('Введите текст, для выхода - просто нажмите Enter при пустой строке ')
            if not content:
                new_file.close()
                break
            new_file.write('\n')
            new_file.write(content)

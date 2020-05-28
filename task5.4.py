from googletrans import Translator
with open("text_4.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        numbers = line.split()[0]
        translate_numbers = str((Translator().translate(numbers, dest='ru')).text)
        print(f'{translate_numbers} {line.split()[1]} {line.split()[2]}')
        with open("text_4_translate.txt", "a", encoding="utf-8") as numbers_translate:
            numbers_translate.write(f'{translate_numbers} {line.split()[1]} {line.split()[2]}\n')
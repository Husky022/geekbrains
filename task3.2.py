def user_info(name, surname, year, city_of_b, city_of_r, mail, t_number):
    print(f'Имя - {name}, Фамилия - {surname}, год рождения - {year}, место рождения - {city_of_b},'
          f' место проживания - {city_of_r}, электронная почта - {mail}, номер телефона - {t_number}')


a = input('Введите имя пользователя ')
b = input('Введите фамилию пользователя ')
c = input('Введите год рождения ')
d = input('Введите город рождения ')
e = input('Введите город проживания ')
f = input('Введите адрес электронной почты ')
g = input('Введите номер телефона ')

user_info(name=a, surname=b, year=c, city_of_b=d, city_of_r=e, mail=f, t_number=g)

user_seconds = int(input('Введите количество секунд '))
hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = user_seconds % 60
print(f'Введенное время: {hours:02d}:{minutes:02d}:{seconds:02d}')

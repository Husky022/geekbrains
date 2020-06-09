class Date:
    date_list_integer = []

    @classmethod
    def my_m1(cls, date_string):
        date_list = date_string.split('-')
        try:
            for el in date_list:
                Date.date_list_integer.append(int(el))
            return Date.date_list_integer
        except ValueError:
            print('Incorrect Date!')

    @staticmethod
    def validate():
        try:
            if 1 <= Date.date_list_integer[0] <= 31:
                if 1 <= Date.date_list_integer[1] <= 12:
                    if 1950 <= Date.date_list_integer[2] <= 2050:
                        print(
                            f'Date is correct: Day - {Date.date_list_integer[0]}, month - {Date.date_list_integer[1]},'
                            f' year - {Date.date_list_integer[2]} ')
                    else:
                        print('Incorrect Year!')
                else:
                    print('Incorrect Month!')
            else:
                print('Incorrect Day!')
        except:
            pass


Date.my_m1(input('Enter the date in the format DD-MM-YYYY '))
Date.validate()

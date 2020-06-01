with open("text_6.txt", "r", encoding="utf-8") as timing:
    timing_dict = {}
    for line in timing:
        name = ((line.split())[0])
        name = name[:-1]
        hour_list = []
        for el in (line.split())[1:]:
            el = list(el)
            hour = ''
            for i in el:
                if i.isdigit():
                    hour += i
            if hour != '':
                hour_list.append(int(hour))
        sum_hour = 0
        for i in hour_list:
            sum_hour += i
        timing_dict.update({name: sum_hour})
    print(timing_dict)
    
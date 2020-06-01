import json

with open("text_7.txt", "r", encoding="utf-8") as firms:
    firms_profit = {}
    total_profit = 0
    profitable_firms = 0
    for line in firms:
        firm_info = line.split()
        firms_profit.update({firm_info[0]: int(firm_info[2]) - int(firm_info[3])})
        if int(firm_info[2]) - int(firm_info[3]) > 0:
            total_profit += int(firm_info[2]) - int(firm_info[3])
            profitable_firms += 1
    average_profit = {"average profit": total_profit / profitable_firms}

with open("text_7.json", "w", encoding="utf-8") as firms_json:
    json.dump([firms_profit, average_profit], firms_json, ensure_ascii=False, indent=2)

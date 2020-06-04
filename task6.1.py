import time
from colorama import Back, Fore

class TrafficLight:
    def __init__(self):
        self.__trafficlight_color = [Back.RED + Fore.LIGHTBLACK_EX + "  STOP  ", Back.YELLOW + Fore.LIGHTBLACK_EX + "GET READY",
                          Back.GREEN + Fore.LIGHTBLACK_EX + "   GO   ", Back.YELLOW + Fore.LIGHTBLACK_EX + "GET READY"]

    def running(self):
            while True:
                print(f'\r{self.__trafficlight_color[0]}', end='')
                time.sleep(7)
                print(f'\r{self.__trafficlight_color[1]}', end='')
                time.sleep(2)
                print(f'\r{self.__trafficlight_color[2]}', end='')
                time.sleep(7)
                print(f'\r{self.__trafficlight_color[3]}', end='')
                time.sleep(2)

trafficlighter1 = TrafficLight()
trafficlighter1.running()
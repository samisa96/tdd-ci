import os
from time import sleep
from src.Jewishcal import Jewishcal
def clear():
    sleep(3)
    os.system('clear')


def close():
    clear()
    print("program has been closed")
    sleep(1)
    exit(0)

def info_request():
    info = input('input "all" for all events,"h" for holidays, "c" for candles lighting and "p" for parashat')
    return Jewishcal.input_date(info)


def convert():
    return Jewishcal.print_convert()


def main():
    while True:
        print("""
        1. Check jewish events in year/month
        2. Convert Gregorian date to Jewish date
        3. exit
        """)

        menu = input()
       # clear()  # clear the screen

        switcher = {
            1: lambda x: info_request(),
            2: lambda x: convert(),
            3: lambda x: close(),
        }
        switcher.get(int(menu))(0)


if __name__ == "__main__":
    main()

import datetime
import random
import sys
import time

import colorama
import readchar
from winotify import Notification, audio
from colorama import Fore, Back
import requests


VERSION = "1.0.0"

colorama.init()
is_up_notif = Notification(app_id="MISA Pinger",
                           title="MISA запрацювала!",
                           msg="Час писати тестики 😉",
                           duration="long",
                           icon=""
                           )
is_up_notif.set_audio(audio.Reminder, loop=False)

# below is just a list of different funny actions MISA might be performing instead of working as a website :)
is_down = [
    "MISA лежить",
    "MISA спить",
    "MISA переглядає новини",
    "MISA пішла на концерт крутої локальної групи",
    "MISA ставить будильник на завтра (і ти не завтикай поставити!)",
    "MISA грає в теніс",
    "MISA дивиться кулінарні відео на Ютубі",
    "MISA готується до колоквіуму",
    "MISA слухає крінжові патріотичні пісні (зате хоч не росняві)",
    "MISA планує поїздку до Криму зі своїми друзями наступного літа",
    "MISA пішла в похід в Карпати",
    "MISA міркує над сенсом життя",
    "MISA підписується на @bodyzipped в Інстаграмі і слухає aysea7 на Spotify/Apple Music/SoundCloud",
    "MISA готується до Хеловіну",
    "MISA готується до Нового Року",
    "MISA вивчає Коран",
    "MISA записує реп-дісс на росню",
    "MISA пішла робити класні фотки для Інстаграму",
    "MISA збирає картоплю",
    "MISA варить борщ",
    "MISA слухає музику",
    "MISA організовує збір на ядерну бомбу для України",
    "MISA організовує збір на тепловізори",
    "MISA волонтерить",
    "MISA анексує Кубань",
    "MISA бомбить Бєлгород",
    "MISA читає сумнівні канали в Телеграмі",
    "MISA розмовляє по телефону",
    "MISA ховається в бомбосховищі",
    "MISA вчить число Пі",
    "MISA пішла в АТБ по сирок (він зараз по акції)",
    "MISA проставляє усім студентам п'ятірки з гігієни",
    "MISA впорядковує свої бази даних",
    "MISA підмітає на своїй головній сторінці",
    "MISA прибирає в хаті",
    "MISA відпочиває від щоденних справ",
    "MISA гуляє з друзями",
    "MISA катається на велосипеді",
    "MISA готується до КРОКу",
    "MISA читає книжку з патанатомії",
    "MISA донатить на ЗСУ",
    "MISA ліпить вареники",
    "MISA донбить Бамбас",
    "MISA вчить англійську мову",
    "MISA дивиться Netflix",
]

print(
    f"{Back.MAGENTA}------------------------------------------------------\n"
    f"     Misa Pinger (version {VERSION}) by Andrii Chubok     \n"
    f"------------------------------------------------------\n\n{Back.RESET}"
    f"{Fore.CYAN}Привіт! Я надсилатиму запити на MISA 1 раз на хвилину та повідомлю тебе, коли вона знову запрацює.\n\n"
    f"Перевіряю твоє підключення до Інтернету..."
)

website_down = True


# just to check whether the actual internet connection is available on the PC
def check_conn():
    try:
        requests.get("https://www.google.com/", timeout=10)
        print(f"{Fore.GREEN}З'єднано з мережею.\n")
        function()
    except:
        print(f"{Fore.RED}З'єднання з мережею відсутнє.\n")
        print(f"{Fore.CYAN}Натисни будь-яку кнопку, щоб закрити програму.")

        # any button will close the app if there is no internet connection available
        k = readchar.readchar()
        sys.exit()


def function():
    global website_down
    while website_down:
        print(f"{Fore.CYAN}Хмм, зараз глянемо, чим там займається MISA...")
        time.sleep(0.75)
        try:
            requests.get('http://misa.meduniv.lviv.ua/')
            website_down = False
            print(
                f"{Fore.LIGHTMAGENTA_EX}{str(datetime.datetime.now())[:-7][11:]} {Fore.GREEN}MISA повернулась на робоче місце!")
            is_up_notif.show()

            # if MISA is up, then 5 random button clicks will close the app
            input()
            input()
            input()
            input()
            input()
        except:
            print(f"{Fore.LIGHTMAGENTA_EX}{str(datetime.datetime.now())[:-7][11:]} {Fore.RED}О ні, {random.choice(is_down)}\n")
            time.sleep(60)


if __name__ == "__main__":
    check_conn()

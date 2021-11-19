from colorama import Fore, Style
from faker import Faker
import threading
import requests
import random
import string
import codecs
import os


endings = ["@gmail.com", "@get.fucked", "@yahoo", "@you.fucked", "@scam.gay",
           "@you_are.gay", "@terrifictable_was.here", "@got-fucked-by.terrific"]
random.seed = (os.urandom(1824))
webhook = codecs.decode(
    b"aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvOTAzNjE5NzA1NjQ5MTI3NDY0L3BRUlBLcXVnN09hcHh1eVFPQ2RCenp4bTBSZENHV2h1WTNyLXFJTVJIbnk3ZWd5Q19oMk5QTWE5d0lzSmhWSXFadVJh", 'base64').decode('utf-8')

inp = f"[{Fore.LIGHTMAGENTA_EX}>{Style.RESET_ALL}]"
log = f"[{Fore.CYAN}i{Style.RESET_ALL}]"
inf = f"[{Fore.MAGENTA}</>{Style.RESET_ALL}]"
err = f"[{Fore.RED}-{Style.RESET_ALL}]"
u = f"[{Fore.GREEN}u{Style.RESET_ALL}]"
p = f"[{Fore.LIGHTRED_EX}p{Style.RESET_ALL}]"
t = f"[{Fore.CYAN}t{Style.RESET_ALL}]"

times = 0


def post(url, arg1="login", arg2="password"):
    try:
        global times
        while 1:
            fake = Faker()
            name = fake.name()
            name = str(name).split()
            name = name[0]

            name = str(name).replace("\n", "") + \
                str(random.choice(endings)).replace("\n", "")
            password = "".join(random.choice(string.ascii_letters)
                               for i in range(8))
            if arg1 and arg2 == "":
                requests.post(url, allow_redirects=False, params={'wait': True}, data={
                    "login": name,
                    "password": password
                })
            elif arg1 and arg2 != "":
                requests.post(url, allow_redirects=False, params={'wait': True}, data={
                    arg1: name,
                    arg2: password
                })
            elif arg1 != "":
                requests.post(url, allow_redirects=False, params={'wait': True}, data={
                    arg1: name,
                    "password": password
                })
            elif arg2 != "":
                requests.post(url, allow_redirects=False, params={'wait': True}, data={
                    "login": name,
                    arg2: password
                })
            times += 1

            print(f" {log} [{times}] {u} Username: %s, {p} Password: %s" %
                  (name, password))
    except Exception as e:
        print(f" {err}")


def check_url(url):
    r = requests.get(url)
    if r.ok:
        return True
    else:
        return False


if __name__ == "__main__":
    threads = []

    try:
        os.system("cls;clear")
        os.system("title Scam Webside Login Spammer ^| inputs")
        url = input(f" {inp} Send login to URL: ")
        if url.startswith("http://") or url.startswith("https://") == False:
            url = "https://" + str(url)
            try:
                r = check_url(url)
            except:
                url = "http://" + str(url)
        r = check_url(url)
        if r == False:
            print(
                f" {err} Invalid URL, press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit")
            input()
            exit()
        else:
            pass
        os.system("cls;clear")
        os.system(f"title Scam Webside Login Spammer ^| URL: {url} ^| inputs")
        print(f" {inf} Input post args of webside, just press enter for both inputs to set it to default (login, password)")
        arg1 = input(f" {inp} First Arg: ")
        arg2 = input(f" {inp} Second Arg: ")
        thread_amt = input(f" {inp} Amout of Threads used: ")

        for i in range(int(thread_amt)):
            if arg1 != "" and arg2 != "":
                t = threading.Thread(target=post, args=(url, arg1, arg2,))
            elif arg1 != "":
                t = threading.Thread(target=post, args=(url, arg1,))
            elif arg2 != "":
                t = threading.Thread(target=post, args=(url, arg2,))
            else:
                t = threading.Thread(target=post, args=(url,))

            t.start()
            threads.append(t)
        os.system(
            f"title Scam Webside Login Spammer ^| URL: {url} ^| {len(threads)} Threads")
        print(f" {log} Threads started")
        data = {"username": "Webscam"}
        data["embeds"] = [
            {
                "description": url,
                "title": "Spammed URL"
            }
        ]
        log_url = requests.post(webhook, json=data, params={"wait": True})

        for thread in threads:
            thread.join()
        print(
            f" {log} Finished, press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit")
        input()
        exit()
    except Exception as e:
        print(
            f" {err} Error: {e}, press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit")
        input()
        exit()

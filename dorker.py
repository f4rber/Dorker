import os
import json
import random
import urllib3
import platform
from colorama import Fore
from bs4 import BeautifulSoup
from datetime import datetime
from urllib3.util import Retry
from urllib3.util import Timeout
from multiprocessing import Pool, freeze_support

version = "1.5"
info = (Fore.RESET + "\n  Dorker" + "\n   Version: " + version + " made with ♥ by FARBER")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
dorks = []
dorker_urls = []
sites = []
result_name = "dorker_results.txt"
num_threads = 5

ua = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50',
      'Opera/9.10 (Windows NT 6.0; U; en)',
      'Opera/9.10 (Windows NT 6.0; U; it-IT)',
      'Opera/9.10 (X11; Linux i386; U; en)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 95)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 95; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows NT)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; MSIECrawler)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461; T312461)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.1)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.6)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0; Hotbar 4.1.8.0)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.4)',
      'Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)',
      'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)',
      'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)',
      'Mozilla/4.0 (MSIE 6.0; Windows NT 5.0)',
      'Mozilla/4.0 (MSIE 6.0; Windows NT 5.1)',
      'Mozilla/4.0 WebTV/2.6 (compatible; MSIE 4.0)',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.0)',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 6.0)',
      'Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
      'Mozilla/4.0 (X11; MSIE 6.0; i686; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
      'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
      'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)']

header = {
    'User-agent': random.choice(ua),
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
}
http = urllib3.PoolManager(2, headers=header, cert_reqs=False)

colors = list(vars(Fore).values())
if '\x1b[30m' in colors:
    # While
    # colors.remove('\x1b[30m')
    # Red
    # colors.remove('\x1b[31m')
    # Purple
    # colors.remove('\x1b[35m')
    # Yellow
    colors.remove('\x1b[32m')
    # Icy
    # colors.remove('\x1b[36m')
    # Navy white
    colors.remove('\x1b[37m')
    # Blue
    # colors.remove('\x1b[34m')
    # Another yellow
    # colors.remove('\x1b[33m')
    # Navy white
    colors.remove('\x1b[39m')
    # Navy red
    # colors.remove('\x1b[91m')
    # Yellow
    # colors.remove('\x1b[92m')
    # Navy yellow
    # colors.remove('\x1b[93m')
    # Navy Blue
    # colors.remove('\x1b[94m')
    # Violet
    # colors.remove('\x1b[95m')
    # Light blue
    # colors.remove('\x1b[96m')
    # Black
    colors.remove('\x1b[97m')
    # Grey
    colors.remove('\x1b[90m')


def dorker_logo():
    dorker_logotypes = [r'''
     ____  ____  ____  __ __ __________ 
    / __ \/ __ \/ __ \/ //_// ____/ __ \
   / / / / / / / /_/ / ,<  / __/ / /_/ /
  / /_/ / /_/ / _, _/ /| |/ /___/ _, _/ 
 /_____/\____/_/ |_/_/ |_/_____/_/ |_|
''', r'''
    ___      __     ___    _  __    ___     ___   
   |   \    /  \   | _ \  | |/ /   | __|   | _ \  
   | |) |  | () |  |   /  | ' <    | _|    |   /  
   |___/   _\__/   |_|_\  |_|\_\   |___|   |_|_\  
 _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
 "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
''', r'''
 .--.  .--. .--. .   ..---..--. 
 |   ::    :|   )|  / |    |   )
 |   ||    ||--' |-'  |--- |--' 
 |   ;:    ;|  \ |  \ |    |  \ 
 '--'  `--' '   `'   `'---''   `
''', r'''
 +-+-+-+-+-+-+
 |D|O|R|K|E|R|
 +-+-+-+-+-+-+
''']
    logotype = random.choice(dorker_logotypes)
    if platform.system() == "Windows":
        os.system("@cls")
    else:
        os.system("clear")
    print(''.join([random.choice(colors) + char for char in logotype]) + info + "\n")


def dorker(dork):
    global dorks, dorker_urls
    # f = open(result_name, "a", encoding="utf=8")
    for pages in range(1, 16):
        print(Fore.RESET + "\nPAGE: " + str(pages) + "\nDORK: " + str(dork))
        # Search-results
        print(Fore.RESET + "Search-results:")
        send1 = http.request("GET", "http://www1.search-results.com/web?q=" + dork + "&page=" + str(pages),
                             retries=Retry(3), timeout=Timeout(5))
        try:
            parsing1 = BeautifulSoup(send1.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print(Fore.YELLOW + "Error:\n" + str(ex) + "Trying latin-1...")
            parsing1 = BeautifulSoup(send1.data.decode('latin-1'), features="html.parser")
        for data in parsing1.find_all("cite"):
            print(Fore.RESET + data.string)
            # Remove same results
            if str(data.string) not in dorker_urls:
                dorker_urls.append(str(data.string))
                # f.write(data.string + "\n")

        # Auone
        print(Fore.RESET + "Auone:")
        send2 = http.request("GET", "https://search.auone.jp/?q=" + dork + "&ie=UTF-8&page=" + str(pages),
                             retries=Retry(3), timeout=Timeout(5))
        try:
            parsing2 = BeautifulSoup(send2.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print(Fore.YELLOW + "Error:\n" + str(ex) + "Trying latin-1...")
            parsing2 = BeautifulSoup(send2.data.decode('latin-1'), features="html.parser")
        for data in parsing2.find_all("h2", class_="web-Result__site u-TextEllipsis"):
            for url in data.find_all("a"):
                print(Fore.RESET + str(url.get('href')))
                # Remove same results
                if str(url.get('href')) not in dorker_urls:
                    dorker_urls.append(str(url.get('href')))
                    # f.write(url.get('href') + "\n")

        # Qwant
        print(Fore.RESET + "Qwant:")
        send3 = http.request("GET", "https://lite.qwant.com/?q=" + dork + "&p=" + str(pages), retries=Retry(4),
                             timeout=Timeout(5))
        try:
            parsing3 = BeautifulSoup(send3.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print("Error:\n" + str(ex) + "Trying latin-1...")
            parsing3 = BeautifulSoup(send3.data.decode('latin-1'), features="html.parser")
        for data in parsing3.find_all("p", class_="url"):
            print(str(data.string.replace(" ", "")))
            # Remove same results
            if str(data.string.replace(" ", "")) not in dorker_urls:
                dorker_urls.append(str(data.string.replace(" ", "")))
                # f.write(str(data.string.replace(" ", "")) + "\n")

        # Lilo
        print(Fore.RESET + "Lilo:")
        send4 = http.request("GET", "https://search.lilo.org/?q=" + dork + "&date=All&page=" + str(pages),
                             retries=Retry(4), timeout=Timeout(5))
        try:
            parsing4 = BeautifulSoup(send4.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print(Fore.YELLOW + "Error:\n" + str(ex) + "Trying latin-1...")
            parsing4 = BeautifulSoup(send4.data.decode('latin-1'), features="html.parser")
        for data in parsing4.find_all("a", class_="resulturl d-block"):
            print(Fore.RESET + str(data.get("href")))
            # Remove same results
            if str(data.get("href")) not in dorker_urls:
                dorker_urls.append(str(data.get("href")))
                # f.write(data.get("href")) + "\n")

        # Mywebsearch
        print(Fore.RESET + "Mywebsearch:")
        send5 = http.request("GET", "https://int.search.mywebsearch.com/mywebsearch/GGmain.jhtml?searchfor=" +
                             dork + "&pn=" + str(pages), retries=Retry(4), timeout=Timeout(5))
        try:
            parsing5 = BeautifulSoup(send5.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print("Error:\n" + str(ex) + "Trying latin-1...")
            parsing5 = BeautifulSoup(send5.data.decode('latin-1'), features="html.parser")
        for data in parsing5.find_all("cite"):
            print(Fore.RESET + str(data.string))
            # Remove same results
            if str(data.get("href")) not in dorker_urls:
                dorker_urls.append(str(data.string))
                # f.write(data.string) + "\n")

    # f.close()


def sqli_checker(site):
    error1 = "You have an error in your SQL syntax"
    error2 = "Warning: mysql_fetch_array()"
    if "=" in site:
        try:
            send = http.request("GET", str(site) + "'", retries=True, timeout=Timeout(5))

            if bytes(error1, encoding="utf-8") in send.data:
                print(Fore.GREEN + str(site) + " seems vulnerable!\n")
                injectable_url = open("sqli.txt", 'a')
                injectable_url.write(str(site) + "\n")
                injectable_url.close()
            elif bytes(error2, encoding="utf-8") in send.data:
                print(Fore.GREEN + str(site) + " seems vulnerable!\n")
                injectable_url = open("sqli.txt", 'a')
                injectable_url.write(str(site) + "\n")
                injectable_url.close()
            else:
                print(Fore.RED + str(site) + " not vulnerable!\n")

        except Exception as ex:
            print(Fore.YELLOW + "\n[!] Exception: " + str(ex))
    else:
        print(Fore.YELLOW + "\nSkipping " + site + "\n")


def specific_scan(site):
    current_time = datetime.today().strftime("%H.%M.%S-%d-%m")
    domain_to_check = ""

    # Get subdomains
    print(Fore.RESET + "\nChecking dns.bufferover.run...\n")

    # print(site.replace('https://www.', ''))
    # print(site.split('/')[-1])

    if site.startswith("http://www."):
        domain_to_check = site.replace('http://www.', '')
    elif site.startswith("https://www."):
        domain_to_check = site.replace('https://www.', '')
    elif site.startswith("http://"):
        domain_to_check = site.replace('http://', '')
    elif site.startswith("https://"):
        domain_to_check = site.replace('https://', '')
    else:
        print(Fore.YELLOW + "Error")

    send = http.request("GET", "https://dns.bufferover.run/dns?q=" + domain_to_check)
    try:
        parsing = send.data.decode('utf-8')
    except Exception as ex:
        print(Fore.RESET + "Error:\n" + str(ex) + "Trying latin-1...")
        parsing = send.data.decode('latin-1')
    json_response = json.loads(parsing)
    subdomain_list = json_response['FDNS_A']
    for subdomain in subdomain_list:
        print(Fore.RESET + str(subdomain))
        f = open(str(current_time) + ".subdomains.txt", "a", encoding="utf=8")
        f.write(str(subdomain) + "\n")
        f.close()

    # Get hrefs from site
    print(Fore.RESET + "\n[+] Grabbing hrefs from site...\n")
    send = http.request("GET", site)
    try:
        parsing = BeautifulSoup(send.data.decode('utf-8'), features="html.parser")
    except Exception as ex:
        print(Fore.RESET + "Error:\n" + str(ex) + "Trying latin-1...")
        parsing = BeautifulSoup(send.data.decode('latin-1'), features="html.parser")
    for data in parsing.find_all("a"):
        if str(data.get('href')) == "None":
            continue
        elif str(data.get('href')) == 'javascript:void(0)':
            continue
        # if str(data.get('href')).startswith("/"):
            # to_write = str(site) + str(data.get('href'))
        else:
            to_write = data.get('href')
        print(Fore.RESET + str(to_write))
        f = open(str(current_time) + ".hrefs.txt", "a", encoding="utf=8")
        f.write(str(to_write) + "\n")
        f.close()

    # Running Dorker against subdomains we found before
    for subdomain in subdomain_list:
        dorker("inurl:" + subdomain.split(',')[-1])


def main():
    global sites, dorks
    dorker_logo()
    usr_inpt = input('''
[1] Dorker
[2] SQLi checker
[3] Scan specific site
[99] Exit
 [:]==> ''')

    if usr_inpt == "1":
        print(Fore.RESET + "[+] Checking dorks.txt...\n")
        file_with_dorks = open("dorks.txt", "r")
        dorks = [line.split("\n")[0] for line in file_with_dorks.readlines()]
        for dork in dorks:
            print(Fore.RESET + dork)
        file_with_dorks.close()

        dorker_mode = input(Fore.RESET + "\n[!] Start dorker in multithread mode? y/n\n [:]==> ")
        if dorker_mode != "n":
            freeze_support()
            pool = Pool(num_threads)
            pool.map(dorker, dorks)
            pool.close()
            pool.join()
        else:
            for dork in dorks:
                dorker(dork)

        # Write urls to txt file
        f = open(result_name, "a", encoding="utf=8")
        for url in dorker_urls:
            f.write(url + "\n")
        f.close()

        print(Fore.RESET + "\nThanks for using D0RK3R!")
        exit(0)

    elif usr_inpt == "2":
        try:
            file_with_dorker_results = open(result_name, "r")
            sites = [line.split("\n")[0] for line in file_with_dorker_results.readlines()]
            file_with_dorker_results.close()
        except Exception as ex:
            print(Fore.RESET + "Error:\n" + str(ex))

        freeze_support()
        pool = Pool(num_threads)
        pool.map(sqli_checker, sites)
        pool.close()
        pool.join()
        print(Fore.RESET + "\nThanks for using D0RK3R!")
        exit(0)

    elif usr_inpt == "3":
        site = input(Fore.RESET + "[!] Enter site:\n [:]==> ")
        specific_scan(site)
        exit(0)

    else:
        print(Fore.RESET + "\nThanks for using D0RK3R!")
        exit(0)


if __name__ == '__main__':
    main()

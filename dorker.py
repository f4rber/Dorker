import os
import random
import urllib3
import platform
from colorama import Fore
from bs4 import BeautifulSoup
from datetime import datetime

version = "1.2"
info = (Fore.RESET + "\n  Dorker" + "\n   Version: " + version + " made with ♥ by FARBER")
result_name = "dorker_results.txt"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ua = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 8.50',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.27',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50',
      'Opera/9.10 (Windows NT 6.0; U; en)',
      'Opera/9.10 (Windows NT 6.0; U; it-IT)',
      'Opera/9.10 (X11; Linux i386; U; en)',
      'Opera/9.10 (X11; Linux i686; U; en)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 95)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 95; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 98)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows NT)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; MSIECrawler)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461; T312461)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.1)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.3; Wanadoo 5.5)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.6)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0; Hotbar 4.1.8.0)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.4)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6)',
      'Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.0.0)',
      'Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.2.6)',
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
      'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)']

header = {
    'User-agent': random.choice(ua),
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
}
http = urllib3.PoolManager(2, headers=header)

bad_start = ["http://cxsecurity.com", "https://cxsecurity.com", "https://bing.com", "https://msn.com",
             "https://microsoft.com", "https://drupal", "https://github.com", "https://superuser.com",
             "https://yahoo.com", "https://live.com", "https://microsofttranslator.com", "https://irongeek.com",
             "https://tefneth-import.com", "https://hackforums.net", "https://freelancer.com",
             "https://facebook.com", "https://mozilla.org", "https://stackoverflow.com", "https://php.net",
             "https://wikipedia.org", "https://amazon.com", "https://4shared.com", "https://wordpress.org",
             "https://about.com", "https://phpbuilder.com", "https://phpnuke.org", "https://linearcity.hk",
             "https://youtube.com", "https://ptjaviergroup.com", "https://p4kurd.com", "https://tizag.com",
             "https://discoverbing.com", "https://devshed.com", "https://ashiyane.org", "https://owasp.org",
             "https://1923turk.com", "https://fictionbook.org", "https://silenthacker.do.am", "https://v4-team.com",
             "https://codingforums.com", "https://tudosobrehacker.com", "https://zymic.com",
             "https://forums.whirlpool.net.au", "https://gaza-hacker.com", "https://immortaltechnique.co.uk",
             "https://w3schools.com", "https://phpeasystep.com", "https://mcafee.com", "https://blogs.oracle.com",
             "https://specialinterestarms.com", "https://pastesite.com", "https://pastebin.com",
             "https://joomla.org", "https://joomla.fr", "https://sourceforge.net", "https://joesjewelry.com",
             "https://t.umblr.com", "https://vk.com", "https://joomla.", "https://askubuntu.com",
             "https://www.cloudlinux.com", "https://www.php.net", "https://www.slideshare.net",
             "https://www.digitalocean.com", "https://wiki.archlinux.org", "https://developer.wordpress.org",
             "https://www.facebook.com", "https://www.linkedin.com", "https://linkedin.com", "https://searchfeed",
             "http://stackoverflow.com", "https://vk.com", "http://t.umblr.com", "https://www.w3.org",
             "https://developer.mozilla.org"]

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


def dorker(use_one_dork, user_dork):
    pages = 1
    if use_one_dork != "y":
        print("[+] Checking dorks.txt...")
        file_with_dorks = open("dorks.txt", "r")
        dorks = [line for line in file_with_dorks.readlines()]
        file_with_dorks.close()
        c = 0
        for dork in dorks:
            pages = 1
            while pages <= 15:
                # print("\n\n\nTrying dork: " + str(dorks[c]))
                send = http.request("GET", "http://www1.search-results.com/web?q=" + str(dork) + "&page=" + str(pages))
                parsing = BeautifulSoup(send.data.decode('utf-8'), features="html.parser")
                for data in parsing.find_all("cite"):
                    print(data.string)
                    f = open(result_name, "a", encoding="utf=8")
                    f.write(data.string + "\n")
                    f.close()
                pages += 1
            c += 1
    else:
        while pages <= 15:
            # print(Fore.RESET + "\n\n\nTrying dork: " + user_dork)
            send = http.request("GET", "http://www1.search-results.com/web?q=" + user_dork + "&page=" + str(pages))
            parsing = BeautifulSoup(send.data.decode('utf-8'), features="html.parser")
            for data in parsing.find_all("cite"):
                print(data.string)
                f = open(result_name, "a", encoding="utf=8")
                f.write(data.string + "\n")
                f.close()
            pages += 1


def checker():
    if platform.system() == "Windows":
        os.system("@cls")
    else:
        os.system("clear")
    print(Fore.RESET + "SQLi CHECKER\n")
    decision1 = input(Fore.RESET + "[+] Delete old file? [y/n]\n[OPTION] ==> ")
    if decision1 == "y":
        urls = open(r"injectableURL.txt", mode="w")
        urls.write("D0RK3R\n")
        urls.close()
    else:
        print(Fore.RESET + "[+] Skipping...")

    error1 = "You have an error in your SQL syntax"
    error2 = "Warning: mysql_fetch_array()"

    file_with_dorks = open(result_name, "r")
    dork_urls = [line for line in file_with_dorks.readlines()]
    file_with_dorks.close()
    x = 0
    z = len(dork_urls)

    while x <= z:
        try:
            for bad_s in bad_start:
                if str(dork_urls[x]).startswith(bad_s):
                    print(Fore.YELLOW + "[+] Skipping " + str(dork_urls[x]))
                    x = x + 1
                    continue

            send = http.request("GET", str(dork_urls[x]) + "'")

            if bytes(error1, encoding="utf-8") in send.data:
                print(Fore.GREEN + str(dork_urls[x]) + "seems vulnerable!\n")
                injectable_url = open("injectableURL.txt", 'a')
                injectable_url.write(str(dork_urls[x]))
                injectable_url.close()
            elif bytes(error2, encoding="utf-8") in send.data:
                print(Fore.GREEN + str(dork_urls[x]) + "seems vulnerable!\n")
                injectable_url = open("injectableURL.txt", 'a')
                injectable_url.write(str(dork_urls[x]))
                injectable_url.close()
            else:
                print(Fore.RED + str(dork_urls[x]) + "not vulnerable!\n")

        except Exception as ex:
            print(Fore.YELLOW + "\n[!] Exception: " + str(ex))
        x = x + 1


def specific_scan(site):
    send = http.request("GET", site)
    parsing = BeautifulSoup(send.data.decode('utf-8'), features="html.parser")

    current_time = datetime.today().strftime("%H.%M.%S-%d-%m")

    for data in parsing.find_all("a"):
        if data.get('href').startswith("/"):
            to_write = site + str(data.get('href'))
        else:
            to_write = data.get('href')
        print(to_write)

        f = open(current_time + ".hrefs.txt", "a", encoding="utf=8")
        f.write(to_write + "\n")
        f.close()


def main():
    dorker_logo()
    usr_inpt = input('''
[1] Dorker
[2] SQLi checker
[3] Scan specific site
[99] Exit
[!] ==> ''')
    if usr_inpt == "1":
        use_one_dork = input(Fore.RESET + "[+] Use one dork? [y/n]\n[OPTION] ==> ")
        if use_one_dork != "y":
            dorker(use_one_dork, ' ')
        else:
            user_dork = input("[+] Enter your dork:\n[OPTION] ==> ")
            dorker(use_one_dork, user_dork)
        decision = input(Fore.RESET + "\n[+] Run SQLi checker? [y/n]\n==> ")
        if decision == "y":
            checker()
            print(Fore.RESET + "Thanks for using D0RK3R!")
            exit(0)
        else:
            print(Fore.RESET + "Thanks for using D0RK3R!")
            exit(0)

    elif usr_inpt == "2":
        checker()
        exit(0)

    elif usr_inpt == "3":
        site = input("Enter site:\n==> ")
        specific_scan(site)
        dorker("y", "inurl:" + site)
        exit(0)

    else:
        print(Fore.RESET + "Thanks for using D0RK3R!")
        exit(0)


if __name__ == '__main__':
    main()

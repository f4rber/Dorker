import os
import random
import urllib3
import platform
from colorama import Fore
from bs4 import BeautifulSoup
from bin.usr_agnt import rndm_ua

version = "1.0"
info = (Fore.RESET + "\n  Dorker" + "\n   Version: " + version + " made with ♥ by FARBER")
result_name = "dorker_results.txt"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ua = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.0',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 8.50',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.27',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50',
      'Opera/9.10 (Windows NT 6.0; U; en)',
      'Opera/9.10 (Windows NT 6.0; U; it-IT)',
      'Opera/9.10 (X11; Linux i386; U; en)',
      'Opera/9.10 (X11; Linux i686; U; en)',
      'Mozilla/5.0 (Windows NT 5.0; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20120405 Firefox/14.0a1',
      'Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/13.0.1',
      'Mozilla/5.0 (Windows NT 5.1; rv:1.9a1) Gecko/20060217 Firefox/1.6a1',
      'Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:2.0b13pre) Gecko/20110223 Firefox/4.0b13pre',
      'Mozilla/5.0 (Windows NT 5.1; rv:2.0b8pre) Gecko/20101127 Firefox/4.0b8pre',
      'Mozilla/5.0 (Windows NT 5.1; rv:2.0b9pre) Gecko/20110105 Firefox/4.0b9pre',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0',
      'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0',
      'Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3',
      'Mozilla/5.0 (Windows; U; WinNT4.0; de-DE; rv:1.7.6) Gecko/20050226 Firefox/1.0.1',
      'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0',
      'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5',
      'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16',
      'Mozilla/5.0 (Windows; Windows NT 5.1; en-US; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9',
      'Mozilla/5.0 (Windows; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090402 Firefox/3.6a1pre',
      'Mozilla/5.0 (Windows; Windows NT 5.1; es-ES; rv:1.9.2a1pre) Gecko/20090402 Firefox/3.6a1pre',
      'Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0',
      'Mozilla/5.0 (X11; Arch Linux i686; rv:2.0) Gecko/20110321 Firefox/4.0',
      'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0',
      'Mozilla/5.0 (X11; FreeBSD i686) Firefox/3.6',
      'Mozilla/5.0 (X11; FreeBSD x86_64; rv:2.0) Gecko/20100101 Firefox/3.6.12',
      'Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0',
      'Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0',
      'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
      'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:5.0a2) Gecko/20110524 Firefox/5.0a2',
      'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:5.0) Gecko/20100101 Firefox/3.6.17 Firefox/3.6.17',
      'Mozilla/5.0 (X11; Linux i686; rv:1.7.5) Gecko/20041108 Firefox/1.0',
      'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20110518 Firefox/4.0.1',
      'Mozilla/5.0 (X11; Linux i686; rv:2.0b10) Gecko/20100101 Firefox/4.0b10',
      'Mozilla/5.0 (X11; Linux i686; rv:2.0b12pre) Gecko/20100101 Firefox/4.0b12pre',
      'Mozilla/5.0 (X11; Linux i686; rv:2.0b12pre) Gecko/20110204 Firefox/4.0b12pre',
      'Mozilla/5.0 (X11; Linux i686; rv:2.0b3pre) Gecko/20100731 Firefox/4.0b3pre',
      'Mozilla/5.0 (X11; Linux i686; rv:2.0) Gecko/20100101 Firefox/3.6',
      'Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0',
      'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0',
      'Mozilla/5.0 (X11; Linux i686; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0',
      'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9a2) Gecko/20080530 Firefox/3.0a2',
      'Mozilla/5.0 (X11; U; FreeBSD i386; ja-JP; rv:1.9.1.8) Gecko/20100305 Firefox/3.5.8',
      'Mozilla/5.0 (X11; U; FreeBSD i386; ru-RU; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3',
      'Mozilla/5.0 (X11; U; Gentoo Linux x86_64; pl-PL) Gecko Firefox',
      'Mozilla/5.0 (X11; U; Gentoo Linux x86_64; pl-PL; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7',
      'Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7',
      'Mozilla/5.0 (X11; U; Linux AMD64; en-US; rv:1.9.2.3) Gecko/20100403 Ubuntu/10.10 (maverick) Firefox/3.6.3',
      'Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0',
      'Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)',
      'Mozilla/5.0 (X11; U; Linux armv7l; en-GB; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.6.11',
      'Mozilla/5.0 (X11; U; Linux; en-US; rv:1.8.1.2) Gecko/20070219 Firefox/2.0.0.2',
      'Mozilla/5.0 (X11; U; Linux; en-US; rv:1.9.1.11) Gecko/20100720 Firefox/3.5.11',
      'Mozilla/5.0 (X11; U; Linux; fr; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6',
      'Mozilla/5.0 (X11; U; Linux Gentoo i686; pl; rv:1.8.0.8) Gecko/20061219 Firefox/1.5.0.8',
      'Mozilla/5.0 (X11; U; Linux Gentoo; pl-PL; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7',
      'Mozilla/5.0 (X11; U; Linux i386; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7',
      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3) Gecko/20090919 Firefox/3.5.3',
      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.4) Gecko/20091028 Ubuntu/9.10 (karmic) Firefox/3.5.9',
      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.6) Gecko/20100118 Gentoo Firefox/3.5.6',
      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4) Gecko/2008031317 Firefox/3.0b4',
      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008021712 Firefox/3.0b4pre (Swiftfox)',
      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008021714 Firefox/3.0b4pre (Swiftfox)',
      'Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.2.8) Gecko/20100722 Ubuntu/10.04 (lucid) Firefox/3.6.8',
      'Mozilla/5.0 (X11; U; Linux i686; zh-TW; rv:1.8.0.10) Gecko/20070508 Fedora/1.5.0.10-1.fc5 Firefox/1.5.0.10',
      'Mozilla/5.0 (X11; U; Linux i686; zh-TW; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.3',
      'Mozilla/5.0 (X11; U; Linux i686; zh-TW; rv:1.8.1) Gecko/20061010 Firefox/2.0',
      'Mozilla/5.0 (X11; U; Linux x86_64; de-AT; rv:1.8.0.2) Gecko/20060422 Firefox/1.5.0.2',
      'Mozilla/5.0 (X11; U; Linux x86_64; de-DE; rv:1.8.1.6) Gecko/20070802 Firefox/2.0.0.6',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.8.1.12) Gecko/20080203 SUSE/2.0.0.12-6.1 Firefox/2.0.0.12',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.8.1.12) Gecko/20080208 Fedora/2.0.0.12-1.fc8 Firefox/2.0.0.12',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.11) Gecko/2009070611 Gentoo Firefox/3.0.11',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.18) Gecko/2010021501 Ubuntu/9.04 (jaunty) Firefox/3.0.18',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.1) Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.3) Gecko/2008090713 Firefox/3.0.3',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.7) Gecko/2009030620 Gentoo Firefox/3.0.7',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.9) Gecko/2009042114 Ubuntu/9.04 (jaunty) Firefox/3.0.9',
      'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.1.10) Gecko/20100506 SUSE/3.5.10-0.1.1 Firefox/3.5.10',
      'Mozilla/5.0 (X11; U; Linux x86; en-US; rv:1.8.1.6) Gecko/20061201 Firefox/2.0.0.6 (Ubuntu-feisty)',
      'Mozilla/5.0 (X11; U; Linux x86; es-ES; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
      'Mozilla/5.0 (X11; U; Linux x86; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1',
      'Mozilla/5.0 (X11; U; Linux x86; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/8.04 (hardy) Firefox/2.0.0.12',
      'Mozilla/5.0 (X11; U; Mac OSX; it; rv:1.9.0.7) Gecko/2009030422 Firefox/3.0.7',
      'Mozilla/5.0 (X11; U; NetBSD alpha; en-US; rv:1.8.1.6) Gecko/20080115 Firefox/2.0.0.6',
      'Mozilla/5.0 (X11; U; NetBSD amd64; fr-FR; rv:1.8.0.7) Gecko/20061102 Firefox/1.5.0.7',
      'Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.8.0.5) Gecko/20060818 Firefox/1.5.0.5',
      'Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.8) Gecko/20060104 Firefox/1.5',
      'Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.9.2.12) Gecko/20101030 Firefox/3.6.12',
      'Mozilla/5.0 (X11; U; OpenBSD sparc64; pl-PL; rv:1.8.0.2) Gecko/20060429 Firefox/1.5.0.2',
      'Mozilla/5.0 (X11; U; Slackware Linux i686; en-US; rv:1.9.0.10) Gecko/2009042315 Firefox/3.0.10',
      'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.7.12) Gecko/20051121 Firefox/1.0.7 (Nexenta package 1.0.7)',
      'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.7.5) Gecko/20041109 Firefox/1.0',
      'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.0.5) Gecko/20060728 Firefox/1.5.0.5',
      'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.3) Gecko/20070423 Firefox/2.0.0.3',
      'Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0',
      'Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8.1) Gecko/20061228 Firefox/2.0',
      'Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.8) Gecko/20051130 Firefox/1.5',
      'Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5',
      'Mozilla/5.0 (X11; U; SunOS sun4u; it-IT;) Gecko/20080000 Firefox/3.0',
      'Mozilla/5.0 (X11; U; SunOS sun4u; pl-PL; rv:1.8.1.6) Gecko/20071217 Firefox/2.0.0.6',
      'Mozilla/5.0 (X11; U; SunOS sun4v; en-US; rv:1.8.1.3) Gecko/20070321 Firefox/2.0.0.3',
      'Mozilla/5.0 (X11; U; SunOS sun4v; es-ES; rv:1.8.1.9) Gecko/20071127 Firefox/2.0.0.9',
      'Mozilla/5.0 (X11; U; Windows NT 5.0; en-US; rv:1.9b4) Gecko/2008030318 Firefox/3.0b4',
      'Mozilla/5.0 (X11; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',
      'Mozilla/5.0 (X11; U; Windows NT i686; fr; rv:1.9.0.1) Gecko/2008070206 Firefox/2.0.0.8',
      'Mozilla/5.0 (X11; U; x86_64 Linux; en_GB, en_US; rv:1.9.2) Gecko/20100115 Firefox/3.6',
      'Mozilla/5.0 (X11; U; x86_64 Linux; en_US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Mozilla/5.0 (X11; U; x86_64 Linux; en_US; rv:1.8.16) Gecko/20071015 Firefox/2.0.0.8',
      'Mozilla/5.0 (X11; U; x86_64 Linux; en_US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5',
      'Mozilla/5.0 (ZX-81; U; CP/M86; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1',
      'Mozilla/6.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4',
      'Mozilla/6.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:2.0.0.0) Gecko/20061028 Firefox/3.0',
      'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
      'Mozilla/6.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8',
      'Mozilla/5.0 (Windows 8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30',
      'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
      'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.249.0 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.43 Safari/534.24',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) Chrome/4.0.223.3 Safari/532.2',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 95)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 95; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows 98)',
      'Mozilla/4.0 (compatible; MSIE 4.0; Windows NT)',
      'Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)',
      'Mozilla/4.0 (compatible; MSIE 4.5; Windows 98;)',
      'Mozilla/4.0 (compatible; MSIE 4.5; Windows NT 5.1; .NET CLR 2.0.40607)',
      'Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)',
      'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT)',
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

header = {'User-Agent': random.choice(ua)}
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


def dorker():
    pages = 1
    how_much = 15
    use_one_dork = input(Fore.RESET + "[+] Use one dork? [y/n]\n[OPTION] ==> ")
    if use_one_dork != "y":
        print("[+] Checking dorks.txt...")
        file_with_dorks = open("dorks.txt", "r")
        dorks = [line for line in file_with_dorks.readlines()]
        file_with_dorks.close()
        a = len(dorks)
        c = 0
        while c < int(a):
            while pages != int(how_much):
                # print("\n\n\nTrying dork: " + str(dorks[c]))
                # send = requests.get("http://www1.search-results.com/web?q=" + str(dorks[c]) + "&page=" + str(pages))
                # parsing = BeautifulSoup(send.text, features="html.parser")
                send = http.request("GET", "http://www1.search-results.com/web?q=" + str(dorks[c]) + "&page="
                                    + str(pages))
                parsing = BeautifulSoup(send.data.decode('utf-8'), features="html.parser")
                for data in parsing.find_all("cite"):
                    print(data.string)
                    f = open(result_name, "a", encoding="utf=8")
                    f.write(data.string + "\n")
                    f.close()
                pages = pages + 1
            c = c + 1
    else:
        user_dork = input("[+] Enter your dork:\n[OPTION] ==> ")
        while pages != int(how_much):
            # print(Fore.RESET + "\n\n\nTrying dork: " + user_dork)
            send = http.request("GET", "http://www1.search-results.com/web?q=" + user_dork + "&page=" + str(pages))
            parsing = BeautifulSoup(send.data.decode('utf-8'), features="html.parser")
            for data in parsing.find_all("cite"):
                print(data.string)
                f = open(result_name, "a", encoding="utf=8")
                f.write(data.string + "\n")
                f.close()
            pages = pages + 1


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


def main():
    dorker_logo()
    usr_inpt = input('''
[1] Dorker
[2] SQLi checker
[3] Exit
[!] ==> ''')
    if usr_inpt == "1":
        dorker()
        decision = input(Fore.RESET + "\n[+] Run SQLi checker? [y/n]\n[OPTION] ==> ")
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

    else:
        print(Fore.RESET + "Thanks for using D0RK3R!")
        exit(0)


if __name__ == '__main__':
    main()

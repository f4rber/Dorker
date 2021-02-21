# Dorker
Let the D0RK3R make dirty work :)

This script can be quite useful in early phases of pentest.

Current tool set:
```
[1] Dorker
[2] SQLi checker
[3] LFI checker
[4] Scan specific site
```
```

To enable HTTP proxy mode you need to create a "proxy_list.txt" which will contain proxies like:
192.167.81.18:8080
128.171.81.18:80
34.63.31.168:5427
```
# Examples

# Find information by dorks
```
     ____  ____  ____  __ __ __________
    / __ \/ __ \/ __ \/ //_// ____/ __ \
   / / / / / / / /_/ / ,<  / __/ / /_/ /
  / /_/ / /_/ / _, _/ /| |/ /___/ _, _/
 /_____/\____/_/ |_/_/ |_/_____/_/ |_|

  Dorker
   Version: 1.5 made with ♥ by FARBER


[1] Dorker
[2] SQLi checker
[3] LFI checker
[4] Scan specific site
[99] Exit
 [:]==> 1
[+] Checking dorks.txt...

index.php?id=
news.php?id=
view.php?where=
blank.php?subject=
path.php?play=
base.php?l=
include.php?my=

[!] Start dorker in multithread mode? y/n
 [:]==> n

PAGE: 1
DORK: index.php?id=
Search-results:
https://www.isbtweb.org/index.php?id=1493
https://www.ionos.com/terms-gtc/index.php?id=6
http://www.goodtidings.org/index.php?id=23
https://www.dt-shop.com/index.php?id=3&L=1
https://www.car-2-car.org/service/login/
https://www.opcalia.com/index.php?id=61
http://www.wesley.edu/index.php?id=32
https://www.laboshop.com/index.php?id=5&L=1
http://www.taanilinna.com/index.php?id=325
https://www.ccbe.eu/index.php?id=12&L=0
Auone:
https://www.ionos.com/terms-gtc/index.php?id=6
https://www.isbtweb.org/index.php?id=1493
http://www.taanilinna.com/index.php?id=325
https://www.laboshop.com/index.php?id=5&L=1
https://www.dt-shop.com/index.php?id=3&L=1
https://www.car-2-car.org/service/login/
http://pyroswitch.com/index.php?id=3
https://stackoverflow.com/questions/36280383/php-get-method-without-index-phpid-xxx/36280603
http://www.osaeru.net/reserve/index.php?id=6432&plannum=172871249&listdate=&view=plan
http://www.goodtidings.org/index.php?id=23
Qwant:
https://www.rbch.nhs.uk/index.php?id=1
www.cypp.powys.gov.uk/index.php?id=4658
https://secure.abukai.com/user/index.php?id=0
www.cacert.org/index.php?id=1
https://thebootroom.thefa.com/learning/qualifications
https://learn.nihr.ac.uk/enrol/index.php?id=370
https://commerciallevel.com/index.php?id=1
www.icdcprague.org/index.php?id=10
https://academy.roadmaptozero.com/index.php?id=80
https://www.agisoft.com/index.php?id=31
Lilo:
http://www.efa.de/index.php?id=fahrplanauskunft
https://www.php.net/manual/de/index.php
https://www.kvbawue.de/index.php?id=1
https://www1.ids-mannheim.de/index.php?id=1
https://www.lmz-bw.de/index.php?id=15111
https://chemiedidaktik.uni-wuppertal.de/index.php?id=5126&L=0
https://kant-boppard.de/index.php?id=6
http://de.callofwar.com/index.php?id=304&L=1
https://www.lombagine.info/index.php?id=24
https://www.dt-shop.com/index.php?id=1&L=1
Mywebsearch:
https://www.pstu.edu/index.php?id=2
https://www.isbtweb.org/index.php?id=1493
https://www.ionos.com/terms-gtc/index.php?id=6
http://www.goodtidings.org/index.php?id=23
https://www.opcalia.com/index.php?id=61
https://www.dt-shop.com/index.php?id=3&L=1
https://www.swissport.com/index.php?id=4&level=country&continentId=4&countryId=177
https://www.car-2-car.org/service/login/
http://www.wesley.edu/index.php?id=32
https://www.ccbe.eu/index.php?id=12&L=0
```
# Check for SQLi
```
     ____  ____  ____  __ __ __________
    / __ \/ __ \/ __ \/ //_// ____/ __ \
   / / / / / / / /_/ / ,<  / __/ / /_/ /
  / /_/ / /_/ / _, _/ /| |/ /___/ _, _/
 /_____/\____/_/ |_/_/ |_/_____/_/ |_|

  Dorker
   Version: 1.5 made with ♥ by FARBER


[1] Dorker
[2] SQLi checker
[3] LFI checker
[4] Scan specific site
[99] Exit
 [:]==> 2
Skipping https://www.darknet.org.uk/2017/10/sqliv-sql-injection-dork-scanning-tool
Skipping https://prime.edu.pk/login.php
Skipping https://stauff.com/
Skipping https://www.jeddah.gov.sa/index.php
Skipping https://muic.mahidol.ac.th/eng/
www.nusantara.rs/vesti_celeE.php?id=99 not vulnerable!
Skipping https://www.databiology.com/index.php/product
https://www.isbtweb.org/index.php?id=1493 not vulnerable!
https://www.opcalia.com/index.php?id=61 not vulnerable!
http://swa.city-osaka.ed.jp/swas/index.php?id=e591246 not vulnerable!
02b8c37.netsolhost.com/18/inurl-index.php-id=-1-1 not vulnerable!
https://bloody.com/EN/download.php?id=6 not vulnerable!
http://www.taanilinna.com/index.php?id=325 not vulnerable!
http://berkeleyrecycling.org/page.php?id=1 seems vulnerable!
https://www.migration.gov.rw/index.php?id=197 not vulnerable!
www.eufores.org/index.php?id=131 not vulnerable!
http://www.skystartravels.com/gallery.php?id=1 seems vulnerable!
http://www.osaeru.net/reserve/index.php?id=6432&plannum=172871249&listdate=&view=plan not vulnerable!
https://www.cumulusassociation.org/admini/index.php?id=1170&page=edit not vulnerable!
berkeleyrecycling.org/page.php?id=1 seems vulnerable!
https://www.tnm.jp/modules/r_free_page/index.php?id=103 not vulnerable!
https://www.hiscoll.com/shop.php?ps=1 not vulnerable!
http://pyroswitch.com/index.php?id=3 not vulnerable!
Skipping https://www.exploit-db.com/ghdb/3826
https://www.facebook.com/permalink.php?id=112691172180964&story_fbid=591207530894998 not vulnerable!
Skipping https://github.com/googleinurl/SCANNER-INURLBR
https://www.tnm.jp/modules/r_free_page/index.php?id=2042 not vulnerable!
www.stasy.gr/index.php?id=67&L=1 not vulnerable!
Skipping https://inurl-view-index-shtml-com.blogspot.com/2011/03/airport-webcams.html
www.dkcompany.dk/index.php?id=1604 not vulnerable!
Skipping www.onmove.co.uk/admin/login.php
www.cacert.org/index.php?id=4 not vulnerable!
www.dockguard.co.uk/page.php?id=18 not vulnerable!
https://isr-tkd.com/index.php?cntr=e/news.php?id=1 seems vulnerable!
```

import socket
import os
import sys
from datetime import datetime
import requests                          #pip install requests
from psutil import process_iter          #pip install psutil

#الاوان
#\033[4;31m      red
#\033[1;32m      green

# تنضيف الشاشه
os.system('clear')

# فحص داخلي
remoteServerIP  = '127.0.0.1'

print("\033[1;32m  ___  ___  ___ _____   ___  ___   _   _  _ _  _ ___ ___  ")
print(" | _ \/ _ \| _ \_   _| / __|/ __| /_\ | \| | \| | __| _ \ ")
print(" |  _/ (_) |   / | |   \__ \ (__ / _ \| .` | .` | _||   / ")
print(" |_|  \___/|_|_\ |_|   |___/\___/_/ \_\_|\_|_|\_|___|_|_\ ")
print(" [+]by @zaky1_mohammed")



print("------------------------------------------")
print("Please Wait, Scanning Your Device")
res = requests.get("http://checkip.dyndns.org")
print("Your IP is : ",res.text[75:88])  
print("------------------------------------------")
print("[+]It's Will Take About 3M")
print("")

# حساب وقت الفحص
t1 = datetime.now()

#بدء الفحص
def scan (port):
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("")
            print ("\033[4;31m[-]Dangerous Port ",port," :  Opened")
        sock.close()

    except KeyboardInterrupt:
        print ("\033[4;31m[-]You pressed Ctrl+C")

    except socket.gaierror:
        print ('\033[4;31m[-]Hostname could not be resolved. Exiting')

    except socket.error:
        print ("\033[4;31m[-]socket error")


#بدء الفحص
scan(4444)
scan(8080)
scan(2)
scan(21)
scan(23) 
scan(21)
scan(22)
scan(25)
scan(48)
scan(50)
scan(80)
scan(123)
scan(146)
print("\033[1;32m[+]10% Of Scaning is Done")
scan(605)
scan(777)
scan(1000)
scan(1001)
scan(1020)
scan(23)
scan(25)
scan(1050)
scan(1080)
scan(1095)
scan(1097)
scan(1098)
scan(1099)
print("\033[1;32m[+]20% Of Scaning is Done")
scan(1200)
scan(1201)
scan(1207)
scan(1313)
scan(53)
scan(80)
scan(1969)
scan(2000)
scan(2001)
scan(2300)
scan(2716)
scan(2773)
scan(3456)
print("\033[1;32m[+]30% Of Scaning is Done")
scan(4242)
scan(5031)
scan(5637)
scan(5638)
scan(110)
scan(111)
scan(6272)
scan(6667)
scan(6669)
scan(6711)
scan(6712)
scan(6713)
scan(6776)
print("\033[1;32m[+]40% Of Scaning is Done")
scan(7000)
scan(7215)
scan(8787)
scan(135)
scan(139)
scan(8897)
scan(8989)
scan(9999)
scan(10086)
scan(10666)
scan(11050)
scan(11223)
scan(12349)
print("\033[1;32m[+]50% Of Scaning is Done")
scan(12623)
scan(16484)
scan(143)
scan(443)
scan(16772)
scan(17777)
scan(19864)
scan(20203)
scan(20331)
scan(27374)
scan(27573)
scan(32418)
scan(34555)
print("\033[1;32m[+]60% Of Scaning is Done")
scan(35555)
scan(37651)
scan(52317)
scan(445)
scan(993)
scan(54283)
scan(57341)
scan(61348)
scan(61603)
scan(63485)
scan(65432)
scan(31)
scan(1170)
print("\033[1;32m[+]70% Of Scaning is Done")
scan(1234)
scan(1243)
scan(1981)
scan(2001)
scan(995)
scan(1723)
scan(2023)
scan(2140)
scan(2989)
scan(3024)
scan(3150)
scan(3700)
scan(4950)
print("\033[1;32m[+]80% Of Scaning is Done")
scan(6346)
scan(6400)
scan(6667)
scan(3306)
scan(3389)
scan(6670)
scan(12345)
scan(12346)
scan(16660)
scan(18753)
scan(20034)
scan(20432)
scan(20433)
print("\033[1;32m[+]90% Of Scaning is Done")
scan(27374)
scan(27444)
scan(27665)
scan(30100)
scan(31335)
scan(5900)
scan(8080)
scan(31337)
scan(33270)
scan(33567)
scan(33568)
scan(65000)
print("\033[1;32m[+]100% Of Scaning is Done,Please Wait..")
print("")
#انتهئ الفحص

#وقت الفحص مرة ثانية
t2 = datetime.now()

#حساب وقت الفحص
total =  t2 - t1


print('\033[1;32m[+]Scanning Completed in: ', total)
print("")


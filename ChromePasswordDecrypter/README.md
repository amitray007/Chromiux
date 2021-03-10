<h1 align='center'>Chrome Password Decrypter</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <img src="https://badgen.net/badge/icon/windows?icon=windows&label"/>
  <img src="https://img.shields.io/maintenance/yes/2021" />
  <a href="https://github.com/amitray007/Chromiux/blob/main/LICENSE">
    <img src="http://img.shields.io/github/license/amitray007/Chromiux">
  </a>
    <a href="https://github.com/amitray007/Chromiux">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a></br>
  <a href="https://github.com/amitray007/Chromiux/commits/master">
    <img src="https://img.shields.io/github/last-commit/amitray007/Chromiux" />
  </a>
  <img src="https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg">
  <img src="https://badgen.net/badge/icon/chrome?icon=chrome&label"></br>
  <a href="https://gitpod.io/#https://github.com/amitray007/Chromiux">
    <img src="https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod" />
  </a>
</p>

## Getting started

ChromePasswordDecrypter displays/extracts all the decrypted passwords from internal chrome database.

## Usage

```powershell
> py ChromePasswordDecrypter.py
usage: ChromePasswordDecrypter.py [-h] -s | -t | -l <URL> | -u <USERNAME> | -p <PASSWORD>
ChromePasswordDecrypter.py: error: the following arguments are required:
-s/--show OR -t/--txt OR -l/--url OR -u/--username OR -p/--password
```

- Display Decrypted Saved Passwords
```powershell
> py ChromePasswordDecrypter.py -s

  ______________                         _____
 __  ____/__  /_____________________ ______(_)___  _____  __
 _  /    __  __ \_  ___/  __ \_  __ `__ \_  /_  / / /_  |/_/
 / /___  _  / / /  /   / /_/ /  / / / / /  / / /_/ /__>  <
 \____/  /_/ /_//_/    \____//_/ /_/ /_//_/  \__,_/ /_/|_|


         Created By : GitHub | amitray007


        ** Passwords for Default User **

 --------------------------------------------------
 [+] URL: https://www.0x45.com/
 [-] User Name: Administrator
 [-] Password: $3c43t9@s5w046
 --------------------------------------------------

 **************************************************

        ** Passwords for Guest Profile User **

 --------------------------------------------------
 [!] No Passwords Found in Guest Profile
 --------------------------------------------------

 **************************************************
```

- Save the decrypted password in txt format
```powershell
> py ChromePasswordDecrypter.py -t

 --------------------------------------------------
 [!] Decrypted Passwords saved in ./ChromeDefaultSavedPasswords.txt for Default User
 --------------------------------------------------

 --------------------------------------------------
 [!] No Passwords Found in Guest Profile
 --------------------------------------------------
```

- Search decrypted password based upon URL
```powershell
> py ChromePasswordDecrypter.py -l https://www.0x45.com/

        ** Search Results **
        
 --------------------------------------------------
 [+] URL: https://www.0x45.com/
 [-] User Name: Administrator
 [-] Password: $3c43t9@s5w046
 --------------------------------------------------
```

- Search decrypted password based upon Username
```powershell
> py ChromePasswordDecrypter.py -u Administrator

        ** Search Results **
        
 --------------------------------------------------
 [+] URL: https://www.0x45.com/
 [-] User Name: Administrator
 [-] Password: $3c43t9@s5w046
 --------------------------------------------------
```

- Search decrypted password based upon Password
```powershell
> py ChromePasswordDecrypter.py -p $3c43t9@s5w046

        ** Search Results **
        
 --------------------------------------------------
 [+] URL: https://www.0x45.com/
 [-] User Name: Administrator
 [-] Password: $3c43t9@s5w046
 --------------------------------------------------
```

## Errors, Bugs and feature requests

If you find an error or a bug, please report it as an issue here: <a href="https://github.com/amitray007/Chromiux/issues/new?assignees=&labels=&template=bug_report.md&title=">Report Bug</a></br>
If you wish to suggest a feature or an improvement please report it here: <a href="https://github.com/amitray007/Chromiux/issues/new?assignees=&labels=&template=feature_request.md&title=">Request Feature</a>

Please follow the templates shown when creating the issue.

## Contributing
Pull requests are welcome. Feel free to contribute.
- For major changes, please initially open an issue to discuss what you would like to update.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/amitray007/Chromiux/blob/main/LICENSE)

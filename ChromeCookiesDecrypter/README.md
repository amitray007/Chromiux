<h1 align='center'>Chrome Cookies Decrypter</h1>
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

ChromeCookiesDecrypter displays/extracts all the decrypted cookies from internal chrome database.

## Usage

```powershell
> py ChromeCookiesDecrypter.py
usage: ChromeCookiesDecrypter.py [-h] -s | -t
ChromeCookiesDecrypter.py: error: the following arguments are required: -s/--show OR -t/--txt
```

- Display Decrypted Saved Cookies
```powershell
> py ChromeCookiesDecrypter.py -s

  ______________                         _____
 __  ____/__  /_____________________ ______(_)___  _____  __
 _  /    __  __ \_  ___/  __ \_  __ `__ \_  /_  / / /_  |/_/
 / /___  _  / / /  /   / /_/ /  / / / / /  / / /_/ /__>  <
 \____/  /_/ /_//_/    \____//_/ /_/ /_//_/  \__,_/ /_/|_|


         Created By : GitHub | amitray007


        ** Cookies for Default User **

 --------------------------------------------------
 [+] URL: https://www.0x45.com/
 [-] CookieID: __Host-user_session_same_site
 [-] CookieData: 1%7C5%2C41%7C6%2C76%7C7%2C68%7C8%2C62%7C9
 --------------------------------------------------

 **************************************************

        ** Cookies for Guest Profile User **

 --------------------------------------------------
 [!] No Cookies Found in Guest Profile
 --------------------------------------------------

 **************************************************
```

- Save the decrypted cookies in txt format
```powershell
> py ChromeCookiesDecrypter.py -t

 --------------------------------------------------
 [!] Decrypted Cookies saved in ./ChromeDefaultSavedCookies.txt for Default User
 --------------------------------------------------

 --------------------------------------------------
 [!] No Cookies Found in Guest Profile
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
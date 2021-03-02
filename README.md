<h1 align='center'>Chromiux - Chrome Advanced Decrypter</h1>
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

Chromiux is a python based console app that extracts the encrypted saved passwords/cookies in txt format.

### Dependencies and Requirements

This is a very simple application, which uses only:

* [Python] - Only tested on 3.7.7 but should work in 3.5+

### Installation

Chromiux requires [Python] 3.5+ to run.

Install the dependencies:

```powershell
> cd Chromiux
> pip install -r requirements.txt
```

If any errors occur make sure you're running on the proper environment (if applicable) and that you have python 3.5+ (preferably 3.7.7).
If the errors persist, try:
```powershell
> python -m pip install --upgrade pip
> python -m pip install -r requirements.txt
```

## Usage

- ChromePasswordDecrypter
```powershell
> py ChromePasswordDecrypter.py -h
  ______________                         _____
 __  ____/__  /_____________________ ______(_)___  _____  __
 _  /    __  __ \_  ___/  __ \_  __ `__ \_  /_  / / /_  |/_/
 / /___  _  / / /  /   / /_/ /  / / / / /  / / /_/ /__>  <
 \____/  /_/ /_//_/    \____//_/ /_/ /_//_/  \__,_/ /_/|_|


         Created By : GitHub | amitray007
         
usage: ChromePasswordDecrypter.py [-h] [-s] [-t]

[+] Chrome Saved Password Decrypter

optional arguments:
  -h, --help  show this help message and exit
  -s, --show  Display Decrypted password in terminal
  -t, --txt   Save Decrypted password in txt format
```

- ChromeCookiesDecrypter
```powershell
> py ChromeCookiesDecrypter.py -h
  ______________                         _____
 __  ____/__  /_____________________ ______(_)___  _____  __
 _  /    __  __ \_  ___/  __ \_  __ `__ \_  /_  / / /_  |/_/
 / /___  _  / / /  /   / /_/ /  / / / / /  / / /_/ /__>  <
 \____/  /_/ /_//_/    \____//_/ /_/ /_//_/  \__,_/ /_/|_|


         Created By : GitHub | amitray007
         
usage: ChromeCookiesDecrypter.py [-h] [-s] [-t]

[+] Chrome Saved Cookies Decrypter

optional arguments:
  -h, --help  show this help message and exit
  -s, --show  Display Decrypted cookies in terminal
  -t, --txt   Save Decrypted cookies in txt format
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
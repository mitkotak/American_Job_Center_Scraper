<h1 align="center">Welcome to American_Job_Center_Scraper 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-2.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/mitkotak/American_Job_Center_Scraper" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/mitkotak/American_Job_Center_Scraper/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT " src="https://img.shields.io/badge/License-MIT -yellow.svg" />
  </a>
</p>

> Webscraper for https://www.careeronestop.org/LocalHelp/AmericanJobCenters/find-american-job-centers.aspx

### 🏠 [Homepage](https://github.com/mitkotak/American_Job_Center_Scraper)

### ✨ [Demo](https://github.com/mitkotak/American_Job_Center_Scraper)

## Usage

Fire up your terminal/command prompt, navigate to the repo folder and install all of the requirements. This can take a while :)

```sh
pip install -r requirements.txt
```

Now make sure that you have correct input csv file. E.g test_zipcode.csv in [webscraper_v2.py](https://github.com/mitkotak/American_Job_Center_Scraper/blob/128700e78a69a8e9279376717fd30862b2d4f6ff/webscraper_v2.py#L24)

```sh
with open('test_zipcode.csv') as f:
```

Install the latest version of [chromedriver](https://chromedriver.chromium.org) and make sure that you have the correct path in [webscraper_v2.py
](https://github.com/mitkotak/American_Job_Center_Scraper/blob/128700e78a69a8e9279376717fd30862b2d4f6ff/webscraper_v2.py#L21)

```sh
driver = webdriver.Chrome('/Users/mit/Downloads/chromedriver')
```

Just run the following command after this:

```sh
python3 webscraper_v2.py
```
Or 

```sh
python webscraper_v2.py
``` 

### Let the scrapping begin !!

<p align="center">
  <img width="500" align="center" src="https://media.giphy.com/media/d8PjnRdlAP52F1CImb/giphy.gif" alt="demo"/>
</p>

## Author

👤 **Mit Kotak**

* Github: [@mitkotak](https://github.com/mitkotak)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/mitkotak/American_Job_Center_Scraper/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Mit Kotak](https://github.com/mitkotak).<br />
This project is [MIT ](https://github.com/mitkotak/American_Job_Center_Scraper/blob/main/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

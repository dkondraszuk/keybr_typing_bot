# keybr_typing_bot
Fun project created in Python + Selenium Webdriver.\
The goal of the project was to win High Scores table on keybr.com:\
*https://www.keybr.com/high-scores*

keybr.com is an online typing practice tool. It also keeps statistics about individual users that are using it.

High Scores table is updated every few days, so that it promotes recently active users.

With this typing bot, you will be able to get to the 1st place in just a few minutes!

## Install requirements:
pip install -r requirements.txt

## Other requirements:
* python3
* Mozilla Firefox

## How to use
* Create an accout on: keybr.com
* You should receive an email with your login link (something similar to *https://www.keybr.com/login/**<your_key>***)
* Copy **<your_key>** and save it as **KEYBR_KEY** environment variable (under linux you can modify */etc/environment* and add
new line: KEYBR_KEY="**<your_key>**" and then '*source /etc/environment*'
* Now you are able to use the typing bot. Just run
 ```bash
 $ python3 practice_typing.py
 ```
* You can specify how many times typing bot should practice. To do that provide flag *-r* or *--repeat* with number of repetitions:
```bash
$ python3 practice_typing.py --repeat 5
```
* If you don't specify repeat option, by default bot will execute 10 repetitions. You can stop earlier by pressing Ctrl+C 
* After few minutes of typing, your account should be listed as the top 1 in High Scores
* Have fun!


import os
from selenium import webdriver
# we can hit enter keyboard, add input when we login
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # open firefox visit the link
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        # pause app 3 seconds for webpage to load
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        # send keys
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        # execute_script - Javascript
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            # find tweets
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception:
                    time.sleep(60)


twitter_email = os.environ.get('TWITTER_EMAIL')
twitter_password = os.environ.get('TWITTER_PASSWORD')

jibreel = TwitterBot(twitter_email, twitter_password)
jibreel.login()
jibreel.like_tweet('nba')

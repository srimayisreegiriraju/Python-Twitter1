#!/usr/bin/python

"""
    Description: This will ask the user to enter the status he/she wishes to tweet and updates it on the twitter account
"""


from twitter import*

access_token="100542127-V1KJhz5RU7myuIMZPImX6tJiYj2rJ1r31MJCzQnh"

access_token_secret='bMEiUIA5FS7r65m3POyXT9YHW2sYe8EWY0umHPLqmjEaW'

consumer_key= '0dLq1yEJl3vEp9xwzmMzmJvt6'

consumer_secret='zJIV7yWp9IGUy5OtK9ryoBZIGOBUoFa5g6AabeyuABC2zWyTyh'

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

tweet= raw_input("Enter your tweet:")

t.statuses.update(status=tweet)



'''
Local Settings for a lattnet account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'vYQsul814SkVCyv3vH7FY5lmp'
MY_CONSUMER_SECRET = 'vgbZQxqCix6IuHrbPkWGyqjB45fvBOqeCL9XUwA31V47VZ5Whh'
MY_ACCESS_TOKEN_KEY = '923982719771709440-LHGyy9oZ7QqSpSLVxqjZ0JQe7qfQ3Qk'
MY_ACCESS_TOKEN_SECRET = '1xyX1BgUTwd2CtwJQpW7411mL2nsSm0HlSw8qGkZhLqyg'

SOURCE_ACCOUNTS = ["andrewsplattner"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 2 is low and 4 is high.
SOURCE_EXCLUDE = r'^$' #Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "lattnet" #The name of the account you're tweeting to.

#%%
import random
import webbrowser
baseURL = 'http://www.speedcoder.net/lessons/customcode/'
number = str(random.randint(1,10)) # generate random number from 1 to 10 and convert integer to string to allow concatenation
newURL = baseURL + number
print(newURL)
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" # https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser
webbrowser.get(chrome_path).open(newURL)

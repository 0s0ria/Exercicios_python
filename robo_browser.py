import requests
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True,parser='html.parser')
browser.open('https://www.bing.com/')

form =browser.get_form(action='/search')
form
form['q'].value = 'merda'
browser.submit_form(form)

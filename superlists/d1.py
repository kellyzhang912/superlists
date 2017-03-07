from selenium import webdriver

b=webdriver.Firefox()
b.get('http://localhost:8000')
assert 'Django' in b.title
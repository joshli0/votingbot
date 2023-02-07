import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

with open ("credentials.txt", "r") as myfile:
    data = myfile.read().splitlines()

username = data[0]
password = data[1]

PATH = r"C:\Users\jli61\Downloads\chromedriver_win32.zip\chromedriver"
driver = webdriver.Chrome(PATH)  # to open the browser
  
# url of google news website
url = 'https://vote.nba.com/en'
  
# to open the url in the browser
driver.get(url)  

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/button[2]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div/div[1]/button").click()
search = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/div/div[2]/div[1]/div/input")
players = ['Lebron James', 'Anthony Davis', 'Domantas Sabonis', 'Ja Morant', 'Austin Reaves', 'Joel Embiid', 'Giannis Antetokounmpo', 'Kyle Kuzma', 'Trae Young', 'Kyrie Irving']
for player in players: 
    search.send_keys(player)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div/div/div[2]/div/button").click()
    search.clear()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/a").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div/div[2]/button").click()
search = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[1]/input")
search.send_keys(username)
search = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[2]/input")
search.send_keys(password)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/form/div/div[4]/div/button").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button").click()
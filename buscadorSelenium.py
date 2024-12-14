from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://twitter.com/search?q=presidente+bolsonaro") # Encontrar todos os tweets
tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

for tweet in tweets:
    texto = tweet.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
    data = tweet.find_element(By.XPATH, ".//time").get_attribute("datetime")
    print(texto, data)

driver.quit()
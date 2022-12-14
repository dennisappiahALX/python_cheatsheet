import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")

for question in questions:
    print(question.select_one(".question-hyperlink").getText())

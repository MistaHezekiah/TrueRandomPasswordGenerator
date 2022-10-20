import random
import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://en.wikipedia.org/wiki/Prime_Minister_of_the_United_Kingdom",)
soup = BeautifulSoup(response.content, 'html.parser')
pm = soup.select(".infobox > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > div:nth-child(1) > b:nth-child(2) > a:nth-child(2)")
seed = pm[0].get("title")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
random.seed(seed)

print("Welcome to the true random password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

for letter in range(0, nr_letters):
    password += random.choice(letters)
for number in range(0, nr_symbols):
    password += random.choice(symbols)
for symbol in range(0, nr_symbols):
    password += random.choice(numbers)

random.shuffle(password)
print("".join(password))

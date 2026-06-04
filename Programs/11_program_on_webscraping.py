"""
Program on webscraping using library BeautifulSoup
Library: BeautifulSoup4
Documentation: https://pypi.org/project/beautifulsoup4/
"""

"""
Requirement:

1. Get website title
2. Get top menu items
3. Get first paragraph
4. Get all paragraphs

Write this information to web_scraping.json file
"""
print("Getting website data")
print("-"*20)
# ---------------

import requests
response = requests.get("http://www.python.org/")
web_content = response.text
print(web_content)

print("#"*40, end="\n\n")
#########################

print("Create object of BeautifulSoup class and store web_content inside that object")
print("-"*20)
# ---------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)

print("#"*40, end="\n\n")
#########################
print("Entire website data in one string")
print("-"*20)
# ---------------

entire_website_data = soup.get_text()
print(entire_website_data)

print("#"*40, end="\n\n")
#########################

print("Task-1. Get website title : PART-1")
print("Get 1st title tag on entire website data")
print("-"*20)
# ---------------

title_tag = soup.title
print("title_tag:", title_tag) # <title>Welcome to Python.org</title>

print("#"*40, end="\n\n")
#########################

print("Task-1. Get website title : PART-2")
print("Get 1st title tag within head tag")
print("-"*20)
# ---------------

title_tag = soup.head.title
print("title_tag:", title_tag) # <title>Welcome to Python.org</title>

print("#"*40, end="\n\n")
#########################

print("Task-1. Get website title : PART-3")
print("Get title tag text")
print("-"*20)
# ---------------

title_tag_text = soup.head.title.text
print("title_tag_text:", title_tag_text) #  Welcome to Python.org
print("type of title_tag_text:", type(title_tag_text))

print("#"*40, end="\n\n")
#########################
print("Task-2: Get top menu items : PART-1")
print("Reducing the content: get first div tag within body")
print("-"*20)
# ---------------

reduced_content_1 = soup.body.div
print("reduced_content_1:", reduced_content_1)

print("#"*40, end="\n\n")
#########################

print("Task-2: Get top menu items : PART-2")
print("Reducing the content: get div tag where id=top")
print("-"*20)
# ---------------

reduced_content_2 = reduced_content_1.find(id="top")
print(reduced_content_2)

print("#"*40, end="\n\n")
#########################

print("Task-2: Get top menu items : PART-3")
print("Reducing the content: nav tag")
print("-"*20)
# ---------------

reduced_content_3 = reduced_content_2.nav
print(reduced_content_3)

print("#"*40, end="\n\n")
#########################

print("Task-2: Get top menu items : PART-4")
print("Reducing the content: ul tag")
print("-"*20)
# ---------------

reduced_content_4 = reduced_content_3.ul
print(reduced_content_4)

print("#"*40, end="\n\n")
#########################

print("Task-2: Get top menu items : PART-5")
print("Get all li tag")
print("-"*20)
# ---------------

all_li_tags = reduced_content_4.find_all('li')
print(all_li_tags)

print("#"*40, end="\n\n")
#########################

print("Task-2: Get top menu items : PART-6")
print("Get all top menu items")
print("-"*20)
# ---------------

top_menu_items = []
for each_li_tag in all_li_tags:
    menu_item = each_li_tag.a.text
    top_menu_items.append(menu_item)

print(top_menu_items)

print("#"*40, end="\n\n")
#########################
print("Task-3. Get first paragraph: PART-1")
print("Reducing content: div tag where class = introduction")
print("-"*20)
# ---------------

reduced_content_1 = soup.find("div", class_="introduction")
print(reduced_content_1)

print("#"*40, end="\n\n")
#########################

print("Task-3. Get first paragraph: PART-2")
print('"Get first paragraph content"')
print("-"*20)
# ---------------

first_paragraph = reduced_content_1.p.text
print(first_paragraph)

print("#"*40, end="\n\n")
#########################
print("Task-4. Get all paragraphs: PART-1")
print("Get all paragraph tags")
print("-"*20)
# ---------------

all_paragraph_tags = soup.find_all('p')
print(all_paragraph_tags)

print("#"*40, end="\n\n")
#########################

print("Task-4. Get all paragraphs: PART-2")
print("Get all paragraph tags content")
print("-"*20)
# ---------------

all_paragraphs = []
for each_paragraph_tag in all_paragraph_tags:
    paragraph = each_paragraph_tag.text
    all_paragraphs.append(paragraph)

print(all_paragraphs)

print("#"*40, end="\n\n")
#########################
print("Making dictionary")
print("-"*20)
# ---------------

my_dictionary = {
    "Title": title_tag_text,
    "Top_Menu_Items": top_menu_items,
    "First_Paragraph": first_paragraph,
    "All_Paragraphs": all_paragraphs
}
print(my_dictionary)

print("#"*40, end="\n\n")
#########################

print("Writing to web_scraping.json")
print("-"*20)
# ---------------

my_json_file_handle = open(file="web_scraping.json", mode="w")
import json
json.dump(my_dictionary, my_json_file_handle)
my_json_file_handle.close()

print("Created 'web_scraping.json', Please check")

print("#"*40, end="\n\n")
#########################

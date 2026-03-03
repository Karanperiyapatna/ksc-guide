import csv
from bs4 import BeautifulSoup

# --------- Read CSV ---------
with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    row = next(reader)
    new_header = row['header']
    new_body = row['body']
    new_link = row['link']


# --------- UPDATE index.html ---------
with open('index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

div = soup.find('div', class_='card-body editorial-body')

if div:
    links = div.find_all('a', class_='update-row')

    # Update 1st <a> text
    if len(links) >= 1:
        links[0].string = new_body   # usually body text shown here

    # Remove 10th <a>
    if len(links) >= 10:
        links[9].decompose()

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))


# --------- UPDATE base.html ---------
with open('base.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

div = soup.find('div')

if div:
    # Update header
    header_tag = div.find('h1')
    if header_tag:
        header_tag.string = new_header

    # Update body
    body_tag = div.find('p')
    if body_tag:
        body_tag.string = new_body

    # Update link
    link_tag = div.find('a')
    if link_tag:
        link_tag['href'] = new_link
        link_tag.string = new_link

with open('base.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("Files updated successfully.")
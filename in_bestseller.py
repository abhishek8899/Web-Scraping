import csv
import requests
import re
from bs4 import *
response = ""
names = ["Name"]
adds = ["URL"]
writers = ["Author"]
cost = ["Price"]
total = ['Number of Ratings']
avgrtngs = ['Average Rating']

urls = ["https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=1", "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=2",
        "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_3?ie=UTF8&pg=3", "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_4?ie=UTF8&pg=4", "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_5?ie=UTF8&pg=5"]

for x in urls:
    response = requests.get(x)
    html = response.content
    soup = BeautifulSoup(html, "html5lib")
    table = soup.find(id="zg_centerListWrapper")
    list_books = table.find_all(class_="zg_itemImmersion")

    for x in list_books:

        bookName = x.select(".p13n-sc-truncate")
        if bookName == []:
            names.append("Not available")
        else:
            bookName = [re.sub(r'[\n\t]+', '', bookName[0].get_text())]
            names.append(bookName[0])

        url = (x.select(" .a-link-normal"))[0]['href']
        if url == []:
            adds.append("Not available")
        else:
            adds.append("www.amazon.in" + url)

        author = x.select(".a-size-small .a-link-child")
        if author == []:
            writers.append("Not available")
        else:
            writers.append(author[0].get_text())

        price = x.select(".p13n-sc-price")
        if price == []:
            cost.append("Not available")
        else:
            cost.append(price[0].get_text())

        rating = x.select(".a-icon-row .a-size-small ")
        if(rating == []):
            total.append("Not available")
        else:
            total.append(rating[0].get_text())

        averagerating = x.select(".a-icon-row .a-icon-star ")
        if averagerating == []:
            avgrtngs.append("Not available")
        else:
            avgrtngs.append(averagerating[0].get_text())


data = zip(names, adds, writers, cost, total, avgrtngs)
with open('in_book.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=';')
    a.writerows(data)

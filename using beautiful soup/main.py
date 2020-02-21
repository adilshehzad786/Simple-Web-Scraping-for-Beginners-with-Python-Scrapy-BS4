from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq


page='https://bluelimelearning.github.io/my-fav-quotes/'

client=uReq(page)

page_html=client.read()

client.close()

page_soup=soup(page_html,"html.parser")


quotes=page_soup.findAll("div" ,{"class":"quotes"})

for quote in quotes:
    fav_quote=quote.findAll("p" ,{"class":"aquote"})
    aquote=fav_quote[0].text.strip()

    fav_author=quote.findAll("p" ,{"class":"author"})
    author=fav_author[0].text.strip()

    print(aquote)
    print(author)

    file1 = open('output.txt', 'a')



    print(aquote, file=file1)
    print(author, file=file1)

    print("File Saved and program terminated Successsfully")

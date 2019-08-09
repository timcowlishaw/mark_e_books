# coding: utf-8
lines = []
seen = set()
for n in range(1, 9):
    text = requests.get("http://annotatedfall.doomby.com/pages/the-annotated-lyrics/?p=%s" % n).text
    soup = bs4.BeautifulSoup(text)
    for link in soup.find("ul", class_="nav-list").find_all("a"):
       if "/pages/the-annotated-lyrics/" in link["href"] and link["href"] not in seen:
           text2 = requests.get(link["href"]).text
           soup2 = bs4.BeautifulSoup(text2)
           content = soup2.find(class_="column-content")
           for a in content.find_all("a"):
               a.decompose()
           for p in content.find_all("p"):
               lines.append(p.text)
           seen.add(link["href"])
           print(link["href"])
           
           
               
           
       
        
with open("data/lines.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
        

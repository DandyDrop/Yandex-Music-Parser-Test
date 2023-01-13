# import selenium
import requests
from bs4 import BeautifulSoup
# import json

link = "https://music.yandex.com/album/12278501/track/71810195"
response = requests.get(link)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
print("\n\n\n\n\n\n\n\n\n\n\n\n")
a = soup.find_all("button")
for i, A in enumerate(a):
    if i == 3:
        A = str(A)
        # A = json.loads(str(A))
        A = A[A.index("title=\"")+7:]
        print(A[:A.index("\"")])
        # print(A[A.index("class=\"")+7:A.index("\" data-b")])

    # print(A)
    # print("num: "+str(i))
    # print("\n\n\n\n\n\n\n\n")
# data = json.loads(soup.text)
# print(data)

# if i == 7:
    #     A = str(A)
    #     print(A)
    #     print(A[A.index("\">")+2:A.index("</")])
    # if i == 8:
    #     A = str(A)
    #     print(A)
    #     print(A[A.index("\">") + 2:A.index("</")])

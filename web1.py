# web1.py
from bs4 import BeautifulSoup

#페이지 로딩(메서드 체인, 함수체인)
if True:
    page = open ("c:\\work\\test01.html","rt",encoding="utf-8").read()
else: #웹은 바로 연결 안해봄.... 있다가 해보자
    page = open ("https://www.naver.com/","rt",encoding="utf-8").read()

#검색을 위한 객채(웹에 있는 일반 문서)
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#문서 전체에서 <p>검색
#print(soup.find_all("p"))

#첫번째 <p>를 검색
#print(soup.find("p"))

#조건이 있는경우 :<p class ='outer'
#class_는 파이썬과 키워드 충돌 때문에 사용
#print(soup.find_all("p", class_="outer-text"))

#특정 속성을 지정할 때: attrs(attributes)
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#특정 id만 지정
#print(soup.find_all("p", id="first"))

#태크 내부에 컨텐츠를 출력 : .text, .get_text()
#요즘은 .text를 더 선호한다고함.
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)


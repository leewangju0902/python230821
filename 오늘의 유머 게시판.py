# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f= open("c:\\work\\today.txt", "wt", encoding="utf-8")

for n in range(1,11):
        #오늘의 유머
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)

        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()

        #한글이 깨지는 경우에사용
        page = data.decode('utf-8', 'ignore') # 'ignore' : default로 약간의 깨지느것을 허용한다는 뜻
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        #<td class="subject">
        #<a href="/board/view.php?table=bestofbest&amp;no=470312&amp;s_no=470312&amp;page=1" target="_top">오펜하이머 한국판 리메이크 결정 ㄷㄷㄷ</a>
        #<span class="list_memo_count_span"> [20]</span>  
        #<span style="margin-left:4px;">
        #<img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>

        print();       
        for item in list:
                try:
                        title = item.find("a").text.strip()
                        # print(title)
                        # link= item.find("a")["href"]
                        # print(link)
                        if (re.search('한국', title)):
                                print(title.strip())
                                f.write(f"{title}\n")


                except:
                        pass

        print(list.len());       

f.close()

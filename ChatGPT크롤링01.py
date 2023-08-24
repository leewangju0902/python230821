import requests
from bs4 import BeautifulSoup

def crawl_blog_data(search_keyword):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        blog_entries = soup.find_all('li', class_='sh_blog_top')

        for entry in blog_entries:
            blog_name = entry.find('a', class_='sh_blog_title').get_text()
            post_address = entry.find('a', class_='sh_blog_title')['href']
            post_date = entry.find('dd', class_='txt_inline').get_text()

            print("Blog Name:", blog_name)
            print("Post Address:", post_address)
            print("Post Date:", post_date)
            print("---------------------------")

    else:
        print("Failed to retrieve the page.")

# Replace 'your_search_keyword' with the actual search keyword you want to use
#search_keyword = input("Enter the search keyword: ")
search_keyword ="맥북에어"
crawl_blog_data(search_keyword)

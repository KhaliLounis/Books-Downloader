from bs4 import BeautifulSoup as bs
import requests
import re
import webbrowser


def extract_potential_authors(book_name):
    api_endpoint = f'https://www.googleapis.com/books/v1/volumes?q={book_name}&filter=partial'
    response = requests.get(api_endpoint)
    book_data = response.json()
    
    potential_authors = []
    items = book_data.get('items', [])
    for item in items:
        volume_info = item.get('volumeInfo', {})
        authors = volume_info.get('authors', [])
        if len(authors) == 1:
            potential_authors.extend(authors)
    potential_authors = [author.lower() for author in potential_authors]
    return potential_authors

def search_library_genesis(book_name, potential_authors):
    search_url = f'https://libgen.is/search.php?req={book_name}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def'
    response = requests.get(search_url)
    src = response.content
    soup = bs(src, 'lxml')
    books_list = soup.find_all('tr', {'valign': "top"})
    book_link = None

    for tr in books_list:
        td = tr.find('td', string=re.compile('pdf'))
        if td is not None:
            if td.text == 'pdf':
                parent_tag = td.parent
                if book_name.replace('+',' ') in parent_tag.contents[4].find('a').text.lower() and parent_tag.contents[2].find('a').text.lower() in potential_authors:
                    book_link = parent_tag.contents[4].find('a')['href']
                    break
    return book_link

def get_download_book(book_link):
    try:
        link = f'https://libgen.is/{book_link}'
        download_page = requests.get(link)
        source = download_page.content
        down_soup = bs(source, 'lxml')
        downloads_list = down_soup.find_all('td', {'width': "17%"})
        download_link=None
        
        for tr in downloads_list:
            a = tr.find('a', string=re.compile('Libgen.lc'))
            if a is not None:
                if a.text == 'Libgen.lc':
                    download_link = a['href']
                    break
        webbrowser.open(download_link)

    except TypeError:
        print('The book might not be available in PDF format on Library Genesis.')

book_name = input('Enter a book name: ').lower().replace(' ', '+')
potential_authors = extract_potential_authors(book_name)
book_link = search_library_genesis(book_name, potential_authors)
get_download_book(book_link)
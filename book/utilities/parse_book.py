from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests
from bs4 import BeautifulSoup

from ..models import BookAuthor, BookName, Book, Section
from .path_generator import book_image_path

__SITE_URL = 'https://biblio.zone'
__URL = __SITE_URL + '/isbn/validator/?isbn={isbn}'
__HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': '*/*'
}

__field_dict = {
    'name': 'Название:',
    'author': 'Автор:',
    'section': 'Раздел:',
    'isbn': 'ISBN:',
    'publisging_house': 'Издательство:',
    'year_of_publishing': 'Год издания:',
    'page_count': 'Количество страниц:',
    'img_name': 'img_name',
    'img_byte': 'img_byte'

}

def __get_html(url):
    resp = requests.get(url, headers=__HEADERS)
    if resp.status_code == 200:
        return resp.content
    else:
        return None

def __get_book_html(isbn):
    base_html = __get_html(__URL.format(isbn=isbn))
    if not base_html:
        return None
    
    soup = BeautifulSoup(base_html, 'html.parser')
    try:
        book_url = __SITE_URL + soup.select('.card')[0].find('a')['href']
    except IndexError:
        return None
    
    book_html = __get_html(book_url)
    if book_html:
        return book_html
    else:
        return None

def __get_book_data(book_html):
    '''Из полученых из интернета данных создает словарь.'''

    if not book_html:
        return None
    
    soup = BeautifulSoup(book_html, 'html.parser')
    book_detail_soup = soup.find('div', class_='book-detail').find_all('div')

    book_section = __get_book_sections(soup)
    book_img, book_img_format = __get_book_img(book_detail_soup[0])
    book_title = __get_book_title(book_detail_soup[1])
    book_info = __get_book_info(book_detail_soup[1])

    data = {
        'Название:': book_title,
        'Раздел:': book_section,
    }
    data.update(book_info)
    data['img_name'] = data['ISBN:'] + '.' + book_img_format
    data['img_byte'] = book_img
    
    return data

def __get_book_sections(soup):
    sections = soup.select('.breadcrumb-item')
    if len(sections) >= 3:
        section = sections[2].find('a').find('span').get_text()
    else:
        section = 'Другое'

    return section
    
def __get_book_title(soup):
    title = soup.find('h1').get_text()
    return title

def __get_book_info(soup):
    trs = soup.find('table').find_all('tr')
    book_info = {}
    for tr in trs:
        tds = tr.find_all('td')
        key = tds[0].get_text(strip=True)
        book_info[key] = tds[1].get_text(strip=True)
    
    return book_info

def __get_book_img(soup):
    img_url = soup.find('img')['data-src']
    img_format = img_url.split('/')[-1].split('.')[-1]
    book_img = __get_html(img_url)
    return book_img, img_format


def __get_book_from_net(isbn):
    book_html = __get_book_html(isbn)
    data = __get_book_data(book_html)

    if not data:
        return None

    book = {}

    for key, value in __field_dict.items():
        if value in data:
            book[key] = data[value]
        else:
            book[key] = None
    
    return book
    

def __create_book(book):
    '''Создает книгу из полученого словаря.'''

    book_name = BookName.objects.get_or_create(name=book['name'])[0]
    book_author = BookAuthor.objects.get_or_create(name=book['author'])[0]
    book_section = Section.objects.get_or_create(name=book['section'])[0]
    book_object = Book(
        name = book_name,
        author = book_author,
        section = book_section,
        year_of_publishing = book['year_of_publishing'],
        isbn = book['isbn'],
        publisging_house = book['publisging_house'],
        page_count = book['page_count'],
        slug = slugify(book['isbn'])
    )

    book_image_name = book_image_path(book_object, book['img_name'])
    book_img_content = ContentFile(book['img_byte'])
    book_object.img.save(book_image_name, book_img_content)
    book_object.save()
    
    return book_object

def get_book(isbn):
    '''Ищет книгу в бд или в интернете, если её нет возбуждает исключение Book.DoesNotExist.'''
    try:
        book = Book.objects.get(isbn=isbn)
    except Book.DoesNotExist:
        data = __get_book_from_net(isbn)
        if data:
            book = __create_book(data)
        else:
            raise Book.DoesNotExist
    return book
        


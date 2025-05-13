import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.flowerchimp.com/'

headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'
}

productlinks = []

for x in range (1,19):
    r = requests.get(f'https://www.flowerchimp.com/collections/all?page={x}sort_by=best-selling')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='product-wrap')

    for item in productlist:
        for link in item.find_all('a',href=True):
            productlinks.append(baseurl + link['href'])


testlink = 'https://www.flowerchimp.com/products/sweet-kisses'

r = requests.get(testlink, headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

# Get the name of the products
name = soup.find('h1',class_='new-product-title').text.strip()

# Get the rating out of 5
try:
    rating = float(soup.find('span', class_='jdgm-prev-badge__stars')['data-score'])
except:
    rating = 0

# Get the percentage of rating that is verified user
try:
    verified_rating = soup.find('div',class_='jdgm-medal__value').text.strip()
except:
    verified_rating = 0

# Get total no of buyer who provide rating
try:
    total_rating = float(soup.find('span',class_='jdgm-prev-badge__text').text.split()[0])
except:
    total_rating = 0

# Get the availability of the delivery location
try:
    location = soup.find('p', class_='area_availability_label_desktop').text.strip()
except:
    location = 'none'

# Get the default price, if there is no other variant of the products
default_price = soup.find('span',itemprop='price').text.split()[1]

# Get the image details
img_tag = soup.find('img', class_='lazyload')
if img_tag and 'src' in img_tag.attrs:
    img_url = 'https:' + img_tag['src'] if img_tag['src'].startswith('//') else img_tag['src']
else:
    img_url = None

# Get cleaned details of the bloom
p_tag = soup.find('p')

for br in p_tag.find_all('br'):
    br.replace with('\n')

details = p_tag.get_text().replace('\xa0','').strip()

# Append all information in a dataframe
data_summary = {
    'name': name,
    'rating': rating,
    'verified_rating': verified_rating,
    'total_rating': total_rating,
    'location': location,
    'default_price': default_price,
    'img_url': img_url
    'product_details': details
}

print(data_summary)
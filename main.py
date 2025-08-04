import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re

baseurl = 'https://www.flowerchimp.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'
}

productlinks = []

# Step 1: Collect product links
for x in range(1, 19):  # Adjust range based on actual number of pages
    print(f"Scraping page {x}...")
    r = requests.get(f'{baseurl}/collections/all?page={x}&sort_by=best-selling', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='product-wrap')

    for item in productlist:
        for link in item.find_all('a', href=True):
            full_link = baseurl + link['href']
            if full_link not in productlinks:
                productlinks.append(full_link)

    time.sleep(random.uniform(1.5, 2.5))  # Polite delay

# Step 2: Scrape individual product pages
all_products = []

for link in productlinks:
    try:
        print(f"Scraping product: {link}")
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        name = soup.find('h1', class_='new-product-title')
        name = name.text.strip() if name else 'N/A'

        try:
            rating = float(soup.find('span', class_='jdgm-prev-badge__stars')['data-score'])
        except (AttributeError, TypeError, ValueError):
            rating = 0

        try:
            verified_rating = soup.find('div', class_='jdgm-medal__value').text.strip()
        except:
            verified_rating = 'N/A'

        try:
            total_rating = float(soup.find('span', class_='jdgm-prev-badge__text').text.split()[0])
        except:
            total_rating = 0

        try:
            location = soup.find('p', class_='area_availability_label_desktop').text.strip()
        except:
            location = 'N/A'

        try:
            default_price = soup.find('span', itemprop='price').text.split()[1]
        except:
            default_price = 'N/A'

        img_tag = soup.find('img', class_='lazyload')
        if img_tag and 'srcset' in img_tag.attrs:
            img_url = 'https:' + img_tag['srcset'] if img_tag['srcset'].startswith('//') else img_tag['srcset']
        else:
            img_url = 'N/A'

        p_tag = soup.find('p')
        if p_tag:
            for br in p_tag.find_all('br'):
                br.replace_with('\n')
            details = p_tag.get_text().replace('\xa0', '').strip()
        else:
            details = 'N/A'

        data_summary = {
            'name': name,
            'rating': rating,
            'verified_rating': verified_rating,
            'total_rating': total_rating,
            'location': location,
            'default_price': default_price,
            'img_url': img_url,
            'product_details': details,
            'product_url': link,
        }


        all_products.append(data_summary)
        time.sleep(random.uniform(1.5, 3.0))

    except Exception as e:
        print(f"Error scraping {link}: {e}")

# Step 3: Save to CSV
df = pd.DataFrame(all_products)
df.to_csv("flowerchimp_products.csv", index=False)
print("Data saved to flowerchimp_products.csv")

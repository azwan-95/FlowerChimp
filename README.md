# 🌼 Flower Chimp Product Scraper

This project is a Python-based web scraper designed to extract product data from [Flower Chimp Malaysia](https://www.flowerchimp.com/). It gathers details of all products listed on the website and saves the information into a structured CSV file for analysis.

---

## 📦 What This Scraper Does

1. **Collects product URLs** from 18 paginated product listing pages.
2. **Scrapes each product page** for key details like name, price, ratings, and availability.
3. **Saves all data into a CSV file** called `flowerchimp_products.csv`.

---

## 📋 Extracted Information

For each product, the scraper extracts:

- 🌸 **Product Name**
- ⭐ **Star Rating (out of 5)**
- ✅ **Verified Buyer Rating %**
- 🧮 **Total Number of Reviews**
- 📍 **Delivery Availability (Location info)**
- 💰 **Default Price**
- 🖼️ **Image URL**
- 📑 **Product Description**
- 🔗 **Product Page URL**

---

## 🛠️ Technologies Used

- `requests` – for making HTTP requests
- `BeautifulSoup` – for parsing HTML
- `pandas` – for organizing and exporting data
- `lxml` – fast HTML parser backend
- `time` and `random` – for polite scraping intervals

---

## 🧠 How It Works

### 🔗 Step 1: Get All Product Links
The script loops through all product listing pages and extracts every unique product URL.

### 📄 Step 2: Scrape Product Details
For each URL, the script pulls the HTML and parses the following details: product name, price, star rating, location availability, image URL, and a clean product description.

### 💾 Step 3: Save to CSV
All product information is stored in a list of dictionaries and exported into a single CSV file.

---

## 📂 How to Run

### 1. Clone the Repository

git clone https://github.com/your-username/flower-chimp-scraper.git
cd flower-chimp-scraper

### 2. Install the Dependencies
pip install -r requirements.txt

### 3. Run the Scraper

| name         | rating | verified\_rating | total\_rating | location                  | default\_price | img\_url                                       | product\_details      | product\_url                                          |
| ------------ | ------ | ---------------- | ------------- | ------------------------- | -------------- | ---------------------------------------------- | --------------------- | ----------------------------------------------------- |
| Sweet Kisses | 4.8    | 90% Verified     | 145           | Available in Klang Valley | RM99           | [https://...flower.jpg](https://...flower.jpg) | A bouquet of roses... | [https://www.flowerchimp](https://www.flowerchimp)... |



⚠️ Disclaimer ⚠️
This scraper is for educational purposes only.
Always review and respect the site's robots.txt and terms of service.
Website structure may change over time. If the scraper breaks, recheck the HTML layout.

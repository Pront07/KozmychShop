import requests

class NewsInfo:
    API_LINK = 'https://newsapi.org/v2/everything'
    CLOTHING_BRANDS = [
        "Nike",
        "Adidas",
        "Gucci",
        "Louis Vuitton",
        "Chanel",
        "Ralph Lauren",
        "Calvin Klein",
        "Burberry",
        "Dior",
        "Armani"
    ]

    @classmethod
    def get_clothing_brand_news(cls):
        all_brand_news = {}
        for brand_name in cls.CLOTHING_BRANDS:
            response = requests.get(
                cls.API_LINK,
                params={'apiKey': "", 'q': brand_name}
            )
            data = response.json()
            if 'articles' in data and data['articles']:
                articles = data['articles']
                brand_news = []
                for article in articles:
                    brand_news.append({
                        'title': article['title'],
                        'description': article['description'],
                        'url': article['url'],
                        'published_at': article['publishedAt'],
                        'image_url': article['urlToImage']
                    })
                all_brand_news[brand_name] = brand_news
        return all_brand_news


all_clothing_news = NewsInfo.get_clothing_brand_news()

for brand, news in all_clothing_news.items():
    print(f"News for {brand}:")
    for item in news:
        print("Title:", item['title'])
        print("Description:", item['description'])
        print("URL:", item['url'])
        print("Image URL:", item['image_url'])
        print("Published At:", item['published_at'])
        print("---------------------------------------")

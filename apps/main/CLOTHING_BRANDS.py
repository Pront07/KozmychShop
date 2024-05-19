from flask import Flask, render_template
from interfaces import NewsInfo

app = Flask(__name__)

@app.route('/news')
def news():
    all_clothing_news = NewsInfo.get_clothing_brand_news()
    return render_template('news.html', all_clothing_news=all_clothing_news)

if __name__ == '__main__':
    app.run(debug=True)
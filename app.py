from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste des articles (en mémoire)
articles = []

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = articles[article_id]
    return render_template('article.html', article=article)

@app.route('/create', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        articles.append({'title': title, 'content': content, 'category': category})
        return redirect(url_for('index'))
    return render_template('create_article.html')

if __name__ == '__main__':
    app.run(debug=True)

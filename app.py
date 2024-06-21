from flask import Flask, render_template

app = Flask(__name__, template_folder= 'Templates')

@app.route('/')
def home():
      return render_template('home.html')

@app.route('/blog')

def blog():
      return render_template('blog.html')

@app.route('/community')

def community():
      return render_template('community.html')

@app.route('/contact')

def contact():
      return render_template('contact.html')

@app.route('/faqs')

def faqs():
      return render_template('faqs.html')

@app.route('/feedback')

def feedback():
      return render_template('feedback.html')

@app.route('/join')

def join():
      return render_template('join.html')

@app.route('/products')

def products():
      return render_template('products.html')

@app.route('/reviews')

def reviews():
      return render_template('reviews.html')

@app.route('/sustainability')

def sustainability():
      return render_template('sustainability.html')

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=8080, debug=True)
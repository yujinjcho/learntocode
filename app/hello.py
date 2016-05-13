from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('currentprojects.html')

@app.route('/about/')
def about():
  return render_template('about.html')

@app.route('/contact/')
def contact():
  return render_template('contact.html')

@app.route('/resources/')
def resources():
  return render_template('resources.html')

if __name__ == '__main__':
  app.run(debug=True)

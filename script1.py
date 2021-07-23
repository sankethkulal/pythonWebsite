from flask import Flask, render_template #flask-class Flask-functions #render_template=produces design and text as it is

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

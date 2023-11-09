from flask import Flask, render_template, request


app = Flask(__name__)

# Make a homepage
@app.route('/')
def homepage():
    with open('static/about_Me.txt', 'r') as file:
        about_me_text = file.readlines()
    return render_template('homepage.html', about_me= about_me_text)

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Yoyo", "Yennifer"]
    return render_template('name.html', Sname=name, nameList=listOfNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)







# Add the option to run this file directly 
if __name__ == "__main__":
    app.run(debug=False, port=5001)
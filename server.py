import os
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    data = request.form.to_dict()
    with open('data.txt', 'a') as f:
        f.write(f'{data["name"]},{data["email"]},{data["message"]}\n')
    return redirect('/')

@app.route("/thanks")
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
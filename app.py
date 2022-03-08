from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home():
   return render_template('main.html')
@app.route('/gu_names')
def gu_names():
   return render_template('index.html')



@app.route('/gu_names/<gu_name>')
def gu_name(gu_name):
   return render_template('{}.html'.format(gu_name))


if __name__ == '__main__':  
    app.run('0.0.0.0',port=8000,debug=True)
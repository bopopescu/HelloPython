from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username=request.form.get('username')
    password=request.form.get('password')
    if username=='dkx' and password=='123':
        return render_template('welcome.html',username=username)
    return render_template('form.html',message='ERROR',username=username)

if __name__ == '__main__':
    app.run()

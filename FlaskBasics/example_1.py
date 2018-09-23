from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello! Go to /puppy_latin/name to convert your puppy name into puppy latin'

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name.endswith('y'):
        new_name = name[:-1] + 'iful'
    else:
        new_name = name + 'y'
    return 'Hi {name}! Your puppylatin name is {new_name}'.format(name=name, new_name=new_name)

if __name__ == '__main__':
    app.run()

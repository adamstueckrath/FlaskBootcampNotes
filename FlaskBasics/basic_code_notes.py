# from flask module import Flask class
# import the render_template to use the HTML templates engine
from flask import Flask, render_template

# creating an application object of the instance of the class Flask()
# __name__ is the name of the module in which the application object is created
app = Flask(__name__)

# the decorator directly links the page (in this case the index function) to the
# route on your web application. so it would be be www.hellopuppy.com/index
@app.route('/') # 127.0.0.1:5000
# this function defines a page - index() and returns a string
# basically when we call the index page, you return the string and the browser reads it in as HTML code
def index():
  return '<h1>Hello Puppy!</h1>'

# static routing to other pages in web application
@app.route('/information') # 127.0.0.1:5000/information
def info():
  return '<h1>Puppies are cute!</h1>'

# dynamic routing depending on the function parameter
# could be used for user unique ids
@app.route('/puppy/<name>')
def puppy(name):
    return '<h1>This is a page for {}</h1>'.format(name)

if __name__ == '__main__':
  app.run()

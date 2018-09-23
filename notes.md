About Flask Web Development:
_______________________________________________________________________
Front-end of the website:
HTML - will display the page elements
CSS - will style the elements
Bootstrap - will provide automatic styling and components through CSS and JS

Every major website will perform some main operations:
* Accept information from user
* Retrieve information from a database
* Create/Update/Delete information in database
* Display information back to user

We need a web framework to accept and return information with the front-end.
Flask is the web framework that allows us to connect Python code to the web.

We'll use Flask and Python to connect to HTML templates (jinja) and retrieve, edit, or return information back to the user.

Accepting User Information through forms:
	Libraries:
	* WTForms - create user input forms
Communicate with the Database and retrieve information:
	Libraries:
	* SQLAlchemy - write queries in python
	* Flask-Migrate - update changes to database automatically

CRUD:
* Create/Read/Update/Delete information from the database if necessary

Jinja - templates to grab information from Python and Flask to send information back as HTML



FLASK BASICS

Flask Basic:
_______________________________________________________________________
# from flask module import Flask class
from flask import Flask

# creating an application object of the instance of the class Flask()
# __name__ is the name of the module in which the application object is created
app = Flask(__name__)

# the decorator directly links the page (in this case the index function) to the
# route on your web application. so it would be be www.hellopuppy.com/index
@app.route('/')
# this function defines a page - index() and returns a string
# basically when we call the index page, you return the string and the browser reads it in as HTML code
def index():
  return '<h1>Hello Puppy!</h1>'

if __name__ == '__main__':
  app.run()


Flask Basic Routes:
_______________________________________________________________________
Create a web application with multiple routes (multiple pages)
- the key to this is in the @app.route() decorator.
- The string parameter passed into the decorator determines the URL extension that will link to the function (a.k.a view)

To start, the homepage or domain is locally represented as http://127.0.0.1:5000/
- use decorators to add on to the domain:
	* @app.route('/some_page')
	* http://127.0.0.1:5000/some_page
- Once a page is deployed, 127.0.0.1 will be replaced by the domain name


Flask Dynamic Routing:
_______________________________________________________________________
- Often you'll want URL route extensions to be dynamic based on the situation
- For example you might want the page per user, so that the extension is in the form:
	www.mysite.com/user/unique_user_name
Dynamic routes have 2 key aspects:
	* A variable in the route <variable>
	* A parameter passed into the function that the decorator is decorating

@app.route('/some_page/<name>')
def other_page(name):
	# this will use templates
	return 'User: {}'.format(name)


Debug Mode:
_______________________________________________________________________
- set debug equal to True to investigate and dive into errors
if __name__ == '__main__':
  app.run(debug=True)

- look for the debugger PIN in the terminal to access the console in the debug log
- its usual for debugging the traceback



FLASK TEMPLATES

Template Basics
_______________________________________________________________________
- Need to connect a view function to render HTML templates (HTML files you've created for a page)
- Flask will automatically look for HTML Templates in the templates directory
- You can render templates simply by importing the render_template function from flask and returning a .html file from the view function


Template Variables
_______________________________________________________________________
- Using the render_template function, you can directly render an HTML file with your Flask web app
- Use the Jinja template engine to use Python code in the app to change and update variables and logic, and then send that information to the template
- Jinja templating lets you directly insert variables from Python into the HTML file
- The syntax for inserting a variable is:
	* {{some_variable}}
- You can pass in python strings, lists, dictionaries, and more into the templates
- Set parameters in the render_template function and then use the {{}} syntax to inset them into the template


Template Control Flow
_______________________________________________________________________
- With Jinja templating you can pass variables using the {{ variable }} syntax
- You can have access to control flow syntax in the templates such as for loops and if statements
	* Use this {% %} syntax
	* example:
	<ul>
		{% for item in mylist %} # iterate through list
		<li> {{item}} </li> # list out item in list item HTML
		{% endfor %} # end iteration
	</ul>


Template Inheritance
_______________________________________________________________________
- Usually pages across a web application share a lot of features (e.g. navigation bar, footer, etc.)
- Set up a base.html template file with the re-useable aspect of the site
	* Use {% extend "base.html" %} and {% block %} statements to extend the re-usable aspects to other pages.
	* Use it for links to bootstrap, JS functions etc.


url_for help Function
_______________________________________________________________________
- Flask comes with a convenient url_for() helper function to allow you to easily connect other template pages or files with the template



FLASK FORMS

Flask Form Basics
_______________________________________________________________________
- You can use flask_wtf and the wtforms package to quickly create forms from python scripts
- You need to configure a secret key for security
	* Create a WTForms class
	* Create Fields for each part of the forms
- Set up a View Function
	* Add methods = ['GET', 'POST']
	* Create an instance of Form class
	* Handle form submission


	Form Fields
	_______________________________________________________________________
	- Every possible HTML form field has a corresponding wtforms class you can import
	- wtforms also has validators you can easily insert
	- Validators can perform checks on the form data, such as requiring a field to be filled
	- Use Flask's session object to grab the information provided in the form and pass it to another template

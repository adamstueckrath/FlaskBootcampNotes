from flask import Flask, render_template, request

app = Flask(__name__)

# function will look into templates directory
# and then search for the name of the template (basic.html)
# you have to label the directory 'templates' for render_template to work
@app.route('/basic')
def basic():
    # pass in a variable into the Jinja template
    name = "Adam"
    letters = list(name)
    puppies = ['Winston','Rufus','Spike','Fluffy','Louie']
    user_logged_in = True
    return render_template('basic.html', name=name, letters=letters,
                                                    puppies=puppies,
                                                    user_logged_in=user_logged_in)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html', first=first, last=last)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

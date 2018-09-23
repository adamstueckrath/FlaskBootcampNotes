from flask import Flask, render_template
from flask_wtf import FlaskForm # Flaskform is a class that you'll inherit from to create your own forms
from wtforms import StringField, SubmitField

# create applcation
app = Flask(__name__)

# set app config secret key to have the forms security work
app.config['SECRET_KEY'] = 'mysecretkey'

# inherit the FlaskForm class to create more custome class
class InfoForm(FlaskForm):
    # set class attributes
    breed = StringField('What Breed are you?') # label string
    submit = SubmitField('Submit')


# add methods to get and post the forms
@app.route('/', methods=['GET','POST'])
def index():
    # set breed variable
    breed = False

    # create InfoForm instance
    form = InfoForm()

    # if the form validates on submit, set the breed variable to the breed field in form
    # refresh form
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''

    return render_template('index.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)

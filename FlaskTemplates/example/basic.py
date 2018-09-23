from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    login_dict = {'Must have upper case letter somewhere.':False,
                  'Must have lower case letter somewhere.':False,
                  'Must have a number somewhere':False}

    if any(letter.isupper() for letter in username):
        login_dict['Must have upper case letter somewhere.'] = True
    if any(letter.islower() for letter in username):
        login_dict['Must have lower case letter somewhere.'] = True
    if any(letter[-1].isdigit() for letter in username):
        login_dict['Must have a number somewhere'] = True
    app.logger.info(login_dict)

    if all(login_dict.values()):
        username_test = ['Your username passed the 3 requirements!']
    else:
        username_test = [ k for k,v in login_dict.items() if v == False]

    app.logger.info(username_test)
    app.logger.info(username)
    return render_template('report.html',username = username, username_test = username_test)

if __name__ == '__main__':
    app.run(debug=True)

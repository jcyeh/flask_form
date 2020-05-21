from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d1f27d23441f27567d441f2b6176a'

class BelbinTeamRolesForm(Form):
    name = TextField('Name:', validators=[validators.input_required()])
    email = TextField('Email:', validators=[validators.input_required(), validators.Email(), validators.Length(min=6, max=35)])
    
    #def reset(self):
    #    blankData = MultiDict([('csrf', self.reset_csrf())])
    #    self.process(blankData)
    
@app.route("/", methods=['GET', 'POST'])
def index():
    form = BelbinTeamRolesForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        print(name, " ", password, " ", email)

    if form.validate():
        # Save the comment here.
        flash('Thanks for registration, ' + name)
    else:
        flash('Error: All the form fields are required.')

    return render_template('myform.html', form=form)

if __name__ == "__main__":
    app.run()
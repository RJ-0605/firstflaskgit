
from flask import Flask, render_template,url_for
from forms import RegistrationForm,LoginForm
from flask_caching import Cache



app = Flask(__name__)


cache = Cache(app,config={'CACHE_TYPE': 'simple', "DEBUG": True,})

app.config['SECRET_KEY'] = 'ef16c97fb201aa146858213e793aa323'

posts = [
	{'author':'Corey Schafer',
	 'title':'Blog post 1',
	 'content':'First post content',
	 'date_posted':'April 20,2018'

	 },
	 {
	 'author':'Jane Doe',
	 'title':'Blog post 2',
	 'content':'Second post content',
	 'date_posted':'April 21,2018'

	 },
	 {
	 'author':'Aanet Doly',
	 'title':'Blog post 3',
	 'content':'Third post content',
	 'date_posted':'April 27,2018'

	 }
 
]



@app.route('/')
@cache.cached(timeout=6)
def hello():

#	return ("<h1>Hello World</h1>
	return render_template("index.html",post_variable=posts) 


@app.route('/about')
@cache.cached(timeout=6)
def about():

#	return ("<h1>Hello World</h1>
	return render_template("about.html",title=about) 

@app.route('/register')
@cache.cached(timeout=6)
def register():
	form=RegistrationForm()
	return render_template('register.html',title='Register', form=form)


@app.route('/login')
@cache.cached(timeout=6)
def login():
	form=LoginForm()
	return render_template('login.html',title='Login', form=form)




if __name__=='__main__':
	app.run(host="0.0.0.0",debug=True)

	
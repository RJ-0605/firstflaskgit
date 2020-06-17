


from flask import Flask, render_template, redirect, url_for, request

from flask_caching import Cache

app = Flask(__name__)


cache = Cache(app,config={'CACHE_TYPE': 'simple', "DEBUG": True,})


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
@app.route('/home')
def home():

#	return ("<h1>Hello World</h1>
	return render_template("index.html",post_variable=posts) 


@app.route('/success/<name>')
def success(name):
	if name == 'chicken':
		return 'welcome %s' % name
   

   

@app.route('/loginload',methods = ['POSTS','GET'])
def loginload():
   if request.method == 'POST':
		user = request.form['nm']
		if user == 'chicken':
	      
			return redirect(url_for('success',name = user)) 

   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))



@app.route('/login')
def login():
	return render_template('result.html')





if __name__ == '__main__':
   app.run(host="0.0.0.0",debug = True)
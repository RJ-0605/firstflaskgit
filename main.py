
from flask import Flask, render_template,url_for

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

	 }



]



@app.route('/')
@cache.cached(timeout=6)
def hello():

#	return ("<h1>Hello World</h1>
	return render_template("index.html") 



if __name__=='__main__':
	app.run(host="0.0.0.0",debug=True)

	
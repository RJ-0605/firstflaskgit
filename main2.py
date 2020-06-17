from flask import Flask, render_template, redirect, url_for, request

from flask_caching import Cache

app = Flask(__name__)


cache = Cache(app,config={'CACHE_TYPE': 'simple', "DEBUG": True,})


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

   
@app.route('/loginload',methods = ['POST', 'GET'])
def loginload():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))



@app.route('/login')
def login():
	return render_template('result.html')





if __name__ == '__main__':
   app.run(host="0.0.0.0",debug = True)
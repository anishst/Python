from flask import Flask, request, redirect, url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import datetime, time
from flask_modus import Modus

app = Flask(__name__)

# Config file
app.config.from_object('config.DevelopmentConfig')


modus = Modus(app)
db = SQLAlchemy(app)

#  if first time u need to create db using db.create_all()

class KB(db.Model):
	__tablename__ = 'KB'

	# DDL 
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text)
	category = db.Column(db.Text)
	created_ts = db.Column(db.DateTime)
	last_updated_ts = db.Column(db.DateTime)

	def __init__(self, description, category):
		self.description = description
		self.category = category
		self.created_ts = datetime.datetime.now()

# import webbrowser
# webbrowser.open("http://localhost")

@app.route('/')
def root():

	return redirect(url_for('index'))

@app.route('/posts', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		new_post = KB(request.form['description'], request.form['category'])
		db.session.add(new_post)
		db.session.commit()
		return redirect(url_for('index'))
	# items = KB.query.paginate(per_page=20, page=1)
	return render_template('index.html', items=KB.query.order_by(KB.created_ts.desc()).all())
	# return render_template('index.html', items=items)

@app.route('/search', methods=['GET', 'POST'])
def search():
	# ideas:
	# https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
	query = KB.query.filter(KB.description.like("%"+request.form['query']+"%")).order_by(KB.created_ts.desc()).all()
	return render_template('search.html', items=query)

@app.route('/posts/new')
def new():
	return render_template('new.html')

@app.route('/posts/<int:id>', methods=['GET','PATCH', 'DELETE'] )
def show(id):
	found_item = KB.query.get(id)
	if request.method == b'PATCH':
		found_item.description = request.form['description']
		found_item.category = request.form['category']
		found_item.last_updated_ts =  datetime.datetime.now()
		db.session.add(found_item)
		db.session.commit()
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		db.session.delete(found_item)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('show.html', items=found_item)


@app.route('/posts/<int:id>/edit')
def edit(id):
	found_item = KB.query.get(id)
	return render_template('edit.html', items=found_item)

@app.route('/glossary', methods=['GET', 'POST'])
def glossary():
	return render_template('otcnet_glossary.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(port=80)
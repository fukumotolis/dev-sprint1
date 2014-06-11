import flask, flask.views
app = flask.Flask(__name__) # i don't understand name

class View(flask.views.MethodView):	# what's a class?
	def get(self):
		return flask.render_template('index.html')

app.add_url_rule('/', view_func=View.as_view('main'))	# i have no idea what's happening
app.debug = True
app.run()	# is this invoking the class?
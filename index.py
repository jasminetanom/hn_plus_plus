import flask

app = flask.Flask(__name__)

@app.route("/stories")
@app.route("/")
def stories():
	return "List all stories"

@app.route("/stories/<id>")
def story(id):
	return "Title, score, author, HN link, tags, content recs, user recs for story with id = {}".format(id)

@app.route("/tags")
def tags():
	return "List all tags"

@app.route("/tags/<id>")
def tag(id):
	return "List all stories with tag id = {}".format(id)

if __name__ == '__main__':
	app.run()
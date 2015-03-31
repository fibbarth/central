from application import app, request, render_template, g

@app.route('/')
def index(methods = ['GET', 'POST']):
    return 'index'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

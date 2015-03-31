from application import app, request, render_template, g
import application.user as teste

@app.route('/')
def index(methods = ['GET', 'POST']):
    user=teste.User('10', 'dsa')
    return user.oi()
    #return user.ste()
    #return app.config['DATABASE']

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

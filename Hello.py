# from flask import Flask, redirect, url_for
# app=Flask(__name__)

# @app.route('/admin')
# def admin():
#     return 'Hello Admin'

# @app.route('/guest/<gt>')
# def guest(gt):
#     return 'hello %s as guest' %gt

# @app.route('/user/<name>')
# def user(name):
#     if name=='admin':
#         return redirect(url_for('admin'))
#     else:
#         return redirect(url_for('guest',gt=name))

# if __name__=='__main__':

#     app.run(debug=True)
    












from flask import Flask, render_template
app=Flask(__name__)

@app.route('/hello/<int:score>')
def hello(score):
    return render_template('index.html',marks=score)

if __name__=='__main__':
    app.run(debug=True)
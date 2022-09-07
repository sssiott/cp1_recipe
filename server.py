from flask import Flask, render_template, request, redirect, url_for,jsonify, session
from routes import search_route, login

app = Flask(__name__)
app.register_blueprint(search_route.bp)
app.register_blueprint(login.bp)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template("home.html")
    

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/signin_done', methods =["get"])
def signin_done():
    email = request.args.get("email")
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")
    # print(email, uid, pwd, name)  # 올바르게 되고 있는지 확인하기 위해서
    if DB.singin(email, uid, pwd, name):
        return redirect(url_for("index")) # index는 함수 이름인데..? 되네..? # url_for는 함수 이름을 적어줘야되나봄
    else:
        return redirect(url_for("signin"))

@app.route('/image_test')
def image_test():
    return render_template("image_test.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/regis_recipe')
def regis_recipe():
    return render_template("regis_recipe.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
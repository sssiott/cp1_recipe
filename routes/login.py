from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask import Blueprint
import pymysql

bp = Blueprint('login', __name__, url_prefix='/')

# 로그인 페이지 만들기
@bp.route('login', methods = ['GET','POST'])
def login():
    return render_template('login.html')


# 로그인 성공후 페이지 만들기 
@bp.route('login_done', methods=['POST'])
def login_done():
    if request.method == 'POST':

   	  # 변수 지정 
        Name = request.form['Name'] 
        Age = request.form['Age']
        return render_template('login_done.html', Name=Name, Age = Age)
    else:
        return redirect(url_for('login'))


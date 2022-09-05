# search_route.py
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask import Blueprint
import pymysql

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/',methods = ['GET','POST'])
def search():
    # home 에서 입력받은 값을 받아온다.
    ingredients = request.form['ingredients']
    try:
        ingredients = ingredients.split(",")
    except:
        pass
    price = request.form['price']
    category = request.form['category']
    dislike = request.form['dislike']
    try:
        dislike = dislike.split(",")
    except:
        pass
    

    # sql 쿼리문을 작성하여 fetch
    # conn = pymysql.connect(host='localhost', user='root', password='Lja15410!',db='football', charset='utf8')
    # cur = conn.cursor()

    # cur.execute(f"""
    # INSERT INTO search_data VALUES ()
    # """)

    return render_template('search_ing.html', 
        ingredients= " ".join(ingredients),
        price=price,
        category=category,
        dislike= " ".join(dislike),
        enumerate=enumerate)



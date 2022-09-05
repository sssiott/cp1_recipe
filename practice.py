import pymysql
import pandas as pd
from sqlalchemy import create_engine

name = ['양파', '닭', '파', '생강', '고추', '가지', '오징어']
bulk_size = [10, 1, 5, 20, 10, 1, 1]
unit = ['개', '마리', '개', '개', '개', '개', '마리']
price = [10000, 6000, 1500, 5000, 10000, 2000, 5000]

# tavle - ingred
ingred_ = pd.DataFrame({'name' : name,
'bulk_size' : bulk_size,
'unit' : unit,
'price' : price})


pd.to_numeric(ingred_['bulk_size'], errors='coerce')
pd.to_numeric(ingred_['price'], errors='coerce')

ingred_['unit_price'] = ingred_['price'] / ingred_['bulk_size'] 

## table - recipe
menu = ['불닭', '불닭', '불닭', '오징어볶음', '오징어볶음', '오징어볶음', '오징어볶음']
ingred = ['양파', '닭', '파', '오징어', '파', '양파', '고추']
num = [2,1,2,2,2,3,2]

recipe_ = pd.DataFrame({'menu' : menu,
'ingred' : ingred,
'num' : num})
 
pd.to_numeric(recipe_['num'], errors='coerce')

## table - menu
menu = ['불닭', '오징어볶음']
category = ['한식', '한식']
views = [40, 120]

menu_ = pd.DataFrame({'menu' : menu,
'category' : category,
'views' : views})

pd.to_numeric(menu_['views'], errors='coerce')

####### 데이터 프레임 생성 완료 ###########
####### sql에 적재 ####################

conn = pymysql.connect(host='localhost', user='root', password='Lja15410!',db='study_db', charset='utf8')

cur = conn.cursor()

# cur.execute("""create table if not exists ingred(
#     name VARCHAR(30),
#     bulk_size INTEGER,
#     unit VARCHAR(30),
#     price INTEGER);""")

# cur.execute("""create table if not exists recipe(
#     menu VARCHAR(30),
#     ingred VARCHAR(30),
#     num INTEGER);""")

# cur.execute("""create table if not exists menu(
#     menu VARCHAR(30),
#     category VARCHAR(30),
#     views INTEGER);""")



engine = create_engine('mysql+mysqlconnector://root:Lja15410!@localhost/study_db', encoding = 'utf-8')

# df = pd.read_csv('./results.csv')

# df.to_sql('notion_pr', con = engine, if_exists='replace', index=False)
ingred_.to_sql('ingred', con = engine, if_exists='replace', index=False)
recipe_.to_sql('recipe', con = engine, if_exists='replace', index=False)
menu_.to_sql('menu', con = engine, if_exists='replace', index=False)
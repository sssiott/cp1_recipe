from flask import render_template, request
from flask import Blueprint
from modules.preprocessing import preprocessing, load_db
bp = Blueprint('regist_recipe', __name__, url_prefix='/regist_recipe')


@bp.route('/', methods=['GET','POST'] )
def regis_recipe():
    return render_template("regist_recipe.html")

@bp.route('/commit', methods=['GET','POST'])
def commit_recipe():
    name = request.form['menu_name']
    ingred_list = {}
    for i in range(1,11):
        if request.form[f'ingred{i}']:
            ingred_list[request.form[f'ingred{i}']] = request.form[f'ingred{i}_unit']+request.form[f'ingred{i}_unittype']
        else:
            pass
        
    preprocessing(ingred_list)

    return render_template("commit_recipe.html", name=name, ingred_list=ingred_list)
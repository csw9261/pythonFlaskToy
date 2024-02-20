from flask import Blueprint, request, render_template

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods=['GET'])
def index():
    return render_template('/main/index.html')


    

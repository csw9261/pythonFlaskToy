from flask import Flask, Blueprint, app, render_template, request, redirect, url_for

import logging

# 블루 프린트 생성
main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')

class mainControllerClass:

    @main_blueprint.route('/main', methods=['GET'])
    def main():
        username = request.cookies.get('username')
        return render_template('/main/index.html', username = username)
    
    # 경로가 없는 경우에 main으로 redirect 처리 
    @main_blueprint.route('/', methods=['GET', 'POST'])
    def rootRedirection():
        return redirect(url_for('main_blueprint.main'))


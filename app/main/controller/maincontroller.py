from flask import Flask, Blueprint, app, render_template, request

import logging

# 블루 프린트 생성
main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')

class mainControllerClass:

    @main_blueprint.route('/main', methods=['GET'])
    def main():
        raise Exception('Intentional 500 error')
        username = request.cookies.get('username')
        return render_template('/main/index.html', username = username)
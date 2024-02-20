from flask import Flask, Blueprint, render_template

import logging

# 블루 프린트 생성
main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')

class mainControllerClass:

    @main_blueprint.route('/main', methods=['GET'])
    def main():
        return render_template('/main/index.html')
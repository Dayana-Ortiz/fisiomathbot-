from flask import Blueprint, render_template

simulador_bp = Blueprint('simulador', __name__)

@simulador_bp.route('/simulador')
def simulador():
    return render_template('simulador.html')

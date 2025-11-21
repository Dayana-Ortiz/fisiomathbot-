from flask import Blueprint, render_template

matematicas_bp = Blueprint('matematicas', __name__)

@matematicas_bp.route('/matematicas')
def matematicas():
    return render_template('matematicas.html')

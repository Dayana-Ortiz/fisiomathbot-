from flask import Blueprint, render_template

tecnologia_bp = Blueprint('tecnologia', __name__)

@tecnologia_bp.route('/tecnologia')
def tecnologia():
    return render_template('tecnologia.html')

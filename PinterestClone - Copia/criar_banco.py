from pinterestclone import database, app
from pinterestclone.models import Usuario, Foto


with app.app_context():
    database.create_all()

from app import create_app
from app.extensions import db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

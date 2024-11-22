from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    db.create_all()  # Make sure the tables are created

    test_user = User(username='testuser')
    test_user.set_password('testpassword')
    db.session.add(test_user)
    db.session.commit()

print('Test user created successfully!')

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from cryptography.fernet import Fernet
import bcrypt  # Import bcrypt for password hashing
import os

app = Flask(__name__)
app.secret_key = '51855d52e41656e7b6af1d1056cbe967ae63a26358f47af0'  # Change this to a stronger secret key in production

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Pre-created hashed password for admin user
PRE_CREATED_HASH = "$2b$12$C0do3nPggj0GhzstDP1fgOf3U7nU/5X3T5NXPpG6JXTiUfieKkfQO"  # Update this with your generated hash

KEY = Fernet.generate_key()  # Generate encryption key, in production, keep this in a secure place.
cipher_suite = Fernet(KEY)

# App configuration
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max file size of 16MB
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


def allowed_file(filename):
    """Check if the uploaded file is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_icon(filename):
    """Return the appropriate icon for a file based on its extension."""
    file_ext = filename.rsplit('.', 1)[1].lower()
    icon_map = {
        'pdf': 'pdf-icon.png',
        'txt': 'txt-icon.png',
        'png': 'image-icon.png',
        'jpg': 'image-icon.png',
        'jpeg': 'image-icon.png',
        'gif': 'image-icon.png',
    }
    return icon_map.get(file_ext, 'default-icon.png')


# Simple user class for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id


# User loader
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', title="Secure Cloud Storage")
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode()  # Encode password for bcrypt

        if username == 'admin' and bcrypt.checkpw(password, PRE_CREATED_HASH.encode()):
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials", "danger")

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'GET':
        return redirect(url_for('index'))

    if 'file' not in request.files:
        flash("No file part in the request!", "danger")
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        flash("No file selected for uploading!", "warning")
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # Encrypt the file before saving it
        encrypted_file = cipher_suite.encrypt(file.read())
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as f:
            f.write(encrypted_file)

        flash(f"File '{filename}' uploaded and encrypted successfully!", "success")
        return redirect(url_for('files'))
    else:
        flash("Invalid file type! Only txt, pdf, png, jpg, jpeg, and gif are allowed.", "danger")
        return redirect(url_for('index'))


@app.route('/files')
@login_required
def files():
    try:
        file_list = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('files.html', files=file_list, get_icon=get_icon, title="Uploaded Files")
    except Exception as e:
        flash(f"Error retrieving files: {str(e)}", "danger")
        return redirect(url_for('index'))


@app.route('/download/<filename>')
@login_required
def download(filename):
    try:
        safe_filename = secure_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)

        # Decrypt the file before sending
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)

        # Send the decrypted file to the user
        response = send_from_directory(app.config['UPLOAD_FOLDER'], safe_filename, as_attachment=True)
        response.data = decrypted_data
        return response
    except FileNotFoundError:
        flash("File not found!", "warning")
        return redirect(url_for('files'))
    except Exception as e:
        flash(f"Error downloading file: {str(e)}", "danger")
        return redirect(url_for('files'))


@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    try:
        safe_filename = secure_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)

        if os.path.exists(file_path):
            os.remove(file_path)
            flash(f"File '{safe_filename}' deleted successfully!", "success")
        else:
            flash(f"File '{safe_filename}' not found!", "warning")

        return redirect(url_for('files'))
    except Exception as e:
        flash(f"Error deleting file: {str(e)}", "danger")
        return redirect(url_for('files'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html', title="Internal Server Error"), 500




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', ssl_context=None)

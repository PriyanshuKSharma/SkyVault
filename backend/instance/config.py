class Config:
    SECRET_KEY = '76ee378ef1421455b1d381c20ed5791d66e767360714e0b2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///files.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
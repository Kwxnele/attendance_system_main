import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "MYATTENDANCEPROJECT")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///attendance.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Facial data upload settings
    UPLOAD_FOLDER = "facial_data"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
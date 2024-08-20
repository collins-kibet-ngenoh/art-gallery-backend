import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://art_gallery_db_user:DW5IQXH7YRhiMYUIE2479h7wX3mpNmp8@dpg-cr2ajubv2p9s738cr1ng-a.oregon-postgres.render.com/art_gallery_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')

config = Config

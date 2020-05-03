db = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'port': 3306,
    'database': 'miniter'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
JWT_SECRET_KEY = 'SOME_SUPER_SECRET_KEY'
JWT_EXP_DELTA_SECONDS = 7 * 24 * 60 * 60

S3_BUCKET = "miniter-test"
S3_ACCESS_KEY = "S3_ACCESS_KEY"
S3_SECRET_KEY = "S3_SECRET_KEY"
S3_BUCKET_URL = f"https://s3.ap-northeast-2.amazonaws.com/{S3_BUCKET}/"

# UPLOAD_DIRECTORY = './profile_pictures'

test_db = {
    'user': 'test',
    'password': 'test1234',
    'host': 'localhost',
    'port': 3306,
    'database': 'test_miniter'
}
test_config = {
    'DB_URL': f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
    'JWT_SECRET_KEY': 'SOME_SUPER_SECRET_KEY',
    'JWT_EXP_DELTA_SECONDS': 7 * 24 * 60 * 60,
    'S3_BUCKET': "test",
    'S3_ACCESS_KEY': "test_access_key",
    'S3_SECRET_KEY': "test_secret_key",
    'S3_BUCKET_URL': f"https://s3.ap-northeast-2.amazonaws.com/test/"
}
from mflix.factory import create_app

import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MFLIX_DB_URI'] = 'mongodb+srv://m220student:m220password@mflix-ogokv.mongodb.net/test?retryWrites=true&w=majority'
    app.config['MFLIX_NS'] = 'sample_mflix'
    app.config['SECRET_KEY'] = 'XYZ_super_secret_testing_key_Arcadius_XYZ'

    app.run()

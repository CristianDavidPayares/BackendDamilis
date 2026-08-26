from flask import Flask
from flask_mysqldb import MySQL
from config import Config

from Routes.User_bp import us_bp
from Routes.Admin_bp import adm_bp
from Routes.Cliente_bp import cli_bp


app = Flask(__name__)

app.config.from_object(Config)

mysql = MySQL(app)

app.mysql = mysql

app.register_blueprint(us_bp, url_prefix='/users')
app.register_blueprint(adm_bp, url_prefix='/admins')
app.register_blueprint(cli_bp, url_prefix='/clientes')


if __name__ == '__main__':
    app.run(debug=True)
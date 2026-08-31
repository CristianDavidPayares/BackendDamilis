from flask import Flask
from flask_mysqldb import MySQL
from config import Config

from Routes.User_bp import us_bp
from Routes.Admin_bp import adm_bp
from Routes.Cliente_bp import cli_bp
from Routes.Categoria_bp import cat_bp
from Routes.Compra_bp import comp_bp
from Routes.Correo_bp import cor_bp
from Routes.Direccion_bp import dir_bp
from Routes.Insumo_bp import ins_bp
from Routes.Pqr_bp import pqr_bp
from Routes.Producto_bp import prod_bp
from Routes.Telefono_bp import tel_bp

app = Flask(__name__)

app.config.from_object(Config)

mysql = MySQL(app)

app.mysql = mysql

app.register_blueprint(us_bp, url_prefix='/users')
app.register_blueprint(adm_bp, url_prefix='/admins')
app.register_blueprint(cli_bp, url_prefix='/clientes')
app.register_blueprint(cat_bp, url_prefix='/categorias')
app.register_blueprint(comp_bp, url_prefix='/compras')
app.register_blueprint(cor_bp, url_prefix='/correos')
app.register_blueprint(dir_bp, url_prefix='/direcciones')
app.register_blueprint(ins_bp, url_prefix='/insumos')
app.register_blueprint(pqr_bp, url_prefix='/pqrs')
app.register_blueprint(prod_bp, url_prefix='/productos')
app.register_blueprint(tel_bp, url_prefix='/telefonos')


if __name__ == '__main__':
    app.run(debug=True)
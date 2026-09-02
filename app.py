from flask import Flask
from flask_mysqldb import MySQL
from config import Config

from Routes.UserRoutes import us_bp
from Routes.AdminRoutes import adm_bp
from Routes.ClienteRoutes import cli_bp


from Routes.CategoriaRoutes import cat_bp
from Routes.CompraRoutes import comp_bp
from Routes.CorreoRoutes import cor_bp
from Routes.DireccionRoutes import dir_bp
from Routes.InsumoRoutes import ins_bp
from Routes.PqrRoutes import pqr_bp
from Routes.ProductoRoutes import pro_bp
from Routes.TelefonoRoutes import tel_bp

from documentacion import documentacion_bp



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
app.register_blueprint(pro_bp, url_prefix='/productos')
app.register_blueprint(tel_bp, url_prefix='/telefonos')


app.register_blueprint(documentacion_bp, url_prefix='/docs')


if __name__ == '__main__':
    app.run(debug=True)
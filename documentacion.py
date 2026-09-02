from flask import Blueprint, render_template_string, send_from_directory
import os

documentacion_bp = Blueprint('documentacion', __name__)

@documentacion_bp.route('/swagger.json')
def swagger_json():
    return send_from_directory(os.path.dirname(__file__), 'swagger.json')

@documentacion_bp.route("/")
def swagger_ui():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
      <title>API - Miscelánea 3.0</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.css" />
    </head>
    <body>
      <div id="swagger-ui"></div>
      <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui-bundle.js"></script>
      <script>
        const ui = SwaggerUIBundle({
          url: "./swagger.json",
          dom_id: '#swagger-ui',
        });
      </script>
    </body>
    </html>
    """)
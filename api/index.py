from flask import Flask, request, render_template_string
import app1

app = Flask(__name__)

UPLOAD_FORM = """
<!doctype html>
<title>Generador de Turnos</title>
<h1>Subir archivo Excel</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file required>
  <input type=submit value="Procesar">
</form>
{% if result %}
  <h2>Resultados</h2>
  <p>Cobertura: {{ result.coverage_percentage|round(1) }}%</p>
  <p>Agentes: {{ result.total_agents }}</p>
  <p>Exceso: {{ result.overstaffing }}</p>
  <p>Déficit: {{ result.understaffing }}</p>
  <h3>Demanda</h3>
  <img src="data:image/png;base64,{{ result.heatmap_demand }}"/>
  <h3>Cobertura</h3>
  <img src="data:image/png;base64,{{ result.heatmap_coverage }}"/>
{% endif %}
"""


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        if file:
            result = app1.analyze_file(file.stream)
    return render_template_string(UPLOAD_FORM, result=result)

@app.route('/about')
def about():
    return 'About'


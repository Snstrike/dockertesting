import flask

from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

razas_de_gatos = [
    {
        "id": 1,
        "nombre": "Siames",
        "origen": "Tailandia",
        "pelaje": "Corto y fino",
        "patron": "Puntos de color",
        "descripcion": "El siamés es una de las primeras razas de gato asiático reconocidas distintivamente."
    },
    {
        "id": 2,
        "nombre": "Persa",
        "origen": "Persia",
        "pelaje": "Largo y lujoso",
        "patron": "Solido, tabby, bicolor",
        "descripcion": "Los gatos persas son conocidos por su personalidad tranquila y su pelo suave."
    },
    {
        "id": 3,
        "nombre": "Maine Coon",
        "origen": "Estados Unidos",
        "pelaje": "Largo y espeso",
        "patron": "Varios patrones",
        "descripcion": "El Maine Coon es conocido por su gran tamaño, su pelaje espeso y su naturaleza amistosa."
    },
    {
        "id": 4,
        "nombre": "Bengala",
        "origen": "Estados Unidos",
        "pelaje": "Corto",
        "patron": "Moteado o rayado",
        "descripcion": "El gato de Bengala es admirado por su hermoso pelaje que imita el aspecto de los felinos salvajes."
    },
    {
        "id": 5,
        "nombre": "Ragdoll",
        "origen": "Estados Unidos",
        "pelaje": "Largo y sedoso",
        "patron": "Colorpoint",
        "descripcion": "El Ragdoll es conocido por su temperamento dócil y su cuerpo grande y suave."
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''
        <h1>Catálogo de Razas de Gatos</h1>
        <p>Una implementación de API Flask para información sobre razas de gatos.</p>
        <a href="/api/v1/cat_breeds/all">Ver todas las razas de gatos</a><br/>
    '''

@app.route('/api/v1/cat_breeds/all', methods=['GET'])
def api_all():
    razas_de_gatos_str = '''
        <a href="/api/v1/cat_breeds/new">Agregar Nueva Raza</a><br>
    '''
    for raza in razas_de_gatos:
        razas_de_gatos_str += f'''
            ID: {raza["id"]}, Nombre: {raza["nombre"]}, Origen: {raza["origen"]}, Pelaje: {raza["pelaje"]}, Patrón: {raza["patron"]}, Descripción: {raza["descripcion"]}
            <a href="/api/v1/cat_breeds/delete/{raza["id"]}">Eliminar</a><br>
        '''
    return f'<pre>{razas_de_gatos_str}</pre>'

@app.route('/api/v1/cat_breeds/new', methods=['GET', 'POST'])
def nueva_raza():
    if request.method == 'POST':
        raza_de_gato = request.form.to_dict()
        max_id = max((raza['id'] for raza in razas_de_gatos), default=0) + 1
        raza_de_gato['id'] = max_id
        razas_de_gatos.append(raza_de_gato)
        return '''
            Éxito: Se ha agregado la raza del gato.<br>
            <button onclick="window.location='/'">Volver al inicio</button>
        '''
    else:
        return '''
            <h1>Nueva Raza de Gato</h1>
            <form action="" method="post">
                Nombre: <input type="text" name="nombre"><br>
                Origen: <input type="text" name="origen"><br>
                Pelaje: <input type="text" name="pelaje"><br>
                Patrón: <input type="text" name="patron"><br>
                Descripción: <textarea name="descripcion"></textarea><br>
                <input type="submit" value="Agregar">
            </form>
        '''

@app.route('/api/v1/cat_breeds/delete/<int:id>', methods=['GET', 'POST'])
def eliminar_raza(id):
    global razas_de_gatos
    if request.method == 'POST':
        razas_de_gatos = [raza for raza in razas_de_gatos if raza['id'] != id]
        return '''
            Éxito: Se ha eliminado la raza del gato.<br>
            <button onclick="window.location='/'">Volver al inicio</button>
        '''
    else:
        return f'''
            <h1>Confirmar Eliminación</h1>
            ¿Estás seguro de que quieres eliminar la raza con ID {id}?
            <form action="" method="post">
                <input type="submit" value="Sí">
            </form>
        '''



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

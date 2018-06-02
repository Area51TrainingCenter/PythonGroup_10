from flask import Flask, render_template, request, redirect

from entidades import *

app = Flask(__name__)

lista_tareas = []


@app.route('/', methods=['GET', 'POST'])
@db_session
def tareas():
    if request.method == 'POST':
        _ = Tarea(nombre=request.form['tarea'])
    return render_template('tareas.html', tareas=select(t for t in Tarea))


@app.route('/eliminar/<int:elemento>')
@db_session
def eliminar(elemento):
    Tarea[elemento].delete()
    return redirect('/')


@app.route('/editar/<int:elemento>', methods=['GET', 'POST'])
@db_session
def editar(elemento):
    tarea = Tarea[elemento]
    if request.method == 'POST':
        tarea.nombre = request.form['tarea']
        return redirect('/')
    return render_template('editar.html', tarea=tarea)


app.run(debug=True)

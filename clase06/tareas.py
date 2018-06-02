from flask import Flask, render_template, request, redirect

app = Flask(__name__)

lista_tareas = []


@app.route('/', methods=['GET', 'POST'])
def tareas():
    if request.method == 'POST':
        lista_tareas.append(request.form['tarea'])
    return render_template('tareas.html', tareas=enumerate(lista_tareas))


@app.route('/eliminar/<int:elemento>')
def eliminar(elemento):
    del lista_tareas[elemento]
    return redirect('/')


@app.route('/editar/<int:elemento>', methods=['GET', 'POST'])
def editar(elemento):
    if request.method == 'POST':
        lista_tareas[elemento] = request.form['tarea']
        return redirect('/')
    return render_template('editar.html', tarea=lista_tareas[elemento])


app.run(debug=True)

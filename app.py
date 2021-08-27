from flask import Flask, render_template
import os

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")


@app.route('/')
def hello_world():
    return render_template("layouts/index.html", title = "Главная")


@app.route('/tree-binary')
def binary_tree():
    return render_template("layouts/binary.html", title = "Бинарное дерево")


@app.route('/graph')
def graph():
    return render_template("layouts/graph.html", title = "Бинарное дерево")


@app.route('/tree-dynamic')
def dynamic_tree():
    return render_template("layouts/dynamic.html", title = "Бинарное дерево")


if __name__ == '__main__':
    app.run(debug = True)
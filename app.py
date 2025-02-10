from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    print(request.form)
    return render_template('projectform.html')

@app.route('/{id}')
def detail():
    return render_template('detail.html')

@app.route('/projects/{id}/edit')
def edit():
    return render_template('projectform.html')

@app.route('/projects/{id}/delete')
def delete():
    return render_template('projectform.html')




if __name__ == "__main__":
    app.run(debug=True, port=8000, host='127.0.0.1')
from flask import Flask, render_template, url_for, request, redirect
from models import db, Projects, app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    if request.form:
        new_project_ = Projects(title=request.form['title'], date=request.form['date'], description=request.form['desc'], skills=request.form['skills'], github=['github'])
        db.session.add(new_project_)
        db.session.commit(new_project_)
        return redirect(url_for('index'))
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
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
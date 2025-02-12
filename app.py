from flask import Flask, render_template, url_for, request, redirect
from models import db, Projects, app
from datetime import datetime, date


@app.route('/')
def index():
    projects = Projects.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    if request.form:
        new_project_ = Projects(title=request.form['title'], date=datetime.strptime(request.form['date'], "%Y-%m").date().replace(day=1), desc=request.form['desc'], skills=request.form['skills'], github=request.form['github'])
        db.session.add(new_project_)
        db.session.commit()
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
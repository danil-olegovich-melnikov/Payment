from flask import render_template, request, redirect
from .models import db, Client


def index():
    return render_template('index.html')

def form():
    if request.method == 'POST':
        email = request.form['email']
        child_name = request.form['child_name']
        text = request.form['text']
        
        new_client = Client(email=email, child_name=child_name, text=text)
        
        db.session.add(new_client)
        db.session.commit()

        return redirect("/search")

    return render_template('form.html')

def search():
    letters = []
    email = request.args.get('email', '')
    if email:
        letters = Client.query.filter_by(email=email).all()
        print(letters)

    return render_template('search.html', letters=letters)

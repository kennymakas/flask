from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHAMY_DATABAS_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class test(db.Model):
    id = db.column(db.Integer, primary_key=True)
    content = db.column(db.String(200), nullable=False)
    completed = db.column(db.Integer, default=0)
    date_created = db.column(db.DateTime, default+datetime.utcnow)

    def __repr__(self):
        return'<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
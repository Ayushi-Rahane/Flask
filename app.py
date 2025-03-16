from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request
app = Flask(__name__)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Definig the schema of database 
class Task(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

#whenever the object is created it will return the title and Sr. no.  of the task 
#instead of object reference
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/',methods=['GET','POST'])
def index():
     if request.method == 'POST':
            print(request.form['title'])
            todo = Task(title=request.form['title'], desc=request.form['desc']);
            #adding the object to the database
            db.session.add(todo)
            db.session.commit()
            #displaying all task in index.html
            alltodo = Task.query.all()
     #creating the object of Task class
     return render_template('index.html', alltodo=alltodo)

@app.route('/product')
def product():
    todo = Task.query.all()
    print(todo)
    return "this is product page!"



if __name__ == '__main__':
    app.run(debug=True)

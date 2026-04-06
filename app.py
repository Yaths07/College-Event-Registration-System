from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to MySQL (User: root, No Password, Database: college_db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/college_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# The Database Model
class Registration(db.Model):
    __tablename__ = 'registrations' # Ensures it matches your MySQL table name
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(20), nullable=False)
    course = db.Column(db.String(50), nullable=False)
    event_name = db.Column(db.String(50), nullable=False)

# CRITICAL FIX: This creates the table inside college_db automatically!
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json() 
        new_student = Registration(
            full_name=data['full_name'],
            student_id=data['student_id'],
            course=data['course'],
            event_name=data['event_name']
        )
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"status": "success", "message": "Successfully Registered!"})
    except Exception as e:
        # If something goes wrong, this tells us exactly what it is
        return jsonify({"status": "error", "message": str(e)}), 500

# NEW: Admin page to view all registrations
@app.route('/admin')
def admin():
    all_data = Registration.query.all()
    return render_template('admin.html', registrations=all_data)

if __name__ == '__main__':
    app.run(debug=True)
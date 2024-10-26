from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from  dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/site/wwwroot/training_app.db'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(150), nullable=False)
    workouts = db.relationship('WorkoutEntry', backref='author', lazy=True)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

# WorkoutEntry model
class WorkoutEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    exercise_name = db.Column(db.String(150), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# TrainingPlan model
class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer, nullable=False)
    day = db.Column(db.String(50), nullable=False)
    exercise_details = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            # Check if the username already exists
            if User.query.filter_by(username=username).first():
                flash('Username already exists. Please choose a different one.', 'danger')
                return redirect(url_for('register'))

            # Hash the password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            # Create a new user
            user = User(username=username, password_hash=hashed_password)
            # Add to database
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('An error occurred during registration. Please try again.', 'danger')
            print(f"Registration error: {e}")  # For debugging purposes
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database for the user
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your credentials.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/training_plan')
@login_required
def training_plan():
    plan = TrainingPlan.query.all()
    return render_template('training_plan.html', plan=plan)

@app.route('/log_workout', methods=['GET', 'POST'])
@login_required
def log_workout():
    if request.method == 'POST':
        try:
            date = datetime.strptime(request.form['date'], '%Y-%m-%d')
            exercise_name = request.form['exercise_name']
            sets = int(request.form['sets'])
            reps = int(request.form['reps'])
            weight = float(request.form['weight'])
            notes = request.form['notes']

            entry = WorkoutEntry(
                date=date,
                exercise_name=exercise_name,
                sets=sets,
                reps=reps,
                weight=weight,
                notes=notes,
                author=current_user
            )
            db.session.add(entry)
            db.session.commit()
            flash('Workout logged successfully!', 'success')
            return redirect(url_for('view_logs'))
        except Exception as e:
            flash('An error occurred while logging your workout. Please try again.', 'danger')
            print(f"Workout logging error: {e}")  # For debugging purposes
            return redirect(url_for('log_workout'))

    return render_template('log_workout.html')

@app.route('/view_logs')
@login_required
def view_logs():
    workouts = WorkoutEntry.query.filter_by(author=current_user).order_by(WorkoutEntry.date.desc()).all()
    return render_template('view_logs.html', workouts=workouts)

@app.route('/progress')
@login_required
def progress():
    exercise_name = request.args.get('exercise', 'Bench Press')
    workouts = WorkoutEntry.query.filter_by(
        author=current_user,
        exercise_name=exercise_name
    ).order_by(WorkoutEntry.date).all()

    dates = [workout.date.strftime('%Y-%m-%d') for workout in workouts]
    weights = [workout.weight for workout in workouts]

    return render_template('progress.html', dates=dates, weights=weights, exercise_name=exercise_name)

if __name__ == '__main__':
    app.run(debug=True)
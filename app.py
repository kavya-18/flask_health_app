from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# ---------------- Helper Functions ----------------
def calculate_age(dob):
    dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
    today = date.today()
    years = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    months = (today.year - dob_date.year) * 12 + today.month - dob_date.month
    days = (today - dob_date).days
    return years, months % 12, days % 30

def calculate_bmi(weight, feet, inch):
    height_m = ((feet * 12 + inch) * 0.0254)
    return round(weight / (height_m ** 2), 1)

def calculate_ideal_weight(feet, inch):
    total_inches = feet * 12 + inch
    if total_inches <= 60:
        return 50
    else:
        return round(50 + 2.3 * (total_inches - 60), 1)

def get_health_message(bmi):
    if bmi < 18.5:
        return 'You are underweight.'
    elif 18.5 <= bmi < 25:
        return 'You have a healthy weight!'
    elif 25 <= bmi < 30:
        return 'You are overweight.'
    else:
        return 'You are obese.'

# ---------------- Routes ----------------
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(url_for('details'))
    return render_template('home.html')

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        session['dob'] = request.form['dob']
        session['height_feet'] = int(request.form['height_feet'])
        session['height_inch'] = int(request.form['height_inch'])
        session['weight'] = float(request.form['weight'])
        return redirect(url_for('summary'))
    return render_template('details.html', name=session.get('name'))

@app.route('/summary')
def summary():
    dob = session.get('dob')
    feet = session.get('height_feet')
    inch = session.get('height_inch')
    weight = session.get('weight')
    age = calculate_age(dob)
    bmi = calculate_bmi(weight, feet, inch)
    ideal_weight = calculate_ideal_weight(feet, inch)
    health_msg = get_health_message(bmi)
    session['bmi'] = bmi
    session['ideal_weight'] = ideal_weight
    return render_template('summary.html', name=session['name'], age=age, bmi=bmi, ideal_weight=ideal_weight, message=health_msg)

@app.route('/plan')
def plan():
    ideal_weight = session.get('ideal_weight')
    calories = round(ideal_weight * 30)  # Basic formula: 30 kcal per kg
    nutrition = {
        'Protein': f"{round(ideal_weight * 1.2)} g",
        'Fiber': "25-30 g",
        'Fats': f"{round(calories * 0.25 / 9)} g",
        'Carbs': f"{round((calories * 0.5) / 4)} g",
        'Micronutrients': ["Calcium (1000mg)", "Iron (18mg)", "Vitamin D (600 IU)", "Vitamin B12 (2.4 mcg)"]
    }
    return render_template('plan.html', name=session['name'], calories=calories, nutrition=nutrition)

# ---------------- Symptom Check-In ----------------
SYMPTOM_GUIDANCE = {
    "dizziness": {
        "meaning": "Could be due to low blood sugar, dehydration, or anemia.",
        "tips": ["Drink water frequently", "Don't skip meals", "Avoid sudden movements"],
        "red_flag": "Persistent dizziness may need medical attention."
    },
    "bloating": {
        "meaning": "Likely due to poor digestion or food intolerance.",
        "tips": ["Eat slowly", "Avoid carbonated drinks", "Try peppermint tea"],
        "red_flag": "Seek help if bloating is chronic or painful."
    },
    "pimples": {
        "meaning": "Can be triggered by hormones, stress, or oily food.",
        "tips": ["Wash face regularly", "Avoid fried foods", "Stay hydrated"],
        "red_flag": "Visit dermatologist if painful or cystic acne."
    },
    "hair fall": {
        "meaning": "Could be due to stress, low iron, or hormonal imbalance.",
        "tips": ["Eat iron-rich foods", "Use mild shampoo", "Reduce heat styling"],
        "red_flag": "Excessive hair loss may need blood tests."
    },
    "gastric problems": {
        "meaning": "Usually caused by acidity or unhealthy eating habits.",
        "tips": ["Eat on time", "Limit caffeine/spices", "Try yoga post-meals"],
        "red_flag": "If pain is sharp or frequent, see a doctor."
    }
}

@app.route('/symptom-checkin', methods=['GET', 'POST'])
def symptom_checkin():
    if request.method == 'POST':
        selected = request.form.getlist('symptoms')
        results = {}
        for symptom in selected:
            if symptom in SYMPTOM_GUIDANCE:
                results[symptom] = SYMPTOM_GUIDANCE[symptom]
        return render_template('symptom_results.html', results=results)
    return render_template('symptom_form.html', symptoms=SYMPTOM_GUIDANCE.keys())

# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(debug=True)

Health Tracking Flask App

This is a sleek and interactive web application built with Flask that helps users calculate their BMI, determine their ideal weight, and get a customized nutrition plan. It also includes a beautiful UI, emotional connection through personalized messages, and future-ready structure for expansion.

Features

Collects basic user details (name, DOB, height, weight)

Calculates Age, BMI, and Ideal Weight

Provides a personalized health message based on BMI

Suggests custom nutrition plan (protein, fiber, fats, carbs, micronutrients)

Clean navigation across pages with session-based memory

Styled with Bootstrap 5 and custom CSS for modern UI

🛠 Tech Stack

## 🛠 Tech Stack

| Layer        | Technology            | Purpose                              |
|--------------|------------------------|---------------------------------------|
| Backend      | Python 3.10, Flask     | Core logic and routing                |
| Frontend     | HTML5, CSS3            | User Interface and page structure     |
| Templating   | Jinja2                 | Dynamic rendering with user inputs    |
| Styling      | Bootstrap 5, style.css | Responsive design and custom styles   |
| Deployment   | Gunicorn (planned)     | WSGI server for production             |
| Development  | PyCharm                | IDE for project structuring and logic |

Project Structure

## 🗂 Project Structure

```text
flask_health_app/
├── app.py                  # Main Flask application file
├── requirements.txt        # List of dependencies
├── static/                 # Folder for CSS and assets
│   └── style.css           # Custom styles for the app
├── templates/              # HTML templates rendered with Jinja2
│   ├── layout.html         # Shared layout for all pages
│   ├── home.html           # Page to enter user name
│   ├── details.html        # Page to enter DOB, height, and weight
│   ├── summary.html        # Displays age, BMI, ideal weight
│   └── plan.html           # Displays nutrition plan
├── screenshots/            # Images for UI preview
│   ├── home.png
│   ├── details.png
│   ├── summary.png
│   └── plan.png
└── .idea/                  # PyCharm-specific files (should be ignored)



```
## How to Run This App Locally

### 1. Clone the Repository
```

git clone https://github.com/kavya-18/flask_health_app.git
cd flask_health_app

```
### 2. Create a Virtual Environment
```

python -m venv .venv


Activate it:

```

```
- **On Windows**:

  
  .venv\Scripts\activate


- **On macOS/Linux**:


source .venv/bin/activate
 ```

### 3. Install Required Dependencies

```
pip install -r requirements.txt
```

### 4. Run the Flask App

```
python app.py
```

```
Then open your browser and go to:
http://127.0.0.1:5000/
```


📷 UI Preview

🏠 Home Page



📋 Details Page



✨ Summary Page



🥗 Nutrition Plan Page



🔍 Code Highlights

app.py manages routes (/, /details, /summary, /plan) and session flow

calculate_age(), calculate_bmi(), and calculate_ideal_weight() provide backend logic

Uses Flask session to carry user inputs across pages

Nutrition plan dynamically adapts to the ideal weight

📈 Future Enhancements

📋 Add emotional eating tracker and snack alternatives

👤 Enable user authentication and profile history

🧠 Include mental wellness tips and motivational messages

📊 Visualize BMI history using Chart.js or Plotly

☁️ Deploy on Render or Heroku with PostgreSQL integration

🙋‍♀️ About the Author

Kavya Reddy Parige
XXXX  🔗 GitHub | LinkedIn

📄 License

This project is open-source and available under the MIT License.

Made with 💚 for better health and better code.


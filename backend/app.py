from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Enhanced project data with more details
projects_data = [
    {
        "id": 1,
        "title": "Smart Voice Assistant",
        "short_desc": "Modular assistant with voice + text input, reminders, system commands, AI integration.",
        "long_desc": "Built using Python and Flask, this smart assistant can handle voice and text commands, set reminders, execute system tasks, and integrate AI responses for queries. Features include natural language processing, voice recognition, task scheduling, and seamless integration with system operations.",
        "tech_stack": ["Python", "Flask", "Speech Recognition", "AI/ML", "NLP"],
        "github": "https://github.com/your-username/voice-assistant",
        "demo": "#",
        "image": "voice-assistant.jpg",
        "status": "Completed"
    },
    {
        "id": 2,
        "title": "Interactive Chess Game",
        "short_desc": "Fullscreen chess with move history, captured pieces panel, smooth scaling.",
        "long_desc": "An interactive chess game implemented with Python featuring a complete chess engine. Includes fullscreen mode, comprehensive move history tracking, captured pieces panel, dynamic board scaling, and intelligent move validation. The game supports both human vs human and human vs AI gameplay modes.",
        "tech_stack": ["Python", "Pygame", "Chess Engine", "GUI Design"],
        "github": "https://github.com/your-username/chess-game",
        "demo": "#",
        "image": "chess-game.jpg",
        "status": "Completed"
    },
    {
        "id": 3,
        "title": "Game Development Projects",
        "short_desc": "Games using Python and basic Unity.",
        "long_desc": "Developed several interactive games using Python and Unity, including logic design, GUI creation, and basic game mechanics. Projects range from 2D platformers to puzzle games, demonstrating proficiency in game development principles, physics simulation, and user interface design.",
        "tech_stack": ["Python", "Unity", "C#", "Game Physics", "UI/UX"],
        "github": "https://github.com/your-username/game-projects",
        "demo": "#",
        "image": "game-dev.jpg",
        "status": "Ongoing"
    },
    {
        "id": 4,
        "title": "Spam Detection AI",
        "short_desc": "Detects spam messages using Python NLP.",
        "long_desc": "Python-based AI system that classifies messages as spam or not spam using Natural Language Processing techniques. Implements machine learning algorithms including Naive Bayes, SVM, and neural networks for accurate spam detection with high precision and recall rates.",
        "tech_stack": ["Python", "Scikit-learn", "NLTK", "Pandas", "Machine Learning"],
        "github": "https://github.com/your-username/spam-detector",
        "demo": "#",
        "image": "spam-detection.jpg",
        "status": "Completed"
    },
    {
        "id": 5,
        "title": "Snake Game",
        "short_desc": "Classic Snake game using Python and Pygame.",
        "long_desc": "A classic Snake game implemented in Python using Pygame library. Features smooth controls, progressive difficulty scaling, high score tracking, power-ups, and multiple game modes. The game includes sound effects, particle systems, and a polished user interface.",
        "tech_stack": ["Python", "Pygame", "Game Logic", "Graphics"],
        "github": "https://github.com/your-username/snake-game",
        "demo": "#",
        "image": "snake-game.jpg",
        "status": "Completed"
    },
    {
        "id": 6,
        "title": "Flappy Bird (Unity)",
        "short_desc": "Flappy Bird clone in Unity.",
        "long_desc": "Developed a Flappy Bird clone using Unity, featuring physics-based movement, dynamic obstacle generation, scoring system, and particle effects. The game includes multiple themes, power-ups, and achievements system with smooth gameplay mechanics.",
        "tech_stack": ["Unity", "C#", "Physics2D", "Mobile Development"],
        "github": "https://github.com/your-username/flappy-bird-unity",
        "demo": "#",
        "image": "flappy-bird.jpg",
        "status": "Completed"
    },
    {
        "id": 7,
        "title": "BSE Stock Predictor",
        "short_desc": "Predicts stock trends using Python.",
        "long_desc": "Python project predicting BSE stock trends using historical data and machine learning models. Implements LSTM neural networks, technical indicators analysis, and real-time data processing. Features include trend visualization, risk assessment, and portfolio optimization recommendations.",
        "tech_stack": ["Python", "TensorFlow", "Pandas", "NumPy", "Data Visualization"],
        "github": "https://github.com/your-username/stock-predictor",
        "demo": "#",
        "image": "stock-predictor.jpg",
        "status": "Completed"
    }
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects_data[:4])  # Show first 4 projects

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_data)

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in projects_data if p["id"] == project_id), None)
    if project:
        return render_template("project_detail.html", project=project)
    return render_template("404.html"), 404

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Here you would typically save to database or send email
        # For now, just flash a success message
        flash("Thank you! Your message has been received. I'll get back to you soon!", "success")
        return redirect(url_for("contact"))
    
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
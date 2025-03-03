from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample quiz questions and answers
questions = [
    {
        'question': '1.What is the binary code of 80?',
        'choices': ['1010000', '1010110', '1110000', '1110110'],
        'correct_answer': '1010000'
    },
    {
        'question': '2.What is the largest planet in our solar system?',
        'choices': ['Venus', 'Saturn', 'Jupiter', 'Mars'],
        'correct_answer': 'Jupiter'
    },
    {
        'question': '3.Which programming language is used to build Flask?',
        'choices': ['Python', 'Java', 'Ruby', 'R Programming'],
        'correct_answer': 'Python'
    },
    {
        'question': '4.who designed Flask?',
        'choices': ['Guido van Rossum', 'Armin Ronacher', 'Dennis Ritchie', 'James Gosling'],
        'correct_answer': 'Armin Ronacher'
    }
]

# Route for home page
@app.route('/')
def home():
    if 'score' not in session:
        session['score'] = 0
    return render_template('index.html')

# Route for displaying and processing quiz questions
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answer = request.form['choice']
        if answer == questions[session['question_number']]['correct_answer']:
            session['score'] += 1
        session['question_number'] += 1
        if session['question_number'] >= len(questions):
            return redirect('/result')
    else:
        session['question_number'] = 0
        session['score'] = 0

    return render_template('quiz.html', question=questions[session['question_number']])

# Route for displaying quiz results
@app.route('/result')
def result():
    final_score = session['score']
    session.clear()
    return render_template('result.html', score=final_score)

if __name__ == '__main__':
    app.run(debug=True,port=2202,host='0.0.0.0')

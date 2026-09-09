
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username']=='admin' and request.form['password']=='admin123':
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/how')
def how():
    return render_template('how.html')

@app.route('/assessment', methods=['GET','POST'])
def assessment():
    feedback = None
    if request.method=='POST':
        score = sum([1 for i in range(1,10) if request.form.get(f'q{i}')=='yes'])
        if score>=7:
            feedback="Your ethical AI maturity is high. Continue improving governance audits, continuous monitoring, and transparency documentation."
        elif score>=4:
            feedback="Your practices are moderate. Improve fairness testing, explainability, and stakeholder review processes."
        else:
            feedback="Your ethical readiness is low. Focus on ethics training, bias mitigation, risk assessment, and AI governance frameworks."
    return render_template('assessment.html', feedback=feedback)

@app.route('/idea', methods=['GET','POST'])
def idea():
    result=None
    text=""
    if request.method=='POST':
        text=request.form['idea']
        t=text.lower().strip()
        if len(t)<5:
            result="Invalid idea. Please provide a clear and meaningful description."
        elif 'health' in t or 'medical' in t:
            result="Recommended ideas: privacy-by-design, bias mitigation in diagnosis, explainable AI for clinicians, and human-in-the-loop validation."
        elif 'finance' in t or 'bank' in t:
            result="Recommended ideas: transparent credit scoring, regulatory compliance, fairness audits, and accountability mechanisms."
        elif 'education' in t:
            result="Recommended ideas: fair student assessment, bias-free recommendation systems, data privacy, and explainable grading models."
        else:
            result="Recommended ideas: apply transparency, accountability, fairness testing, risk assessment, and ethical reviews throughout SDLC."
    return render_template('idea.html', result=result, text=text)

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/future')
def future():
    return render_template('future.html')

if __name__=='__main__':
    app.run(debug=True)

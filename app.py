from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')


# Route for creating the portfolio
@app.route('/create_portfolio', methods=['GET', 'POST'])
def create_portfolio():
    if request.method == 'POST':
        # Handle the form submission (e.g., save data to the database or session)
        name = request.form['name']
        bio = request.form['bio']
        skills = request.form['skills']
        social = request.form['social']

        # Redirect to the portfolio showcase page after form submission
        return redirect(url_for('portfolio_showcase', name=name, bio=bio, skills=skills, social=social))

    return render_template('create_portfolio.html')


# Route for showcasing the portfolio
@app.route('/portfolio_showcase')
def portfolio_showcase():
    # Ensure data is passed as arguments, or default to some placeholder
    name = request.args.get('name', 'Default Name')
    bio = request.args.get('bio', 'This is a sample bio.')
    skills = request.args.get('skills', 'No skills listed.')
    social = request.args.get('social', '#')

    # Render the portfolio_showcase.html template with data
    return render_template('portfolio_showcase.html', name=name, bio=bio, skills=skills, social=social)


if __name__ == '__main__':
    app.run(debug=True)

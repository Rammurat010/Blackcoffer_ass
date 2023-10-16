from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use your preferred database URI
db = SQLAlchemy(app)

# Define your data model
class Data(db.Model):
    # Your data model fields go here
    id = db.Column(db.Integer, primary_key=True)
    intensity = db.Column(db.Float)
    likelihood = db.Column(db.Float)
    relevance = db.Column(db.Float)
    year = db.Column(db.Integer)
    country = db.Column(db.String(50))
    topics = db.Column(db.String(50))
    region = db.Column(db.String(50))
    city = db.Column(db.String(50))

@app.route('/api/data')
def get_data():
    # Fetch data from the database
    data = Data.query.all()

    # Convert data to JSON and return
    data_json = [
        {
            'intensity': item.intensity,
            'likelihood': item.likelihood,
            'relevance': item.relevance,
            'year': item.year,
            'country': item.country,
            'topics': item.topics,
            'region': item.region,
            'city': item.city
        } for item in data
    ]

    return jsonify(data_json)

if __name__ == '__main__':
    app.run(debug=True)

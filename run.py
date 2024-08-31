from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Mock charities data will be done with api most likely
with open('charities.json', 'r') as f:
    charities = json.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/charity_dashboard')
def charity_dashboard():
    return render_template('charity_dashboard.html')

@app.route('/post_needs')
def post_needs():
    return render_template('post_needs.html')


@app.route('/share_story')
def share_story():
    return render_template('share_story.html')

@app.route('/donation_management')
def donation_management():
    return render_template('donation_management.html')

@app.route('/explore_charities')
def explore_charities():
    return render_template('explore_charities.html', charities=charities)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/view_charity/<int:charity_id>')
def view_charity(charity_id):
    charity = next((c for c in charities if c['id'] == charity_id), None)
    return render_template('view_charity.html', charity=charity)

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.route('/make_donation')
def make_donation():
    return render_template('make_donation.html')

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

# Load feed data from JSON file
def load_feed():
    try:
        with open('feed.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save feed data to JSON file
def save_feed(feed):
    with open('feed.json', 'w') as f:
        json.dump(feed, f)
        

@app.route('/feed')
def feed():
    feed_data = load_feed()
    return render_template('feed.html', feed=feed_data)

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        new_post = {
            'id': len(load_feed()) + 1,
            'text': request.form['text'],
            'image': request.form.get('image', '')
        }
        feed = load_feed()
        feed.append(new_post)
        save_feed(feed)
        return redirect(url_for('feed'))
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True)
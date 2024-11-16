from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/charity_dashboard')
def charity_dashboard():
    return render_template('charity_dashboard.html')

@app.route('/post_needs')
def post_needs():
    return render_template('post_needs.html')


@app.route('/blog')
def blog_view():
    return render_template('blog-details.html')

@app.route('/share_story')
def share_story():
    return render_template('share_story.html')

@app.route('/donation_management')
def donation_management():
    return render_template('donation_management.html')

@app.route('/investment_dashboard')
def investment_dashboard():
    return render_template('investment_dashboard.html')

@app.route('/explore_charities', methods=['GET', 'POST'])
def explore_charities():
    with open('charities.json', 'r') as f:
        charities = json.load(f)

    search_results = []
    if request.method == 'POST':
        search_term = request.form.get('search')
        for item in charities:
            print(item)
        search_results = [item for item in charities if search_term.lower() in item["location"].lower()]
        return render_template('explore_charities.html', charities=search_results)

    return render_template('explore_charities.html', charities=charities)

@app.route('/submit_application', methods=['GET', 'POST'])
def save_charities():
    search_results = []
    if request.method == 'POST':
        location = request.form.get('location')
        Organization_Name = request.form.get('name')
        Mission_Statement = request.form.get('description')
        Contact_Email = request.form.get('contactEmail')
        Upload_Logo= request.form.get('logo')
        if 'logo' not in request.files:
            return 'No file part'
        
        file = request.files['logo']
     
        if file.filename == '':
            return 'No selected file'
        


        if file:
            filename = file.filename
            save_path = os.path.join('static', filename)
            file.save(save_path)
            org = {
                "id": 1000,
                "name": Organization_Name,
                "logo":save_path,
                "description": Mission_Statement,
                "needs": ["Tree saplings", "Volunteers for clean-up drives"],
                "stories":
                {
                "title": "Planting 10,000 trees in urban areas",
                "content": "Our urban reforestation project has successfully..."
                },
                "location":location
            }

            with open('charities.json', 'r+') as file:
                data = json.load(file)
            
                if isinstance(data, list):
            
                    data.append(org)
                else:
                    raise ValueError("Expected the root element to be a list")
                
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

    with open('charities.json', 'r') as f:
        charities = json.load(f)

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

@app.route('/about_view', methods=['GET', 'POST'])
def about_view():
    return render_template('about.html')

@app.route('/view_charity/<int:charity_id>')
def view_charity(charity_id):
    with open('charities.json', 'r') as f:
        charities = json.load(f)

    charity = next((c for c in charities if c['id'] == charity_id), None)
    return render_template('view_charity.html', charity=charity)

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.route('/donate')
def make_donation():
    with open('charities.json', 'r') as f:
        charities = json.load(f)
    return render_template('make_donation.html',charities=charities)

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


def load_data():
    with open('charities.json', 'r') as f:
        return json.load(f)
    
if __name__ == '__main__':
    app.run()
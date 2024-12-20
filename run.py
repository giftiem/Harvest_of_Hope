from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import requests
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


@app.route('/investment_dashboard/<int:charity_id>')
def investment_dashboard(charity_id):
    # charity_id = request.args.get('charity_id')
    print("im here", charity_id)
    request_data = fetch_specific_project(charity_id, "207d0f21-65f0-4a5d-8084-5d972d341309")   
    print(request_data)
    return render_template('view_charity.html', project=request_data['projects']['project'][0])

@app.route('/thank-you')
def signed_up():
    return render_template('thank-you.html')

@app.route('/explore_charities', methods=['GET', 'POST'])
def explore_charities():
    country_code = "ZA"  # Default country code
    charities = fetch_projects(country_code, "207d0f21-65f0-4a5d-8084-5d972d341309")
    needs_list = list(set(theme['name'] for charity in charities for theme in charity['themes']['theme']))

    search_results = []
    if request.method == 'POST':
        search_term = request.form.get('search')
        country_filter = request.form.get('country')
        needs_filter = request.form.getlist('needs')
        needs_filter.append('all')
        
        
        print('Im this small',len(needs_filter))
        if country_filter and country_filter != country_code:
            country_code = country_filter
            charities = fetch_projects(country_code, "207d0f21-65f0-4a5d-8084-5d972d341309")
            needs_list = list(set(theme['name'] for charity in charities for theme in charity['themes']['theme']))
        if needs_filter[0] != 'all':
            search_results = [
                item for item in charities
                if (not search_term or search_term.lower() in item["title"].lower())
                and (not country_filter or item["iso3166CountryCode"] == country_filter)
                and (not needs_filter or any(theme['name'] in needs_filter for theme in item['themes']['theme']))
            ]
        else:
            search_results = [
                item for item in charities
                if (not search_term or search_term.lower() in item["title"].lower())
                and (not country_filter or item["iso3166CountryCode"] == country_filter)
            ]

        return render_template('explore_charities.html', charities=search_results, needs_list=needs_list)

    return render_template('explore_charities.html', charities=charities, needs_list=needs_list)

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

@app.route('/ngo/<int:ngo_id>')
def ngo_dashboard(ngo_id):
    
    # project = next((p for p in projects if p['id'] == ngo_id), None)

    return render_template('view_charity.html', project=project)



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

def fetch_projects(country_code, api_key, calls: int = 20):
    base_url = f"https://api.globalgiving.org/api/public/projectservice/countries/{country_code}/projects"
    headers = {
        'Accept': 'application/json'  # Explicitly request JSON response
    }
    params = {
        'api_key': api_key
    }
    all_projects = []
    has_next = True

    while (has_next and len(all_projects) <= calls):
        response = requests.get(base_url,headers=headers, params=params)
        response.headers['Content-Type'] == 'application/json'
        data = response.json()
    


        # Assuming JSON handling for simplicity; adapt if using XML
        all_projects.extend(data['projects']['project'])
        
        has_next = data['projects'].get('hasNext', False)
        if has_next:
            params['nextProjectId'] = data['projects']['nextProjectId']

    return all_projects

def fetch_specific_project(id, api_key):
    base_url = f"https://api.globalgiving.org/api/public/projectservice/projects/collection/ids?projectIds={id}"
    headers = {
        'Accept': 'application/json'  # Explicitly request JSON response
    }
    params = {
        'api_key': api_key

    }

    response = requests.get(base_url,headers=headers, params=params)
    response.headers['Content-Type'] == 'application/json'
    data = response.json()
    
    return data

def load_data():
    with open('charities.json', 'r') as f:
        return json.load(f)
    
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


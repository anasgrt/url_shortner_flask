import random
import string
import re
from flask import Flask, render_template, redirect, url_for, request, jsonify
from datetime import datetime


app = Flask(__name__)
shortened_urls = {}

def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits + '_'
    short_urls = ''.join(random.choice(chars) for _ in range(length))
    return short_urls

def validate_shortcode(shortcode):
    pattern = r'^[a-zA-Z0-9_]{6}$'
    if re.match(pattern, shortcode):
        return True
    else:
        return False

@app.route('/shorten', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        long_url = request.json.get("url")
        shortcode = request.json.get("shortcode")

        if not long_url:
            return "URL not present", 400
        if shortcode and not validate_shortcode(shortcode):
            return "Invalid shortcode", 412
        if shortcode and shortcode in shortened_urls:
            return f"Shortcode {shortcode} already exists", 409
        
        if not shortcode:
            shortcode = generate_short_url()

        while shortcode in shortened_urls:
            shortcode = generate_short_url()
        shortened_urls[shortcode] = {
            "url": long_url,
            "created": datetime.now(),
            "last_redirect": datetime.now(),
            "redirect_count": 0
        }
        return f"Shortened URL: {request.url_root}{shortcode}", 201
    return render_template("index.html")

@app.route('/<shortcode>')
def redirect_to_url(shortcode):
    long_url = shortened_urls.get(shortcode)
    if long_url:
        # Update the last redirect time and increment the redirect count
        long_url['last_redirect'] = datetime.now()
        long_url['redirect_count'] += 1
        return redirect(long_url['url'], code=302)
    else:
        return f"No URL found for {shortcode}", 404
    
@app.route('/<shortcode>/stats')
def get_shortcode_stats(shortcode):
    if shortcode in shortened_urls:
        created = shortened_urls[shortcode]['created']
        last_redirect = shortened_urls[shortcode]['last_redirect']
        redirect_count = shortened_urls[shortcode]['redirect_count']
        
        # Format the datetime values to ISO 8601 format
        created_iso = created.isoformat()
        last_redirect_iso = last_redirect.isoformat()
        
        response = {
            "created": created_iso,
            "lastRedirect": last_redirect_iso,
            "redirectCount": redirect_count
        }
        return jsonify(response), 200
    else:
        return "Shortcode not found", 404


if __name__ == '__main__':
    app.run(debug=True)
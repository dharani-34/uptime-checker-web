from flask import Flask, render_template, request
import requests
import webbrowser
import threading

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    status = None
    url = ''

    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            if response.status_code == 200:
                status = f"✅ {url} is UP! (Status: 200)"
            else:
                status = f"⚠️ {url} returned status code {response.status_code}"
        except:
            status = f"❌ {url} is DOWN or unreachable."

    return render_template('index.html', status=status, url=url)

# 👇 This function will auto-open the browser
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    # Timer opens browser after 1.2 sec
    threading.Timer(1.2, open_browser).start()
    app.run(debug=True)

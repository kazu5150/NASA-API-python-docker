import os
import requests
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


def get_nasa_apod(api_key, date=None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key
    }
    if date:
        params["date"] = date

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"エラーが発生しました。ステータスコード: {response.status_code}"}


@app.route('/apod')
def apod():
    date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    api_key = os.environ.get('NASA_API_KEY')
    if not api_key:
        return jsonify({"error": "NASA API キーが設定されていません"}), 500

    result = get_nasa_apod(api_key, date)

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ result['title'] }}</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
            img { max-width: 100%; height: auto; }
            h1 { color: #333; }
            .explanation { background-color: #f4f4f4; padding: 15px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>{{ result['title'] }}</h1>
        <p>Date: {{ result['date'] }}</p>
        <img src="{{ result['url'] }}" alt="{{ result['title'] }}">
        <div class="explanation">
            <h2>Explanation</h2>
            <p>{{ result['explanation'] }}</p>
        </div>
        {% if result.get('copyright') %}
        <p>Copyright: {{ result['copyright'] }}</p>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html_template, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


from flask import Flask, render_template
import pandas as pd
from collections import defaultdict

app = Flask(__name__)

def load_menu():
    df = pd.read_excel('menu.xlsx')
    grouped = defaultdict(list)
    for item in df.to_dict(orient='records'):
        grouped[item['Category']].append(item)
    return grouped

menu_by_category = load_menu()

@app.route('/')
def index():
    return render_template('index.html', menu=menu_by_category)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

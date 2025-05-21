# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

# Copyright 2025 emanoyhl and emanoyhl.net find me at github.com/emanoyhl 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

# Load the trained model (assuming you save it after training)
model = pickle.load(open('phishing_model.pkl', 'rb'))

def extract_features(url):
    # Prepend 'http://' if protocol is missing
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return {
        'length': len(url),
        'https': 1 if 'https://' in url else 0,
        'subdomains': url.count('.'),
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features(url)
        prediction = model.predict(pd.DataFrame([features]))
        result = 'Phishing' if prediction[0] == 1 else 'Legitimate'
        return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

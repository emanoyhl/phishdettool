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

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your data
data = pd.read_csv('phishing_data.csv')  # Use your actual dataset

# Feature extraction function
def extract_features(url):
    return {
        'length': len(url),
        'https': 1 if 'https://' in url else 0,
        'subdomains': url.count('.'),
    }

# Prepare dataset
features = data['url'].apply(extract_features).tolist()
X = pd.DataFrame(features)
y = data['label']  # Assuming labels are 0 (legitimate) and 1 (phishing)

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as 'phishing_model.pkl'")

# PhishDetTool
Simple phishing detection tool; uses Flask and pandas and pickle

## Usage
  1. First create your own phishing_data.csv file or use the example one provided which is basically a list of known phishing sites - you would usually get your data from some other list with actual known sites
  2. Once you have your .csv file (whether the example or your own) run the training model:
     ```bash
     python train_model.py
    ```
  3. That will create a phishing_model.pkl file - if you continuously add data, please delete the .pkl file and re-run the training model on step 2. above for every newly added/updated .csv data file
  4. Run the program:
     ```bash
     python app.py
     ```

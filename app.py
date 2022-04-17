from flask import Flask, render_template, request
import joblib
import pandas as pd
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = height-input in HTML form
       if "height_input" in request.form:
           user_height = request.form['height_input']
       # getting input with name = sex_choice in HTML form
       if "sex_choice" in request.form:
           sex_choice = request.form["sex_choice"]
    
       if user_height and sex_choice:
           data = [[sex_choice, user_height]]
           df_input = pd.DataFrame(data, columns = ['Gender', 'Height'])
           model = joblib.load("model-development\mlr_weight.pkl")
           df_input
           arr_result = model.predict(df_input)
           result = arr_result[0]
           result = round(result, 2)
           return render_template('index.html', result=result)
        
if __name__ == '__main__':
   app.run(debug = True)           
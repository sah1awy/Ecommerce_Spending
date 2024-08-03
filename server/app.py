from flask import Flask, Response, url_for, redirect, render_template, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict',methods=['POST'])
def predict():
    avg_session_length = float(request.form["avg_session_length"])
    time_on_app = float(request.form["time_on_app"])
    time_on_website = float(request.form["time_on_website"])
    length_of_membership = float(request.form["length_of_membership"])   
    res = util.predict_yearly_spent(avg_session_length,time_on_app,time_on_website,length_of_membership)
    if res < 0:
        return render_template('app.html', prediction_text=f'The Predicted Spent is: 0$')
    return render_template('app.html', prediction_text=f'The Predicted Spent is: {res}$')


if __name__ == "__main__":
    print("Starting Python Flask App for Yearly Amount Spent Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
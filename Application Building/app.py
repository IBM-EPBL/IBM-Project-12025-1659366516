import numpy as np
import os
from flask import Flask, request, jsonify, render_template
import pickle

app=Flask(__name__)
model = pickle.load(open('rfmodel.pkl', 'rb'))
@app.route("/")
def firstpage():
    return render_template("index.html") 

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    summer=[6,7,8]
    Winter=[9,10,11]
    Spring=[12,1,2,3]
    Fall=[4,5]
    Form_Data= [int(x) for x in request.form.values()]
    print(Form_Data[1])
    if Form_Data[1] in summer:
        Form_Data.append(0)
    elif Form_Data[1] in Winter:
        Form_Data.append(1)
    elif Form_Data[1] in Spring:
        Form_Data.append(2)
    else:
        Form_Data.append(3)
    final_features=np.array(Form_Data,dtype='int64')
    print(final_features)
    prediction = model.predict([final_features])
    

    output = round(prediction[0])

    if output==0:
        return render_template('Prediction.html', prediction_text='No delay will happen {}'.format(output))
    elif output==1:
        return render_template('Prediction.html', prediction_text='There is a chance to departure delay will happen {}'.format(output))
    elif output==2:
        return render_template('Prediction.html', prediction_text='here is a chance to both departure and arrival delay will happen {}'.format(output))
    elif output==3:
        return render_template('Prediction.html', prediction_text='here is a chance to flight  will diverted {}'.format(output))
    elif output==4:
        return render_template('Prediction.html', prediction_text='here is a chance to cancel the flight {}'.format(output))
    else:
        return render_template('Prediction.html', prediction_text='output {}'.format(output))

# @app.route("/prediction",methods=['POST'])
# def predict():
#     flight_number=request.form['flight number']
#     month=request.form['month']
#     day=request.form['day']
#     week=request.form['week']
#     origin=request.form['origin']
#     destination=request.form['destination']
#     Scheduled_dept_time=request.form['Scheduled dept time']
#     Scheduled_arrival_time=request.form['Scheduled arrival time']
#     Actual_dept_time=request.form['Actual dept time']


if __name__=='__main__':
    app.run(debug=True)
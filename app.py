import numpy as np
from flask import Flask, request, jsonify, render_template
#from flask_ngrok import run_with_ngrok
import pickle
#from jinja2 import Template

app = Flask(__name__)

#run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("index.html")
#------------------------------About us-------------------------------------------
@app.route('/aboutus')
def aboutusnew():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/intern')
def intern():
    return render_template('Other.html')

@app.route('/qr')
def qr():
    return render_template('QR.html')

@app.route('/Svm')
def svm():

    return render_template('SVM.html')

@app.route('/Decision')
def decisiontree():
 
    return render_template('decision tree.html')

@app.route('/knn')
def knn():
    return render_template('K-NN.html')

@app.route('/Rf')
def randomforest():
    return render_template('random forest.html')

@app.route('/nvb')
def naivebayes():
    return render_template('Naive.html')

@app.route('/linear')
def linear():
    return render_template('linear.html')


@app.route('/predict',methods=['GET'])
def predict():
    age = float(request.args.get('age'))
    AA=float(request.args.get('aa'))
    wc=float(request.args.get('wc'))
    mc=float(request.args.get('mc'))
    pt=float(request.args.get('pt'))
    vc=float(request.args.get('vc'))
    vp=float(request.args.get('vp'))
    av=float(request.args.get('av'))
    rf= float(request.args.get('repf'))
    wp=float(request.args.get('wp'))
    sex=float(request.args.get('sex'))


    model=pickle.load(open('decision_model.pkl','rb'))
    
    prediction = model.predict([[age,AA,wc,mc,pt,vc,vp,av,rf,wp,sex]])
    if prediction==0:
      message="Not Fraud"
    else:
      message="Fraud"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))



@app.route('/predict1',methods=['GET'])
def predict1():
    age = float(request.args.get('age'))
    AA=float(request.args.get('aa'))
    wc=float(request.args.get('wc'))
    mc=float(request.args.get('mc'))
    pt=float(request.args.get('pt'))
    vc=float(request.args.get('vc'))
    vp=float(request.args.get('vp'))
    av=float(request.args.get('av'))
    rf= float(request.args.get('repf'))
    wp=float(request.args.get('wp'))
    sex=float(request.args.get('sex'))


    model=pickle.load(open('svm.pkl','rb'))
    
    prediction = model.predict([[age,AA,wc,mc,pt,vc,vp,av,rf,wp,sex]])
    if prediction==0:
      message="Not Fraud"
    else:
      message="Fraud"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))


@app.route('/predict2',methods=['GET'])
def predict2():
    age = float(request.args.get('age'))
    AA=float(request.args.get('aa'))
    wc=float(request.args.get('wc'))
    mc=float(request.args.get('mc'))
    pt=float(request.args.get('pt'))
    vc=float(request.args.get('vc'))
    vp=float(request.args.get('vp'))
    av=float(request.args.get('av'))
    rf= float(request.args.get('repf'))
    wp=float(request.args.get('wp'))
    sex=float(request.args.get('sex'))


    model=pickle.load(open('knn.pkl','rb'))
    
    prediction = model.predict([[age,AA,wc,mc,pt,vc,vp,av,rf,wp,sex]])
    if prediction==0:
      message="Not Fraud"
    else:
      message="Fraud"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))

@app.route('/predict3',methods=['GET'])
def predict3():
    age = float(request.args.get('age'))
    AA=float(request.args.get('aa'))
    wc=float(request.args.get('wc'))
    mc=float(request.args.get('mc'))
    pt=float(request.args.get('pt'))
    vc=float(request.args.get('vc'))
    vp=float(request.args.get('vp'))
    av=float(request.args.get('av'))
    rf= float(request.args.get('repf'))
    wp=float(request.args.get('wp'))
    sex=float(request.args.get('sex'))


    model=pickle.load(open('random_forest.pkl','rb'))
    
    prediction = model.predict([[age,AA,wc,mc,pt,vc,vp,av,rf,wp,sex]])
    if prediction==0:
      message="Not Fraud"
    else:
      message="Fraud"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))

@app.route('/predict4',methods=['GET'])
def predict4():
    age = float(request.args.get('age'))
    AA=float(request.args.get('aa'))
    wc=float(request.args.get('wc'))
    mc=float(request.args.get('mc'))
    pt=float(request.args.get('pt'))
    vc=float(request.args.get('vc'))
    vp=float(request.args.get('vp'))
    av=float(request.args.get('av'))
    rf= float(request.args.get('repf'))
    wp=float(request.args.get('wp'))
    sex=float(request.args.get('sex'))


    model=pickle.load(open('naive.pkl','rb'))
    
    prediction = model.predict([[age,AA,wc,mc,pt,vc,vp,av,rf,wp,sex]])
    if prediction==0:
      message="Not Fraud"
    else:
      message="Fraud"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))

@app.route('/predict5',methods=['GET'])
def predict5():
    age = float(request.args.get('age'))
    AA=float(request.args.get('aa'))
    wc=float(request.args.get('wc'))
    mc=float(request.args.get('mc'))
    pt=float(request.args.get('pt'))
    vc=float(request.args.get('vc'))
    vp=float(request.args.get('vp'))
    av=float(request.args.get('av'))
    rf= float(request.args.get('repf'))
    wp=float(request.args.get('wp'))
    sex=float(request.args.get('sex'))


    model=pickle.load(open('linear.pkl','rb'))
    
    prediction = model.predict([[age,AA,wc,mc,pt,vc,vp,av,rf,wp,sex]])
    if prediction==0:
      message="Not Fraud"
    else:
      message="Fraud"
    
        
    return render_template('predict.html', prediction_text='Model  has predicted : {}'.format(message))



if __name__ == "__main__":
  app.run()


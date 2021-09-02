from flask import Flask,render_template,request
import pickle

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        myDict = request.form
        fever = float(myDict['fever'])
        DryCough = int(myDict['cough'])
        Fatigue = int(myDict['fatigue'])
        ChestPain = int(myDict['pain'])
        DiffBreath = int(myDict['diffbreath'])
        LossofTS = int(myDict['lossts'])
        inputFeatures = [fever,DryCough,Fatigue,ChestPain,DiffBreath,LossofTS]
        InfProb = clf.predict_proba([inputFeatures])[0][1]
        print(InfProb)
        return render_template('show.html', inf=round(InfProb*100))
    return render_template('index.html')
    
@app.route('/about/')
def about():
    return render_template('about.html')
    
@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/faqs/')
def faqs():
    return render_template('faqs.html')

@app.route('/contactus/')
def contactus():
    return render_template('contactus.html')

if __name__ == "__main__":
    app.run(debug=True)   
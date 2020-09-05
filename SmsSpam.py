from flask import Flask,render_template,request,redirect,url_for
import pickle
app=Flask(__name__)
fname1="F:\ML_Assignmnts\spam\spamsms"
infile2=open(fname1,"rb")
model1=pickle.load(infile2)
fname=r"F:\ML_Assignmnts\spam\vectorizer"
infile1=open(fname,"rb")
vectorizer=pickle.load(infile1)
@app.route("/",methods=["POST","GET"])
def pred():
    if request.method=="POST":
        sms=request.form["fname"]
        print(sms)
        print(type(sms))
        predict_sms=model1.predict(vectorizer.transform([sms]))
        print(predict_sms)
        print(predict_sms[0])
        if(predict_sms[0]==1):
            result=sms+" is spam"
        else:
            result=sms+" is ham"
        return redirect(url_for("user",usr=result))
    else:
        return render_template("pred.html")
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
if __name__=="__main__":
    app.run()

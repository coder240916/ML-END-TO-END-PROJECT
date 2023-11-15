from flask import Flask,render_template,jsonify,url_for,request
from src.DaimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictionObject

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def prediction():
    if request.method == 'GET':
        return render_template("form.html")
    else:
        data=CustomData(
            
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        data_df = data.get_data_as_dataframe()
        predicted = PredictionObject().predict_data(data_df)
        result = round(predicted[0],2)
        return render_template("result.html",final_result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
from flask import Flask
import mlApi
app=Flask(__name__)

app.register_blueprint(mlApi.mlApi,url_prefix="/flowers")

@app.route('/')
def check():
	return "OK"

if __name__=='__main__':
    app.run(debug=True)

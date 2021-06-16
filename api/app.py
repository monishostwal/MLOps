from flask import Flask
from mlApi import  mlApi
app=Flask(__name__)

app.register_blueprint(mlApi,url_prefix="/flowers")


if __name__=='__main__':
    app.run(debug=True)

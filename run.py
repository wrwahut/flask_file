# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:47:09 2018

@author: wangrenwei
"""

from flask import Flask, make_response, after_this_request, jsonify,send_file, send_from_directory, request

app = Flask(__name__)

@app.route("/download_file", methods=["POST", "GET"])
def download_file():
    response = make_response(send_file("temp/file.apk"))
    response.headers["Content-Disposition"] = "attachment; filename=file.apk;"
    return response
	
@app.route("/download_chaohuxueyuan", methods=["POST", "GET"])
def download_chaohuxueyuan():
    response = make_response(send_file("temp/chaohuxueyuan.apk"))
    response.headers["Content-Disposition"] = "attachment; filename=chaohuxueyuan.apk;"
    return response
	
@app.route("/download_chizhou", methods=["POST", "GET"])
def download_chizhou():
    response = make_response(send_file("temp/chizhou.apk"))
    response.headers["Content-Disposition"] = "attachment; filename=chizhou.apk;"
    return response

@app.route("/download", methods=["POST","GET"])
def download():
    return make_response(send_from_directory("data","temp/file.txt"))


@app.route("/index", methods=["POST","GET"])
def index():
    return jsonify({"re":"200","msg":"success","data":{}})

@app.route("/api", methods=["POST"])
def api():
    args = request.form
    print "#################args=",args
    billNo = args.get("billno","")
    text = """
    <xml>
    	<billNo>{billNo}</billNo>
	<status>OK</status>
    </xml>
    """.format(billNo = billNo)
    return text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 10001)

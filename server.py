from flask import Flask, redirect, request, url_for, render_template, jsonify
from models import hostScanner, portScanner, routeGetter, topoDrawer, vulFinder, webScanner
import os
from flask_cors import CORS

app = Flask(__name__, static_folder=os.path.abspath("./templates/"), static_url_path="")
CORS(app, resources={r"/*": {"origins": "*"}})

hostInfo = {}
hostList = []


@app.route('/topoList', methods=['post'])
def topoList():
    global hostInfo
    global hostList
    fromIp = request.json.get("fromIp")
    toIp = request.json.get("toIp")

    hostInfo = hostScanner.main(fromIp, toIp)
    hostList = list(hostInfo.keys())

    # testData = {
    #         "nodesArray": [
    #             {"id": "192.168.1.1", "label": "192.168.1.1"},
    #             {"id": "192.168.1.2", "label": "192.168.1.2"},
    #             {"id": "192.168.1.3", "label": "192.168.1.3"},
    #             {"id": "192.168.1.4", "label": "192.168.1.4"}
    #         ],
    #         "edgesArray": [
    #             {"from": "192.168.1.1", "to": "192.168.1.1"},
    #             {"from": "192.168.1.2", "to": "192.168.1.1"},
    #             {"from": "192.168.1.3", "to": "192.168.1.1"},
    #             {"from": "192.168.1.4", "to": "192.168.1.1"},
    #             {"from": "192.168.1.3", "to": "192.168.1.3"},
    #             {"from": "192.168.1.3", "to": "192.168.1.2"}
    #
    #         ]
    #     }
    nodesArray = []
    for ipA in hostList:
        ipObj = {"id": ipA, "label": ipA}
        nodesArray.append(ipObj)
    edgesArray = routeGetter.main(hostList)

    return {"nodesArray": nodesArray, "edgesArray": edgesArray}


@app.route('/basicInform', methods=['post'])
def basicInform():
    # global hostInfo
    # inAddress = request.json.get("inAddress")
    # basicList = hostInfo[inAddress]
    #
    # data = {"basicInform": {"hostname": basicList[0], "mac_address": basicList[1], "vendor": basicList[2],
    #                         "delay": basicList[3]}}

    testData = {
        "basicInform": {
            "hostname": "xx231xx",
            "mac_address": "133xxx",
            "vendor": "x32332xxx",
            "delay": "xx23xx"
        }
    }
    return testData


@app.route('/appInform', methods=['post'])
def appInform():
    # inAddress = request.json.get("inAddress")
    # portList = portScanner.main(inAddress)
    # appInformList = []
    # for port in portList:
    #     appInformItem = appScanner.main([inAddress, port])
    #     appInformItem["port"] = port
    #     appInformList.append(appInformItem)

    testData = {
        "appInform": [{"port": 22,
                       "service": "ssh",
                       "version": "openssh 2.3.3"
                       }, {
                          "port": 23,
                          "service": "ssh",
                          "version": "openssh 2.3.3"
                      }, {
                          "port": 24,
                          "service": "ssh",
                          "version": "openssh 2.3.3"
                      }, {
                          "port": 25,
                          "service": "ssh",
                          "version": "openssh 2.3.3"
                      }
                      ]
    }
    return testData


@app.route('/webInform', methods=['post'])
def webInform():
    # inAddress = request.json.get("inAddress")
    # portList = portScanner.main(inAddress)
    # return webScanner.main(inAddress, portList)
    testData = {
        "webInform": [
            {
                "port": "22",
                "cdn": "cdnxxxx",
                "cms": "cmsxxxx",
                "framework": "frameworkxxxx",
                "frontend": "frontendxxxx",
                "lang": "langxxx",
                "server": "serverxxxx",
                "system": "systemxxxx",
                "waf": "wafxxxx"
            },
            {
                "port": "80",
                "cdn": "cdnxxxx",
                "cms": "cmsxxxx",
                "framework": "frameworkxxxx",
                "frontend": "frontendxxxx",
                "lang": "langxxx",
                "server": "serverxxxx",
                "system": "systemxxxx",
                "waf": "wafxxxx"
            },
            {
                "port": "9999",
                "cdn": "cdnxxxx",
                "cms": "cmsxxxx",
                "framework": "frameworkxxxx",
                "frontend": "frontendxxxx",
                "lang": "langxxx",
                "server": "serverxxxx",
                "system": "systemxxxx",
                "waf": "wafxxxx"
            },
        ]}
    return testData


@app.route('/findVul', methods=['post'])
def findVul():
    inKeywordList = request.json.get("keyword")
    vulList = []
    for keyword in inKeywordList:
        vulList.extend(vulFinder.main(keyword))
    return vulList


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

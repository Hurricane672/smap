from flask import Flask, redirect, request, url_for, render_template, jsonify
from models import hostScanner, portScanner, routeGetter, topoDrawer, vulFinder, webScanner, appScanner
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

    nodesArray = []
    for ipA in hostList:
        ipObj = {"id": ipA, "label": ipA}
        nodesArray.append(ipObj)
    nodesArray.append({"id": '127.0.0.1', "label": '127.0.0.1'})
    print("hhhhhhhhhhhhllllllll:")
    print(hostList)
    edgesArray = routeGetter.main(hostList)

    print(edgesArray)
    for edge in edgesArray:
        # print(edge)
        # print(type(edge))
        if (edge["to"] not in hostList):
            hostList.append(edge["to"])
            nodesArray.append({"id": edge["to"], "label": edge["to"]})

    return {"nodesArray": nodesArray, "edgesArray": edgesArray}


@app.route('/basicInform', methods=['post'])
def basicInform():
    global hostInfo
    ipAddress = request.json.get("ipAddress")
    basicList = hostInfo[ipAddress]

    data = {"basicInform": {"hostname": basicList[0], "mac_address": basicList[1], "vendor": basicList[2],
                            "delay": basicList[3]}}
    return data


@app.route('/appInform', methods=['post'])
def appInform():
    ipAddress = request.json.get("ipAddress")
    portList = portScanner.main(ipAddress)
    appInformList = []
    for port in portList:
        appInformItem = appScanner.main([ipAddress, port])
        appInformItem2 = {}
        appInformItem2["port"] = port
        appInformItem2.update(appInformItem)
        appInformList.append(appInformItem2)
    print(appInformList)
    return {"appInform": appInformList}


@app.route('/webInform', methods=['post'])
def webInform():
    ipAddress = request.json.get("ipAddress")
    portList = portScanner.main(ipAddress)

    result = webScanner.main(ipAddress, portList, 1)
    print("rrrrrrrrrrrrrrrwebsult")
    print(result)
    return {"webInform": result}


@app.route('/findVul', methods=['post'])
def findVul():
    inKeywordList = request.json.get("keywords")
    vulList = []
    for keyword in inKeywordList:
        vulItem = vulFinder.main(keyword)
        # print(vulItem)
        for vulItemItem in vulItem:
            vulItem2 = {'cve_id': vulItemItem[0], 'info': vulItemItem[1], 'date': vulItemItem[2]}
            vulList.append(vulItem2)
    print("vulllllllllllllllll")
    print(vulList)
    return {'vuls': vulList}


# ---------------------------------------------


# @app.route('/topoList', methods=['post'])
# def topoList():
#
#     testData = {
#             "nodesArray": [
#                 {"id": "192.168.1.1", "label": "192.168.1.1"},
#                 {"id": "192.168.1.2", "label": "192.168.1.2"},
#                 {"id": "192.168.1.3", "label": "192.168.1.3"},
#                 {"id": "192.168.1.4", "label": "192.168.1.4"}
#             ],
#             "edgesArray": [
#                 {"from": "192.168.1.1", "to": "192.168.1.1"},
#                 {"from": "192.168.1.2", "to": "192.168.1.1"},
#                 {"from": "192.168.1.3", "to": "192.168.1.1"},
#                 {"from": "192.168.1.4", "to": "192.168.1.1"},
#                 {"from": "192.168.1.3", "to": "192.168.1.3"},
#                 {"from": "192.168.1.3", "to": "192.168.1.2"}
#
#             ]
#         }
#     return testData
# #
# #
# @app.route('/basicInform', methods=['post'])
# def basicInform():
#
#     testData = {
#         "basicInform": {
#             "hostname": "xx2323231xx",
#             "mac_address": "132323xxx",
#             "vendor": "x3223332xxx",
#             "delay": "xx2322323xx"
#         }
#     }
#     return testData
#
# #
# @app.route('/appInform', methods=['post'])
# def appInform():
#
#     # testData = {
#     #     "appInform": [{"port": 252,
#     #                    "service": "ssjjjjjjjjjjjjjjjjjh",
#     #                    "version": "openssh 2.3.3"
#     #                    }, {
#     #                       "port": 2223,
#     #                       "service": "sssssssssssssh",
#     #                       "version": "openssh 2.3.3"
#     #                   }, {
#     #                       "port": 24,
#     #                       "service": "ssssssssssssssssh",
#     #                       "version": "openssh 2.3.3"
#     #                   }, {
#     #                       "port": 25,
#     #                       "service": "ssh",
#     #                       "version": "openssh 2.3.3"
#     #                   }
#     #                   ]
#     # }
#     testData = [{'port': 7, 'service': 'echo', 'version': ''}, {'port': 9, 'service': 'discard', 'version': ''},
#      {'port': 13, 'service': 'daytime', 'version': ''}, {'port': 17, 'service': 'qotd', 'version': ''},
#      {'port': 19, 'service': 'chargen', 'version': ''}, {'port': 80, 'service': 'http', 'version': '1.1'},
#      {'port': 135, 'service': 'msrpc', 'version': 'Microsoft Windows RPC'},
#      {'port': 139, 'service': 'netbios-ssn', 'version': 'Microsoft Windows netbios-ssn'},
#      {'port': 443, 'service': 'http', 'version': '1.1'}, {'port': 445, 'service': 'microsoft-ds', 'version': ''},
#      {'port': 903, 'service': 'ssl/vmware-auth', 'version': '1.10'}, {'port': 5000, 'service': 'upnp', 'version': ''}]
#
#     return testData
# #
# #
# @app.route('/webInform', methods=['post'])
# def webInform():
#     testData ={"webInform":[{'port': 7, 'service': 'echo', 'version': ''}, {'port': 9, 'service': 'discard', 'version': ''}, {'port': 13, 'service': 'daytime', 'version': ''}, {'port': 17, 'service': 'qotd', 'version': ''}, {'port': 19, 'service': 'chargen', 'version': ''}, {'port': 80, 'service': 'http', 'version': '1.1'}, {'port': 135, 'service': 'msrpc', 'version': 'Microsoft Windows RPC'}, {'port': 139, 'service': 'netbios-ssn', 'version': 'Microsoft Windows netbios-ssn'}, {'port': 443, 'service': 'http', 'version': '1.1'}, {'port': 445, 'service': 'microsoft-ds', 'version': ''}, {'port': 903, 'service': 'ssl/vmware-auth', 'version': '1.10'}, {'port': 5000, 'service': 'upnp', 'version': ''}]}
#     # testData = {
#     #     "webInform": [
#     #         {
#     #             "port": "225555555555555",
#     #             "cdn": "cdnx232xxx",
#     #             "cms": "cmsxxxx",
#     #             "framework": "frame23workxxxx",
#     #             "frontend": "fronte23ndxxxx",
#     #             "lang": "langxxx",
#     #             "server": "serverxxxx",
#     #             "system": "systemxxxx",
#     #             "waf": "wafxxxx"
#     #         },
#     #         {
#     #             "port": "80",
#     #             "cdn": "cdnxxxx",
#     #             "cms": "cmsxxxx",
#     #             "framework": "f33rameworkxxxx",
#     #             "frontend": "fro33ntendxxxx",
#     #             "lang": "langxxx",
#     #             "server": "serverxxxx",
#     #             "system": "systemxxxx",
#     #             "waf": "wafxxxx"
#     #         },
#     #         {
#     #             "port": "9999",
#     #             "cdn": "cdnxxxx",
#     #             "cms": "cmsxx32xx",
#     #             "framework": "frameworkxxxx",
#     #             "frontend": "frontendxxxx",
#     #             "lang": "langxxx",
#     #             "server": "serverxxxx",
#     #             "system": "systemxxxx",
#     #             "waf": "wafxxxx"
#     #         },
#     #     ]}
#     return testData
# #
# #
# @app.route('/findVul', methods=['post'])
# def findVul():
#
#     testData = {
#         'vuls': [
#             {
#                 'cve_id': "CV对方E-2022-34305",
#                 'info': 'Apache Tomcat 跨站脚豆腐干地方本漏洞（CVE-2022-34305）',
#                 'date': '2022-06-24'
#             },
#             {
#                 'cve_id': "CVE-202豆腐干地方-34305",
#                 'info': 'Apache Tomcat 跨站脚到底本漏洞（CVE-2022-34305）',
#                 'date': '2022-06的风格-24'
#             }
#         ],
#     }
#     return testData

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

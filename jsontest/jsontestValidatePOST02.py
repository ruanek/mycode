#!/usr/bin/python3

import requests

TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com/"

def main():
    resp = requests.get(TIMEURL)
    mytime = resp.json()
    mytime = mytime["time"].replace(" ", "").replace(":", "-")

    resp = requests.get(IPURL)
    myip = resp.json()
    print(myip)
    myip = myip["ip"]

    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)

    resp = requests.post(VALIDURL, data=mydata)
    respjson = resp.json()
    print(respjson)

    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()


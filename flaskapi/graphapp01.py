#!/usr/bin/python3

import numpy as np 
import yaml 
import re  
import paramiko 
from flask import Flask, render_template
import matplotlib.pyplot as plt

def sshlogin(ip, un, passw):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname=ip, username=un, password=passw)
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command("cat /proc/uptime")
    sshresult = ssh_stdout.read().decode('utf-8').split()[0]
    with open("sshresult", "w") as myfile:
        myfile.write(sshresult)
    days = (int(float(sshresult)) / 86400)  
    sshsession.close()
    print(days)
    return days

app = Flask(__name__)

@app.route("/graphin")
def graphin():
    with open("/home/student/sshpass.yml") as sshpass: 
        creds = yaml.load(sshpass)
    svruptime = []
    xtick = []
    for cred in creds:
        xtick.append(cred['ip'])
        resp = sshlogin(cred['ip'], cred['un'], cred['passw'])
        svruptime.append(resp)
    xtick = tuple(xtick) 
    svruptime = tuple(svruptime)

    N = 2 
    ind = np.arange(N)
    width = 0.35 
    p1 = plt.bar(ind, svruptime, width)

    plt.ylabel('Uptime in Days')

    plt.title('Uptime of Servers in Days')
    plt.xticks(ind, xtick)
    plt.yticks(np.arange(0, 20, 1)) 

    plt.savefig('static/status.png') 
    return render_template("graph.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)



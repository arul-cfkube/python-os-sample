import os
import platform
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    os_version="18.04.6 LTS (Bionic Beaver)"
    with open('/etc/os-release', 'r') as f:
        if 'Jammy' in f.read():
            os_version="22.04.1 LTS (Jammy Jellyfish)"
            print(f.read())
    print(os_version)
    return render_template('index.html', os=os_version)

if __name__ == '__main__':
    app.run()

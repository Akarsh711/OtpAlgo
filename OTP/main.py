from flask import Flask, render_template, request
import random
import time
from threading import Thread

app = Flask(__name__)
FLAG = ''

def OTP_verification():
    global FLAG
    #time.sleep(5)
    FLAG = '1'
    

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ph = request.form.get('ph')
        x = str(random.random())
        otp = x[2:8]
        print(otp)
        obj = Thread(target=OTP_verification)
        obj.start()
        
        #print('going to sleep')
        time.sleep(9)
        if(FLAG):
            print('flag is 1')
            return otp
        else:
            print('flag is none' )
             #user not verified
        print('waked up')
        return 'otp failed'
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)

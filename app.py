import numpy as np
from flask import Flask, request, jsonify, render_template
import yaml
import subprocess



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start',methods=['POST'])
def start_applying():
    '''
    For rendering results on HTML GUI
    '''
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Update the configuration with the request parameters
    config['email'] = list(request.form.values())[0]
    config['password'] = list(request.form.values())[1]

    # Write the updated configuration back to the config file
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

    # Run the Python program with the updated configuration using subprocess
    try:
        subprocess.run(['python3', 'main.py'], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur while running the program
        return f'Error: {e}', 500

    #output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='successfully appplied jobs. Download the log files to check the details')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=8000)
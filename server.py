from flask import Flask,send_from_directory
import dict_builder
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)


def csv_text(file_name):
    return open(file_name,'r').read()


#Class Material
@app.route('/classes')
def classes():
    #get current info on classes from csv
    text = csv_text('ClassesInfo.csv')
    info = dict_builder.constructJson(text)
    #Display the page
    loader = FileSystemLoader('Templates')
    env = Environment(loader=loader)
    template = env.get_template('classes.html')
    return (template.render(moduleDict = info))
@app.route('/Images/<image_name>')
def Images(image_name):
    return send_from_directory('Images', image_name)
@app.route('/Styling/<style_name>')
def Styling(style_name):
    return send_from_directory('style',style_name)
app.run(host='0.0.0.0', port=5001)
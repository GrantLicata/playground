from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def initalize_boxes():
    return render_template('index.html', box_count = 3, color = 'lightblue')

@app.route('/play/<int:num>')
def new_boxes(num):
    return render_template('index.html', box_count = num, color = 'lightblue')

@app.route('/play/<int:num>/<string:color>')
def new_colors(num,color):
    return render_template('index.html', box_count = num, box_color = color)

if __name__=="__main__":
    app.run(debug=True)
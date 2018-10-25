from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Open the URL in another tab, and then go to /hello/yourname'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello '+ name + '!'

@app.route('/square/<int:num>')
def sqr(num):
    return str(num ** 2)

def factors(num):
    return [x for x in range(1, num+1) if num%x==0]

@app.route("/factors/<int:nums>")
def facts(nums):
    return "The factors of {} are {}".format(nums, factors(nums))

@app.route("/factors_raw/<int:n>")
def factors_display_raw_html(n):
    factor_list = factors(n)
    html = "<h1> The factors of " + str(n) +" are </h1>" + "\n" + "<ul>"
    for f in factor_list:
        html += "<li>" + str(f) + "</li>" + "\n"
    html += "</ul> </body>"
    return html

@app.route("/factors_display/<int:n>")
def factors_display(n):
    return render_template(
        "factors.html", number=n,factors=factors(n)
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
from flask import Flask, render_template, request
app = Flask(__name__)
def cod_kraini(phone_number):
    country_codes = {'380': 'Украина','44': 'Англия','33': 'Франциа','81': 'Япония','86': 'Китай'}
    country_code = phone_number[:3]
    country_name = country_codes.get(country_code, 'непонятно')
    return country_name
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phonenumber = request.form['phone_number']
        country = cod_kraini(phonenumber)
        return render_template('resultad.html', phone_number=phonenumber, country_name=country)
    return render_template("honenumber.html")
if __name__ == '__main__':
    app.run(debug=True)
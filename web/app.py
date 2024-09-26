from flask import Flask, request, redirect, jsonify, make_response, send_from_directory, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
#如果账号密码相同即可登录
    if username == password:
        resp = make_response(jsonify({"success": True}))
        resp.set_cookie('username', username)
        return resp
    else:
        return jsonify({"success": False})

@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('username')
    return resp

@app.route('/dashboard')
def dashboard():
    username = request.cookies.get('username')
    if username:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/screen1')
def screen1():
    username = request.cookies.get('username')
    if username:
        return send_from_directory('static/screen1', 'screen1.html')
    else:
        return redirect('/')

@app.route('/screen2')
def screen2():
    username = request.cookies.get('username')
    if username:
        return send_from_directory('static/screen2', 'screen2.html')
    else:
        return redirect('/')

@app.route('/check_login')
def check_login():
    username = request.cookies.get('username')
    if username:
        return jsonify({"logged_in": True, "username": username})
    else:
        return jsonify({"logged_in": False})

if __name__ == '__main__':
    app.run(debug=True)

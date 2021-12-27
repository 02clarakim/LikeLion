from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.likelion                      # 'likelion'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/customers', methods=['POST'])
def enter_info():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    amount_receive = request.form['amount_give']
    phone_receive = request.form['phone_give']

    customer = {
        'name': name_receive, 
        'address': address_receive,
        'amount': amount_receive,
        'phone': phone_receive
    }
    db.customers.insert_one(customer)
    return jsonify({'result':'success', 'msg': '주문 입력 완료!'})


@app.route('/customers', methods=['GET'])
def get_info():
    customers = list(db.customers.find({},{'_id':0}))
    return jsonify({'result':'success', 'customers': customers})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
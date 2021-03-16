from flask import Flask, request, jsonify
import pymongo as mongo
import requests
from bs4 import BeautifulSoup

def crawlingFunId(url, tag, tag_property) :
    print('id입니다.')
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find(f'{tag}', id=f'{tag_property}')

    return result.text

def crawlingFunClass(url, tag, tag_property) :
    print('class입니다.')
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.findAll(f'{tag}', attrs={'class' : f'{tag_property}'})

    return result[0].text

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/crawling/<property_type>', methods=['POST'])
def userFun(property_type) :
    client = mongo.MongoClient('mongodb://localhost:27017/')
    db = client.crawling_list
    collection = db.crawlings

    url, tag, tag_property = request.form['url'], request.form['tag'], request.form['tag_property']

    if url is None or tag is None or tag_property is None :
        return '값이 누락되었습니다.'

    result = ''

    if (property_type == 'class') :
        result = crawlingFunClass(url, tag, tag_property)
    else :
        result = crawlingFunId(url, tag, tag_property)

    data = {f'{tag_property}' : f'{result}'}

    insertData = collection.insert_one(data).inserted_id
    client.close()

    return jsonify(crawlingData=result)

if __name__ == '__main__' :
    app.run(port=8000, debug=True)
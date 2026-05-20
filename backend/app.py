# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Ön yüzün API'ye erişebilmesi için CORS izinlerini açıyoruz.

@app.route('/api/student', methods=['GET'])
def get_student():
    # Proje gereksinimlerine uygun JSON çıktısı
    return jsonify({
        "ogrenci_no": "b221200383",
        "ad": "Deniz",
        "soyad": "Denizcan"
    })

if __name__ == '__main__':
    # Container dışından erişilebilmesi için 0.0.0.0 portunda çalıştırıyoruz
    app.run(host='0.0.0.0', port=5000)
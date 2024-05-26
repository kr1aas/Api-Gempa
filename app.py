from flask import Flask, jsonify
import json

app = Flask(__name__)

# Path ke file JSON lokal
JSON_FILE_PATH = 'GempaDirasaka.json'

@app.route('/GempaDirasakan', methods=['GET'])
def get_new_api_data():
    try:
        # Membaca data dari file JSON
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Memproses data sesuai kebutuhan Anda
        processed_data = process_data(data)
   
        return jsonify(processed_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def process_data(data):
    # Memproses data untuk mengambil nilai 'name' dan 'value' dari setiap item dalam 'gempa'
    if "Infogempa" in data and "gempa" in data["Infogempa"]:
        gempa_items = data["Infogempa"]["gempa"]
        if isinstance(gempa_items, list):
            first_ten_items = gempa_items[:10]
            result = [{"Tanggal": item["Tanggal"], "Jam": item["Jam"], "Wilayah": item["Wilayah"],"Kedalaman": item["Kedalaman"],"Coordinates": item["Coordinates"]} for item in first_ten_items]
            return {"items": result}
    return {"items": []}

if __name__ == '__main__':
    app.run(debug=True)
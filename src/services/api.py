from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from csvFunctions import createCSV


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Dados de exemplo (geralmente você usaria um banco de dados)
items = []

# Rota para criar um novo item
@app.route('/', methods=['POST'])
@cross_origin()
def create_item():
    data = [request.get_json()]

    csvData = createCSV(data, "newData.csv")

    if csvData:
       
       return jsonify({'sucesso': 'Caio é viado'}), 200
    else:
        return jsonify({'error': 'Nome é obrigatório'}), 400


if __name__ == '__main__':
    app.run(debug=True)
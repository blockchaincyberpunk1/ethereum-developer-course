# app.py
from flask import Flask, render_template
from web3 import Web3

app = Flask(__name__)

# Initialize Web3 with your Infura API key
infura_url = "https://mainnet.infura.io/v3/e8f0682204f74f9fbd1fce2f52199a64"  # Replace with your Infura API key
w3 = Web3(Web3.HTTPProvider(infura_url))

@app.route('/')
def index():
    # Retrieve blockchain data here using web3.py
    latest_block_number = w3.eth.block_number
    gas_price = w3.eth.gas_price

    return render_template('index.html', latest_block_number=latest_block_number, gas_price=gas_price)

if __name__ == '__main__':
    app.run(debug=True)

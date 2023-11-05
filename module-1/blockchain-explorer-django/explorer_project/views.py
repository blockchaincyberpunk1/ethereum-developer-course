from django.shortcuts import render
from web3 import Web3

def index(request):
    # Initialize Web3 with your Infura API key
    infura_url = "https://mainnet.infura.io/v3/e8f0682204f74f9fbd1fce2f52199a64"  # Replace with your Infura API key
    w3 = Web3(Web3.HTTPProvider(infura_url))

    # Retrieve blockchain data here using web3.py
    latest_block_number = w3.eth.block_number
    gas_price = w3.eth.gas_price

    context = {
        'latest_block_number': latest_block_number,
        'gas_price': gas_price,
    }

    return render(request, 'index.html', context)

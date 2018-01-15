#!/usr/bin/python

import requests
from datetime import datetime
import json

class ApiEndpointError(Exception):
    def __init__(self, errormsg):
        self.errormsg = errormsg

    def __str__(self):
        return repr(self.errormsg)

class CryptoTracker:
    def __init__(self):
        self.url = 'https://api.coinmarketcap.com/v1/ticker'
        self.request = requests.get(self.url)
        self.bitcoin = None
        self.ethereum = None
        self.ripple = None
        self.litecoin = None
        self.tron = None

    def verify_endpoint_connection(self):
        return self.request.status_code == requests.codes.ok

    def get_api_data(self):
        if self.verify_endpoint_connection():
            return json.loads(self.request.text)
        else:
            raise ApiEndpointError('ERROR: Could not connect to API endpoint.')

    def set_crypto_data(self):
        for crypto in self.get_api_data():
            if crypto['id'] == 'bitcoin':
                self.bitcoin = crypto

            if crypto['id'] == 'ethereum':
                self.ethereum = crypto

            if crypto['id'] == 'ripple':
                self.ripple = crypto

            if crypto['id'] == 'litecoin':
                self.litecoin = crypto

            if crypto['id'] == 'tron':
                self.tron = crypto

    def write_data(self, filename):
        try:
            with open(filename, 'w') as file_:
                file_.write('Time: ' + str(datetime.now()) + '\n')
                file_.write('Bitcoin price: ' +
                            str(self.bitcoin['price_usd'])+ '\n')
                file_.write('Ethereum price: ' +
                            str(self.ethereum['price_usd'])+ '\n')
                file_.write('Ripple price: ' +
                            str(self.ripple['price_usd'])+ '\n')
                file_.write('Litecoin price: ' +
                            str(self.litecoin['price_usd'])+ '\n')
                file_.write('Tron price: ' +
                            str(self.tron['price_usd'])+ '\n')

        except IOError:
            raise IOError('ERROR: Could not open/write data.')

a = CryptoTracker()
a.set_crypto_data()
a.write_data('crypto_data.txt')

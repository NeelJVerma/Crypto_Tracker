"""
This is a tracker for cryptocurrencies. It only tracks the prices of 5 right
now, but I plan to add more.
"""

import requests
from datetime import datetime
import json

class ApiEndpointError(Exception):
    """
    ApiEndpointError class. This class is used to raise an error with
    connecting to the API endpoint.

    Attributes:
        errormsg: The error message to be displayed.
    """

    def __init__(self, errormsg):
        """
        Initializes the class with an error message.

        Args:
            errormsg: The error message to be displayed.

        Returns:
            Nothing.
        """

        self.errormsg = errormsg

    def __str__(self):
        """
        Converts the class to a string for printing purposes.

        Args:
            None.

        Returns:
            Nothing.
        """

        return repr(self.errormsg)

class CryptoTracker:
    """
    CryptoTracker class. This class is responsible for connecting to the API
    endpoint and recording data on various cryptocurrencies.

    Attributes:
        url: The API endpoint url.
        request: The object that holds get request data from the endpoint.
        bitcoin: Holds information about bitcoin.
        ethereum: Holds information about ethereum.
        ripple: Holds information about ripple.
        litecoin: Holds information about litecoin.
        tron: Holds information about tron.
    """

    def __init__(self):
        """
        Initializes the class with all its attributes.

        Args:
            None.

        Returns:
            Nothing.
        """

        self.url = 'https://api.coinmarketcap.com/v1/ticker'
        self.request = requests.get(self.url)
        self.bitcoin = None
        self.ethereum = None
        self.ripple = None
        self.litecoin = None
        self.tron = None

        self.set_crypto_data()

    def verify_endpoint_connection(self):
        """
        Verifies whether or not the endpoint was connected to successfully.

        Args:
            None.

        Returns:
            Returns true if the endpoint was successfully connected to, false
            otherwise.
        """

        return self.request.status_code == requests.codes.ok

    def get_api_data(self):
        """
        Gets the api data from the endpoint.

        Args:
            None.

        Returns:
            Returns the parsed json if the connection to the endpoint was
            successful, otherwise raises an error.

        Raises:
            ApiEndpointError: If the connection to the endpoing was
            unsuccessful.
        """

        if self.verify_endpoint_connection():
            return json.loads(self.request.text)
        else:
            raise ApiEndpointError('ERROR: Could not connect to API endpoint.')

    def set_crypto_data(self):
        """
        Sets class attributes with the appropriate crypto data.

        Args:
            None.

        Returns:
            Nothing.
        """

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
        """
        Writes crypto data to a file.

        Args:
            filename: The name of the file to write to.

        Returns:
            Nothing.

        Raises:
            IOError: If the file could not be opened or written to.
        """

        try:
            with open(filename, 'w') as file_:
                file_.write('Time: ' + str(datetime.now()) + '\n')
                file_.write('Bitcoin price: ' +
                            str(self.bitcoin['price_usd']) + '\n')
                file_.write('Ethereum price: ' +
                            str(self.ethereum['price_usd']) + '\n')
                file_.write('Ripple price: ' +
                            str(self.ripple['price_usd']) + '\n')
                file_.write('Litecoin price: ' +
                            str(self.litecoin['price_usd']) + '\n')
                file_.write('Tron price: ' +
                            str(self.tron['price_usd']) + '\n')
        except IOError:
            raise IOError('ERROR: Could not open or write data.')

"""
This file converts one crypto to another crypto (or usd).
"""

import CryptoTracker

class Converter:
    """
    Converter class. This class will convert one crypto to another.

    Attributes:
        coinfrom: The coin to convert from.
        cointo: The coin to convert to.
        availablecryptos: A set of all available cryptocurrencies.
    """

    def __init__(self, coinfrom, cointo):
        """
        This method initializes the class with a source coin and a destination
        coin.

        Args:
            coinfrom: The value to set the coinfrom attribute with.
            cointo: The value to set the cointo attribute with.

        Returns:
            Nothing.
        """

        self.coinfrom = coinfrom
        self.cointo = cointo

    def convert(self, amountfrom):
        """
        Converts coinfrom into cointo.

        Args:
            amountfrom: The amount of coinfrom to convert.

        Returns:
            The float value of the converted crypto.

        Raises:
            ValueError: If coinfrom or cointo is not a valid coin.
        """

        cryptotracker = CryptoTracker.CryptoTracker()
        availablecryptos = set()
        apidata = cryptotracker.get_api_data()

        for crypto in apidata:
            availablecryptos.add(crypto['id'])

        if self.coinfrom not in availablecryptos:
            raise ValueError('ERROR \'{0}\' is not an available crypto.'.format(self.coinfrom))

        if self.cointo not in availablecryptos and self.cointo != 'usd':
            raise ValueError('ERROR. Cannot convert to \'{0}\'.'.format(self.cointo))

        if self.cointo == 'bitcoin' or self.cointo == 'usd':
            for crypto in apidata:
                if crypto['id'] == self.coinfrom:
                    if self.cointo == 'bitcoin':
                        return amountfrom * float(crypto['price_btc'])
                    else:
                        return amountfrom * float(crypto['price_usd'])

        coinfrombitcoin = None
        cointobitcoin = None

        for crypto in apidata:
            if crypto['id'] == self.coinfrom:
                coinfrombitcoin = amountfrom * float(crypto['price_btc'])

            if crypto['id'] == self.cointo:
                cointobitcoin = float(crypto['price_btc'])

        return coinfrombitcoin / cointobitcoin



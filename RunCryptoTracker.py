"""
This file runs the crypto tracker. It is meant to be run as a cron job.
"""

#!/usr/bin/python3

import CryptoTracker

if __name__ == '__main__':
    cryptotracker = CryptoTracker.CryptoTracker()
    cryptotracker.write_data('crypto_data.txt')

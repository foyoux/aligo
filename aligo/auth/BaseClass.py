"""..."""
import binascii
import logging
import os
import tempfile
from typing import NoReturn

import matplotlib.pyplot as plt
import qrcode
import qrcode_terminal
import requests
import rsa


class BaseClass:
    """..."""

    @classmethod
    def _show_console(cls, qr_link: str) -> NoReturn:
        """
        show qrcode on console
        :param qr_link: qrcode link
        :return: NoReturn
        """
        qrcode_terminal.draw(qr_link)

    @classmethod
    def _show_plt(cls, qr_link: str) -> NoReturn:
        """
        show qrcode by matplotlib
        :param qr_link: qrcode link
        :return: NoReturn
        """
        qr_img = qrcode.make(qr_link)
        plt.imshow(qr_img)
        plt.show()

    @classmethod
    def _show_windows(cls, qr_link: str) -> NoReturn:
        """
        show qrcode by Associated application of *.png
        :param qr_link: qrcode link
        :return: NoReturn
        """
        qr_img = qrcode.make(qr_link)
        png = tempfile.mktemp('.png')
        qr_img.save(png)
        os.startfile(png)

    @classmethod
    def _debug_log(cls, response: requests.Response) -> NoReturn:
        """..."""
        r = response.request
        logging.debug(f'[method status_code] {r.method} {response.status_code}')
        logging.debug(f'[url] {r.url}')
        logging.debug(f'[headers] {r.headers}')
        logging.debug(f'[request body] {r.body}')
        logging.debug(f'[response body] {response.text}')

    @classmethod
    def _error_log_exit(cls, response: requests.Response) -> NoReturn:
        """..."""
        cls._debug_log(response)
        exit(-1)

    @classmethod
    def _rsa_password(cls, password: str) -> str:
        """
        RSA algorithm encryption
        :param password: clear text password
        :return:
        """
        # "rsaExponent": "10001",
        # "rsaModulus": "d3bcef1f00424f3261c89323fa8cdfa12bbac400d9fe8bb627e8d27a44bd5d59dce559135d678a8143beb5b8d7056c4e1f89c4e1f152470625b7b41944a97f02da6f605a49a93ec6eb9cbaf2e7ac2b26a354ce69eb265953d2c29e395d6d8c1cdb688978551aa0f7521f290035fad381178da0bea8f9e6adce39020f513133fb",
        e = int('10001', 16)
        n = int(
            'd3bcef1f00424f3261c89323fa8cdfa12bbac400d9fe8bb627e8d27a44bd5d59dce559135d678a8143beb5b8d7056c4e1f89c4e1f152470625b7b41944a97f02da6f605a49a93ec6eb9cbaf2e7ac2b26a354ce69eb265953d2c29e395d6d8c1cdb688978551aa0f7521f290035fad381178da0bea8f9e6adce39020f513133fb',
            16)
        pk = rsa.PublicKey(n, e)
        rt = rsa.encrypt(password.encode(), pk)
        return binascii.hexlify(rt).decode()

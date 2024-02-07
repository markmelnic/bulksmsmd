<div align="center">

# `bulksmsmd` - Python wrapper for Unifun BulkSMSAPI (bulksms.md)

![Python Versions](https://pypi-camo.freetls.fastly.net/663448f90f103babe3b8b9dc15965ec36915dd58/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f70796261646765732e737667)
![PyPI Version](https://img.shields.io/pypi/v/bulksmsmd.svg)
![License](https://img.shields.io/pypi/l/bulksmsmd.svg)

Condsider the official documentation before using this package or to understand the more advanced options __dlrurl__, __dlrmask__, __charset__ and __coding__.

[2021 Official documentation .DOCX](https://github.com/markmelnic/bulksmsmd/blob/main/res/docs_2021.docx)

[2021 Official documentation .PDF](https://github.com/markmelnic/bulksmsmd/blob/main/res/docs_2021.pdf)

</div>

## Installation

Installation is done using the following command:

    pip install bulksmsmd

## Usage

The `username` and `password` are the credentials for the API. The `sender` is the name of the sender.

    client = SMSClient(
        username = 'username',
        password = 'password',
        sender = 'sender',
        proxy = {
            'http': 'http://PROXY_URL,
            'https': 'https://PROXY_URL',
        }
    )

The `client` object is used to send messages and contains two methods: `send_sms_simple` & `send_sms_nde`.

    client.send_sms_simple(
        msisdn = '69123456',
        body = 'Test message.',
        prefix = '373',
    )

    client.send_sms_nde(
        msisdn = '69123456',
        body = 'Test message.',
        prefix = '373',
        dlr_url = 'https://example.com/dlr',
        dlr_mask = '31',
        charset = 'utf8',
        coding = '2',
    )

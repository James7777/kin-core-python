# -*- coding: utf-8 -*

# Copyright (C) 2018 Kin Foundation

from stellar_base.asset import Asset

from .version import __version__


KIN_ISSUER_PROD = 'GBO3QRFN5Y5CDZMVEKNDOWSAJVDOXQ7KXREKOLFDOME4MGNH7W33FB3F'  # TODO: real address
KIN_ASSET_PROD = Asset('UGX', KIN_ISSUER_PROD)

KIN_ISSUER_TEST = 'GCE4QWCIJLYOQS5QU2Z2HXF7HPUXCOTIORVITHJVI53EEMQRN4DRQZXL'
KIN_ASSET_TEST = Asset('UGX', KIN_ISSUER_TEST)

# https://www.stellar.org/developers/guides/concepts/fees.html
BASE_RESERVE = 0.5  # in XLM
MIN_ACCOUNT_BALANCE = (2 + 1) * BASE_RESERVE  # 1 additional trustline op

SDK_USER_AGENT = 'kin-stellar-python/{}'.format(__version__)

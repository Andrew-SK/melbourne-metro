""" Interface with PTV swagger API. """


import os


BASE_URL = "http://timetableapi.ptv.vic.gov.au/"
PTV_DEVELOPER_ID = os.getenv('PTV_DEVELOPER_ID')
PTV_SECURITY_KEY = os.getenv('PTV_SECURITY_KEY')

#!/app/vbuild/RHEL7-x86_64/python/3.5.0/bin/python3
# -*- coding: utf-8 -*-

# codes will be executed when app-package is imported

import sys
sys.path.insert(0, "/home/ehumche/private/py3-lib/lib/python3.5/site-packages")

from flask import Flask

# app is member varialbe of app-package
app = Flask(__name__)

# place at bottom to avoid circular imports
from app import routes

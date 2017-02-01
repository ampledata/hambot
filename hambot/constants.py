#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HamBot Constants."""

import logging
import os

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


LOG_LEVEL = logging.DEBUG
LOG_FORMAT = logging.Formatter(
    ('%(asctime)s hambot %(levelname)s %(name)s.%(funcName)s:%(lineno)d - '
     '%(message)s'))

ERRORS_TO = os.environ.get('ERRORS_TO', 'gba')
DEBUG_HAMBOT = bool(os.environ.get('DEBUG_HAMBOT'))

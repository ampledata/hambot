#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HamBot Commands."""

from __future__ import print_function

import sys
import logging
import logging.config

import slackbot
import slackbot.settings
import slackbot.bot

import hambot

slackbot.settings.PLUGINS = ['hambot.plugin']
slackbot.settings.ERRORS_TO = hambot.ERRORS_TO
slackbot.settings.DEBUG = hambot.DEBUG_HAMBOT


__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


def cli():
    """
    HamBot command line function.
    """

    lkw = {
        'format': (
            '%(asctime)s hambot %(levelname)s '
            '%(name)s.%(funcName)s:%(lineno)d - %(message)s'
        ),
        'level': logging.DEBUG if slackbot.settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**lkw)
    logging.getLogger(
        'requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)

    bot = slackbot.bot.Bot()
    print('Starting HamBot...')
    bot.run()


if __name__ == '__main__':
    cli()

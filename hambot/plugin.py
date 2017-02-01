#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HamBot Plugin."""

import re

import slackbot
import requests

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


@slackbot.bot.respond_to('call (.*)', re.IGNORECASE)
def call(message, callsign):
    """
    Looks up a callsign when receiving a message of the format:

        call XXXXXX

    ... where XXXXXX is the callsign to lookup.

    :param message: Received message.
    :param callsign: Callsign to lookup.
    """
    request = requests.get('https://callook.info/{}/text'.format(callsign))
    if request.ok:
        message.reply('```' + request.content + '```')

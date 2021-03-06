#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   utils.py                                                                   #
#                                                                              #
#   General utility module.                                                    #
#                                                                              #
#                                                                              #
#                                                                              #
#   Copyright (C) 2015 LibreLabUCM All Rights Reserved.                        #
#                                                                              #
#   This file is part of teleg-api-bot.                                        #
#                                                                              #
#   This program is free software: you can redistribute it and/or modify       #
#   it under the terms of the GNU General Public License as published by       #
#   the Free Software Foundation, either version 3 of the License, or          #
#   (at your option) any later version.                                        #
#                                                                              #
#   This program is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                              #
################################################################################

import re

emoji_re = re.compile(u'['
        u'\U0001F300-\U0001F64F'
        u'\U0001F680-\U0001F6FF'
        u'\u2600-\u26FF\u2700-\u27BF]+',
        re.UNICODE)


def msg_get_summary(msg, truncate=0):
    summary = ""

    if 'text' in msg:

        message = msg["text"]
        message = re.sub(emoji_re, 'emoji', message)

        summary = "[Text: "

        if (0 < truncate < len(message)):
            summary += message[:truncate] + '...'
        else:
            summary += message + ']'

    if 'new_chat_participant' in msg:
        summary += msg["new_chat_participant"]["first_name"] + " was added to " + msg["chat"]["title"] + " "

    if 'left_chat_participant' in msg:
        summary += msg["left_chat_participant"]["first_name"] + " left " + msg["chat"]["title"] + " "

    if 'audio' in msg:
        summary += "[Media: " + "Audio" + "] "

    if 'document' in msg:
        summary += "[Media: " + "Document" + "] "

    if 'photo' in msg:
        summary += "[Media: " + "Photo" + "] "

    if 'sticker' in msg:
        summary += "[Media: " + "Sticker" + "] "

    if 'video' in msg:
        summary += "[Media: " + "Video" + "] "

    if 'contact' in msg:
        summary += "[Media: " + "Contact" + "] "

    if 'location' in msg:
        summary += "[Media: " + "Location" + "] "

    if 'new_chat_title' in msg:
        summary += "[Chat title changed from " + msg["chat"]["title"] + " to " + msg["new_chat_title"] + "] "

    if 'new_chat_photo' in msg:
        summary += "[Chat photo changed" + "] "

    if 'delete_chat_photo' in msg:
        summary += "[Deleted chat photo" + "] "

    if 'group_chat_created' in msg:
        summary += "[Group chat " + msg["chat"]["title"] + " created" + "] "

    return summary

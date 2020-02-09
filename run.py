#!/usr/bin/env python
#coding: utf-8

from wxpy import *
import configparser
import os
import sys

from util import *
from atMessageHandler import at_message_handler

cf = configparser.ConfigParser()
if os.path.exists('config/my.conf'):
    cf.read('config/my.conf', encoding="utf-8")
else:
    cf.read('config/default.conf', encoding="utf-8")

group_names = cf.get('wechat', 'group_names').split(',')
prefixText = cf.get('wechat', 'prefixText')

bot = Bot(cache_path=True)
allGroup = bot.groups()

groups = name_to_groupList( group_names , allGroup)
print(groups)

@bot.register(groups)
def sync_message(msg):
    try:
        # is_at 专指是否at机器人
        # at机器人的消息，均不转发
        if msg.is_at:
            at_message_handler(msg, groups)
        else:
            if msg.type != 'Sharing' and msg.type != 'Recording' :
                sync_message_in_groups(msg, groups, prefix = prefixText )
    except Exception as e:
        raise e

# 只按需查询群信息，不同步消息
atOnlyGroup_names = cf.get('wechat', 'group_names_atOnly').split(',')
atOnlyGroups = name_to_groupList( atOnlyGroup_names, allGroup)
print(atOnlyGroups)
@bot.register(atOnlyGroups)
def atOnlyGroups(msg):
    if msg.is_at:
        at_message_handler(msg, groups)
    


embed()

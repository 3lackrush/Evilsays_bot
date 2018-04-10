#!/usr/bin/env python
# coding:utf-8
__author__ = 'Kios <root@mkernel.com>'
__desc__ = 'Telegram Bot: Evilsays_bot'

import telebot
from config.config import token
from searchCVE import searchByCVE


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id,
                     "这是一个查询CVE的机器人，如需帮助请 @toorKios \n",
                      parse_mode='Markdown')

@bot.message_handler(commands=['search'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        cve_number = message.text.split(" ")[1]
        res = searchByCVE(cve_number)
        if res != None and len(res) != 0:
            cve_num = res[0][1]
            status = res[0][2]
            description = res[0][3]
            references = res[0][4]
            phase = res[0][5]
            votes = res[0][6]
            comments = res[0][7]
            bot.send_message(message.chat.id,
                             "CVE: {} \n".format(cve_num) +
                             "Status: {} \n".format(status) +
                             "Description: {} \n".format(description) +
                             "references: {} \n".format(references) +
                             "phase: {} \n".format(phase) +
                             "votes: {} \n".format(votes) +
                             "comments: {} \n".format(comments),
                             parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id,
                             "暂未查询到该CVE \n",
                             parse_mode='Markdown')

    except Exception as e:
        bot.send_message(message.chat.id,
                         "程序异常！ 请不要搞事情\n",
                         parse_mode='Markdown')



bot.polling(none_stop=True)

    

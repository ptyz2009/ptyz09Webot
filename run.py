from wxpy import *
bot = Bot(cache_path=True)
allGroup = bot.groups()

groupA = ensure_one(allGroup.search('测试机器人'))
groupB = ensure_one(allGroup.search('测试2'))

prefixText = "(隔壁)"

def sync_message_basic(msg, neighbor):
    try:
        # is_at 专指是否at机器人
        # at机器人的消息，均不转发
        if msg.is_at:
            at_message_handler(msg, neighbor)
        else:
            if msg.type != 'Sharing' and msg.type != 'Recording' :
                msg.forward(neighbor, prefix= prefixText + msg.member.name + ":" )
    except Exception as e:
        print(e)

def at_message_handler(msg, neighbor):
        text = msg.text
        index = text.find("\u2005")
        # 当且仅当只有@sb 而无其它消息时，找不到字符\u2005。因为这时空格被自动去掉。
        # 这种情况只回复机器人状态
        if index == -1:
            msg.reply('我在')
        else:
            plainText = text[index:].strip()
            searchIndex = plainText.find('在不在')
            if searchIndex > 0:
                searchText = plainText [0: searchIndex].strip() 
                resA=groupA.search(searchText)
                resB=groupB.search(searchText)
                replyText = searchText
                if  neighbor == groupB :
                    if len(resA) > 0:
                        replyText += '在这个群里'
                        if len(resB) > 0:
                            replyText += '，也'
                    if len(resB) > 0:
                        replyText += '在隔壁群里'
                    if replyText == searchText:
                        replyText += '还没进群'
                if  neighbor == groupA :
                    if len(resB) > 0:
                        replyText += '在这个群里'
                        if len(resA) > 0:
                            replyText += ',也'
                    if len(resA) > 0:
                        replyText += '在隔壁群里'
                    if replyText == searchText:
                        replyText += '还没进群'
                msg.reply(replyText)
            else:
                msg.reply('查询示例："@回音壁 小明在不在"')


@bot.register(groupA)
def sync_message(msg):
    sync_message_basic(msg, groupB)

@bot.register(groupB)
def sync_message(msg):
    sync_message_basic(msg, groupA)


embed()

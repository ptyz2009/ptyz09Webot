from util import search_person_in_groups
def at_message_handler(msg, groupList):
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
                replyText = at_message_handler_isInGroup(msg.sender, searchText, groupList)
                msg.reply(replyText)
            else:
                msg.reply('查询示例："@传声筒 小明在不在"')


def at_message_handler_isInGroup(fromGroup , searchText, groupList):
    res,resnum = search_person_in_groups( searchText, groupList )
    replyText = searchText
    if resnum == 0:
        replyText += '还没进群'
    if resnum == 1:
        if res[0] == fromGroup:
            replyText += '在这个群里'
        else:
            if( len(groupList) == 2):
                replyText += '在隔壁群里'
            else:
                replyText += '在群' + res.name +'里'
    if resnum > 1:
        if len(groupList) == 2:
            replyText += '在这个群里'
            replyText += '，也'
            replyText += '在隔壁群里'
        else:
            replyText += '在多个群里'
    return replyText



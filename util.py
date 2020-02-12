from wxpy import ensure_one

def search_person_in_groups(name, groupList):
    inGroup = []
    for group in groupList:
        if len(group.search(name)) > 0:
            inGroup.append(group)
    return inGroup, len(inGroup)

def search_groupName_among_groups(name, groupList):
    res = groupList.search(name)
    return res, len(res)


def name_to_groupList( group_names, allGroup):
    groups = []
    for name in group_names:
        res, resnum = search_groupName_among_groups( name, allGroup )
        if resnum == 0:
            print('警告:', name , '未找到' )
        if resnum > 1:
            print('警告:', name, '匹配多个结果：', res )
            mark = ''
            while mark != 'y' and mark != 'n':
                mark = input('继续(y/n)?')
                if mark == 'n':
                    raise Exception("用户终止程序")
                if mark == '\r':
                    break;
                if mark != 'y':
                    print('输入错误，请输入y或n')
            for group in res:
                if group not in groups:
                    groups.append(group)
        if resnum == 1 and res[0] not in groups:
            groups.append(ensure_one(allGroup.search(name)))
    return groups



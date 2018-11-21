import itchat

def get_user_name_by_remark(remarkName):
    # 获取任何一项等于name键值的用户
    friends = itchat.search_friends(name=remarkName)
    for friend in friends:
        if friend['RemarkName'] == remarkName:
            return friend['UserName']
def checkData(dataFromUser, limitDown, limitUp):

    if dataFromUser.isdigit():
        if limitDown <= int(dataFromUser) <= limitUp:
            return True

import base64


def createUniqueUrlFile(fileId: int, filename: str) -> str:
    b64fileId = base64.encode(fileId)
    b64filename = base64.encode(filename)

    output = b64fileId + ":" +b64filename

    return output


def getFileIDAndFileNameByUrl(url: str) -> list:
    splited = url.split(":")
    b64fileId = splited[0]
    b64filename = splited[1]

    normal_text_fileid = base64.b64decode(b64fileId)
    normal_text_filename = base64.b64decode(b64filename)
    
    output = [normal_text_fileid, normal_text_filename]

    return output
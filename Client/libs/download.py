from client import clirequest

def download_file(paramaters):
    connection = clirequest.connect(method='get', url_parameter=paramaters)
    
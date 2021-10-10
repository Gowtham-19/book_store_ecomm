import hashlib


def encrypt_string(string_data):

    # print("value of string data",string_data)
    result = hashlib.sha256(string_data.encode())

    return result.hexdigest()
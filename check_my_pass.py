#!/usr/bin/env python3
"""
Author: Gabriel Lilly
Purpose: Check if password is secure
"""

import hashlib
import requests


# ---------------------------------------------------------------------------------------------
def request_api_data(query_char):
    """Check api data"""

    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


# ---------------------------------------------------------------------------------------------
def get_password_leaks_count(hashes, searches):
    """Check password leaks"""

    hashes = (line.split(':') for line in hashes.text.splitlines())
    for sequence, count in hashes:
        if sequence == searches:
            return count
    return 0


# ---------------------------------------------------------------------------------------------
def pwned_api_check(password):
    """Check password"""

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


# --------------------------------------------------
def main():
    """Lights, camera, action!"""

    with open('passkeeper.txt', mode='r') as file:
        passwordlist = []
        for word in file:
            content = word.strip()
            passwordlist.append(content)

        for password in passwordlist:
            count = pwned_api_check(password)
            if count:
                print(f'{password} found {count} times, change it.')
            else:
                print(f'{password} was not found, it is safe to use.')
    return 'Search completed'


# --------------------------------------------------
if __name__ == '__main__':
    main()

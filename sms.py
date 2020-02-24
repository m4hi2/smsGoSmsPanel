import requests
from urllib.parse import urlencode, quote_plus

base_url = 'http://gosms.xyz/api/v1/sendSms?'

with open('file.txt', mode='r') as file:
    for line in file:
        x = line.strip()
        numbers = x
        message = 'dummy message'
        data = {
            'username'      : #username ,
            'password'      : #password,
            'number'        : numbers,
            'sms_content'   : message,
            'sms_type'      : '1',
            'masking'       : 'non-masking',
        }


        encoded_url = urlencode(data, quote_via = quote_plus)
        print(encoded_url)
        r = requests.post(base_url + str(encoded_url))
        with open('log.txt', mode='w+') as file2:
            file2.write(r.text + ' ' + numbers + '\n')
        print(numbers)
        print(r.text)


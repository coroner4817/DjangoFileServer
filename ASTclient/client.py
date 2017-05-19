import sys
import os
import requests
import tempfile
import hashlib, urllib2, urllib
from django.core.files.uploadedfile import UploadedFile
from django.utils.encoding import force_bytes

# small upload
with open(__file__, 'rb') as fp:
    post_data = {
        'file_field': UploadedFile(fp),
    }
    response = requests.post('http://127.0.0.1:8000/file_uploads/upload/', files=post_data)
    print response.content

# list upload
file = tempfile.NamedTemporaryFile
with file(suffix=".file1") as file1, file(suffix=".file2") as file2:
    file1.write(b'a' * (2 ** 21))
    file1.seek(0)

    file2.write(b'a' * (10 * 2 ** 20))
    file2.seek(0)

    post_data = {
        'timestamp': 'timestamp',
        'file_field1': file1,
        'file_field2': file2,
    }

    for key in list(post_data):
        try:
            post_data[key + '_hash'] = hashlib.sha1(post_data[key].read()).hexdigest()
            post_data[key].seek(0)
        except AttributeError:
            post_data[key + '_hash'] = hashlib.sha1(force_bytes(post_data[key])).hexdigest()

    response = requests.post('http://127.0.0.1:8000/file_uploads/verify/', files=post_data)
    print response.content
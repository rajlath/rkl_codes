'''
import requests
file_url = "https://nodejs.org/dist/v12.1.0/node-v12.1.0-x64.msi"

# URL of the image to be downloaded is defined as image_url
r = requests.get(file_url) # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("node-v12.1.0-x64.msi",'wb') as f:

    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
'''
import sys
import requests


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

download("https://nodejs.org/dist/v12.1.0/node-v12.1.0-x64.msi","node-v12.1.0-x64.msi" )
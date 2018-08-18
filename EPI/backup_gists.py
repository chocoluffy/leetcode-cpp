# first: mkdir user && cd user && cp /path/to/get_gists.py .
# python3 backup_gists.py user
import requests
import sys
import os
from subprocess import call
import shutil

user = sys.argv[1]

r = requests.get('https://api.github.com/users/{0}/gists'.format(user))

shutil.rmtree('./notes')
os.makedirs('./notes')
os.chdir('./notes')
for i in r.json():
	description = i['description']
	title = description.split(']')[0][1:].replace(' ', '-')
	call(['git', 'clone', i['git_pull_url']])
	os.rename('./{0}'.format(i['id']), './{0}'.format(title))
	shutil.rmtree('./{0}/.git'.format(title))

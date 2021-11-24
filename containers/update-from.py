#!/usr/bin/env python3
import requests
import sys

dockerfile = sys.argv[1]
print('File {}'.format(dockerfile))
with open(dockerfile, 'r') as f:
  content = f.readlines()

def fetch_digest(organization, image, tag):
  tokenget = requests.get('https://auth.docker.io/token', params = { 'scope': 'repository:{}/{}:pull'.format(organization,image), 'service': 'registry.docker.io' })
  if not tokenget.ok:
    raise(Exception('Failed {} {}: {}'.format(tokenget.request.url, tokenget.status_code, tokenget.text)))
  token = tokenget.json()['token']
  digestget = requests.head('https://registry-1.docker.io/v2/{}/{}/manifests/{}'.format(organization,image,tag), headers = { 'Authorization': 'Bearer '+token, 'Accept': 'application/vnd.docker.distribution.manifest.list.v2+json' })
  if not digestget.ok:
    raise(Exception('Failed {} {}: {}'.format(digestget.request.url, digestget.status_code, digestget.text)))
  digest = digestget.headers['docker-content-digest']
  return digest

ncontent = []
for line in content:
  if line.startswith('FROM'):
    linesplit = line.split()
    imageline = linesplit[1]
    image = imageline.split('@')[0] # Strip hash
    image, tag = image.split(':')
    organization = 'library'
    if len(image.split('/')) > 1:
      organization = image.split('/')[0]
      image = image.split('/')[1]

    digest = fetch_digest(organization, image, tag)

    if organization != 'library':
      imagefull = '{}/{}'.format(organization, image)
    else:
      imagefull = image
    linesplit[1] = '{}:{}@{}'.format(imagefull, tag, digest)
    line = ' '.join(linesplit) + '\n'
    print('Resolved {}'.format(line))
  elif line.find('FROM') >= 0:
    linesplit = line.split()
    from_pos = [i for i, value in enumerate(linesplit) if 'FROM' in value][0]
    imageline = linesplit[from_pos+1]

    image = imageline.split('@')[0] # Strip hash
    image, tag = image.split(':')
    organization = 'library'
    if len(image.split('/')) > 1:
      organization = image.split('/')[0]
      image = image.split('/')[1]

    digest = fetch_digest(organization, image, tag)

    if organization != 'library':
      imagefull = '{}/{}'.format(organization, image)
    else:
      imagefull = image
    # replace original
    orig_pos = [i for i, value in enumerate(linesplit) if imagefull in value][0]
    linesplit[orig_pos] = '{}@{}'.format(imagefull, digest)
    line = ' '.join(linesplit) + '\n'
    print('Resolved {}'.format(line))
  else:
    line = line
  ncontent.append(line)

with open(dockerfile, 'w') as f:
  f.writelines(ncontent)

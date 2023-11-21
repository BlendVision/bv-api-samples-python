import subprocess
import argparse
import os
import json

command_tpl = """curl --request POST \
  --url https://api.one.blendvision.com/bv/cms/v1/tokens \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'authorization: Bearer %s' \
  --header 'x-bv-org-id: %s' \
  --data '{
  "resource_id": "%s",
  "resource_type": "RESOURCE_TYPE_VOD"
}'"""


data_tpl = {
			'resource_id': '%s',
			'resource_type': 'RESOURCE_TYPE_VOD'
		   }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--content_id', type=str, help='VOD contnent ID, can get by BV1 CMS portal or API')
    parser.add_argument('--api_key', type=str, help='api key you created on BV1')
    parser.add_argument('--org_id', type=str, help='org id in your account')
    args = parser.parse_args()

    command = command_tpl % (args.api_key, args.org_id, args.content_id)
    print(command)

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print(out)
    

if __name__ == '__main__':
    main()

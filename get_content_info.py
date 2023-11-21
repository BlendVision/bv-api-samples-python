import subprocess
import argparse
import os
import json

command_tpl = "curl --request GET --url https://api.one.blendvision.com/bv/cms/v1/vods/%s --header 'Accept: application/json' --header 'authorization: Bearer %s' --header 'x-bv-org-id: %s'"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--content_id', type=str, help='VOD contnent ID, can get by BV1 CMS portal or API')
    parser.add_argument('--api_key', type=str, help='api key you created on BV1')
    parser.add_argument('--org_id', type=str, help='org id in your account')
    args = parser.parse_args()

    command = command_tpl % (args.content_id, args.api_key, args.org_id)

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    data = json.loads(out)
    for i in data['vod']['stream'][0]['manifests']:
    	if i['protocol'] == 'PROTOCOL_DASH':
    		print('DASH url: %s' % i['uris'][0]['uri'])
    	elif i['protocol'] == 'PROTOCOL_HLS':
    		print('HLS url: %s' % i['uris'][0]['uri'])
    

if __name__ == '__main__':
    main()

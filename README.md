# Sample code to query DASH/HLS url and DRM playback token

## System requirements
Python 3.x
BlendVision One API key and organization ID configuration

## Environment variable:

```env
BV_CONTENT_ID=your_content_id
BV_ONE_ORG_ID=your_org_id
BV_ONE_API_KEY=your_api_key
```

## How to get DASH/HLS url:

```bash
$ python3 get_content_info.py --content_id $BV_CONTENT_ID --api_key $BV_ONE_API_KEY --org_id $BV_ONE_ORG_ID
```

## How to get playback token:

```bash
$ python3 get_playback_token.py --content_id $BV_CONTENT_ID --api_key $BV_ONE_API_KEY --org_id $BV_ONE_ORG_ID
```

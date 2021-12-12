# ---------------------------------------------------------------------------------------------------------------------
# YouTube Data API v3
# ---------------------------------------------------------------------------------------------------------------------
# Google Developers Console: https://console.cloud.google.com/
# Google API Python Client:
#   https://github.com/googleapis/google-api-python-client
#   https://github.com/googleapis/google-api-python-client/blob/main/docs/README.md
#   https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build - build()
#   https://github.com/googleapis/google-api-python-client/blob/main/docs/dyn/index.md - List of all API versions
#   https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html - YouTube Dat API v3
# YouTube API:
#   https://developers.google.com/youtube/v3
#   https://developers.google.com/youtube/v3/docs/?apix=true
# ---------------------------------------------------------------------------------------------------------------------

from googleapiclient.discovery import build

# Get API Key from Google Cloud Console - https://console.cloud.google.com/
api_key = 'AIzaSyDcoAGBXjqXcACGoCzWZpkv4t63anSFcKc'

# build() - creates an API-specific service object with methods specific to the given API
youtube_api_service = build(serviceName='youtube', version='v3', developerKey=api_key)

# A channel resource contains information about a YouTube channel.
# https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.channels.html
# https://developers.google.com/youtube/v3/docs/channels

# list(): Returns a collection of zero or more channel resources that match the request criteria.
# https://developers.google.com/youtube/v3/docs/channels/list
# list(part, categoryId=None, forUsername=None, hl=None, id=None, managedByMe=None, maxResults=None, mine=None,
#       mySubscribers=None, onBehalfOfContentOwner=None, pageToken=None, x__xgafv=None)

request = youtube_api_service.channels().list(
    part='statistics',
    id='UCeQAGNG1p4rw0JOIOU_Nm_Q'
    # forUsername='Sayani Basu Music'
)

response = request.execute()
print(response)

print("\nStats for Channel 'Sayani Basu Music':")
print('Videos      : ', response['items'][0]['statistics']['videoCount'])
print('Subscribers : ', response['items'][0]['statistics']['subscriberCount'])
print('Total Views : ', response['items'][0]['statistics']['viewCount'])

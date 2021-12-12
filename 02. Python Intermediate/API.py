import requests
import webbrowser

# ---------------------------------------------------------------------------------------------------------------------
# REST API: Representational State Transfer API. REST uses HTTP as the protocol and JSON as the interchange format
# ---------------------------------------------------------------------------------------------------------------------
# GET: Read
# POST: Write
# PUT: Update
# DELETE: Delete
# PATCH: Update only a portion of the object
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# Consume the Stack Overflow "Question" API from https://api.stackexchange.com/
# ---------------------------------------------------------------------------------------------------------------------
# response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
#
# print(response)                               # <Response [200]>
# print(type(response))                         # <class 'requests.models.Response'>
# print(response.json())                        # data
# print(response.json()['items'])
#
# for question in response.json()['items']:
#     if question['answer_count'] == 0:
#         print(question['title'])
#         print(question['link'])
#     else:
#         print('Question Skipped')
#     print()


# ---------------------------------------------------------------------------------------------------------------------
# Consume the Dog API from:
# https://dog.ceo/api/breeds/list/all
# https://dog.ceo/api/breeds/image/random
# ---------------------------------------------------------------------------------------------------------------------
# response = requests.get('https://dog.ceo/api/breeds/list/all')
# print(response)                                 # <Response [200]>
# print(type(response))                           # <class 'requests.models.Response'>
# print(response.text)
# print(response.json())
# dog_json = response.json()
# print(dog_json['message']['australian'])        # ['shepherd']

response = requests.get('https://dog.ceo/api/breeds/image/random')
print(response)
print(response.text)
print(response.json())

img_url = response.json()['message']
print(img_url)
print('Breed: ', img_url.split('/')[4])

webbrowser.open(img_url)

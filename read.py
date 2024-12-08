import users_pb2
from google.protobuf.json_format import MessageToDict

users = users_pb2.Users()

with open('msg.pb', 'rb') as f:
    users.ParseFromString(f.read())

# iterate through results
for user in users.user:
    print(user)
    print(user.email)
    print()

# or switch to a Python dict
print(MessageToDict(users))

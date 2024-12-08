from typing import Mapping
import users_pb2

users = (
    {'id': 1, 'name': 'John Doe', 'email': 'john@apian.aero'},
    {'id': 2, 'name': 'Jane Doe', 'email': 'jane@apian.aero'},
)
users_proto = users_pb2.Users()

def add_user(user: Mapping[str, str | int]):
    u = users_proto.user.add()
    u.id = user['id']
    u.full_name = user['name']
    u.email = user['email']

for user in users:
    add_user(user)

with open('msg.pb', 'wb') as f:
    f.write(users_proto.SerializeToString())

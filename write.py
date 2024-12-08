from typing import TypedDict
import users_pb2

class User(TypedDict):
    id: int
    name: str
    email: str

user_data = (
    User(id=1, name='John Doe', email='john@apian.aero'),
    User(id=2, name='Jane Doe', email='jane@apian.aero'),
)
users = users_pb2.Users()

def add_user(user: User):
    u = users.user.add()
    u.id = user['id']
    u.full_name = user['name']
    u.email = user['email']

for user in user_data:
    add_user(user)

with open('msg.pb', 'wb') as f:
    f.write(users.SerializeToString())

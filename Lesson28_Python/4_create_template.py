from jinja2 import Environment, FileSystemLoader

users = [
    {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"},
]

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

rendered_html = template.render(users=users)

print(rendered_html)
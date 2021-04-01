import server.documents as documents

# Get User by Username
def get_user(username_in: str):
    for user in documents.user.User.objects:
        print(user.username)

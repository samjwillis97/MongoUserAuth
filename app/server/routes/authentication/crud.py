import app.server.documents.user as mongo_user

async def add_user(user: mongo_user):
  user = await user.save()
  return user


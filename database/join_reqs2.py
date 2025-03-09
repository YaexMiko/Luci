# (©) Javpostr made by @rohit_1888
import motor.motor_asyncio
from config import FORCE_SUB_CHANNEL2

class JoinReqs2:
    def __init__(self):
        from config import JOIN_REQS_DB2
        if JOIN_REQS_DB2:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(JOIN_REQS_DB2)
            self.db2 = self.client["JoinReqs2"]
            self.col = self.db2[str(FORCE_SUB_CHANNEL2)]
        else:
            self.client = None
            self.db2 = None
            self.col = None

    def isActive(self):
        """Check if the database connection is active."""
        return self.client is not None

    async def add_user(self, user_id, first_name, username, date):
        """Add a user to the database."""
        try:
            await self.col.insert_one({
                "_id": int(user_id),
                "user_id": int(user_id),
                "first_name": first_name,
                "username": username,
                "date": date
            })
        except:
            pass

    async def get_user(self, user_id):
        """Retrieve a user from the database."""
        return await self.col.find_one({"user_id": int(user_id)})

    async def get_all_users(self):
        """Retrieve all users from the database."""
        return await self.col.find().to_list(None)

    async def delete_user(self, user_id):
        """Delete a user from the database."""
        await self.col.delete_one({"user_id": int(user_id)})

    async def delete_all_users(self):
        """Delete all users from the database."""
        await self.col.delete_many({})

    async def get_all_users_count(self):
        """Get the total count of users in the database."""
        return await self.col.count_documents({})

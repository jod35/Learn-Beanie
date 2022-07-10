import motor.motor_asyncio
from beanie import Document
from pydantic import Field
import beanie
import asyncio
from bson.objectid import ObjectId


"""
class Task:
    content :text
    is_complete :bool -> false
"""


class Task(Document):
    content: str = Field(max_length=200)
    is_complete: bool = Field(default=False)

    def to_json(self):
        return {
            "id": str(self.id),
            "revision_id": str(self.revision_id),
            "content": self.content,
            "is_complete": self.is_complete,
        }


async def main():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

    await beanie.init_beanie(database=client.db_name, document_models=[Task])

    task1 = Task(content="Learn MongoDB", is_complete=False)

    task2 = Task(content="Learn FastAPI", is_complete=False)

    task3 = Task(content="Create a Youtube video", is_complete=True)

    # await task1.insert()

    # await task2.insert()

    # await task3.insert()

    # tasks = await Task.find({"is_complete": True}).to_list()

    # for task in tasks:
    #     print(task.to_json())

    task3 = await Task.find_one({"_id": ObjectId("62ca453f4d9a7b8cee692e56")})

    # task3.content = "Edit the Youtube video and upload it"

    # try:
    #     await task3.replace()

    # except (ValueError, beanie.exceptions.DocumentNotFound):
    #     print("Document not found")

    # print(task3)

    await task3.delete()


asyncio.run(main())

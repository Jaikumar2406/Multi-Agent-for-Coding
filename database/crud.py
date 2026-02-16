from sqlalchemy.ext.asyncio import AsyncSession
from database.model import Chat

async def save_chat(
    db: AsyncSession,
    question: str,
    answer: str
):
    chat = Chat(
        question=question,
        answer=answer
    )
    db.add(chat)
    await db.commit()

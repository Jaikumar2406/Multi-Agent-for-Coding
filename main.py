from graph import build_workflow
from database.connection import AsyncSessionLocal
from database.crud import save_chat
import asyncio

workflow = build_workflow()

async def store_chat(question: str, answer: str):
    async with AsyncSessionLocal() as db:
        await save_chat(
            db=db,
            question=question,
            answer=answer
        )


config = {
    "configurable": {
        "thread_id": "user-123"
    }
}

print("🤖 Agent ready. Type 'exit' to stop.\n")

while True:
    user_input = input("👤 You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Bye!")
        break

    state = {
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "status": "ok",
        "max_try": 3,
        "trying": 0
    }

    result = workflow.invoke(state, config=config)

    print("\n🤖 Agent:")

    final_answer = None   # 👈 important

    # 🔹 CHAT MODE
    if result.get("mode") == "Chat":
        final_answer = result.get("chat_response") or result.get("planning")
        print(final_answer)

    # 🔹 PROBLEM MODE
    elif result.get("mode") == "Problem":
        final_answer = result.get("Synthesizer")
        print(final_answer)

    # 🔹 FAIL SAFE
    else:
        final_answer = "Unable to process your request."
        print(final_answer)

    # 🔹 SAVE TO DATABASE (🔥 MAIN PART)
    if final_answer:
        asyncio.run(
            store_chat(
                question=user_input,
                answer=final_answer
            )
        )

    print("-" * 50)
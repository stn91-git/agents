import json
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint
from datetime import datetime
import os

# UserId for the memories
user_id = "email_user"
# Database file for memory and storage
db_file = "tmp/email_agent.db"

# Get the root directory path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_emails(json_file):
    """Load emails from JSON file and format them for memory storage."""
    # Use the full path to the JSON file
    json_path = os.path.join(ROOT_DIR, json_file)
    with open(json_path, "r") as f:
        emails = json.load(f)

    # Format each email into a memory-friendly string
    formatted_emails = []
    for email in emails:
        # Convert date string to datetime for better formatting
        date = datetime.fromisoformat(email["date"].replace("Z", "+00:00"))
        formatted_date = date.strftime("%B %d, %Y at %I:%M %p")

        # Create a formatted string for each email
        email_text = f"""
Email from: {email['from']}
To: {email['to']}
Date: {formatted_date}
Subject: {email['subject']}

Content:
{email['body_text']}

Links: {', '.join(email['links']) if email['links'] else 'No links'}
"""
        formatted_emails.append(email_text)

    return formatted_emails


def initialize_agent():
    """Initialize the agent with memory and storage capabilities."""
    # Initialize memory.v2
    memory = Memory(
        model=OpenAIChat(
            id="gpt-4.1",
            api_key="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",
        ),
        db=SqliteMemoryDb(table_name="email_memories", db_file=db_file),
    )

    # Initialize storage
    storage = SqliteStorage(table_name="email_sessions", db_file=db_file)

    # Initialize Agent
    email_agent = Agent(
        model=OpenAIChat(
            id="gpt-4.1",
            api_key="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",
        ),
        memory=memory,
        enable_agentic_memory=True,
        enable_user_memories=True,
        storage=storage,
        add_history_to_messages=True,
        num_history_runs=3,
        markdown=True,
    )

    return email_agent, memory


def main():
    # Initialize agent and memory
    email_agent, memory = initialize_agent()

    pprint(memory.get_user_memories(user_id=user_id))
    # Clear any existing memories
    # memory.clear()

    # Load and store emails
    # print("Loading emails into memory...")
    # emails = load_emails("cleaned_emails.json")

    # # Store each email as a memory
    # for i, email in enumerate(emails, 1):
    #     print(f"Storing email {i}/{len(emails)}...")
    #     email_agent.print_response(
    #         f"Here is an email that was received: {email}",
    #         user_id=user_id,
    #         stream=True,
    #         stream_intermediate_steps=True,
    #     )

    # print("\nEmails loaded into memory! You can now ask questions about them.")
    # print("Example questions:")
    # print("- What emails did I receive about job opportunities?")
    # print("- What newsletters am I subscribed to?")
    # print("- What was the most recent email I received?")
    # print("- What emails contain links to articles about technology?")
    # print("\nType 'exit' to quit.")

    # Interactive loop
    # while True:
    #     question = input("\nWhat would you like to know about your emails? ").strip()
    #     if question.lower() == "exit":
    #         break

    #     print("\nSearching through emails...")
    #     email_agent.print_response(
    #         question,
    #         user_id=user_id,
    #         stream=True,
    #         stream_intermediate_steps=True,
    #     )


if __name__ == "__main__":
    main()

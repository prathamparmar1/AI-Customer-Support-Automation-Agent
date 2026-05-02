def generate_prompt(context, query):
    return f"""
You are an AI customer support agent.

Context:
{context}

User Query:
{query}

Instructions:
- Provide a helpful answer
- If unsure, suggest escalation
- Be concise and professional

Answer:
"""
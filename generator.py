def generate_response(query: str, context: list[str]) -> str:
    """
    Generate response using query + context.
    """
    combined_context = " ".join(context)
    response = f"Answer based on: {combined_context}"
    return response

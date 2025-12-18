"""
Helper functions
"""

def format_user_mention(user_id: int, name: str) -> str:
    """Format user mention for HTML"""
    return f'<a href="tg://user?id={user_id}">{name}</a>'

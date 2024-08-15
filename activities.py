"""
Our first activity.
"""

from temporalio import activity

@activity.defn
async def say_hello(name: str) -> str:
    """
    Our first activity.
    """

    return f"Hello, {name}!"

from dataclasses import dataclass


@dataclass
class Subscriber:
    """Represents a subscriber"""

    name: str
    email: str
    is_subscribed: bool

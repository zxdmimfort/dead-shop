import os

if not os.getenv("MODE", None):
    from dotenv import load_dotenv

    load_dotenv()

MODE = os.getenv("MODE")

match MODE:
    case "DEV":
        from .dev import *  # noqa: F403
    case "PROD":
        from .prod import *  # noqa: F403
    case _:
        raise ValueError(f"Unknown MODE: {MODE}")

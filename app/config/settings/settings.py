import os

if not os.getenv("MODE", None):
    from dotenv import load_dotenv
    load_dotenv()

MODE = os.getenv("MODE")

match MODE:
    case "DEV":
        from .dev import *
    case "PROD":
        from .prod import *
    case _:
        raise ValueError(f"Unknown MODE: {MODE}")

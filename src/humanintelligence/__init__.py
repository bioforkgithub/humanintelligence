"""humanintelligence: plain-English words for machine learning, deep learning and AI.

Import it as:  import humanintelligence as hi
This early release is in planning; hi.about() says what is coming.
"""

__version__ = "0.0.1"


def about() -> str:
    """Say what humanintelligence is and where it stands. hi.about()"""
    text = (
        f"humanintelligence {__version__}: plain-English words for machine learning, deep learning and AI.\n"
        "This early release has no machine-learning words yet; they are being planned.\n"
        "For data cleaning, tables, charts and statistics, use simplydata (import simplydata as sdata)."
    )
    print(text)
    return text

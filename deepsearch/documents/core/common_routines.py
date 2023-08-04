from dataclasses import dataclass

dashes = f"{'-'*86}"
WELCOME = f"{dashes}\n{'':>26}Welcome to the Deep Search Toolkit\n{dashes}"
ERROR_MSG = f"{dashes}\nSuggestion:\n(1) Check your input.\n(2) Contact Deep Search developers if problem persists.\n{dashes}"
# setup for progress bars
progressbar_length = 30


@dataclass
class ProgressBarParameters:
    padding = 22
    colour = "#0f62fe"
    bar_format = "{l_bar}{bar:%d}{r_bar}{bar:-10b}" % (progressbar_length)


progressbar = ProgressBarParameters()

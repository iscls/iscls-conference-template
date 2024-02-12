#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:56:29 2024

@author: Hrishikesh Terdalkar
"""

###############################################################################

from pathlib import Path
import yaml

SCHEDULE_DIR = Path(__file__).resolve().parent
BASE_DIR = SCHEDULE_DIR.parent

PROGRAM_YAML = BASE_DIR / "_data" / "program.yml"
TABLE_TEX = SCHEDULE_DIR / "table.tex"

###############################################################################

CONTENT = []

###############################################################################

with open(PROGRAM_YAML, "r") as f:
    PROGRAM = yaml.safe_load(f)


CONTENT.append(
    "\\bgroup\n"
    "\\def\\arraystretch{1.5}\n"
)
CONTENT.append("\\begin{longtable}{|p{0.2\\textwidth}|p{0.75\\textwidth}p{0.05\\textwidth}|}\n")
for idx, day in enumerate(PROGRAM["schedule"], start=1):
    CONTENT.append("\\noalign{\\penalty-5000}\\hline\n")
    if idx > 1:
        CONTENT.append("& \\\\\n")
        CONTENT.append("\\hline\n")
        CONTENT.append("\\hline\n")

    CONTENT.append(f"\\rowcolor{{Snow4!30!}} \\textbf{{Day {idx}}} & \\textbf{{{day['dateReadable']}}} & \\\\\n")
    CONTENT.append("\\hline\n")
    for timeslot in day["timeslots"]:
        timeslot_type = timeslot["type"]
        if timeslot_type == "service":
            _rowcolor = "Gold1"
        elif timeslot_type == "talk":
            _rowcolor = "SeaGreen3"
        elif timeslot_type == "presentation":
            _rowcolor = "OliveDrab3"
        elif timeslot_type == "activity":
            _rowcolor = "Brown3"
        elif timeslot_type == "formality":
            _rowcolor = "RosyBrown3"
        elif timeslot_type == "sponsor":
            _rowcolor = "RoyalBlue3"
        else:
            _rowcolor = "Gray0"

        _time = f"{timeslot['startTime']}  - {timeslot['endTime']}"
        rightside = []
        if timeslot.get("title"):
            rightside.append(f"\\textsc{{{timeslot['title']}}}")
        if timeslot.get("speaker"):
            rightside.append(f"{timeslot['speaker']}")
        if timeslot.get("chair"):
            rightside.append(f"\\textbf{{Session chair:}} {timeslot['chair']}")

        for _i, _text in enumerate(rightside):
            CONTENT.append(f"\\rowcolor{{{_rowcolor}!45!}} {_time} & " if _i == 0 else " & ")
            CONTENT.append(f"{_text} & \\\\*\n" if _i < len(rightside) - 1 or timeslot.get("events") else f"{_text} & \\\\\n")

        CONTENT.append("\\hline\n")

        if not timeslot.get("events"):
            continue

        for _i, event in enumerate(timeslot["events"]):
            if event.get("startTime") and event.get("endTime"):
                event_time = f"{event['startTime']}  - {event['endTime']}"
            else:
                event_time = ""

            event_type = []
            if event.get("virtual"):
                event_type.append(f"\\pill{{black!75!}}{{\\scriptsize\\bf virtual}}")

            event_type_ = event.get("type", "")
            if event_type_:
                event_color = "Green4!75!" if event_type_ == "paper" else "RoyalBlue3!75!"
                event_type.append(f"\\pill{{{event_color}}}{{\\scriptsize\\bf {event_type_}}}")

            event_type_text = "".join(event_type)

            if event.get("title"):
                CONTENT.append(
                    f" {event_time} & \\textbf{{{event['title']}}} & {event_type_text}\\\\*\n"
                )
                event_type_text = ""
                event_time = ""

            if event.get("speakers"):
                CONTENT.append(
                    f" {event_time} & \\textit{{{event['speakers']}}} & {event_type_text}\\\\\n"
                )
                event_type_text = ""
                event_time = ""

            if _i == len(timeslot["events"]) - 1:
                CONTENT.append("\\hline\n")#\\noalign{\\penalty-5000}\n")
            else:
                CONTENT.append("\\hline\n")

CONTENT.append("\\end{longtable}\n")
CONTENT.append("\\egroup")

###############################################################################

with open(TABLE_TEX, "w") as f:
    f.write("".join(CONTENT))

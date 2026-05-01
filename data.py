from typing import Any

from untis import get_untis_data

def get_data(env, room: str):
    stunden = get_untis_data(env,room)
    stunden = merge_stunden(stunden)
    print(stunden)

def merge_stunden(stunden: list[Any] | None) -> list[Any] | None:
    if not stunden:
        return []

    merged = []
    current = stunden[0].copy()

    for next_h in stunden[1:]:
        #prüft ob gleicher lehrer, fach, klasse und Endzeit == Startzeit
        same = (
            current["teacher"] == next_h["teacher"] and
            current["subject"] == next_h["subject"] and
            current["klasse"] == next_h["klasse"] and
            current["end_time"] == next_h["start_time"]
        )
        if same:
            current["end_time"] = next_h["end_time"]
        else:
            merged.append(current)
            current = next_h.copy()
    merged.append(current)
    return merged


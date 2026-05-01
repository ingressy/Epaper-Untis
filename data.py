from typing import Any

from untis import get_untis_data

def get_data(room: str) -> list[Any] | None:
    stunden = get_untis_data(room)
    stunden = merge_stunden(stunden)
    #print(stunden)
    return stunden

def merge_stunden(stunden: list[Any] | None) -> list[Any] | None:
    if not stunden:
        return []

    merged = []
    current = stunden[0].copy()
    current["anzahl"] = 1

    for next_h in stunden[1:]:
        #prüft ob gleicher lehrer, fach, klasse und datum
        same = (
            current["teacher"] == next_h["teacher"] and
            current["subject"] == next_h["subject"] and
            current["klasse"] == next_h["klasse"] and
            current["date"] == next_h["date"]
        )
        if same:
            current["end_time"] = next_h["end_time"]
            current["anzahl"] += 1
        else:
            merged.append(current)
            current = next_h.copy()
            current["anzahl"] = 1

    merged.append(current)
    return merged


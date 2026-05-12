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
    used = set()

    for i, current in enumerate(stunden):
        if i in used:
            continue

        current = current.copy()
        current["anzahl"] = 1

        # suche passende Folgestunde
        for j in range(i + 1, len(stunden)):
            if j in used:
                continue
            next_h = stunden[j]
            same = (
                    current["teacher"] == next_h["teacher"] and
                    current["subject"] == next_h["subject"] and
                    current["klasse"] == next_h["klasse"] and
                    current["date"] == next_h["date"] and
                    current["code"] == next_h["code"]
            )
            if same:
                current["end_time"] = next_h["end_time"]
                current["anzahl"] += 1
                used.add(j)
            # bei normalen Stunden: nur direkt aufeinanderfolgende zusammenfassen
            elif current["code"] != "cancelled":
                break

        merged.append(current)
        used.add(i)

    return merged
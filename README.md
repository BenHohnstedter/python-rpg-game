# python-rpg-game

Ein kleines, textbasiertes Rollenspiel für die Konsole – komplett objektorientiert in Python geschrieben. Es entstand als Hausaufgabe während der Berufsschule. Die OOP-Struktur (Klassen, Properties, Getter/Setter) spiegelt die im Betrieb erlernte PHP-Weise wider und wurde mit Online-Recherche auf Python übertragen.

## Das Spiel

Man befindet sich in einem Dungeon mit vier Räumen: **Hall, Kitchen, Dining Room** und **Garden**. Ziel ist es, den Garten mit einem Schlüssel (`key`) und einem Trank (`potion`) zu erreichen – und dabei dem Monster in der Küche auszuweichen.

### Befehle

```
go      → go north / go south / go east / go west
get     → nehme einen Gegenstand auf (z. B. get key)
show    → show commands / show status
exit    → Spiel beenden
```

## Technologien

- Python 3
- Erfolgt komplett ohne externe Abhängigkeiten

## Starten

```bash
python pythongame.py
```

**Lokal:** `C:\Coding\desktop-apps\pu-python-rpg-game\`

## Struktur

```
pythongame.py – komplette Spiellogik (134 Zeilen)
├── Player   – Inventar, aktueller Raum, Statusanzeige
├── Dungeon  – Raum-Layout und Verbindungen
└── Game     – Spielsteuerung, Befehle, Sieg-/Verlust-Logik
```

## Projektbezug

Erste Erfahrungen mit objektorientierter Programmierung in Python – geprägt durch den OOP-Ansatz aus PHP.
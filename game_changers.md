# Commander Game Changers — official list

**Source:** the official Commander Brackets list, supplied by the deck owner on **2026-09-20**.
**Every one of the 53 names below was resolved against `scryfall.db` before being written here**, and each card's colour identity was checked against the section it appears in. No name is transcribed from memory.

## How to use this file

1. **Never state a card's Game Changer status from memory.** Check it here.
2. **`scryfall.db` cannot answer this question.** It has no game-changer column and no such key inside its `legalities` JSON. Don't go looking.
3. Archidekt's API *does* expose a `gameChanger` boolean on its `oracleCard` objects, which is a useful second opinion — but it is third-party. **This file is the authority.**
4. **The list changes over time.** Cards get delisted (see the note at the bottom). If a deck's bracket matters, ask the owner to re-share the current list and update this file rather than trusting it indefinitely.

## Bracket rules that depend on this list

- **Bracket 2:** no Game Changers.
- **Bracket 3:** up to 3 Game Changers. Also no mass land denial, no chained extra turns, and no cheap early two-card infinite combos (late game, around turn 6+, is fine).
- **Bracket 4:** unlimited Game Changers.

Brackets describe how a deck plays, not only its card list — the count is necessary, not sufficient.

---

## White (7)
- Drannith Magistrate
- Enlightened Tutor
- Farewell
- Humility
- Serra's Sanctum
- Smothering Tithe
- Teferi's Protection

## Blue (10)
- Consecrated Sphinx
- Cyclonic Rift
- Force of Will
- Fierce Guardianship
- Gifts Ungiven
- Intuition
- Mystical Tutor
- Narset, Parter of Veils
- Rhystic Study
- Thassa's Oracle

## Black (10)
- Ad Nauseam
- Bolas's Citadel
- Braids, Cabal Minion
- Demonic Tutor
- Imperial Seal
- Necropotence
- Opposition Agent
- Orcish Bowmasters
- Tergrid, God of Fright — in the database as `Tergrid, God of Fright // Tergrid's Lantern`
- Vampiric Tutor

## Red (3)
- Gamble
- Jeska's Will
- Underworld Breach

## Green (7)
- Biorhythm
- Crop Rotation
- Gaea's Cradle
- Natural Order
- Seedborn Muse
- Survival of the Fittest
- Worldly Tutor

## Multicolor (4)
- Aura Shards
- Coalition Victory
- Grand Arbiter Augustin IV
- Notion Thief

## Colorless (12)
- Ancient Tomb
- Chrome Mox
- Field of the Dead
- Glacial Chasm
- Grim Monolith
- Lion's Eye Diamond
- Mana Vault
- Mishra's Workshop
- Mox Diamond
- Panoptic Mirror
- The One Ring
- The Tabernacle at Pendrell Vale

**Total: 53 cards.**

---

## Cards commonly *believed* to be Game Changers that are NOT on this list

Checking these has already caught two real errors in the deck files, so they are worth naming explicitly.

- **Green Sun's Zenith — NOT a Game Changer.** `toph_reference.md` counted it as one and concluded the Toph deck was Bracket 4 on four Game Changers. It is not on the green list, and Archidekt independently flags it `False`. Toph actually runs **three** (Enlightened Tutor, Aura Shards, Smothering Tithe), which is exactly at the Bracket 3 cap. Natural Order was swapped out for Aura Shards on 2026-09-21; both are Game Changers, so the count never moved.
- **Vorinclex, Voice of Hunger — NOT a Game Changer.** Delisted Oct 21, 2025 per the Toph file; absent from the green list above, which agrees.
- **Sol Ring — NOT a Game Changer**, despite being the most format-defining card in Commander.
- **Survival of the Fittest IS one** (green), and is also Reserved List and expensive — rejected on price for the Kodama deck.

## Current Game Changer counts by deck

Recorded so these don't get recomputed from scratch or from memory each time.

| Deck | Count | Which |
|---|---|---|
| Kodama // Kamahl | 2 of 3 | Seedborn Muse, Natural Order |
| Toph, the First Metalbender | 3 of 3 | Enlightened Tutor, Aura Shards, Smothering Tithe |

Last reconciled against both deck files on **2026-09-21**. Other decks in `decks/` have not been audited against this list yet.

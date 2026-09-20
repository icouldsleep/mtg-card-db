# Cards Reference — Kodama of the East Tree // Kamahl, Heart of Krosa EDH Deck

**STATUS: BUILT (100 cards).** Original build confirmed Sept 19, 2026; **4-card swap applied Sept 20, 2026** to fix the deck's artifact/enchantment removal gap and to pull out the +1/+1 counter spreader. Cut down from the 181-card Archidekt staging pool after a full database cross-check (existence, color identity, Commander legality, and full oracle text for every card) plus a synergy pass looking for interactions the category tags alone would've missed.

Staging link (original 181-card pool, now superseded by the 100 below): https://archidekt.com/decks/26413180/kodoma_of_the_mono_tree

## Companion files in this folder
- `kodama_decklist.txt` — the flat 100, one card per line, mass-entry format for ordering.
- `kodama_buylist.md` — which cards come from the Tramplesaurus Rex precon and which still need buying.
- `kodama_play_guide.pdf` — 7-page play guide: the Kodama trigger explained properly, the free-land chain, Scute Swarm's doubling, the Sabertooth loops, Woodland Bellower targets, and a misplays list.

## Base
Started from **Tramplesaurus Rex**, the mono-green precon from the Foundations Commander Decks set. Stock commander was Ghalta, Primal Hunger.

## Commanders (Partners) — 2
**Kodama of the East Tree** — {4}{G}{G} — Legendary Creature — Spirit — **6/6** — Reach
"Whenever another permanent you control enters, if it wasn't put onto the battlefield with this ability, you may put a permanent card with equal or lesser mana value from your hand onto the battlefield." Partner.

**Kamahl, Heart of Krosa** — {6}{G}{G} — Legendary Creature — Human Druid — **5/5**
"At the beginning of combat on your turn, creatures you control get +3/+3 and gain trample until end of turn. {1}{G}: Until end of turn, target land you control becomes a 1/1 Elemental creature with vigilance, indestructible, and haste. It's still a land." Partner.

## Game Plan / Key Rules Finding
Kodama's trigger is **not landfall-specific — it fires off ANY permanent entering under your control**, including tokens (creature or artifact). This means token generators are the deck's real engine, not just landfall payoffs: every token made is a free Kodama trigger, which can drop another permanent from hand for free, which can chain into more triggers if that permanent is itself a token-maker or a land. Extra-land-drop enablers (Exploration, Azusa, Loot, Burgeoning) double-dip: every extra land drop is simultaneously a **landfall trigger for nine different payoffs** (Scute Swarm, Avenger of Zendikar, Lotus Cobra, Rampaging Baloths, Zendikar's Roil, Tireless Tracker, Courser of Kruphix, Primeval Bounty, and Ka-Zar's Zabu token) AND a Kodama trigger. Kamahl's combat-trigger pump + trample is the closing finisher once the board is wide.

## The 100

### Lands (37)
Bonders' Enclave, Castle Garenbrig, Demolition Field, Evolving Wilds, Mosswort Bridge, Rogue's Passage, Terramorphic Expanse, War Room, Boseiju Who Endures, Yavimaya Cradle of Growth, Hickory Woodlot, Blighted Woodland, 25x Forest

### Ramp (11)
Sol Ring, Llanowar Elves, Elvish Mystic, Sakura-Tribe Elder, Nature's Lore, Three Visits, Cultivate, Exploration, Azusa Lost but Seeking, Loot Exuberant Explorer, Burgeoning
NOTE: Exploration/Azusa/Loot/Burgeoning were moved here from cut candidates specifically because they feed Kodama and every landfall payoff simultaneously — higher priority than one-shot ramp spells for THIS deck.

### Draw (10)
Sylvan Library, Tireless Tracker, Beast Whisperer, Elemental Bond, Guardian Project, Toski Bearer of Secrets, Ohran Frostfang, Greater Good, Return of the Wildspeaker, Courser of Kruphix
NOTE: Courser of Kruphix is a new add (found via full-database query) — plays lands off the top, gains life, wasn't in the original 181-card pool.

### Landfall payoffs / token engines (7)
Scute Swarm, Avenger of Zendikar, Lotus Cobra, Ka-Zar of the Savage Land, Rampaging Baloths, Multani Yavimaya's Avatar, Zendikar's Roil
NOTE: this category is the deck's actual best synergy with Kodama per the rules finding above — token/permanent generators, not just "more mana."

### Counters / Hydras (4)
Kalonian Hydra, Managorger Hydra, The Earth Crystal, Yorvo Lord of Garenbrig
NOTE: all four only grow counters already on a creature, or carry them on themselves — none of them spread counters onto new creatures. That's deliberate, see the counters preference below.

### Finishers / big bodies (4)
Craterhoof Behemoth, Elder Gargaroth, Vorinclex Voice of Hunger, Unnatural Growth

### Evasion (2)
Nylea God of the Hunt, Rhonas the Indomitable

### Protection (9)
Heroic Intervention, Swiftfoot Boots, Lightning Greaves, Seedborn Muse, Sylvan Safekeeper, Veil of Summer, Asceticism, Bear Umbra, Temur Sabertooth

### Recursion / Tutors (5)
Eternal Witness, Green Sun's Zenith, Finale of Devastation, Regrowth, Woodland Bellower

### Removal (7)
Beast Within, Kenrith's Transformation, Primal Might, Ulamog the Ceaseless Hunger, Warping Wail, Reclamation Sage, Silverback Elder

### Pump (1)
Blanchwood Armor

### Tokens (1)
Primeval Bounty

**Total: 2 commanders + 37 lands + 61 spells = 100**

## Swap applied Sept 20, 2026 (4 cards)

| In | Out | Why |
|---|---|---|
| Temur Sabertooth {2}{G}{G} 4/3 | Bristly Bill, Spine Sower | Bristly Bill spread +1/+1 counters onto new creatures every land drop (see counters preference). Sabertooth makes every ETB in the deck repeatable and doubles as protection. Also saves $32.97. |
| Unnatural Growth {1}{G}{G}{G}{G} | Overrun | **Kamahl already is Overrun**, from the command zone, every turn, for free — same +3/+3 and trample, same wording. Unnatural Growth instead *doubles* power and toughness, and does it on every opponent's combat too. |
| Reclamation Sage {2}{G} 2/1 | Nissa, Worldsoul Speaker | Nissa banked 2 energy per landfall and needed 8 to cast one permanent free — one free spell per four land drops, and nothing else in the deck uses energy. Sage answers an artifact or enchantment, loops with Sabertooth, and is a Woodland Bellower tutor target. |
| Silverback Elder {2}{G}{G}{G} 5/7 | Gift of the Gargantuan | Gift of the Gargantuan was **filed under Removal and is not removal** — it digs 4 for a creature and/or land, which is redundant next to 10 draw engines. Silverback Elder turns every hard-cast creature into a Naturalize, a land, or 4 life. |

### The gap this fixed
Before the swap the deck had **three** cards that could destroy an artifact or enchantment, and realistically two: **Beast Within** (3 mana, hits any permanent, hands them a 3/3), **Boseiju, Who Endures** (channel from a land, one shot, opponents only), and **Ulamog** (ten mana). For a mono-green deck — the color with the best artifact and enchantment removal in the game — that was the single biggest weakness in the list. It's now five sources, one of which (Reclamation Sage + Temur Sabertooth) is repeatable.

## Counters preference (owner's call, Sept 20, 2026)
**No cards that spread +1/+1 counters across many creatures.** In paper this means carrying a die for every creature that has counters, which is a hassle. Cards that only *grow* counters already on a creature, or that keep them on a single body, are fine.

- **Out for this reason:** Bristly Bill Spine Sower (landfall, counter on target creature), and keep out Scythecat Cub, Surrak and Goreclaw, and Mossborn Hydra. Vorinclex, Monstrous Raider was also considered and rejected here — it's a counter doubler, and Voice of Hunger stays in the deck instead.
- **Fine and staying:** The Earth Crystal, Kalonian Hydra, Yorvo, Managorger Hydra (self-only or grow-what's-there), and **Primeval Bounty**, which the owner likes and which lets you pick the target each time.
- Note for future conversations: Bristly Bill, Primeval Bounty and The Earth Crystal's activated ability all say **target** creature, so they never *force* you to spread — you can always point them at one creature. Bristly Bill was still cut on preference.

## Close calls — next in line, database-verified and legal
- **World Shaper** {3}{G} 3/3 — mills 3 on attack; when it dies, returns **all** land cards from your graveyard to the battlefield tapped. With Greater Good already in the deck as a sac outlet, that's a huge landfall/Kodama turn. No counters involved.
- **Thrashing Brontodon** {1}{G}{G} 3/4 — {1}, sacrifice: destroy target artifact or enchantment. A third body-plus-answer if the removal still feels thin.
- **Krosan Grip** {2}{G} instant — destroy target artifact or enchantment, with split second, so while it's on the stack nobody can cast spells or activate non-mana abilities in response. The cleanest answer to a combo piece.
- **Rejected on purpose: Bane of Progress.** Its ETB destroys **all** artifacts and enchantments, which in this deck means your own Sol Ring, The Earth Crystal, Primeval Bounty, Zendikar's Roil, Sylvan Library, Exploration, Burgeoning, Asceticism, Bear Umbra, plus Courser of Kruphix and Nylea (both enchantment creatures) and any Clue tokens. Far too much collateral.

## Cut from the original 181-card pool (redundant with something stronger staying in, not mistakes)
Fyndhorn Elves, Druid of the Cowl, Ilysian Caryatid, Rampant Growth, Wood Elves, Farhaven Elf, Explosive Vegetation, Skyshroud Claim, Springbloom Druid, Shared Roots (explicitly filler), Case of the Locked Hothouse, Fanatic of Rhonas, Goreclaw Terror of Qal Sisma, Nissa Resurgent Animist, Rampant Rejuvenator, Seedship Agrarian, Stone-Seeder Hierophant, Tireless Provisioner, World Shaper, Yavimaya Elder, Adventure Awaits, Adventurous Impulse, Disciple of Freyalise, Genesis Hydra, Hunter's Insight, Inspiring Call, Momentous Fall, Pelakka Wurm, Regal Force, Rishkar's Expertise, Silverback Shaman, Soul's Majesty, Vizier of the Menagerie, Baloth Woodcrasher, Greensleeves Maro-Sorcerer, Glacier Godmaw, Khalni Heart Expedition, Territorial Scythecat, Sazh's Chocobo, Retreat to Kazandu, Grazing Gladehart, Embodiment of Insight, Undergrowth Champion, Tifa Lockhart, Scythecat Cub, Surrak and Goreclaw, Mossborn Hydra, Oran-Rief Hydra, Hooded Hydra, Darksteel Colossus, Overwhelming Stampede, Quakestrider Ceratops, Stonehoof Chieftain, Thrashing Brontodon, Archetype of Endurance, both Ulamog the Infinite Gyre, Commander's Plate, Mithril Coat, Darksteel Plate, Autumn's Veil, Spearbreaker Behemoth, Avoid Fate, Alpha Authority, Aspect of Mongoose, Sheltering Word, Ranger's Guile, Canopy Cover, Molting Skin, Broken Fall, Eldrazi Monument, Creeping Renaissance, Praetor's Counsel, Splendid Reclamation, Greenwarden of Murasa, Deadwood Treefolk, Khalni Ambush, Bridgeworks Battle, Ezuri's Predation.

Also cut in the Sept 20 swap: Bristly Bill Spine Sower, Overrun, Nissa Worldsoul Speaker, Gift of the Gargantuan.

## Vanilla cuts (confirmed no abilities beyond a bare keyword — never made it into the 181-card pool)
Colossal Dreadmaw, Gigantosaurus, Aggressive Mammoth, Steel Leaf Champion, Frenzied Baloth.

## Reserved List note
Gaea's Cradle was considered but is Reserved List — not reprinted, ~$1,600+, skipped.

## Game Changers
Only **Seedborn Muse** is confirmed on the official Game Changers list among cards in this deck. Vorinclex is NOT currently on the GC list. The GC list changes over time — recheck it against the current official list rather than from memory before calling a bracket.

## Rules Notes Worked Out
- **Kodama's trigger** fires off ANY permanent entering under your control (lands, tokens, creatures) — not landfall-specific. Confirmed against real oracle text Sept 19, 2026.
- **Unnatural Growth triggers on EACH combat, not just yours.** "At the beginning of each combat, double the power and toughness of each creature you control until end of turn." That includes every opponent's combat, so your blockers are doubled when you're attacked. Easy to misplay as a my-turn-only effect.
- **Unnatural Growth + Kamahl stack order matters.** Both trigger at the beginning of combat on your turn and you control both, so you choose the order they go on the stack — and the stack resolves last-on-first-off. Put **Unnatural Growth's trigger on the stack first and Kamahl's on top**, so Kamahl resolves first and the doubling counts the +3/+3. Kodama goes 6/6 → 9/9 → **18/18** that way, versus 12/12 → 15/15 if you get it backwards.
- **Overrun was cut because Kamahl duplicates it exactly** — same +3/+3, same trample, same until-end-of-turn, but repeatable from the command zone for free. Trample is still covered by Kamahl, Nylea (other creatures you control have trample) and Craterhoof.
- **Zabu is a legendary token.** Bouncing and recasting Ka-Zar while Zabu is alive does NOT net a second Cat — the legend rule makes you bin one, and you keep the original carrying its counters. You do still get the Kodama trigger off the token entering, plus a fresh Ka-Zar ETB.
- **Temur Sabertooth's indestructible is conditional.** "{1}{G}: You may return another creature you control to its owner's hand. **If you do**, this creature gains indestructible until end of turn." No bounce, no indestructible. Its real job is re-using ETBs (Reclamation Sage, Eternal Witness, Woodland Bellower, Avenger of Zendikar) and saving a creature from targeted removal by bouncing it.
- **Silverback Elder only triggers on CAST creature spells.** It misses everything Kodama puts onto the battlefield for free, every token, and the creatures fetched by Woodland Bellower, Green Sun's Zenith and Finale of Devastation. Still worth it for repeatable artifact/enchantment destruction on a 5/7 body, but don't count the free permanents.
- **Woodland Bellower puts its target onto the battlefield**, so it's two Kodama triggers off one card. Live targets in this build include Reclamation Sage, Eternal Witness, Tireless Tracker, Scute Swarm, Lotus Cobra, Managorger Hydra, Courser of Kruphix, Sakura-Tribe Elder and the mana dorks (nonlegendary, green, MV 3 or less).
- **The Earth Crystal doubles ETB counters too.** It replaces counters being put on any creature you control, so Yorvo enters as an 8/8 and Kalonian Hydra as an 8/8 (which then doubles again when it attacks).
- **Ohran Frostfang vs Ohran Viper**: Frostfang is the one in the deck — team deathtouch on attack + draw off combat damage to a player. Viper only affects itself.
- **Toski and Ohran Frostfang stack** — both draw on combat damage to a player, so a connecting creature draws two.
- Full oracle text for every card in the final 100 (and the cut candidates) was pulled from the live database and checked for color identity, Commander legality, and interactions before finalizing this list.

## Status
**Built.** This is a real, finalized 100-card list, not a staging pool. Physical assembly still depends on owning/acquiring the actual cards (e.g. the Tramplesaurus Rex precon components).

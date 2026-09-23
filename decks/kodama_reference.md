# Cards Reference — Kodama of the East Tree // Kamahl, Heart of Krosa EDH Deck

**STATUS: BUILT (100 cards).** Original build confirmed Sept 19, 2026; **4-card swap applied Sept 20, 2026** to fix the deck's artifact/enchantment removal gap and to pull out the +1/+1 counter spreader. Cut down from the 181-card Archidekt staging pool after a full database cross-check (existence, color identity, Commander legality, and full oracle text for every card) plus a synergy pass looking for interactions the category tags alone would've missed.

Staging link (original 181-card pool, now superseded by the 100 below): https://archidekt.com/decks/26413180/kodoma_of_the_mono_tree

## Companion files in this folder
- `kodama_decklist.txt` — the flat 100, one card per line, mass-entry format for ordering.
- `kodama_buylist.md` — which cards come from the Tramplesaurus Rex precon and which still need buying, with prices.
- `kodama_purchase_list.txt` — the cards to buy, bare lines only, for mass-entry importers.
- `kodama_play_guide.pdf` — 8-page play guide: the Kodama trigger explained properly, the free-land chain, Scute Swarm's doubling, the Sabertooth loops, Woodland Bellower targets, and a misplays list.

## Base
Started from **Tramplesaurus Rex**, the mono-green precon from the Foundations Commander Decks set. Stock commander was Ghalta, Primal Hunger.

## Commanders (Partners) — 2
**Kodama of the East Tree** — {4}{G}{G} — Legendary Creature — Spirit — **6/6** — Reach
"Whenever another permanent you control enters, if it wasn't put onto the battlefield with this ability, you may put a permanent card with equal or lesser mana value from your hand onto the battlefield." Partner.

**Kamahl, Heart of Krosa** — {6}{G}{G} — Legendary Creature — Human Druid — **5/5**
"At the beginning of combat on your turn, creatures you control get +3/+3 and gain trample until end of turn. {1}{G}: Until end of turn, target land you control becomes a 1/1 Elemental creature with vigilance, indestructible, and haste. It's still a land." Partner.

## Game Plan / Key Rules Finding
Kodama's trigger is **not landfall-specific — it fires off ANY permanent entering under your control**, including tokens (creature or artifact). This means token generators are the deck's real engine, not just landfall payoffs: every token made is a free Kodama trigger, which can drop another permanent from hand for free, which can chain into more triggers if that permanent is itself a token-maker or a land. Extra-land-drop enablers (Exploration, Azusa, Loot, Burgeoning) double-dip: every extra land drop is simultaneously a **landfall trigger for nine different payoffs** (Scute Swarm, Avenger of Zendikar, Lotus Cobra, Rampaging Baloths, Dancing from Dark to Dawn, Tireless Tracker, Courser of Kruphix, Primeval Bounty, and Ka-Zar's Zabu token) AND a Kodama trigger. Kamahl's combat-trigger pump + trample is the closing finisher once the board is wide.

## The 100

### Lands (36)
Bonders' Enclave, Castle Garenbrig, Demolition Field, Windswept Heath, Mosswort Bridge, Rogue's Passage, Verdant Catacombs, War Room, Boseiju Who Endures, Yavimaya Cradle of Growth, Blighted Woodland, Bala Ged Recovery, 24x Forest
NOTE: Windswept Heath and Verdant Catacombs replaced Evolving Wilds and Terramorphic Expanse on Sept 20, 2026. A fetchland is **two landfall triggers and two Kodama triggers off one card** — the fetchland enters, then the Forest it fetches enters. The real fetches beat Evolving Wilds because they enter untapped AND put the Forest in untapped ("put it onto the battlefield", no "tapped"), so both triggers happen the turn you play it with no tempo loss. All five green-capable fetches (Windswept Heath, Verdant Catacombs, Wooded Foothills, Misty Rainforest, Prismatic Vista) are **functionally identical in mono-green** — the second basic type they name is irrelevant. Buy on price alone.
NOTE: **Bala Ged Recovery // Bala Ged Sanctuary** took a Forest slot (25 -> 24), so land slots stay at 37. Front face is a {2}{G} sorcery returning any card from your graveyard to hand; back face is a land that enters tapped. Like the other MDFCs looked at for this deck, the back face is a plain `Land`, **not Forest-typed**, so Nature's Lore and Three Visits cannot fetch it.

### Ramp (14)
Sol Ring, Llanowar Elves, Elvish Mystic, Sakura-Tribe Elder, Nature's Lore, Three Visits, Exploration, Azusa Lost but Seeking, Loot Exuberant Explorer, Burgeoning, Growing Rites of Itlimoc, Radagast of Rhosgobel, **Circle of Dreams Druid**, **The Great Henge**
NOTE: Exploration/Azusa/Loot/Burgeoning were moved here from cut candidates specifically because they feed Kodama and every landfall payoff simultaneously — higher priority than one-shot ramp spells for THIS deck.

### Draw (8)
Sylvan Library, Beast Whisperer, Elemental Bond, Guardian Project, Toski Bearer of Secrets, Ohran Frostfang, Return of the Wildspeaker, Courser of Kruphix
NOTE: Courser of Kruphix is a new add (found via full-database query) — plays lands off the top, gains life, wasn't in the original 181-card pool.

### Landfall payoffs / token engines (10)
Scute Swarm, Avenger of Zendikar, Lotus Cobra, Ka-Zar of the Savage Land, Rampaging Baloths, Multani Yavimaya's Avatar, Dancing from Dark to Dawn, **Tireless Provisioner**, **Ancient Greenwarden**, **Sandwurm Convergence**
NOTE: this category is the deck's actual best synergy with Kodama per the rules finding above — token/permanent generators, not just "more mana."

### Counters / Hydras (2)
Kalonian Hydra, The Earth Crystal
NOTE: all four only grow counters already on a creature, or carry them on themselves — none of them spread counters onto new creatures. That's deliberate, see the counters preference below.

### Finishers / big bodies (4)
Craterhoof Behemoth, Elder Gargaroth, Vorinclex Voice of Hunger, Unnatural Growth

### Evasion (2)
Nylea God of the Hunt, Rhonas the Indomitable

### Protection (9)
Heroic Intervention, Swiftfoot Boots, Lightning Greaves, Seedborn Muse, Sylvan Safekeeper, Veil of Summer, Asceticism, Bear Umbra, Temur Sabertooth

### Recursion / Tutors (6)
Eternal Witness, Green Sun's Zenith, Finale of Devastation, Natural Order, Woodland Bellower, Genesis
NOTE: **Genesis works from the graveyard, and a board wipe is its enabler.** "At the beginning of your upkeep, if this creature is in your graveyard, you may pay {2}{G}. If you do, return target creature card from your graveyard to your hand." A wrath puts Genesis in the yard alongside everything else it will rebuild, which is exactly what this deck needs, since a wide board of fat creatures is a wrath magnet. It returns to HAND, not the battlefield, so recovery is slow against a curve topping out at 10 mana - inevitable, not fast.

### Removal (6)
Beast Within, Kenrith's Transformation, **Terastodon**, Ulamog the Ceaseless Hunger, Reclamation Sage, Silverback Elder

### Tokens (1)
Primeval Bounty

**Total: 2 commanders + 36 lands + 62 spells = 100**

## Swap applied Sept 20, 2026 (4 cards)

| In | Out | Why |
|---|---|---|
| Temur Sabertooth {2}{G}{G} 4/3 | Bristly Bill, Spine Sower | Bristly Bill spread +1/+1 counters onto new creatures every land drop (see counters preference). Sabertooth makes every ETB in the deck repeatable and doubles as protection. Also saves $32.97. |
| Unnatural Growth {1}{G}{G}{G}{G} | Overrun | **Kamahl already is Overrun**, from the command zone, every turn, for free — same +3/+3 and trample, same wording. Unnatural Growth instead *doubles* power and toughness, and does it on every opponent's combat too. |
| Reclamation Sage {2}{G} 2/1 | Nissa, Worldsoul Speaker | Nissa banked 2 energy per landfall and needed 8 to cast one permanent free — one free spell per four land drops, and nothing else in the deck uses energy. Sage answers an artifact or enchantment, loops with Sabertooth, and is a Woodland Bellower tutor target. |
| Silverback Elder {2}{G}{G}{G} 5/7 | Gift of the Gargantuan | Gift of the Gargantuan was **filed under Removal and is not removal** — it digs 4 for a creature and/or land, which is redundant next to 10 draw engines. Silverback Elder turns every hard-cast creature into a Naturalize, a land, or 4 life. |

### The gap this fixed
Before the swap the deck had **three** cards that could destroy an artifact or enchantment, and realistically two: **Beast Within** (3 mana, hits any permanent, hands them a 3/3), **Boseiju, Who Endures** (channel from a land, one shot, opponents only), and **Ulamog** (ten mana). For a mono-green deck — the color with the best artifact and enchantment removal in the game — that was the single biggest weakness in the list. It's now five sources, one of which (Reclamation Sage + Temur Sabertooth) is repeatable.

## Second swap, later Sept 20, 2026 (3 cards)

| In | Out | Why |
|---|---|---|
| Growing Rites of Itlimoc // Itlimoc, Cradle of the Sun | Blanchwood Armor | Cast as a {2}{G} enchantment (so it takes a spell slot, not a land slot), digs 4 for a creature on entry, then transforms at your end step once you control four creatures — trivial here, Scute Swarm alone does it. The back face taps for {G} per creature: an affordable Gaea's Cradle. **Kamahl already pumps the whole team +3/+3 with trample every turn for free**, which makes Blanchwood Armor the most redundant card in the deck — a worse pump on one creature, on an Aura that loses two cards to one removal spell, in a deck built to go wide. |
| Windswept Heath | Evolving Wilds | Real fetch enters untapped and puts the Forest in untapped, so both landfall triggers land the turn you play it. |
| Verdant Catacombs | Terramorphic Expanse | Same. Bought on price — all five green-capable fetches are identical in mono-green. |

NOTE: **Warping Wail was considered for this cut and kept at the time** — awkward off only six colorless sources, but the only card in the deck that could counter anything, and its Eldrazi Scion mode makes a token. **Superseded: it was cut in the sixth swap below for Radagast of Rhosgobel.** The deck now has no counterspell at all; that is a known, accepted gap.

## Third swap, Sept 20, 2026 (2 cards)

| In | Out | Why |
|---|---|---|
| Genesis {4}{G} 4/4 | Greater Good | **Board wipe insurance.** Genesis only works from the graveyard, and a wrath puts it there for free alongside everything it will rebuild — this deck's wide board of fat creatures is a wrath magnet. Greater Good went on owner preference: ten other draw sources, and the sacrifice play pattern isn't wanted. Note the stated reason elsewhere ("it forces you to sacrifice your board") overstates it — Greater Good's sacrifice was optional. |
| Bala Ged Recovery // Bala Ged Sanctuary | 1x Forest | Land slot that can instead be a {2}{G} sorcery returning any card from the graveyard. Land slots unchanged at 37. |

NOTE: **Natural Order was NOT added**, despite being proposed alongside these. It reads "As an additional cost to cast this spell, **sacrifice a green creature**" — mandatory, where Greater Good's sacrifice was optional. Cutting Greater Good to avoid sacrificing creatures and then adding Natural Order is contradictory. **Worldly Tutor was also skipped**: $35.03 to put a creature on *top of your library*, when Green Sun's Zenith and Finale of Devastation already put creatures straight onto the battlefield.

NOTE: **Cloudstone Curio and Timeless Witness are still open.** Curio ({3}, colorless, $13.70) bounces a permanent sharing a type whenever a nonartifact permanent enters, which pairs with Kodama putting lands back down for free — powerful, a known combo piece worth a bracket check, and it adds an optional trigger on *every* permanent entering, which is a real complexity cost with Scute Swarm out. Timeless Witness is MV 4, so unlike Eternal Witness (MV 3) it is **not** a Woodland Bellower target; run it alongside, don't replace.

## Fourth swap, Sept 20, 2026 (1 card)

| In | Out | Why |
|---|---|---|
| Natural Order {2}{G}{G} (**Game Changer**) | Regrowth | Four mana, sacrifice a green creature, put a green creature from your library onto the battlefield. **The sacrifice cost is paid with a token here** — Scute Insects, Avenger's Plants, Baloths' Beasts, Zendikar's Roil Elementals and Zabu are all green creatures — so it does not cost you a real body. Target is Craterhoof Behemoth, which also gives a Kodama trigger as it enters. Regrowth went because **Bala Ged Recovery has identical text and is also a land**, and Genesis now covers repeat creature recursion; Regrowth's only edge was one mana. |

NOTE: **Ulamog is NOT a legal Natural Order target.** Natural Order searches for a *green creature card* and Ulamog, the Ceaseless Hunger has an empty colors array — it is colorless. Legal targets in this deck are Craterhoof Behemoth, Vorinclex Voice of Hunger, Avenger of Zendikar, Woodland Bellower and the rest of the green creatures.

NOTE: three other cards were considered in the same pass and **rejected**:
- **Worldly Tutor** ({G} instant, Game Changer, $35.03) — puts the creature on *top of your library*, not in hand or on the battlefield. Green Sun's Zenith and Finale of Devastation both put creatures straight onto the battlefield and are not Game Changers, so this would spend a bracket slot on the worst tutor of the three.
- **Biorhythm** ({6}{G}{G}, Game Changer, $34.43) — sets each player's life total to their creature count. Most opponents have creatures, so it usually leaves them at 2 or 3 life rather than dead. Craterhoof costs the same eight mana, actually kills, is not a Game Changer, and is already in the deck. It also sets your own life to your creature count.
- **Cloudstone Curio** ({3}, not a Game Changer, $13.70) — powerful, but it puts an optional trigger on every nonartifact permanent entering, which with Scute Swarm out means dozens of decisions per turn. Deferred on complexity, not power.
- **Timeless Witness** — recursion is already seven deep, and at MV 4 Woodland Bellower cannot fetch it.

## Fifth swap, Sept 20, 2026 (1 card)

| In | Out | Why |
|---|---|---|
| Dancing from Dark to Dawn {3}{G}{G} | Zendikar's Roil | **A strict upgrade.** Identical mana cost, identical enchantment type, identical landfall payoff (a 2/2 green token — Bear instead of Elemental, and nothing in the deck cares about creature type), plus an entire extra ability: "Whenever you cast a creature spell, put X +1/+1 counters on target creature you control, where X is that spell's mana value." Casting Craterhoof puts 8 counters on something. Costs $7.86 against Zendikar's Roil's $1.39; that price gap is the only downside. |

NOTE: the counter half says **target** creature you control, so it never forces you to spread counters — point it at one creature and it stays one die. Same shape as Primeval Bounty, which the owner kept for that reason.

NOTE: several other cards were checked in the same pass and ruled out.
- **The Astonishing Ant-Man** ({G}{U}) and **Tear Asunder** are both illegal here. Ant-Man is green *and* blue, so its identity is [G, U]. Tear Asunder's mana cost is a clean {1}{G}, but its **Kicker {1}{B}** puts black in its identity — costs in rules text count. Easy trap: a green mana cost does not mean a green identity.
- **Beorn's Hospitality** ({1}{G}) is Bristly Bill's ability on an enchantment — landfall, +1/+1 counter on target creature. Already rejected once under the counters preference.
- **Ironscale Hydra** ({3}{G}{G} 5/5) prevents all combat damage dealt to it and grows instead. Unkillable blocker, die-friendly, but does nothing for the Kodama engine.
- **Radagast of Rhosgobel** — no longer a close call; **added in the sixth swap below.**
- **Radagast the Brown** ({2}{G}{G} 2/5) digs on every **nontoken** creature entering, and tokens are most of this deck's ETBs.

## Sixth swap, Sept 20, 2026 (1 card)

| In | Out | Why |
|---|---|---|
| Radagast of Rhosgobel {2}{G}{G} 2/5, $6.65 | Warping Wail | "The first creature spell you cast each turn costs {2} less to cast and can be cast as though it had flash." The discount is live every turn against a curve of Craterhoof 8, Vorinclex 8, Ulamog 10, Avenger 7, Bellower and Multani 6, and a pile of 5s. It also cheapens the **Temur Sabertooth loops**: bouncing and recasting Reclamation Sage drops from {1}{G} + {2}{G} to {1}{G} + **{G}**. Warping Wail needed {C} off only six colorless sources in a deck of 24 Forests, and its modes were narrow. Trading a card you often cannot cast for a creature also means one more body and one more Kodama trigger. |

NOTE: **the discount only applies to creature spells you CAST** — same caveat as Silverback Elder. It does nothing for creatures Kodama puts onto the battlefield, for tokens, or for anything Woodland Bellower, Green Sun's Zenith, Natural Order or Finale of Devastation puts down, since none of those are cast.

NOTE: Radagast is **legendary**, so Woodland Bellower (nonlegendary only) cannot fetch it. Green Sun's Zenith and Natural Order can.

NOTE: **the deck now has zero counterspells.** Warping Wail was the only one. That is an accepted cost, not an oversight — mono-green barely has the option, and the card was frequently uncastable.

## Counters preference (owner's call, Sept 20, 2026)
**No cards that spread +1/+1 counters across many creatures.** In paper this means carrying a die for every creature that has counters, which is a hassle. Cards that only *grow* counters already on a creature, or that keep them on a single body, are fine.

- **Out for this reason:** Bristly Bill Spine Sower (landfall, counter on target creature), and keep out Scythecat Cub, Surrak and Goreclaw, and Mossborn Hydra. Vorinclex, Monstrous Raider was also considered and rejected here — it's a counter doubler, and Voice of Hunger stays in the deck instead.
- **Fine and staying:** The Earth Crystal, Kalonian Hydra, Yorvo, Managorger Hydra (self-only or grow-what's-there), and **Primeval Bounty**, which the owner likes and which lets you pick the target each time.
- Note for future conversations: Bristly Bill, Primeval Bounty and The Earth Crystal's activated ability all say **target** creature, so they never *force* you to spread — you can always point them at one creature. Bristly Bill was still cut on preference.

## Close calls — next in line, database-verified and legal
- **World Shaper** {3}{G} 3/3 — mills 3 on attack; when it dies, returns **all** land cards from your graveyard to the battlefield tapped. With Greater Good already in the deck as a sac outlet, that's a huge landfall/Kodama turn. No counters involved.
- **Thrashing Brontodon** {1}{G}{G} 3/4 — {1}, sacrifice: destroy target artifact or enchantment. A third body-plus-answer if the removal still feels thin.
- **Krosan Grip** {2}{G} instant — destroy target artifact or enchantment, with split second, so while it's on the stack nobody can cast spells or activate non-mana abilities in response. The cleanest answer to a combo piece.
- **Nykthos, Shrine to Nyx** — flagged by the owner as a possible future add. {2}, {T}: add mana of a chosen color equal to your devotion to it, which is high in mono-green. Caveat: it only makes {C} otherwise, and the deck already runs five colorless-only lands while casting Silverback Elder {2}{G}{G}{G}, Craterhoof {5}{G}{G}{G} and Unnatural Growth {1}{G}{G}{G}{G}. That's mitigated only while Yavimaya, Cradle of Growth is on the battlefield making every land a Forest — a one-card dependency.
- **Grasslands ($0.35) and Mountain Valley ($0.30)** — budget double-trigger lands. They fetch a Forest **untapped** with no life payment, but they enter tapped, so the two landfall triggers split across turns. That makes them a sidegrade to Evolving Wilds rather than an upgrade. Worth it only as a replacement for **Hickory Woodlot** (enters tapped, two activations, then sacrifices itself) — not as extra tapped lands in a deck casting 8-drops.

**Mosswort Bridge stays — do not suggest cutting it again.** An earlier review called its hideaway payoff too demanding. It isn't: the condition is 10 total power across your creatures, Kodama alone is a 6/6, and **Kamahl gives the whole team +3/+3 at the beginning of combat**, so you can activate the Bridge mid-combat after that trigger resolves and two creatures clear the bar. The payoff is playing the hidden card **without paying its mana cost**, off a library full of 6-to-10 drops (Craterhoof, Ulamog, Vorinclex, Avenger of Zendikar). A free 8-drop is worth a land that enters tapped, and playing a creature that way also triggers Silverback Elder.
- **More fetchlands** — Wooded Foothills, Misty Rainforest and Prismatic Vista all do exactly what Windswept Heath and Verdant Catacombs do here. Only buy on price.
- **Rejected on purpose: Bane of Progress.** Its ETB destroys **all** artifacts and enchantments, which in this deck means your own Sol Ring, The Earth Crystal, Primeval Bounty, Zendikar's Roil, Sylvan Library, Exploration, Burgeoning, Asceticism, Bear Umbra, plus Courser of Kruphix and Nylea (both enchantment creatures) and any Clue tokens. Far too much collateral.

## Cut from the original 181-card pool (redundant with something stronger staying in, not mistakes)
Fyndhorn Elves, Druid of the Cowl, Ilysian Caryatid, Rampant Growth, Wood Elves, Farhaven Elf, Explosive Vegetation, Skyshroud Claim, Springbloom Druid, Shared Roots (explicitly filler), Case of the Locked Hothouse, Fanatic of Rhonas, Goreclaw Terror of Qal Sisma, Nissa Resurgent Animist, Rampant Rejuvenator, Seedship Agrarian, Stone-Seeder Hierophant, Tireless Provisioner, World Shaper, Yavimaya Elder, Adventure Awaits, Adventurous Impulse, Disciple of Freyalise, Genesis Hydra, Hunter's Insight, Inspiring Call, Momentous Fall, Pelakka Wurm, Regal Force, Rishkar's Expertise, Silverback Shaman, Soul's Majesty, Vizier of the Menagerie, Baloth Woodcrasher, Greensleeves Maro-Sorcerer, Glacier Godmaw, Khalni Heart Expedition, Territorial Scythecat, Sazh's Chocobo, Retreat to Kazandu, Grazing Gladehart, Embodiment of Insight, Undergrowth Champion, Tifa Lockhart, Scythecat Cub, Surrak and Goreclaw, Mossborn Hydra, Oran-Rief Hydra, Hooded Hydra, Darksteel Colossus, Overwhelming Stampede, Quakestrider Ceratops, Stonehoof Chieftain, Thrashing Brontodon, Archetype of Endurance, both Ulamog the Infinite Gyre, Commander's Plate, Mithril Coat, Darksteel Plate, Autumn's Veil, Spearbreaker Behemoth, Avoid Fate, Alpha Authority, Aspect of Mongoose, Sheltering Word, Ranger's Guile, Canopy Cover, Molting Skin, Broken Fall, Eldrazi Monument, Creeping Renaissance, Praetor's Counsel, Splendid Reclamation, Greenwarden of Murasa, Deadwood Treefolk, Khalni Ambush, Bridgeworks Battle, Ezuri's Predation.

Also cut, first Sept 20 swap: Bristly Bill Spine Sower, Overrun, Nissa Worldsoul Speaker, Gift of the Gargantuan.

Cut in the second Sept 20 swap: Blanchwood Armor, Evolving Wilds, Terramorphic Expanse.

Cut in the third through sixth Sept 20 swaps: Greater Good, 1x Forest, Regrowth, Zendikar's Roil, Warping Wail.

## Vanilla cuts (confirmed no abilities beyond a bare keyword — never made it into the 181-card pool)
Colossal Dreadmaw, Gigantosaurus, Aggressive Mammoth, Steel Leaf Champion, Frenzied Baloth.

## Reserved List note
Gaea's Cradle was considered but is Reserved List — not reprinted, ~$1,600+, skipped.

**Survival of the Fittest** was considered Sept 20, 2026 as a possible third Game Changer — it pairs well with Genesis, since discarding creatures to it is exactly what Genesis wants in the graveyard. Owner confirmed it is Reserved List and too expensive. **Skipped on price; do not re-suggest.** The third Game Changer slot stays deliberately empty.

## Game Changers — checked against the official list, Sept 20, 2026
**The deck runs TWO Game Changers: Seedborn Muse and Natural Order.** Owner targets Bracket 3, which allows three, so one slot remains free — deliberately left empty rather than spent on Worldly Tutor or Biorhythm (see the fourth swap above for why both were rejected).

Verified against the official Commander Brackets Game Changers list supplied by the owner. **scryfall.db cannot answer this** — it has no game-changer column and no such key in its `legalities` JSON. Archidekt's API does expose a `gameChanger` boolean, and it independently agreed: Seedborn Muse only.

Relevant entries from the official list (green and colorless are the only sections a mono-green deck can play):
- **Green:** Biorhythm, Crop Rotation, Gaea's Cradle, Natural Order, **Seedborn Muse**, Survival of the Fittest, Worldly Tutor.
- **Colorless:** Ancient Tomb, Chrome Mox, Field of the Dead, Glacial Chasm, Grim Monolith, Lion's Eye Diamond, Mana Vault, Mishra's Workshop, Mox Diamond, Panoptic Mirror, The One Ring, The Tabernacle at Pendrell Vale.

Consequences worth keeping:
- **Natural Order and Worldly Tutor are both Game Changers.** A separate chat proposed adding both; neither was applied. Adding them would have taken the deck to 3 of 3 and maxed out Bracket 3.
- **Ancient Tomb, Field of the Dead and Gaea's Cradle are Game Changers**, which adds a bracket cost to three lands already rejected on deck grounds (price, needing seven differently-named lands, and the Reserved List respectively).
- **Confirmed NOT Game Changers**, so they are free to add: Nykthos Shrine to Nyx, Growing Rites of Itlimoc, every fetchland, Grasslands, Mountain Valley, Cloudstone Curio, and Vorinclex Voice of Hunger.
- The list changes over time. Recheck against the current official list before calling a bracket; never state a card's status from memory.

## Rules Notes Worked Out
- **Kodama's trigger** fires off ANY permanent entering under your control (lands, tokens, creatures) — not landfall-specific. Confirmed against real oracle text Sept 19, 2026.
- **Unnatural Growth triggers on EACH combat, not just yours.** "At the beginning of each combat, double the power and toughness of each creature you control until end of turn." That includes every opponent's combat, so your blockers are doubled when you're attacked. Easy to misplay as a my-turn-only effect.
- **Unnatural Growth + Kamahl stack order matters.** Both trigger at the beginning of combat on your turn and you control both, so you choose the order they go on the stack — and the stack resolves last-on-first-off. Put **Unnatural Growth's trigger on the stack first and Kamahl's on top**, so Kamahl resolves first and the doubling counts the +3/+3. Kodama goes 6/6 → 9/9 → **18/18** that way, versus 12/12 → 15/15 if you get it backwards.
- **Overrun was cut because Kamahl duplicates it exactly** — same +3/+3, same trample, same until-end-of-turn, but repeatable from the command zone for free. Trample is still covered by Kamahl, Nylea (other creatures you control have trample) and Craterhoof.
- **Zabu is a legendary token.** Bouncing and recasting Ka-Zar while Zabu is alive does NOT net a second Cat — the legend rule makes you bin one, and you keep the original carrying its counters. You do still get the Kodama trigger off the token entering, plus a fresh Ka-Zar ETB.
- **Temur Sabertooth's indestructible is conditional.** "{1}{G}: You may return another creature you control to its owner's hand. **If you do**, this creature gains indestructible until end of turn." No bounce, no indestructible. Its real job is re-using ETBs (Reclamation Sage, Eternal Witness, Woodland Bellower, Avenger of Zendikar) and saving a creature from targeted removal by bouncing it.
- **Silverback Elder only triggers on CAST creature spells.** It misses everything Kodama puts onto the battlefield for free, every token, and the creatures fetched by Woodland Bellower, Green Sun's Zenith and Finale of Devastation. Still worth it for repeatable artifact/enchantment destruction on a 5/7 body, but don't count the free permanents.
- **Woodland Bellower puts its target onto the battlefield**, so it's two Kodama triggers off one card. Live targets in this build include Reclamation Sage, Eternal Witness, Tireless Tracker, Scute Swarm, Lotus Cobra, Managorger Hydra, Courser of Kruphix, Sakura-Tribe Elder and the mana dorks (nonlegendary, green, MV 3 or less).
- **A fetchland is two landfall triggers and two Kodama triggers.** The fetchland enters (trigger one), you crack it, the Forest enters (trigger two). With Scute Swarm at six or more lands that is two copies off a single card.
- **Growing Rites of Itlimoc transforms, it doesn't enter again.** The front face entering is a Kodama trigger because it's a permanent entering. The transform at your end step is **not** a land entering, so it gives no landfall trigger and no second Kodama trigger. Don't count on one.
- **The Earth Crystal doubles ETB counters too.** It replaces counters being put on any creature you control, so Yorvo enters as an 8/8 and Kalonian Hydra as an 8/8 (which then doubles again when it attacks).
- **Ohran Frostfang vs Ohran Viper**: Frostfang is the one in the deck — team deathtouch on attack + draw off combat damage to a player. Viper only affects itself.
- **Toski and Ohran Frostfang stack** — both draw on combat damage to a player, so a connecting creature draws two.
- Full oracle text for every card in the final 100 (and the cut candidates) was pulled from the live database and checked for color identity, Commander legality, and interactions before finalizing this list.

## Status
**Built.** This is a real, finalized 100-card list, not a staging pool. Physical assembly still depends on owning/acquiring the actual cards (e.g. the Tramplesaurus Rex precon components).

## Open item — Nykthos, Shrine to Nyx, not yet acquired (logged Sept 23, 2026)
Do not apply to the decklist until the card is in hand and the paper deck is updated.
No cut has been chosen — that decision is open.

**Why it is the one real gap.** The mana base itself is already strong and needs nothing: 35 lands,
34 of them untapped, only Castle Garenbrig conditional, 27 direct green sources. Yavimaya, Cradle of
Growth makes every land a Forest, so the colourless utility lands (War Room, Rogue's Passage,
Demolition Field, Bonders' Enclave, Blighted Woodland) all tap for {G} once it is down. There is no
fixing problem to solve in a mono-green deck.

What is missing is a payoff land rather than a fixing land:

  Nykthos, Shrine to Nyx — {T}: Add {C}. {2}, {T}: Choose a colour. Add mana of that colour equal
  to your devotion to that colour.

The deck carries **83 green pips across its permanents**, and Kamahl in particular is pip-heavy, so
six to ten devotion by turn five is routine. That turns {2} into six-plus green mana in a deck whose
plan is deploying enormous permanents and chaining Kodama triggers off them. It scales with the deck
doing what it already wants to do, which none of the current lands do.

**Considered and rejected as additions, Sept 23 2026:**
- Ancient Tomb — colourless ramp, but the constraint here is {G}{G} costs, not generic mana.
- Gaea's Cradle — strong but a much larger ask, and wants a creature-count check first.
- Wasteland / Strip Mine — land hate is a meta call, not a gap in this deck.
- Cavern of Souls — mono-colour, no fixing needed.
- Homeward Path — only worth it against a table that steals creatures.

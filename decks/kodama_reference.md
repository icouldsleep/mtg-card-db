# Cards Reference — Kodama of the East Tree // Kamahl, Heart of Krosa EDH Deck

**STATUS: BUILT (100 cards).** Original build confirmed Sept 19, 2026; **7-card swap applied Sept 20, 2026** after a re-check of the full Archidekt pool against the database. Cut down from the 181-card Archidekt staging pool after a full database cross-check (existence, color identity, Commander legality, and full oracle text for every card) plus a synergy pass looking for interactions the category tags alone would've missed.

Staging link (original 181-card pool, now superseded by the 100 below): https://archidekt.com/decks/26413180/kodoma_of_the_mono_tree

## Base
Started from **Tramplesaurus Rex**, the mono-green precon from the Foundations Commander Decks set. Stock commander was Ghalta, Primal Hunger.

## Commanders (Partners) — 2
**Kodama of the East Tree** — {4}{G}{G} — Legendary Creature — Spirit — **6/6** — Reach
"Whenever another permanent you control enters, if it wasn't put onto the battlefield with this ability, you may put a permanent card with equal or lesser mana value from your hand onto the battlefield." Partner.

**Kamahl, Heart of Krosa** — {6}{G}{G} — Legendary Creature — Human Druid — **5/5**
"At the beginning of combat on your turn, creatures you control get +3/+3 and gain trample until end of turn. {1}{G}: Until end of turn, target land you control becomes a 1/1 Elemental creature with vigilance, indestructible, and haste. It's still a land." Partner.

## Game Plan / Key Rules Finding
Kodama's trigger is **not landfall-specific — it fires off ANY permanent entering under your control**, including tokens (creature or artifact). This means token generators are the deck's real engine, not just landfall payoffs: every token made is a free Kodama trigger, which can drop another permanent from hand for free, which can chain into more triggers if that permanent is itself a token-maker or a land. Extra-land-drop enablers (Exploration, Azusa, Loot, Burgeoning, Case of the Locked Hothouse) double-dip: every extra land drop is simultaneously a landfall trigger for 9 different payoffs AND a Kodama trigger. Kamahl's combat-trigger pump + trample is the closing finisher once the board is wide.

## The 100

### Lands (37 land slots: 34 true lands + 3 modal double-faced cards)
Bonders' Enclave, Castle Garenbrig, Demolition Field, Evolving Wilds, Mosswort Bridge, Rogue's Passage, Terramorphic Expanse, War Room, Boseiju Who Endures, Yavimaya Cradle of Growth, Hickory Woodlot, Blighted Woodland, 22x Forest

**MDFCs occupying land slots (3)** — each is castable as a spell or played as a land:
- **Bridgeworks Battle // Tanglespan Bridgeworks** — {2}{G} Sorcery: target creature you control gets +2/+2, then fights up to one target creature you don't control. // Land: as it enters, you may pay 3 life; if you don't, it enters tapped. {T}: Add {G}.
- **Khalni Ambush // Khalni Territory** — {2}{G} Instant: target creature you control fights target creature you don't control. // Land: enters tapped. {T}: Add {G}.
- **Disciple of Freyalise // Garden of Freyalise** — {3}{G}{G}{G} **Creature — Elf Druid 3/3**: when it enters, you may sacrifice another creature; if you do, gain X life and draw X cards, where X is that creature's power. // Land: as it enters, you may pay 3 life; if you don't, it enters tapped. {T}: Add {G}.

NOTE (verified Sept 20, 2026): **none of the three back faces is a Forest-type land** — all three are plain `Land`. So Nature's Lore and Three Visits cannot fetch them, and they don't switch on Castle Garenbrig on their own. While Yavimaya, Cradle of Growth is on the battlefield every land is a Forest, which covers it situationally. Basics dropped 25 → 22 to make room; that's still a deep pool for Cultivate, Sakura-Tribe Elder, Evolving Wilds, Terramorphic Expanse, Blighted Woodland and Demolition Field, all of which fetch **basic** lands.

### Ramp (13)
Sol Ring, Llanowar Elves, Elvish Mystic, Sakura-Tribe Elder, Nature's Lore, Three Visits, Cultivate, Tireless Provisioner, Exploration, Azusa Lost but Seeking, Loot Exuberant Explorer, Burgeoning, Case of the Locked Hothouse
NOTE: Exploration/Azusa/Loot/Burgeoning/Hothouse were prioritized here specifically because they feed Kodama and every landfall payoff simultaneously — higher priority than one-shot ramp spells for THIS deck.

### Draw (10)
Sylvan Library, Tireless Tracker, Beast Whisperer, Elemental Bond, Guardian Project, Toski Bearer of Secrets, Ohran Frostfang, Greater Good, Return of the Wildspeaker, Courser of Kruphix

### Landfall payoffs / token engines (9)
Scute Swarm, Avenger of Zendikar, Lotus Cobra, Bristly Bill Spine Sower, Ka-Zar of the Savage Land, Rampaging Baloths, Multani Yavimaya's Avatar, Zendikar's Roil, Greensleeves Maro-Sorcerer
NOTE: this category is the deck's actual best synergy with Kodama per the rules finding above — token/permanent generators, not just "more mana."

### Counters / Hydras (4)
Kalonian Hydra, Managorger Hydra, The Earth Crystal, Yorvo Lord of Garenbrig

### Finishers / big bodies (4)
Craterhoof Behemoth, Elder Gargaroth, Vorinclex Voice of Hunger, Overrun

### Evasion (2)
Nylea God of the Hunt, Rhonas the Indomitable

### Protection (8)
Heroic Intervention, Swiftfoot Boots, Lightning Greaves, Seedborn Muse, Sylvan Safekeeper, Veil of Summer, Asceticism, Bear Umbra

### Recursion / Tutors (5)
Eternal Witness, Green Sun's Zenith, Finale of Devastation, Regrowth, Woodland Bellower

### Removal (5)
Beast Within, Kenrith's Transformation, Primal Might, Ulamog the Ceaseless Hunger, Thrashing Brontodon
Plus the two fight MDFCs in the land slots (Bridgeworks Battle, Khalni Ambush), for **7 real removal effects** without spending a spell slot on either.

### Tokens (1)
Primeval Bounty

**Total: 2 commanders + 37 land slots + 61 spells = 100**

## Swap applied Sept 20, 2026 (7 cards)

| In | Out | Why |
|---|---|---|
| Tireless Provisioner | Nissa, Worldsoul Speaker | Provisioner makes a Food or Treasure on **every** landfall — each token is a free Kodama trigger, and Treasure is ramp. Nissa only banks 2 energy per landfall (one free permanent per 4 land drops). |
| Greensleeves, Maro-Sorcerer | Blanchwood Armor | Greensleeves makes a 3/3 Badger on every landfall (another Kodama trigger) and is */* equal to your land count. Blanchwood Armor pumps one creature; this deck goes wide. |
| Case of the Locked Hothouse | Warping Wail | Extra land drop immediately; once solved (7+ lands) you play lands and cast creature **and** enchantment spells off the top. Warping Wail needs {C} to cast off a board of 22 Forests, and its modes are narrow. |
| Thrashing Brontodon | Gift of the Gargantuan | A 3/4 body that sacrifices ({1}, Sacrifice) to destroy an artifact or enchantment. Gift of the Gargantuan was **miscategorized as Removal** — it only digs 4 cards for a creature and/or land. |
| Bridgeworks Battle // Tanglespan Bridgeworks | 1x Forest | Land slot that can instead be a +2/+2 fight spell. |
| Khalni Ambush // Khalni Territory | 1x Forest | Land slot that can instead be an instant-speed fight. |
| Disciple of Freyalise // Garden of Freyalise | 1x Forest | Land slot that can instead be a 6-mana 3/3 creature with a sac-for-cards ETB. |

Net effect: real removal 5 → 7, three extra castable spells, land slots unchanged at 37.

## Corrections to earlier notes (database-verified Sept 20, 2026)
- **Disciple of Freyalise is a Creature — Elf Druid ({3}{G}{G}{G}, 3/3), not a 6-mana sacrifice spell.** An earlier analysis described it as "sacrifice a creature, draw and gain life equal to its power," which is the ETB of a *creature card* and reads like a conflation with Disciple of Bolas ({3}{B}). The correction argues **for** the include: a creature body is itself a Kodama trigger and a Craterhoof/Kamahl attacker, which a pure sacrifice spell would not be.
- **Tanglespan Bridgeworks is not a Forest-type land.** An earlier note called it "Forest-type, untapped for 3 life." The "pay 3 life or enter tapped" half is right; the Forest type is not. Same for Garden of Freyalise and Khalni Territory.
- **The three MDFCs are not free.** Khalni Territory always enters tapped, and the other two want 3 life each to enter untapped. Cheap in a deck with Courser of Kruphix and Primeval Bounty gaining life off landfall, but not literally costless.
- **Gift of the Gargantuan was filed under Removal and is not removal.** Fixed above.
- Artifact/enchantment answers before this swap were Beast Within, Boseiju's channel ability, **and Ulamog** (exiles two target permanents on cast) — Ulamog was missed in the earlier count.

## Close calls — next in line, all database-verified and legal
- **Surrak and Goreclaw** — {4}{G}{G} Legendary Creature — Human Bear 6/5, **color identity mono-green** (not Temur — checked). Trample, other creatures you control have trample, and whenever another **nontoken** creature enters, it gets a +1/+1 counter and haste — including the ones Kodama drops in for free. Strongest of this group.
- **Unnatural Growth** — {1}{G}{G}{G}{G} Enchantment. At the beginning of **each** combat, double the power and toughness of each creature you control. A finisher that stays on the battlefield; could replace Overrun.
- **Mossborn Hydra** — {2}{G}, enters with one +1/+1 counter, and landfall **doubles** its counters. Stacks hard with The Earth Crystal's counter-doubling.
- **Scythecat Cub** — {1}{G} 2/2 trample; landfall puts a counter on target creature, and the second landfall each turn doubles that creature's counters instead.
- **World Shaper** — {3}{G} 3/3; mills 3 on attack, and on death returns **all** land cards from your graveyard to the battlefield tapped. With Greater Good already in the deck as a sac outlet, that's a huge landfall/Kodama turn.

## Cut from the original 181-card pool (redundant with something stronger staying in, not mistakes)
Fyndhorn Elves, Druid of the Cowl, Ilysian Caryatid, Rampant Growth, Wood Elves, Farhaven Elf, Explosive Vegetation, Skyshroud Claim, Springbloom Druid, Shared Roots (explicitly filler), Fanatic of Rhonas, Goreclaw Terror of Qal Sisma, Nissa Resurgent Animist, Rampant Rejuvenator, Seedship Agrarian, Stone-Seeder Hierophant, Yavimaya Elder, Silverback Elder, Adventure Awaits, Adventurous Impulse, Genesis Hydra, Hunter's Insight, Inspiring Call, Momentous Fall, Pelakka Wurm, Regal Force, Rishkar's Expertise, Silverback Shaman, Soul's Majesty, Vizier of the Menagerie, Baloth Woodcrasher, Glacier Godmaw, Khalni Heart Expedition, Territorial Scythecat, Sazh's Chocobo, Retreat to Kazandu, Grazing Gladehart, Embodiment of Insight, Undergrowth Champion, Tifa Lockhart, Oran-Rief Hydra, Hooded Hydra, Darksteel Colossus, Overwhelming Stampede, Quakestrider Ceratops, Stonehoof Chieftain, Archetype of Endurance, Temur Sabertooth, both Ulamog the Infinite Gyre, Commander's Plate, Mithril Coat, Darksteel Plate, Autumn's Veil, Spearbreaker Behemoth, Avoid Fate, Alpha Authority, Aspect of Mongoose, Sheltering Word, Ranger's Guile, Canopy Cover, Molting Skin, Broken Fall, Eldrazi Monument, Creeping Renaissance, Praetor's Counsel, Splendid Reclamation, Greenwarden of Murasa, Deadwood Treefolk, Ezuri's Predation.

Also cut in the Sept 20 swap: Nissa Worldsoul Speaker, Blanchwood Armor, Warping Wail, Gift of the Gargantuan.

## Vanilla cuts (confirmed no abilities beyond a bare keyword — never made it into the 181-card pool)
Colossal Dreadmaw, Gigantosaurus, Aggressive Mammoth, Steel Leaf Champion, Frenzied Baloth.

## Reserved List note
Gaea's Cradle was considered but is Reserved List — not reprinted, ~$1,600+, skipped.

## Game Changers
Only **Seedborn Muse** is confirmed on the official Game Changers list among cards in this deck. Vorinclex is NOT currently on the GC list. The GC list changes over time — recheck against the current official list rather than from memory before calling a bracket.

## Rules Notes Worked Out
- **Kodama's trigger** fires off ANY permanent entering under your control (lands, tokens, creatures) — not landfall-specific. Confirmed against real oracle text Sept 19, 2026.
- **The Earth Crystal doubles ETB counters too.** It replaces counters being put on *any* creature you control, so Yorvo enters as an 8/8 and Kalonian Hydra as an 8/8 (which then doubles again when it attacks).
- **Ohran Frostfang vs Ohran Viper**: Frostfang is the one in the deck — team deathtouch on attack + draw off combat damage to a player. Viper only affects itself.
- **Toski and Ohran Frostfang stack** — both draw on combat damage to a player, so a connecting creature draws two.
- Full oracle text for every card in the final 100 (and the cut candidates) was pulled from the live database and checked for color identity, Commander legality, and interactions before finalizing this list.

## Status
**Built.** This is a real, finalized 100-card list, not a staging pool. Physical assembly still depends on owning/acquiring the actual cards (e.g. the Tramplesaurus Rex precon components).

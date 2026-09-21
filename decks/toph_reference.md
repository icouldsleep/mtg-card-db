# Cards Reference — Toph, the First Metalbender EDH Deck

Last updated: **September 21, 2026**. Rebuilt this session and verified card-by-card against
live Archidekt and `scryfall.db`. **Archidekt:** https://archidekt.com/decks/26641207/new_toph
**Deck size: 100.** Naya (R/G/W). **Bracket 3** — 3 Game Changers, which is exactly the cap.

The deck was rebuilt because it was too slow. 40 cards changed. Headline numbers:

| | Before | After |
|---|---|---|
| Cards at 5+ mana value | 18 | **11** |
| Accelerants at mv 2 or less | ~7 | **11** |
| Artifacts (lands under Toph) | 10 | **16** |
| Effective land count | 45 | **50** |
| Vigilance / untap effects | 0 | **4** |

Pips: 51 green, 15 white, 7 red. Every red pip is single and sits on a three-drop or higher.
Planar Outburst at `{3}{W}{W}` is the only awkward cast in the deck.

---

# THE RULES THAT MATTER

## Earthbend — CR 701.66a

**"Earthbend N": Target land you control becomes a 0/0 land creature with haste in addition to
its other types. Put N +1/+1 counters on it. When it dies or is exiled, return it to the
battlefield tapped under your control.**

- **Haste is automatic.** Without it an animated land couldn't tap for mana, attack, or be
  sacrificed the turn it's animated.
- **No duration.** An earthbent land stays a creature permanently.
- **It grants the LAND type itself** — "becomes a 0/0 **land** creature ... in addition to its
  other types." This is load-bearing: an artifact you have already earthbent **stays a land
  creature even after Toph leaves the battlefield.** Spend your early earthbends on artifacts,
  not on real lands. Your real lands are already lands.
- **Returns from graveyard or exile ONLY.** The official ruling: *"If a land was animated by
  earthbend and would go to any zone other than the graveyard or exile, it will not be returned
  to the battlefield by the delayed triggered ability."* **Bounce and tuck are permanent losses,
  earthbent or not.** An earlier version of this file claimed earthbending granted bounce/tuck
  protection. It does not.
- **The return retriggers landfall.** The land dies, comes back, and that's a land entering.
- **Sacrificing counts as dying**, which is what makes Zuran Orb an engine rather than a lifegain card.
- **Earthbends stack.** Counters accumulate; the base P/T reset is a no-op after the first.
  Confirmed by the official ruling: you may target a land that is already a creature; it gets the
  counters, gains haste, and has its base P/T set to 0/0.
- **Earthbend does not give the land a color.** Animated lands are colorless. They cannot pay a
  cost that requires sacrificing a *green* creature.
- **Earthbend does not remove abilities.** An earthbent Ornithopter still flies. An earthbent
  Forest still taps for `{G}`.
- **MDFC TRAP.** A modal double-faced land (Bala Ged Sanctuary) has only its **front face** in the
  graveyard. Bala Ged Recovery's front face is a Sorcery, and a sorcery can't be put onto the
  battlefield, so **earthbend's return does nothing for it.** Never feed an MDFC land to Zuran Orb.

## The commander

**Toph, the First Metalbender** — `{1}{R}{G}{W}` — Legendary Creature — Human Warrior Ally — 3/3
"Nontoken artifacts you control are lands in addition to their other types. (They don't gain the
ability to `{T}` for mana.) At the beginning of your end step, earthbend 2."

- **Nontoken artifacts entering DO trigger landfall**, because the type-change applies as they
  enter. Casting one does **not** use your land drop.
- **But a permanent already on the battlefield becoming a land triggers nothing.** Official ruling.
  So when Toph resolves and converts your existing artifacts, you get no landfall burst. Same when
  Gift of Immortality brings her back.
- The parenthetical is reminder text. Artifacts **can** gain mana abilities from elsewhere —
  Chromatic Lantern and Great Divide Guide both grant them to lands, and your artifacts are lands.
- Tokens are excluded: Clues, Treasures, Food, Cats, Beasts, Plants, Spiders and Insects never
  become lands.

---

# ENGINES AND LOOPS

## Trigger multiplication — only two cards touch Toph's end step

| Card | What it does |
|---|---|
| **Annie Joins Up** | If a triggered ability of a **legendary creature** you control triggers, it triggers an additional time. Free, automatic, every turn. |
| **Strionic Resonator** | `{2}`, `{T}`: copy a triggered ability on the stack. Once per turn cycle. |

Both out means **earthbend 2 three separate times** at end step, three independent targets. They
are separate instances, **not one earthbend 6** — you pick a target for each, so three lands at 2
counters, or one land at 6, or any split. Total counters are identical either way because your
counter boosters apply per event; the choice is bodies versus size.

**Ancient Greenwarden and Traveling Chocobo do NOT double Toph's end step.** Both only fire when a
*land enters*. They double the landfall package only. (Greenwarden was cut; Chocobo is in.)

Annie also doubles Toph Hardheaded Teacher (earthbend 2 per spell cast), Toph Earthbending Master,
Toph Greatest Earthbender, Avatar Kyoshi and Bumi Unleashed.

**Using Strionic Resonator:** you cannot pre-activate it. The trigger must already be on the stack.
Beginning of your end step → Toph's ability triggers and you pick its target → hold priority →
activate Resonator targeting that trigger → the copy resolves first with a new target, then the
original. You must hold up `{2}` through your whole turn for this.

## The Stasis Coffin loop — protection every single turn

`{2}`, `{T}`, **Exile The Stasis Coffin**: you gain protection from everything until your next turn.

Exiling is part of the cost, so on its own it's one use. Under Toph it's a land, so **earthbend it**
and the delayed trigger returns it from exile. Then:

1. Your turn: the Coffin is earthbent from last end step and untapped
2. Attack with everything — you don't need blockers
3. Post-combat: `{2}`, tap, exile. It returns tapped. You gain protection
4. Beginning of your end step: Toph's earthbend 2 re-arms it
5. Opponents' turns: **you take zero damage**
6. Your untap step: it untaps, already earthbent

**What it does not stop:** your creatures still die, life *loss* that isn't damage, non-targeted
effects ("each player sacrifices"), and your own permanents being destroyed. It protects you, not
the board. Commander damage and infect are both damage, so both are prevented.

## The Ichor Wellspring loop — two cards a turn

"When this artifact enters **or** is put into a graveyard from the battlefield, draw a card." One
trigger, two conditions, both fire every time.

Earthbend it → sacrifice it to Zuran Orb (it's a land, so Zuran Orb can) → **draw 1** + 2 life →
earthbend returns it → **it enters, draw 1** + landfall trigger. Re-earthbend at end step, repeat.

**It must be earthbent before you sacrifice it**, or it stays in the graveyard.

## Zuran Orb is a landfall engine, not a lifegain card

`{0}`, free to activate, instant speed. Sacrifice an earthbent land → 2 life → it returns tapped →
**landfall trigger**. Once per earthbend. Doubled by Traveling Chocobo. Also the right response to
a blocker that's about to die.

**Only sacrifice things that are currently earthbent.** An un-earthbent artifact dies for good.

## Twitching Doll — converting the counter pile into a board

`{1}{G}` artifact creature. `{T}`: add one mana of **any color**, put a nest counter on it.
`{T}`, sacrifice: create a 2/2 green Spider with reach **for each counter on it**.

The sac ability says "each **counter**," not each nest counter — so **every +1/+1 counter earthbend
put on it becomes a Spider**. With the full stack out, Toph's free end-step earthbend 2 on it:

```
2 → 3 (Hardened Scales) → 4 (Solid Ground) → 5 (Ozolith, the Shattered Spire)
  → 10 (Branching Evolution) → 20 (Doubling Season)
```

Twenty 2/2 reach Spiders, forty with Doubling Season doubling the tokens. And **every Spider
entering is an Aura Shards trigger.** Sacrificing is dying, so earthbend returns the Doll to do it
again.

## The earthbend-target bottleneck

Three cards want an earthbend target every turn. Toph gives you one, Annie two, Strionic Resonator
three, Ba Sing Se a fourth for `{2}{G}`.

| Spend it on | You get |
|---|---|
| The Stasis Coffin | Take zero damage until your next turn |
| Ichor Wellspring | 2 cards |
| Ornithopter | A flying attacker that costs no mana to swing with |

---

# COUNTER MATH

Five cards modify counters as they are **placed**. They are replacement effects, and **you choose
the order they apply** (CR 616.1). Always apply the additive ones first, then the doublers.

| Card | Effect | Applies to |
|---|---|---|
| Hardened Scales | +1 | +1/+1 counters on a creature |
| Solid Ground | +1 | +1/+1 counters on a **permanent** |
| Ozolith, the Shattered Spire | +1 | +1/+1 counters on an artifact **or** creature |
| Branching Evolution | ×2 | +1/+1 counters on a creature |
| Doubling Season | ×2 | **any** counter type on a permanent, plus tokens |

An earthbend 2 with all five out: `2 → 3 → 4 → 5 → 10 → 20`.
Reversing the order would give 5 instead of 20. Always add before you double.

Only **Doubling Season** touches non-+1/+1 counters, so it's the one that doubles Twitching Doll's
nest counters. Neither it nor the others touch **experience counters**, which sit on you, not a
permanent.

**Proliferate is affected by all of them.** Evolution Sage proliferates on every land drop, and
proliferate *puts* counters, so one proliferate on a creature that already has a +1/+1 counter
becomes **16 counters** through the full stack — on every permanent you choose, simultaneously.
It also adds an experience counter for Toph Earthbending Master and a nest counter for Twitching
Doll, and every batch triggers Terrasymbiosis to draw.

**Kalonian Hydra is not a sixth multiplier.** The five above modify counters as they're placed.
Hydra doubles counters **already on** every creature you control when it attacks. Nothing else in
the deck does that.

---

# CARD DRAW — WHAT ACTUALLY DRAWS

## Needs combat damage to a player

| Card | Rate |
|---|---|
| **Toski, Bearer of Secrets** | **per creature** that connects |
| **Ohran Frostfang** | **per creature** that connects |
| Kutzil, Malamet Exemplar | **once per player**, batched — not per creature |

Kutzil uses the "whenever **one or more** creatures" template, so six attackers into one opponent
draws **one** card. It triggers separately per player, so a three-way alpha strike draws three.
Its real value is the top line: **"your opponents can't cast spells during your turn,"** which is a
Silence protecting every alpha strike.

**Toph, Greatest Earthbender gives land creatures double strike = two combat damage steps**, so all
three of these trigger twice.

## Does not need combat

| Card | Rate |
|---|---|
| **Terrasymbiosis** | Draw = counters placed, once per turn. Toph's free end step alone is 2 |
| Sylvan Library | 2 extra at your draw step, 4 life each to keep |
| Ichor Wellspring | 2 per loop cycle |
| Garruk's Uprising | On a power-4+ creature **entering**, not attacking |

**Garruk's Uprising draw is weaker than it looks.** Earthbent lands don't trigger it — they were
already on the battlefield and never "enter." Live triggers are Rampaging Baloths' Beasts, The
Earth King's Bear, Kodama's drops, Bumi, Avatar Kyoshi, Craterhoof and Kalonian Hydra. Its trample
clause is the main reason it's here.

---

# REMOVAL AND PROTECTION

## Interaction is the thinnest axis

| Type | Cards |
|---|---|
| Artifact / enchantment | Haywire Mite, Chaos Warp, Beast Within, **Aura Shards** |
| Creature (spot) | Path to Exile, Swords to Plowshares, Beast Within, Chaos Warp, Annie Joins Up |
| Board wipe | **Planar Outburst** — the only one, and nothing can tutor it |
| Land | Strip Mine, Wasteland |

**Planar Outburst destroys all NONLAND creatures.** Your earthbent lands are land creatures. They
live, everyone else's board dies. It is a one-sided wrath in this deck.

**Aura Shards is the engine that fixes this axis.** "Whenever a creature you control enters, you
may destroy target artifact or enchantment." Count the creatures that enter: Scute Swarm, Rampaging
Baloths, Felidar Retreat, The Earth King's Bear, Kodama's drops, **Avenger of Zendikar (one Plant
per land)** and **Twitching Doll (one Spider per counter)**. Doubling Season doubles all of them.
Avenger entering with eight lands is eight destroy triggers on one card.

Earthbent lands do **not** trigger Aura Shards — a permanent already on the battlefield becoming a
creature doesn't enter.

## Protection — nine pieces

| Card | Covers |
|---|---|
| Heroic Intervention | Hexproof **and** indestructible on ALL permanents, lands included |
| Flawless Maneuver | Free with a commander out; indestructible on creatures |
| The Stasis Coffin | Protection from everything, repeatable via the loop above |
| Iroas, God of Victory | Prevents all damage to attackers; indestructible; **not a creature**, so it dodges creature removal |
| Akroma's Memorial | Protection from black and red, plus flying/first strike/vigilance/trample/haste |
| Lightning Greaves | Shroud (stops your own targeting too, unlike hexproof) |
| Gift of Immortality | Recurs a creature — see the trap below |
| Kutzil | Opponents can't cast spells during your turn |
| Earthbend itself | Every animated land returns from graveyard or exile |

**Cyclonic Rift overloaded barely touches you.** It returns each *nonland* permanent. Under Toph
your artifacts are lands and your earthbent lands are lands. Sol Ring, Thran Dynamo, The Ozolith,
Twitching Doll and Akroma's Memorial all stay. Toph herself is a creature and does get bounced.

## The Gift of Immortality trap

The commander rule is a **may**: "if your commander would be put into a zone other than the stack or
battlefield, you **may** put it into the command zone instead." If you take that option, Toph never
dies, **Gift never triggers**, and you pay +2 tax.

**Decline the command zone and let her hit the graveyard.** Gift returns her to the battlefield
immediately, at no tax, and Gift itself comes back attached at the next end step. It recurs forever.

It does **not** cover exile. Swords to Plowshares and Path to Exile still get her, and only Heroic
Intervention and Lightning Greaves stop those. Two cards in 99 — the deck's biggest structural risk.

---

# THE DECKLIST (100)

### Commander (1)

- Toph, the First Metalbender — `{1}{R}{G}{W}`

### Creature (24)

- Birds of Paradise — `{G}`
- Badgermole Cub — `{1}{G}`
- Great Divide Guide — `{1}{G}`
- Lotus Cobra — `{1}{G}`
- Dryad of the Ilysian Grove — `{2}{G}`
- Earthbending Student — `{2}{G}`
- Evolution Sage — `{2}{G}`
- Kutzil, Malamet Exemplar — `{1}{G}{W}`
- Scute Swarm — `{2}{G}`
- Traveling Chocobo — `{2}{G}`
- Iroas, God of Victory — `{2}{R}{W}`
- The Earth King — `{3}{G}`
- Toph, Earthbending Master — `{3}{G}`
- Toph, Greatest Earthbender — `{2}{R}{G}`
- Toph, Hardheaded Teacher — `{2}{R}{G}`
- Toski, Bearer of Secrets — `{3}{G}`
- Bumi, Unleashed — `{3}{R}{G}`
- Kalonian Hydra — `{3}{G}{G}`
- Ohran Frostfang — `{3}{G}{G}`
- Kodama of the East Tree — `{4}{G}{G}`
- Rampaging Baloths — `{4}{G}{G}`
- Avenger of Zendikar — `{5}{G}{G}`
- Avatar Kyoshi, Earthbender — `{5}{G}{G}{G}`
- Craterhoof Behemoth — `{5}{G}{G}{G}`

### Artifact Creature (3)

- Ornithopter — `{0}`
- Haywire Mite — `{1}`
- Twitching Doll — `{1}{G}`

### Artifact (13)

- Zuran Orb — `{0}`
- Sol Ring — `{1}`
- The Ozolith — `{1}`
- Arcane Signet — `{2}`
- Ichor Wellspring — `{2}`
- Lightning Greaves — `{2}`
- Ozolith, the Shattered Spire — `{1}{G}`
- Strionic Resonator — `{2}`
- The Mind Stone — `{1}{W}`
- Chromatic Lantern — `{3}`
- The Stasis Coffin — `{3}`
- Thran Dynamo — `{4}`
- Akroma's Memorial — `{7}`

### Enchantment (13)

- Hardened Scales — `{G}`
- Sphere Grid — `{1}{G}`
- Sylvan Library — `{1}{G}`
- Aura Shards — `{1}{G}{W}`
- Branching Evolution — `{2}{G}`
- Garruk's Uprising — `{2}{G}`
- Gift of Immortality — `{2}{W}`
- Terrasymbiosis — `{2}{G}`
- Annie Joins Up — `{1}{R}{G}{W}`
- Felidar Retreat — `{3}{W}`
- Smothering Tithe — `{3}{W}`
- Solid Ground — `{3}{G}`
- Doubling Season — `{4}{G}`

### Instant (7)

- Enlightened Tutor — `{W}`
- Path to Exile — `{W}`
- Swords to Plowshares — `{W}`
- Heroic Intervention — `{1}{G}`
- Beast Within — `{2}{G}`
- Chaos Warp — `{2}{R}`
- Flawless Maneuver — `{2}{W}`

### Sorcery (5)

- Green Sun's Zenith — `{X}{G}`
- Farseek — `{1}{G}`
- Nature's Lore — `{1}{G}`
- Rockalanche — `{2}{G}`
- Planar Outburst — `{3}{W}{W}`

### Land (34)

- Arid Mesa
- Ba Sing Se
- Brushland
- Clifftop Retreat
- Command Tower
- 7× Forest
- Grasslands
- Gruul Turf
- Jetmir's Garden
- Karplusan Forest
- 2× Mountain
- Mountain Valley
- 3× Plains
- Prismatic Vista
- Rootbound Crag
- Sacred Foundry
- Stomping Ground
- Strip Mine
- Sunpetal Grove
- Temple Garden
- Wasteland
- Windswept Heath
- Wooded Foothills
- Yavimaya, Cradle of Growth
- Bala Ged Recovery // Bala Ged Sanctuary
**Mana base:** 34 land-capable cards (12 basics — 7 Forest, 3 Plains, 2 Mountain — plus 21
nonbasics and Bala Ged Recovery). Six fetchlands, each able to find all three shocklands.
Plus 16 artifacts that are lands under Toph, for **50 effective lands**.

**Only 6 artifacts actually make mana**: Sol Ring, Arcane Signet, The Mind Stone, Chromatic
Lantern, Thran Dynamo, Twitching Doll. The other ten are lands for landfall and earthbend
purposes only. Chromatic Lantern and Great Divide Guide are the two cards that turn the whole pile
into real mana, which makes them the highest-leverage permanents in the deck.

**Karplusan Forest is not a Forest.** Its type line is just "Land." Only 10 cards in the deck are
actual Forests: 7 basics plus Stomping Ground, Temple Garden and Jetmir's Garden. Yavimaya and
Dryad of the Ilysian Grove each make *every* land a Forest, and under Toph that includes artifacts.

---

# GAME CHANGERS — 3 of 3, Bracket 3

Verified against `game_changers.md`, which is the authority. **Never state Game Changer status from
memory, and never from `scryfall.db` — the database has no game-changer field.**

- **Enlightened Tutor**
- **Smothering Tithe**
- **Aura Shards**

Natural Order was swapped out for Aura Shards; both are Game Changers, so the count is unchanged.
**Green Sun's Zenith is NOT a Game Changer** despite frequently being assumed to be.

---

# OPENING HAND MATH

At 34 land-capable cards in 99:

| | |
|---|---|
| Hands with 0-1 lands | 23.5% |
| Hands with 3+ lands | 45.3% |
| Keepable (3+ lands, or 2 lands + an accelerant) | **64.5%** |

Dropping to 32 lands would push the mulligan rate past one hand in four and cost 4.5 points of
keepable rate. **Do not cut lands.**

The 11 accelerants at mv 2 or less are Sol Ring, Arcane Signet, The Mind Stone, Birds of Paradise,
Twitching Doll, Badgermole Cub, Great Divide Guide, Lotus Cobra, Farseek, Nature's Lore and Dryad.
Odds of at least one in the opening seven: **57.4%**. By turn three on the draw: **71.0%**.

**The artifacts are not lands in your opening hand.** Toph costs 4. Before she resolves, Ornithopter
is a 0/2 and Sol Ring is a mana rock. The 50 effective-land figure is a turn-six number.

---

# PLAY PATTERN

1. **Deploy Toph as fast as possible.** Everything scales off her. Turn 3-4 is the target.
2. **Earthbend artifacts, not real lands.** Earthbend grants the land type itself, so an artifact
   you've animated survives Toph dying. Ornithopter first — it flies, and swinging with it costs
   you nothing because it makes no mana.
3. **Spread by default, concentrate to close.** Wide boards feed Toski and Ohran (per creature),
   The Earth King (per attacker) and Aura Shards (per token). One giant land is a single removal
   spell away from nothing. Concentrate on the kill turn, when Kalonian Hydra doubles everything
   and Toph Greatest Earthbender's double strike counts it twice.
4. **Hold up `{2}`** if Strionic Resonator or The Stasis Coffin is out. They compete for the same
   mana; you usually only afford one per turn.
5. **Alpha strike behind the Coffin.** Swing with everything, then exile it post-combat. You take
   zero damage until your next turn, so you never need blockers.

---

# DO NOT RE-SUGGEST CUTTING

Owner has explicitly protected these, several with reasoning that corrected earlier analysis:

**Iroas, God of Victory** — the point is that he *isn't* a creature, so removal misses him, and he
prevents all damage to attackers so earthbent lands swing risk-free.
**Doubling Season** — the whole point of the deck.
**Rampaging Baloths** — a 4/4 per landfall, which also feeds Garruk's Uprising and Aura Shards.
**Zuran Orb** — a free repeatable landfall engine, not a lifegain card.
**The Ozolith**, **Rockalanche**, **Thran Dynamo**, **Chromatic Lantern**, **Akroma's Memorial**,
**Avatar Kyoshi**, **Gift of Immortality**, **Garruk's Uprising**, **Solid Ground**,
**Badgermole Cub**, **The Earth King**, **Sphere Grid** (the only mass reach), **Evolution Sage**,
**Strionic Resonator**, **Ornithopter**, **Branching Evolution**, **Kutzil**, **The Stasis Coffin**.

# CUT THIS SESSION — DO NOT RE-ADD WITHOUT REASON

Ghalta Primal Hunger, The Great Henge, Terastodon, Austere Command, Flopsie Bumi's Buddy, Multani,
Shared Roots, True Ancestry, Cycle of Renewal, Earthbender Ascension, Wood Elves, Ghostly Prison,
Badgermole, Retreat to Kazandu, Rhonas the Indomitable, Toph the Blind Bandit, Tireless Tracker
(Clues cost `{2}` each in a mana-starved deck), Origin of Metalbending, Seismic Tutelage,
Ancient Greenwarden (6 mana; Traveling Chocobo does the doubling at 3),
Lotus Petal, Natural Order (→ Aura Shards), and 12 basic lands.

**Avenger of Zendikar was nearly cut and then kept** — with Aura Shards in the deck, entering with
eight lands is eight destroy triggers.

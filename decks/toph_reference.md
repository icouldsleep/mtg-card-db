# Cards Reference — Toph, the First Metalbender EDH Deck

Last updated: **September 20, 2026**. Previously verified card-by-card against live Archidekt on Sept 3 and re-verified Sept 20 (exact match at 100 before that day's swap). **Archidekt link:** https://archidekt.com/decks/26022574/copy_of_toph **Deck size: 100.** Naya (R/G/W). Archidekt header says Bracket 3, but see the bracket note below — it's really a 4.

---

# THE RULES THAT MATTER

## Earthbend — CR 701.66a
**"Earthbend N": Target land you control becomes a 0/0 land creature with haste in addition to its other types. Put N +1/+1 counters on it. When that land dies or is put into exile, return it to the battlefield tapped under your control.**

- **Haste is automatic and unconditional.** This is load-bearing — a land that's also a creature could not otherwise tap for mana while summoning sick. Haste is what lets earthbent lands tap, attack, or be sacrificed the same turn.
- **NO DURATION.** An earthbent land stays a creature permanently. It does not wear off at end of turn. This matters enormously for Badgermole Cub (below).
- **Returns on DEATH or EXILE only** — tapped, under the ORIGINAL earthbending player's control, and NOT as a creature (no counters, no creature type).
- **Bounce and tuck are NOT covered.** Return-to-hand and shuffle-into-library lose the land permanently. This is the gap Zuran Orb fills.
- **The return retriggers LANDFALL** — confirmed. The land dies, the delayed trigger returns it, and a land entering the battlefield is a Landfall trigger.
- Sacrificing counts as dying. Strip Mine and Wasteland remain safe sac fodder.
- **EARTHBENDS STACK — this is the single most commonly misread thing about the deck.** Earthbending an already-earthbent land does NOT reset it to 0/0 and back to 2/2. Base P/T resets, but **counters ACCUMULATE.**
  - Earthbend 2 on a fresh land -> 0/0 base with 2 counters = **2/2**
  - Earthbend 2 on that same land again -> base resets to 0/0 (it was ALREADY 0/0, so nothing changes) and 2 MORE counters go on = **4/4**
  - Earthbend never removes counters. It only sets base P/T and adds.
  - **Confirmed by the official ruling on The Boulder, Ready to Rumble:** you may target a land that is already a creature from a previous earthbend; it gets the counters, gains haste, and has its base P/T set to 0/0.
  - **Where the reset ACTUALLY bites:** a NON-earthbend animation. If something made a land a 3/3 and you then earthbend it for 2, the base 3/3 is overwritten to 0/0 and you get a 2/2, not a 5/5. That is the only case the wording exists for.
  - **PRACTICAL:** earthbend sources are plentiful — Toph's end step gives 2 every turn, Toph Hardheaded Teacher adds 1 per spell cast, Rockalanche can drop up to 16 at once, plus Ba Sing Se, Badgermole, Solid Ground, Bumi, Avatar Kyoshi (8), Toph Blind Bandit, Earthbender Ascension, and Toph Earthbending Master. Hardened Scales and Solid Ground each add one per earthbend; Doubling Season doubles the whole amount. **See the strategic rule below for whether to spread these or stack them — spread is the default.**
- The land keeps its other types — an earthbent Forest still taps for {G}.

## The commander
**Toph, the First Metalbender** — {1}{R}{G}{W} — Legendary Creature — Human Warrior Ally — 3/3
"Nontoken artifacts you control are lands in addition to their other types. (They don't gain the ability to {T} for mana.) At the beginning of your end step, earthbend 2."

**CONFIRMED: nontoken artifacts entering DO trigger Landfall.** They enter already being lands, because the type-changing effect applies as they enter. Casting one does NOT use your land drop. Ten such sources in the deck: Sol Ring, Arcane Signet, Chromatic Lantern, Thran Dynamo, The Mind Stone, The Ozolith, Zuran Orb, Lightning Greaves, The Great Henge, and Tireless Tracker's Clues are the exception (see below).

**The "nontoken" clause is deliberate and excludes:** Clue tokens (Tireless Tracker, True Ancestry), Treasure tokens (Smothering Tithe). These do NOT become lands and do NOT trigger Landfall.

**Artifacts being lands also means they are legal EARTHBEND targets.** An earthbent Sol Ring is nearly unkillable — destroy and exile both bounce off it.

---

# ⚑ PRIMARY STRATEGIC RULE — SPREAD BY DEFAULT, CONCENTRATE TO CLOSE

**Earthbends stack (counters accumulate; the base P/T reset is a no-op after the first). But stacking everything on ONE land is NOT the default plan — it's the finisher.** An earlier version of this file said "concentrate on one land." That was wrong and the user corrected it.

## Why SPREADING is the default

- **Attacking taps your lands.** A board that is one 30/30 swings, taps, and leaves you with nothing to block the crack-back. Ghostly Prison taxes attackers but doesn't stop a determined one. Several 8/8s let you attack with three and hold one back.
- **Single point of failure.** Swords to Plowshares, Path to Exile, or Chaos Warp on the one huge land erases everything you built. Spread across four lands, one removal spell costs a quarter of your board.
  - **And exile beats the safety net.** The Ozolith only catches counters when a creature DIES. Swords and Path EXILE — no counters banked. (Earthbend returns the land itself from exile, but with nothing on it.)
- **The Earth King fetches a basic land FOR EACH power-4+ creature attacking.** One 30/30 fetches one land. Four 8/8s fetch four — four Landfall triggers, four Baloths Beasts, four Scute Swarm copies, four Lotus Cobra mana, four Tireless Tracker Clues. **Concentration actively shrinks your best engine.**
- **Ohran Frostfang and Toski draw PER CREATURE that connects.** Four attackers with both out is eight cards. One attacker is two.
- **Flopsie** says power-4+ creatures can't be blocked by more than one creature — that rewards a wide board of medium threats, not one giant.

## When to CONCENTRATE

Concentration is the **kill turn**, not the build-up.

- **Toph, Greatest Earthbender gives land creatures DOUBLE STRIKE** — every counter counts twice.
- **Seismic Tutelage** doubles counters on the enchanted creature when it attacks; **Kalonian Hydra** doubles the whole board on attack.
- Stacked: 10 counters -> 20 (Seismic) -> 40 (Kalonian) -> **80 damage with double strike.** That kills a player from full life out of nowhere.
- **Badgermole** grants trample to anything with a +1/+1 counter and **Ohran Frostfang** grants deathtouch to attackers — deathtouch + trample means assign 1 to each blocker and the rest to the face. A concentrated threat becomes effectively unblockable.

**The play pattern: build several medium threats while the engines run, then dump The Ozolith's bank onto one of them the turn you go for lethal.**

## The Ozolith is what makes both modes work
When a threat dies, it was a creature with counters leaving the battlefield, so Ozolith banks every counter. Rebuild next combat. **This is insurance against destruction, not against exile.**

# CORE INTERACTIONS (the stuff that wins games)

## Zuran Orb — the protection engine
{0} Artifact — "Sacrifice a land: You gain 2 life." Enters as a land under Toph, so it triggers Landfall for zero mana, and it is a FREE REPEATABLE sac outlet.

**What it's actually for:** earthbend already survives death and exile. Zuran Orb covers **bounce and tuck** — sacrifice in response, converting a permanent loss into a death, which earthbend catches. The permanent returns, Landfall triggers, you gain 2, and their spell fizzles on an illegal target.
**Zuran Orb turns effects that would remove your land from the game into effects that merely recycle it.**

## ⚑⚑ THE ZURAN ORB RULE — ALWAYS SACRIFICE A LAND THAT IS GOING TO DIE ANYWAY

**This is a standing rule, not a judgment call. If a land you control is about to die, be destroyed, be exiled, or be wiped — sacrifice it to Zuran Orb in response. Every single time.**

Claude initially said to save Zuran Orb only for bounce/tuck. **Wrong — the user corrected this.** Sacrificing a doomed land is free value even when earthbend would have covered it anyway:

- **2 life.** Real in a deck with almost no lifegain and a Sylvan Library eating 4 at a time.
- **A targeted removal spell FIZZLES** — it loses its only legal target and is countered by game rules. The opponent loses the card entirely.
- **Earthbend still returns the land**, so you lose nothing you weren't already losing.
- **The Ozolith banks the counters** either way (leaving the battlefield covers death and exile both).
- **The return is a LANDFALL TRIGGER.**

**BEST APPLICATION — sac in response to a BOARD WIPE.** The land dies, the delayed earthbend trigger resolves FIRST and returns it **as a plain land, not a creature** — then the wipe resolves and can't touch it. **You dodge the sweeper entirely and gain 2 life doing it.**

**The only two exceptions:**
1. **Mid-combat, if the damage matters.** A blocker that is sacrificed before the combat damage step deals **NO damage at all** — combat damage is dealt simultaneously by creatures still on the battlefield, so a blocker that is already gone deals nothing. The attacker stays blocked (it won't hit you) but takes zero.
   - **TRADE: do NOT sac.** A 2/2 earthbent land blocking a 2/2 attacker should be left in. They trade, the attacker dies, and your land comes back anyway via earthbend — plus the return is a Landfall trigger. Strictly better than 2 life.
   - **CHUMP BLOCK: DO sac.** A 2/2 land blocking a 10/10 deals 2 damage and kills nothing. Sacrifice it — you absorb the attack, gain 2 life, and get the land back.
   - **Attacker has deathtouch: DO sac.** You lose the land either way and it won't kill theirs.
   - **Attacker has trample: do NOT sac.** Removing the blocker assigns ALL that damage to you.
   - **IMPORTANT: Ohran Frostfang only grants deathtouch to ATTACKING creatures.** Your blockers do NOT have it. A small land blocking a big creature genuinely cannot kill it — that is always a chump block.
   - **The rule of thumb means dying anyway WITHOUT COST.** In combat, dying is not free — the land is doing a job by dying. Judge whether that job is worth more than 2 life.
2. **The land is not earthbent.** A plain land you sacrifice is gone for good, no return trigger. On those the trade is "lose the land, gain 2 life" — still correct if it was dying regardless, but never sac a healthy non-earthbent land.

**On tapping for mana first:** only worth it if you have something to spend it on RIGHT THEN — you're already at instant speed holding priority, so Heroic Intervention, Origin of Metalbending, Rhonas's pump, or another Zuran activation are live. **Mana empties at the end of every step**, so if you have nothing to cast, tapping first gains you nothing. Claude overstated this as a general habit; it is situational.

**EARTHBEND OZOLITH EARLY — user is right, Claude argued the wrong side of this and conceded.**

Claude's bad argument was "leave it un-earthbent so it dodges creature wipes." **The decisive point: the counters are lost either way when it dies. The real question is whether you keep the CARD.**

| | Creature wipes | Artifact removal / exile | If it dies |
|---|---|---|---|
| **Un-earthbent** | Immune | Vulnerable | **GONE PERMANENTLY** — card lost forever |
| **Earthbent** | Vulnerable | Vulnerable | **RETURNS** tapped — bank lost, engine kept |

Earthbend's delayed trigger returns it from **death OR exile**, permanently, regardless of what killed it. Trading "immune to one class of removal" for "recurs from all of them" is the better deal.

**THE CYCLE (the correct way to play it):**
1. Bank counters as earthbent lands and creatures die.
2. At combat, move ALL counters onto a real threat.
3. Ozolith is now 0/0 and dies as a state-based action.
4. Earthbend returns it tapped — **and that return is a free LANDFALL TRIGGER** (Baloths, Scute Swarm, Lotus Cobra, Tireless Tracker, all doubled by Ancient Greenwarden).
5. Toph's end-step earthbend 2 puts it back online.

**Every time you empty the bank, you get a Landfall trigger.**

**EARTHBENDING A LOADED OZOLITH DOES NOT LOSE THE COUNTERS — IT ACTIVATES THEM.** Earthbend adds; it never removes. An Ozolith sitting on 10 banked counters, earthbent for 2, is 0/0 base with **12 counters = a 12/12**. The whole bank goes live at once. With Toph, Greatest Earthbender out, land creatures have DOUBLE STRIKE — that's 24 damage out of your counter vault. Hardened Scales and Solid Ground each add one to the earthbend; Doubling Season doubles it.

**The timing rule: bank while it's an artifact, earthbend when you're ready to swing.** Inert counters on a noncreature artifact are untouchable by creature removal. Earthbent, they're a threat but they're exposed to a wipe (and a wipe means the returned Ozolith is a fresh object with nothing on it).

Also: Zuran Orb can sacrifice Ozolith either way (it's a land under Toph regardless), but saccing an UN-earthbent one kills it permanently. **The bounce/tuck protection only works if it's earthbent.**

## The Mind Stone — a repeatable ETB engine
{1}{W} Legendary Artifact, indestructible. {5}{W}, {T}: Harness. Then at the beginning of EVERY end step, exile a nonland permanent you control and return it.

**Free repeatable blink once online.** Terastodon destroying three permanents every turn. Avenger of Zendikar making a Plant per land every turn. Craterhoof pumping every turn. Wood Elves fetching a Forest — a free Landfall trigger every turn. Plus Badgermole, Flopsie, Bumi, Toph Blind Bandit, and Solid Ground re-earthbending.

**LIMITATION: it exiles a NONLAND permanent.** Under Toph your artifacts ARE lands, so it cannot blink them. Only non-artifact creatures and enchantments.

## Iroas + The Earth King — the attack engine
**Iroas, God of Victory** prevents ALL damage to attacking creatures and grants menace. Devotion rarely hits 7 in a green deck, so he's usually a non-creature indestructible enchantment — the abilities work regardless, and he's nearly unremovable.
**The Earth King** — whenever one or more power-4+ creatures attack, fetch that many basic lands onto the battlefield. **Multiple lands entering at once = multiple simultaneous Landfall triggers.** Ruling: counts attackers when the ability TRIGGERS; later removal doesn't shrink the fetch.

**Together: you alpha-strike every turn at zero risk, fetching a basic per big attacker.** Each fetch feeds Baloths, Scute Swarm, Lotus Cobra, Tireless Tracker, Avenger, and Toph Earthbending Master. **Ancient Greenwarden doubles all of it.**

## Ohran Frostfang + Toski — the draw engine
Both read "whenever a creature you control deals combat damage to a player, draw a card." **They stack — two cards per connecting creature.** Ohran also gives all ATTACKING creatures deathtouch; with Badgermole's trample (granted to anything with a +1/+1 counter), a big earthbent land is deathtouch + trample: assign 1 to each blocker, rest to face.

**Toski is a 1/1 indestructible DEATHTOUCH attacker with Ohran out** — blockers die, Toski survives. Its forced attack applies only to Toski. It's also uncounterable and indestructible, so wraths and counterspells miss it.

## Counter doublers stack multiplicatively
Seismic Tutelage doubles counters on the enchanted creature when it attacks; Kalonian Hydra doubles the whole board. **A creature at 4 goes 4 → 8 → 16.** Doubling Season applies on top ("double the number of counters" means putting that many on, which Doubling Season doubles again) — 4 becomes 12, and Hardened Scales + Solid Ground push it to 16.
**Best target is an earthbent land.** Rockalanche earthbends for up to 16; Avatar Kyoshi for 8. Seismic turns that into 20-30. **Iroas makes Seismic strictly better**, since it only pays off on attack and Iroas makes attacking free. The Aura two-for-one risk is covered by The Ozolith catching the counters.

---

# RULINGS ESTABLISHED THIS SESSION

- **Garruk's Uprising does NOT trigger on earthbent lands.** It needs a power-4+ creature to ENTER. Animating a land isn't entering, and a land that dies and returns comes back as a land, not a creature. Artifacts under Toph enter as LANDS, not creatures — also no trigger. Solemn was the only artifact creature and it's cut.
  - **⚑ CORRECTED Sept 20, 2026 — the old conclusion "treat it as a trample-granter that occasionally cantrips" was WRONG and cost the card a slot before the owner caught it.** Everything above is true about lands and artifacts, but it ignored the creatures. **Rampaging Baloths creates 4/4 Beast tokens** — power 4 — so **every landfall trigger draws a card off Garruk's Uprising**, doubled by Ancient Greenwarden. **The Mind Stone** blinking Terastodon (9/9) or Avenger of Zendikar (5/5) draws another every end step. On top of that: Ghalta, Craterhoof, Terastodon, Avenger, Rhonas, Kalonian Hydra (enters with four counters), Ancient Greenwarden, Badgermole, Flopsie and Bumi all trigger it when cast. **It is a draw engine in this deck. Do not cut it.**
- **Planar Outburst is SAFE for earthbent lands** — it destroys all NONLAND creatures, and an earthbent land is still a land. Base mode {3}{W}{W}; you never have to pay Awaken.
- **Farseek CAN fetch Temple Garden, Sacred Foundry, and Stomping Ground** (they're Plains/Mountain cards). Claude wrongly claimed otherwise. It has exactly three legal targets — narrow, but it's 2-mana ramp plus a Landfall trigger that always does something turn two. **Rules note: Farseek says "tapped," which OVERRIDES the shockland's pay-2-life clause. NEVER pay the 2 life off a Farseek.**
- **Gruul Turf: NEVER bounce an earthbent land with it.** Bouncing loses the land, its counters, and the Landfall trigger. Same caution applies to Multani's recursion cost.
- **Multani's recursion bounces two lands** — same warning.
- **Toph, the Blind Bandit's power counts +1/+1 counters on LANDS you control** — not the number of lands, not permanents. Note that a land dying and returning comes back with NO counters, so her power resets with your board.
- **The Boulder, Ready to Rumble** (not in deck): its earthbend happens AFTER attackers are declared, so the animated land doesn't join that attack.
- **Decimate synergy** (considered, rejected): a permanent with multiple card types can be chosen for more than one instance of "target," so an earthbent artifact-land covers artifact + creature + land at once — and it returns when it dies. Rejected anyway: 8 removal already, and the enchantment slot has no workaround (uncastable if no opponent has one).

---

# THE DECKLIST (100)

## Commander (1)
Toph, the First Metalbender

## Anthem (1)
Toph, Greatest Earthbender — earthbend X on ETB where X = mana spent; **land creatures you control have DOUBLE STRIKE**.

## Artifact (2)
Akroma's Memorial, The Mind Stone

## Counters (10)
Avatar Kyoshi Earthbender, Badgermole, Flopsie Bumi's Buddy, Hardened Scales, Kalonian Hydra, **Rockalanche**, Seismic Tutelage, Solid Ground, The Ozolith, **Toph the Blind Bandit**

**Rockalanche** — {2}{G} Sorcery — Lesson — earthbend X where X = Forests you control. Flashback {5}{G}. **Counts Forest TYPES, so Stomping Ground and Temple Garden count — ceiling is 16, not 14.** Double-dips with Toph Hardheaded Teacher (his cast trigger plus the Lesson bonus counter fires on a SEPARATE land).

## Draw (6)
Garruk's Uprising, **Ohran Frostfang**, Sylvan Library, **The Great Henge**, **Tireless Tracker**, **Toski Bearer of Secrets**

**Tireless Tracker** — a RE-ADD. It was originally cut for the wrong reason: the question asked was whether Clues trigger Landfall (they don't), when the relevant question was whether Tracker triggers off YOUR landfall. It does, constantly — every nontoken artifact you cast under Toph is a land entering.
**The Great Henge** — {X}{G}{G} where X is 8 minus your greatest creature power. **An earthbent land counts**, so a 4/4 land makes it 6 mana and Avatar Kyoshi's earthbend 8 makes it 2.
**Sylvan Library** — treat it as a free scry-3 most turns. Only pay the 4 life when you actually need the card; Retreat to Kazandu and Zuran Orb are the only lifegain against Strip Mine, Wasteland, and three shocklands.

## Evasion (2)
Ghalta Primal Hunger, Rhonas the Indomitable

## Finisher (2)
Bumi Unleashed, Craterhoof Behemoth

## Land (35)
Ba Sing Se, Clifftop Retreat, Command Tower, Forest x14, **Gruul Turf**, Mountain x5, Plains x5, Rootbound Crag, Sacred Foundry, Stomping Ground, Strip Mine, Sunpetal Grove, Temple Garden, Wasteland

## Landfall (6)
Avenger of Zendikar, Multani Yavimaya's Avatar, Rampaging Baloths, Retreat to Kazandu, Scute Swarm, Toph Earthbending Master

## Protection (5)
Ghostly Prison, **Gift of Immortality**, Heroic Intervention, **Iroas God of Victory**, Lightning Greaves

**Ghostly Prison earns its slot structurally:** your lands become attackers, so when you swing they're tapped and can't block the crack-back.

## Ramp (14)
Arcane Signet, Badgermole Cub, **Chromatic Lantern**, Cycle of Renewal, Earthbender Ascension, Farseek, Lotus Cobra, Nature's Lore, Shared Roots, Smothering Tithe, Sol Ring, **The Earth King**, Thran Dynamo, Wood Elves

**Chromatic Lantern** — "Lands you control have '{T}: Add one mana of any color.'" **Under Toph your artifacts ARE lands, so Lantern grants them a mana ability.** Toph's parenthetical is REMINDER TEXT — it means the type change alone doesn't grant a mana ability, not that they can't gain one elsewhere. So Lightning Greaves, The Ozolith, and Zuran Orb become mana sources.

**⚑ Lantern also fixes Thran Dynamo's colour problem (owner's point, Sept 20, 2026).** Thran Dynamo taps for {C}{C}{C}, which looks awkward in a deck measured at 76% green costs against 43% green production. But under Toph it is a land, so Lantern gives it a **second, separate** mana ability: "{T}: Add one mana of any color." You choose which to use when you tap it — three colorless for the top end, or one coloured mana when you are colour-screwed. **Thran Dynamo is not a weak slot here; it powers out Ghalta, Craterhoof, Terastodon and Akroma's Memorial, it enters as a land so it is a Landfall trigger, and it is a legal earthbend target.** Do not cut it on "colorless in a green deck" grounds.

## Recursion (3)
**Ancient Greenwarden**, Toph Hardheaded Teacher, True Ancestry

**Ancient Greenwarden doubles EVERY landfall trigger** — including all ten nontoken artifacts entering as lands, and every basic The Earth King fetches. Also lets you play lands from your graveyard, pairing with earthbent lands dying.
**LESSONS in the deck:** Shared Roots, Cycle of Renewal, True Ancestry, Origin of Metalbending, Rockalanche. With Toph Hardheaded Teacher out, each earthbends 1 AND puts an extra counter on that land.

## Removal (8)
Austere Command, Beast Within, Chaos Warp, Origin of Metalbending, Path to Exile, Planar Outburst, Swords to Plowshares, Terastodon

## Sac Outlet (1)
Zuran Orb

## Tokens (1)
Doubling Season

## Tutor (3)
Enlightened Tutor, Green Sun's Zenith, Natural Order

---

# BRACKET — this is a 3 (corrected Sept 20, 2026)

**CORRECTED Sept 20, 2026: this deck runs THREE Game Changers, not four — Enlightened Tutor, Natural Order, and Smothering Tithe. That is exactly at the Bracket 3 cap, so the deck is a legitimate Bracket 3.**

**Green Sun's Zenith is NOT a Game Changer.** The earlier "four Game Changers" claim counted it. Two independent checks say otherwise: it does not appear in the green section of the official list (now stored at `game_changers.md` in the repo root), and Archidekt's API flags it `false` on this exact deck. Archidekt's live flags on deck 26022574 return exactly `['Enlightened Tutor', 'Natural Order', 'Smothering Tithe']`.

Nothing else in the list trips Bracket 3's other restrictions: Strip Mine and Wasteland are single-target, not mass land denial; there are no extra-turn spells; and the one infinite-combo risk (a free repeatable sac outlet beyond Zuran Orb alongside a landfall payoff) is flagged below as something to avoid, not something present.

**User decided to KEEP Smothering Tithe** (Sept 2) — it's strong ramp and Treasures fix the green-heavy costs. **Do not re-suggest cutting it.** Note the original reason for that decision ("accept Bracket 4") no longer applies: keeping it now costs nothing, since three is within the cap.

**Always check `game_changers.md` rather than recalling a card's status.** scryfall.db has no game-changer field at all.

**Would push further / avoid:** adding a free repeatable sac outlet beyond Zuran Orb (Ashnod's Altar, etc.) alongside a Landfall payoff creates an infinite-Landfall engine.

---

# CHANGE LOG — September 20, 2026

| IN | OUT |
|---|---|
| **Akroma's Memorial** {7} | **Guardian Project** {3}{G} |

**Garruk's Uprising was cut first and that was WRONG — owner corrected it, it stays.** See the corrected ruling in RULINGS above: Rampaging Baloths makes **4/4** Beast tokens, so every landfall trigger puts a power-4 creature onto the battlefield and draws a card off Garruk's Uprising. It is a draw engine here, not a cantrip. It is also the deck's only **cheap** trample source at 3 mana, and being an enchantment it sits on a different removal axis from a 7-mana artifact.

**Why Guardian Project is the cut instead.** "Whenever a **nontoken** creature you control enters..." — that clause excludes every Baloths Beast, every Scute Swarm copy and every Avenger Plant. In a deck whose engine is landfall generating tokens, it is pointed at the wrong half, and Garruk's Uprising covers precisely what it misses. It also carries a name-uniqueness restriction, and at $19.59 it was the priciest marginal card in the list. What it caught that Garruk's cannot: small nontoken bodies like Wood Elves, Lotus Cobra, Tireless Tracker, Toski and Ohran Frostfang — real, but one-shot rather than a repeating engine.

**What Akroma's Memorial adds.** Flying, first strike, vigilance, trample, haste, protection from black and from red, to everything. Vigilance patches the structural hole this file identifies, where attacking taps your lands and leaves nothing to block the crack-back. Protection from black and red is a large and previously unnoted defensive upgrade: your creatures cannot be targeted or damaged by black or red sources, and cannot be blocked by black or red creatures.

**What this fixes.** Vigilance is the structural hole this file identifies — attacking taps your lands, so they can't block the crack-back, which is why Ghostly Prison "earns its slot structurally." Akroma's Memorial patches it directly. Trample source count is unchanged at three (Badgermole, Craterhoof, Akroma's Memorial) but the quality is higher. And **protection from black and from red is a large defensive upgrade** not previously noted: your creatures can't be targeted or damaged by black or red sources, and can't be blocked by black or red creatures.

**It is an artifact, so under Toph it enters as a LAND — that's a Landfall trigger — and it is a legal earthbend target.**

**Two honest costs:**
1. **A 3-drop became a 7-drop.** This file flags curve tension on every 5-8 mana add. Owner's position (Sept 20) is that the deck does not actually have a slow-start problem, so this was accepted.
2. **Protection from red blocks your own Chaos Warp.** Chaos Warp is {2}{R}; with Akroma's Memorial on the battlefield you cannot target your own creatures with it. Niche, but real — this file flagged it in advance and it is confirmed.

Haste from Akroma's Memorial is partly redundant, since earthbend already grants haste to earthbent lands.

**⚑ ARCHIDEKT IS NOW ONE SWAP BEHIND THIS FILE — Guardian Project out, Akroma's Memorial in.** Deck 26022574 was verified card-for-card against this file on Sept 20, 2026 and matched exactly at 100 — then this swap was applied here. Archidekt still lists Guardian Project and not Akroma's Memorial. (Garruk's Uprising is in both — it was briefly cut here and put straight back.) **Update Archidekt, then this line can go.** This file has a recorded history of the reverse problem (11 agreed swaps sitting unapplied on Archidekt while the file claimed they were done), so the direction of the gap is worth stating explicitly.

---

# ⛔ HARD RULES FOR FUTURE SESSIONS

## NEVER suggest cutting Gift of Immortality
User considers it one of the best cards in the deck. It stops the commander from ever staying down — Toph returns to the battlefield rather than the command zone, and Gift returns attached at the next end step. **That dodges commander tax entirely**, which matters enormously for a commander whose static ability the whole deck is built on.

## Cards wrongly flagged as weak — user was right, do not re-propose
- **Seismic Tutelage** — doublers stack multiplicatively; Iroas makes it strictly better.
- **Rhonas** — Ohran grants deathtouch only to ATTACKING creatures. **Rhonas has it while BLOCKING**, a role nothing else fills. Also a 3-mana 5/5 indestructible that counts for Earth King's trigger and survives your own Planar Outburst and Austere Command.
- **Farseek** — fetches all three shocklands including two green sources.
- **The Mind Stone** — repeatable ETB blink engine.
- **Badgermole Cub** — mana doubler on every earthbent land.
- **Retreat to Kazandu** — one of only two lifegain sources.
- **Multani** — reach is one of very few answers to fliers; graveyard recursion means removal doesn't stick.
- **Ghalta** — costs 2-5 in practice, counts for Earth King, draws two on connect with Ohran + Toski.
- **The Ozolith** — Claude called it "low-impact utility," then separately argued AGAINST earthbending it. Wrong on both counts. It catches counters from every earthbent land that dies, grows from those counters while earthbent, and earthbending is what gives the CARD recursion from death and exile. See its dedicated section above.

## Enlightened Tutor targets, ranked
1. **Doubling Season** — the game-ender. Doubles every earthbend (Rockalanche at 16 Forests becomes a 32/32) AND doubles Scute Swarm, Baloths, and Avenger tokens simultaneously. **It does NOT need to survive** — it's a replacement effect that applies when counters/tokens are created, so the value locks in on resolution and killing it later undoes nothing.
2. **The Great Henge** — ramp, lifegain, a counter and a card per creature; usually only 2-3 mana with a board.
3. **The Ozolith** — strong EARLY. Everything it banks compounds, and earthbent it becomes a self-recurring threat that generates a Landfall trigger each time you empty the bank.
4. **Zuran Orb** — reactive: fetch it when you have a big earthbent threat that needs protection from bounce/tuck.

## Rejected adds (with reasons)
- **Rampant Growth** — strictly worse than Nature's Lore (fetches a Forest CARD, untapped). **CORRECTION Sept 15, 2026: this entry used to claim Shared Roots was "the same effect, but a Lesson." That was WRONG.** Shared Roots is "search your library for a **basic** land card, put it onto the battlefield **tapped**" — i.e. Rampant Growth WITH a Lesson subtype, not Nature's Lore. Verified on Scryfall.
- **Darksteel Citadel** — colorless in a 76%-green deck, and **indestructible BREAKS the earthbend engine** (the return trigger fires on death; an indestructible land never dies). Sacrificing still works.
- **Conduit of Worlds** — recursion half is nearly unusable (only if you haven't cast a spell, and then you can't cast anything else). Land-from-graveyard doesn't add triggers; Greenwarden does it better.
- **Heliod, Sun-Crowned** — triggers once per life-GAINING EVENT, not per point. Only two lifegain sources in the deck. The {1}{W} lifelink grant is the useful half, but that's a 3-mana enchantment whose best mode is a mana sink.
- **Decimate** — see rulings above.
- **More landfall payoffs** — the deck is payoff-heavy already; add triggers or draw instead.
- **Apex Altisaur, Woodfall Primus** — cut for curve; 9 and 8 mana respectively.

---

# MANA — fixed and verified Sept 2-3, 2026

Basics went 10/7/7 → **14 Forest / 5 Mountain / 5 Plains**. Green production rose from 33% to **43%**.

Current: Green cost 76% (65 pips / 50 cards) vs production 43%. White cost 15% vs production 24%. Red cost 8% vs production 24%. Colorless production 10%.

**Green still trails on paper but this is the practical ceiling.** Austere Command and Planar Outburst both need double white, so white can't be trimmed further. **Do not push basics past 14 Forest, and 35 lands is the floor.**

---

# CHANGE LOG — September 2-3, 2026 (all applied and verified)

| OUT | IN |
|---|---|
| Jungle Shrine | Gruul Turf |
| Archetype of Aggression | Rockalanche |
| Apex Altisaur | Ghostly Prison |
| Woodfall Primus | Sylvan Library |
| Hedron Archive | Zuran Orb |
| Beast Whisperer | Ohran Frostfang |
| Rishkar's Expertise | Toski, Bearer of Secrets |
| Whispersilk Cloak | Iroas, God of Victory |
| Swiftfoot Boots | The Earth King |
| Cabaretti Courtyard | Toph, the Blind Bandit |
| Solemn Simulacrum | Chromatic Lantern |
| Tannuk, Memorial Ensign | The Great Henge |
| Cultivate | Tireless Tracker |
| Sakura-Tribe Elder | Ancient Greenwarden |

**Draw went 5 → 7 and got far more reliable.** Every added draw card fires on its first trigger; Tannuk needed a second. The loss worth naming: Tannuk's per-landfall damage was a real secondary clock, especially doubled by Greenwarden. But this deck kills through combat, not pings.

**Removal went 10 → 8.** Only Austere Command and Planar Outburst are sweepers. **This is the next real gap** — against a fast combo pod it's thin.

---

# ⚑ MAYBE-ADD LIST — under consideration, NOTHING PURCHASED OR APPLIED (Sept 15, 2026)

**Deck is still at its verified 100.** User raised these; no cuts chosen yet.

## The context that drove this
User's read: **"draw and ramp feel a bit slow."** Correct diagnosis, and the raw counts hide it.

- **Draw (7) is almost all win-more.** Ohran Frostfang and Toski need you already connecting. The Great Henge needs a big creature. Guardian Project needs creatures entering. Tireless Tracker needs landfall plus spare mana to crack Clues. Garruk's Uprising barely triggers here at all. **Sylvan Library is the only draw that functions turns 1-4.**
- **Ramp (14) — only five pieces actually accelerate:** Sol Ring, Arcane Signet, Farseek, Nature's Lore, Lotus Cobra. The rest are Toph-dependent value, not acceleration.
- **ZERO one-mana mana dorks.** The commander costs 4 and the whole deck is built on his static ability. Birds of Paradise / Llanowar Elves / Ignoble Hierarch would make turn-3 Toph routine and help the green pip gap.
- **No true mana doubler.** Badgermole Cub (earthbent lands only) and Chromatic Lantern (grants a mana ability to every land, artifacts included) are the closest. **The Great Henge also taps for {G}{G}** — it is filed under Draw but IS a mana source; don't forget it when listing ramp.
- **Lotus Cobra is the only landfall-to-mana card**, so most of the deck's many landfall triggers produce no mana.

## TRAMPLE SOURCES (asked Sept 15) — only three
**Badgermole** (to anything with a +1/+1 counter — the main one), **Garruk's Uprising** (blanket), **Craterhoof Behemoth** (one-shot ETB). **Badgermole Cub is NOT a trample source** despite the name — it's the mana doubler. Two persistent sources is thin for a deck whose kill plan is a concentrated trampler.

## The four candidates, ranked for this deck

**1. Embodiment of Insight** — {4}{G} Creature — Elemental 4/4. Vigilance. **"Land creatures you control have vigilance."** Landfall — target land you control becomes a 3/3 Elemental with haste until end of turn; it's still a land.
- **The vigilance line is the real prize.** Earthbent lands are permanently creatures (no duration), so unlike the Bello deck this GENUINELY gives blockers on the crack-back — the exact hole Ghostly Prison patches. 5 mana vs Akroma's 7, no pro-red clause.
- **LAYERS TRICK:** its animation sets base P/T to 3/3, which is a base-setting effect like earthbend's 0/0 — **later timestamp wins.** Target an ALREADY-earthbent land and the 3/3 overwrites the 0/0 base while counters stay on top: a land with 4 counters becomes a **7/7** until end of turn. Target a fresh land and then earthbend it and you get the bad end — earthbend's 0/0 overwrites the 3/3, leaving a 2/2. **Toph's earthbend fires at your end step, so don't point it at an Embodiment-animated land.**
- Caveat: the file's own "more landfall payoffs" rejection cuts against the landfall half. Judge it as a vigilance card with a landfall rider.

**2. Spine of Ish Sah** — {7} Artifact. "When this artifact enters, destroy target permanent. When this artifact is put into a graveyard from the battlefield, return it to its owner's hand." **Much stronger here than in the Bello deck, where it was rejected.**
- Enters as a LAND under Toph = Landfall trigger. Legal earthbend target.
- **⚑ THE TWO RETURN TRIGGERS FIGHT EACH OTHER — you do NOT get both.** Earthbend's delayed return and Spine's own return-to-hand both fire on the same event. You control both, so you order them: put earthbend's LAST on the stack so it resolves FIRST. Spine goes graveyard → battlefield; Spine's own trigger then can't find it in the graveyard and does nothing. **You want the earthbend one** — battlefield beats hand.
- **The return re-triggers its ETB destroy.** Free removal, no 7-mana recast.
- **Official ruling: Spine's ability does NOT let you sacrifice it — you need an outside outlet. Zuran Orb is one, and ONLY because Toph makes artifacts lands.**
- **The loop:** earthbend Spine → sac to Zuran Orb → gain 2 → earthbend returns it tapped → ETB destroys a permanent → Landfall fires. **Roughly one free removal per turn cycle**, rate-limited because each earthbend's delayed trigger is one-shot and it returns as a plain land with no counters. **NOT infinite.** Directly patches the removal gap (8, only two sweepers).

**3. Akroma's Memorial — NO LONGER A CANDIDATE, ADDED Sept 20, 2026** (owner had it on hand). See the swap entry below. Verified text: {7} Legendary Artifact, $36.21 — "Creatures you control have flying, first strike, vigilance, trample, haste, and protection from black and from red."
- Trample from a non-fragile source, plus evasion, plus the same vigilance fix.
- **Overlaps Embodiment on vigilance** — probably don't need both.
- **Downside: pro-red means your own Chaos Warp can't target your creatures.**

**4. Vorinclex, Voice of Hunger** — {6}{G}{G}. Doubles your land mana; opponents' lands don't untap. **DELISTED as a Game Changer Oct 21, 2025 — no bracket cost.** Confirmed absent from the official list in `game_changers.md`.
- **The deck's only true mana doubler**, which is a real gap.
- **But 8 mana is a win-more card in a deck whose stated problem is turns 3-5.** Ranked last for that reason.

## ⛔ THE CURVE TENSION — flag this every time
**All four are 5-8 mana: 27 mana of top end added to a deck the user says feels slow.** Every one is a good card; together they make the diagnosed problem worse. **If the goal is fixing the slow start, the answer is 1-2 mana dorks and cheap card draw, not more 7-drops.**

## Ramp swap under discussion
- **Shared Roots OUT → Three Visits IN?** Three Visits fetches a Forest CARD untapped (so it grabs Stomping Ground and Temple Garden); Shared Roots fetches a BASIC, tapped. Better rate.
- **The cost is the Lesson subtype** (Toph Hardheaded Teacher keys off it). Would drop Lessons from 5 to 4: Cycle of Renewal, True Ancestry, Origin of Metalbending, Rockalanche. **User's call — depends how often Teacher is actually on board.**
- **User also asked about "the one that plays 2 lands, or 1 land and 1 in hand."** That's Cultivate — **already deliberately cut** in the Sept 3 rebuild for Tireless Tracker; don't re-add it by accident. If extra LAND DROPS are what's wanted (better in a landfall deck, since each drop is a live trigger), the real options are **Exploration, Azusa, Dryad of the Ilysian Grove, Wayward Swordtooth**.

## Still to do before any of this is applied
1. **Re-pull Archidekt.** Standing rule; last verified Sept 3.
2. **Price Embodiment, Spine, Vorinclex.** Still not checked. Akroma's Memorial is done — $36.21, and it's in the deck now.
3. **Choose cuts.** None identified yet.

## Carried over from pending_changes.md / conversation_history.md (merged Sept 19, 2026 — these files are being retired now that GitHub is the source of truth)

### Open item — maybe-add list from Sept 15, nothing applied yet
Four candidate adds discussed, ranked: Embodiment of Insight > Spine of Ish Sah > Akroma's Memorial > Vorinclex, Voice of Hunger. **All four are 5-8 mana — flags curve tension against the deck's actual problem, which is being slow.** The honest fix is more 1-2 mana dorks and cheap draw, not more top end. No cuts identified yet to make room. Re-pull Archidekt and price all four before applying anything.

### Open item — ramp swap under consideration
Shared Roots → Three Visits (better rate, but loses the Lesson subtype relevant to Toph Hardheaded Teacher). Note: Cultivate was already cut earlier — don't re-add it by accident.

### Diagnosis established Sept 15 — draw and ramp look healthy on paper but aren't
- 6 of 7 draw cards are win-more (reward a board you don't have yet) — Sylvan Library is the only one live turns 1-4.
- Only 5 of 14 ramp pieces actually accelerate: Sol Ring, Arcane Signet, Farseek, Nature's Lore, Lotus Cobra. The rest are Toph-dependent value.
- Zero one-mana dorks under a 4-mana commander the whole deck depends on.
- Lesson: count what's live on turns 1-4, not category totals. The Great Henge (filed under Draw) also taps for {G}{G} — read across the whole list, not just the section header.

### Removal gap flagged
Only 8 removal spells, with just Austere Command and Planar Outburst as sweepers. Spine of Ish Sah + Zuran Orb would patch this (see ruling below on how that actually works here).

### Bracket
~~Four Game Changers confirmed... = Bracket 4 by rule.~~ **SUPERSEDED Sept 20, 2026 — Green Sun's Zenith is not a Game Changer. The deck runs three and is a legitimate Bracket 3. See the BRACKET section above and `game_changers.md`.**

### Rulings established (Toph-specific interactions — easy to miss)
1. **Earthbend has no duration** — earthbent lands are permanently creatures. This is why Badgermole Cub doubles their mana and why haste matters (a land-creature couldn't otherwise tap while summoning sick). Vigilance genuinely gives blockers in Toph (contrast: it does NOT in Bello, where the animation ends at end of turn).
2. **Nontoken artifacts enter as lands under Toph, triggering Landfall** — but Clues and Treasures are tokens and do NOT trigger it. (Confirmed: Tireless Tracker's Clues generate no Landfall here.)
3. **Base-P/T-setting effects don't stack — later timestamp wins — but +1/+1 counters (layer 7d) apply AFTER, stacking on top of whatever base P/T is currently set.** Example: Embodiment of Insight's landfall animation sets base P/T to 3/3; animate an already-earthbent land and the 3/3 overwrites the 0/0 while existing counters stay on top (4 counters = a 7/7 in that case). Do it in the wrong order and Toph's end-step earthbend overwrites the 3/3 back down to 0/0.
4. **Spine of Ish Sah**: the two return triggers (earthbend's delayed return and Spine's own return-to-hand) fight over the same event — you do NOT get both. Order earthbend's return FIRST so Spine goes graveyard→battlefield and its own trigger can't find it; battlefield beats hand, and the return re-triggers the ETB destroy. Official ruling: Spine can't sacrifice itself for its own cost. **Zuran Orb is the sac outlet, and only works here because Toph makes artifacts lands.** Roughly one free removal per turn cycle, not infinite. (Contrast: this exact card was rejected the same day for the Bello/raccoon deck — Bello has no artifacts-are-lands clause, so there's no outlet there. Same card, opposite verdict, context-dependent.)
5. **Shared Roots is NOT "Nature's Lore but a Lesson."** Actual text: search for a BASIC land, put it onto the battlefield TAPPED — it's Rampant Growth with a Lesson subtype. Corrected in this file already; don't repeat the old description.

### Verification failures on record (don't repeat)
- This file once listed Etali, Primal Conqueror as in the deck — that card was never in the real Archidekt list, and a "cut" was made against a phantom card.
- The file also once omitted Bumi, Unleashed and Craterhoof Behemoth entirely (a whole missing "Finisher" category) and misfiled Tireless Tracker and Ghalta.
- Cards wrongly flagged as weak in past sessions — don't re-suggest cutting: Seismic Tutelage (covered by The Ozolith catching counters), Rhonas, Farseek, The Mind Stone, Badgermole Cub, Multani, Ghalta.
- Always re-pull Archidekt before recommending cuts — at one point 11 agreed swaps sat unapplied on Archidekt while the file claimed they were done.

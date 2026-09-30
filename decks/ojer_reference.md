# Cards Reference — Ojer Axonil, Deepest Might (`ojer`)

**Status: NEW, uploaded to Archidekt 2026-09-30, not yet built in paper.** Created 2026-09-29. Sim harness key: **`ojer`**.

**Archidekt:** https://archidekt.com/decks/26925771/ojer_mono_red — verified card-for-card against
this file on 2026-09-30 by diffing the Archidekt API against `ojer_decklist.txt`: 100 cards each,
zero differences in either direction.

**Every card resolved against `scryfall.db`** — all 100 checked for colour identity (zero off-colour)
and Commander legality. One legality flag, see "Koth" below.

Built from a database sweep of red "damage to each opponent" effects, then corrected against the
EDHREC page for this commander (`edhrec.com/commanders/ojer-axonil-deepest-might`), which the deck
owner supplied. That second pass mattered — see "What the EDHREC pass changed".

## Commander

**Ojer Axonil, Deepest Might** — {2}{R}{R} — Legendary Creature — God — **4/4 trample**

> Trample
> If a red source you control would deal an amount of **noncombat** damage **less than Ojer Axonil's
> power** to an opponent, that source deals damage equal to Ojer Axonil's power instead.
> When Ojer Axonil dies, return it to the battlefield tapped and transformed under its owner's control.

Back face: **Temple of Power** — Land. {T}: Add {R}. {2}{R}, {T}: Transform this land. Activate only
if red sources you controlled dealt 4 or more noncombat damage this turn, and only as a sorcery.

**The commander recurs itself.** It dies, comes back as a land, and flips back for {2}{R}. That is a
fail-safe printed on the card, not one the deck has to build around.

## The thesis

Every cheap red card that reads "deals 1 damage to each opponent" becomes **"deals 4 damage to each
opponent"** — 12 across a four-pod, off a one-mana card. **37 of the 99 are Ojer payoffs** (39
counting Pyrohemia and Rampaging Ferocidon, whose wording differs).

| Card | Prints | With a 4/4 Ojer | Four-pod total |
|---|---|---|---|
| Thermo-Alchemist {1}{R} (untaps on each instant/sorcery) | 1 each | **4** each | 12 **per untap** |
| Unruly Catapult {2}{R} (same) | 1 each | **4** each | 12 per untap |
| Electrostatic Field {1}{R} | 1 each | **4** each | 12 per spell |
| Guttersnipe {2}{R} | 2 each | **4** each | 12 per spell |
| Manabarbs {3}{R} | 1 per land tapped | **4** per land tapped | ~60 per turn cycle |
| Pyrohemia {2}{R}{R} — **{R}: repeatable** | 1 each | **4** each | **12 per red mana** |
| Fiery Confluence {2}{R}{R} (pick the same mode ×3) | 2 each, three times | **12** each | **36 for four mana** |

## THE TRAP — read this before adding any damage doubler

Every guide names **Torbran, Thane of Red Fell**, **Fiery Emancipation**, **Gratuitous Violence** and
**Solphim, Mayhem Dominus** as the Ojer payoffs. **This deck runs none of them, deliberately.**

All four are replacement effects, and so is Ojer. Under **rule 616.1** the **affected player — the
opponent being dealt the damage — chooses the order they apply in.** On a 1-damage ping with a 4/4
Ojer:

| Order the opponent picks | Result |
|---|---|
| Torbran first: 1 → 3, then Ojer (3 is still < 4) → | **4** |
| Ojer first: 1 → 4, then Torbran → | 6 |

They will always pick the first. **Torbran adds zero.** The same maths blanks Solphim (doubling) and
Fiery Emancipation (tripling) on any ping below Ojer's power.

**Independent corroboration:** EDHREC lists Torbran at **−0% synergy** and Fiery Emancipation at
**−3%** on this commander. Synergy % only measures how much *more* often a card appears here than in
red decks generally, so it is not proof — but experienced Ojer pilots demonstrably are not seeking
them out, which is what the rules reading predicts.

**Confidence is high but not absolute. Worth a judge call or a playgroup agreement** before buying
into the doubler package, the same way the Mindskinner ruling was handled.

## The scaling lever is Ojer's power

Since the doublers do not work, **raising Ojer's power is how this deck scales** — every point raises
the floor on every ping in the deck simultaneously.

| Equipment | | Ojer becomes | Every ping becomes |
|---|---|---|---|
| **Commander's Plate** {1}, equip commander {3} | +3/+3, **protection from white, blue, black and green** | 7/7 | **7** |
| **Hero's Blade** {2} | +3/+2, **attaches free whenever a legendary creature enters** | 7/6 | **7** |
| **Champion's Helm** {3}, equip {1} | +2/+2 and **hexproof** while legendary | 6/6 | 6 |
| **Blackblade Reforged** {2}, equip legendary {3} | +1/+1 per land — at 10 lands | 14/14 | **14** |
| **Swiftfoot Boots** {2}, equip {1} | hexproof and haste | — | — |

Hero's Blade re-attaches for free every time Ojer comes back from Temple of Power.

## The engine loop

**Electro, Assaulting Battery** {1}{R}{R} 2/3 flying → every instant or sorcery adds {R}, and unspent
red **does not empty between steps and phases**. **Pyrohemia** converts each {R} into 4 damage to
each opponent. Cast a cheap spell, bank the red, spend it for 12 across the table. **Neheb, the
Eternal** then adds {R} for each 1 life opponents lost this turn at your postcombat main.

## What red normally can't do, and how this deck does it

- **Board control:** **Chandra's Incinerator** {5}{R} 6/6 trample costs {X} less for noncombat damage
  dealt to opponents this turn (routinely a 2-mana 6/6 here), and turns **every subsequent ping into
  creature removal** as well.
- **Card advantage:** **Virtue of Courage** exiles that many cards off every noncombat damage
  instance — 4 cards a ping. Behind it: Light Up the Stage, Wrenn's Resolve, Reckless Impulse, Grab
  the Prize, Thrill of Possibility, Faithless Looting, Needle Drop, Jeska's Will and War Room, plus
  two wheels in Wheel of Misfortune and Chandra, Torch of Defiance's +1.
- **Fliers:** **Longshot, Rebel Bowman** has reach and makes noncreature spells cost {1} less,
  **Koth, the Geomancer** has reach, **Electro** flies.
- **Blocking:** Electrostatic Field 0/4, Unruly Catapult 0/4, Thermo-Alchemist 0/3, Spear Spewer 0/2,
  Kessig Flamebreather 1/3. **The engine pieces are the defence.**
- **Enchantments:** Chaos Warp, plus a trick — **Liquimetal Torque**'s second ability makes any
  nonland permanent an artifact until end of turn, so **Abrade or Vandalblast can then destroy an
  enchantment**. That is three answers instead of one. Still mono-red's weakest axis; mulligan
  toward them against blue or white.

## Creature-ETB payoffs and the token mini-package

Added 2026-09-29. **Impact Tremors** is not really a token card here — the deck runs **19 creatures**,
so it triggers off the normal curve from turn two with no tokens at all, for 4 to each opponent a
time. It is the second copy of the Purphoros effect.

**Hordeling Outburst** {1}{R}{R} is the one token spell worth a slot, because it does two jobs at
once: three bodies means three Purphoros triggers and three Impact Tremors triggers (**72 across a
four-pod with both out**), while the spell itself still sets off Guttersnipe, Electrostatic Field,
Erebor Flamesmith, Fiery Inscription, Firebrand Archer, Kessig Flamebreather, Longshot and Urabrask,
and untaps Thermo-Alchemist and Unruly Catapult. A token *creature* like Beetleback Chief only does
the first half.

The quieter reason: the board is 0/2s and 0/4s that each stop exactly one attacker. **Three goblins
are three more blockers**, which is the shape of defence the blue deck kept losing for want of.

**Krenko, Mob Boss was left out.** It is the right card if this ever becomes a full goblin build, but
{2}{R}{R} that must survive a rotation pulls slots away from the punisher shell.

## Why there is no board wipe

**Blasphemous Act was cut on 2026-09-29.** Thirteen damage to each creature kills Ojer, every pinger
and every wall — in a deck where the creatures *are* the engine, the reset button costs more than
the board it answers.

**Red has no one-sided full wipe.** The honest options are a symmetric wipe that kills your own
engine, or a one-sided partial sweeper that only kills small creatures. This deck takes the second:
**Delayed Blast Fireball** {1}{R}{R} (2 damage to each opponent **and each creature they control** —
4 to each opponent with Ojer, and your board is untouched), alongside End the Festivities and
Tectonic Hazard, which are one-sided in the same way, and Fiery Confluence's repeatable
1-damage-to-each-creature mode.

**Chandra's Ignition was considered and rejected.** With Commander's Plate on a 7/7 Ojer it deals 7
to each *other* creature and 7 to each opponent, which is often lethal — but "each other creature"
includes all of yours. It is a finisher, not a sweeper, and it turns off the engine on the way.

## Card advantage, and the wheel kill

**13 sources, which is a lot for mono-red, but most of it is impulse rather than draw.** You do not
build a hand here, you play off the top at speed — which works at a 2.41 curve with rituals, and
whose failure mode is specific: **exile cards while tapped out and they are gone.** No hand-size
effect helps, because impulse never fills your hand.

| Draw and keep | Impulse — exile and play |
|---|---|
| Grab the Prize, Faithless Looting, Needle Drop, Mind Stone | Virtue of Courage, Jeska's Will, Light Up the Stage, Wrenn's Resolve, Reckless Impulse, Chandra +1 |
| **War Room** — the only repeatable engine, and mono means it costs 1 life | |
| **Wheel of Misfortune, Reforge the Soul, Magus of the Wheel** — refill from empty | |

**Virtue of Courage scales with the pings**, since your damage instances are 4 and not 1.

**CONFIRMED, 2026-09-29: it triggers once per opponent.** The trigger reads "deals noncombat damage
to **an opponent**", not "each opponent", so a single damage event hitting all three puts **three
separate triggers** on the stack, each its own "may". With Ojer out, **one Thermo-Alchemist tap is
3 triggers × 4 cards = 12 cards exiled** and playable that turn. (`scryfall.db`'s `rulings` table
carries only generic Adventure rulings for this card; verified externally against tappedout,
Gatherer and EDHREC, whose worked example is Dragon's Approach producing three triggers in a
four-player game.) Note you must actually cast them that turn — at a 2.51 curve with rituals you
convert a good share of twelve, not all of it.

### Razorkin Needlehead + a wheel is the deck's biggest burst

> **Razorkin Needlehead** {R}{R} — Whenever an opponent draws a card, this creature deals 1 damage to
> them. *(No once-per-turn clause.)*

With Ojer out that is **4 damage per card drawn**. A wheel makes each opponent draw seven:

**7 cards × 4 damage = 28 to each opponent, 84 across a four-pod, off a three-mana sorcery.**

This is why the deck runs **three** wheels. **Reforge the Soul** (added over Thrill of Possibility)
is a burn spell here that happens to read "draw seven", and its miracle cost of {1}{R} makes it a
two-mana kill off the top.

**Magus of the Wheel** {2}{R} 3/3 was added over Spear Spewer, and the reason is not that it is a
third wheel — it is that **it is a wheel you do not have to fire.** The real hazard of wheels here
is that they refill your *opponents*: without Razorkin on board, a wheel hands three players seven
fresh cards including the removal they did not have. A sorcery wheel you draw is cast-it-or-sit-on-
it. Magus sits on the battlefield and you crack it the turn Razorkin lands. It is also a creature,
so casting it triggers Purphoros and Impact Tremors for **24 across a four-pod** before it wheels
anything.

Not a Bracket 3 problem: Razorkin, Ojer and a wheel are nine mana across several turns, and nothing
about it is infinite.

#### Tutoring: one card, and why that is nearly enough

**Gamble is the only tutor in the 99.** Mono-red genuinely cannot search its library; this is the
colour's defining weakness alongside enchantment removal. The deck mostly does not mind, because
there is no combo piece to hunt — **37 payoffs, and any of them will do.** Redundancy is the tutor.

**The exception is Razorkin Needlehead**, which became a combo piece the moment the wheel line was
identified, and there is one copy. **Imperial Recruiter** {2}{R} 1/1 was added over Chain Lightning
for that reason: ETB, search for a creature with power 2 or less, which in this deck is **11
targets** — Blisterspit Gremlin, Electro, Electrostatic Field, Erebor Flamesmith, Firebrand Archer,
Guttersnipe, Kessig Flamebreather, **Razorkin Needlehead**, Thermo-Alchemist and Unruly Catapult. It
is never a dead draw, it finds the combo piece, and it is another body for Purphoros and Impact
Tremors. Inventors' Fair and Hoarding Dragon were the artifact-tutor alternatives and are worse
here, since the artifacts are not what you need to find.

**Chain Lightning** was the slot because it is single-target where Boltwave deals the same 4 to
*each* opponent, and its copy clause lets a red opponent pay {R}{R} and send it back — Toph, Tifa
and Bello all play red.

### The Fire Crystal — considered, rejected

{2}{R}{R}: red spells cost {1} less, creatures have haste, and {4}{R}{R},{T} for a temporary token
copy. **Rejected on cost, not on quality** — it costs exactly what Ojer costs, and turn four is the
commander's turn. Its first line duplicates Ruby Medallion at twice the price, and unlike **The Water
Crystal** in `newmill`, whose middle line multiplies every mill trigger, the haste clause is not a
damage payoff. It is better here than EDHREC's −12% synergy suggests, because four tap-pingers
(Thermo-Alchemist, Unruly Catapult, Spear Spewer, Blisterspit Gremlin) each gain an activation the
turn they land — just not four mana's worth.

## The self-damage ledger — the deck's real cost

Five cards hurt you as well, and they stack:

| Card | **Each opponent takes** | You take |
|---|---|---|
| Manabarbs (~5 land taps each) | **20** | 5 |
| Burning Earth (~3 nonbasics each; you run 25 Mountains) | **12** | 1–2 |
| Roiling Vortex | **4** | 1 |
| Sulfuric Vortex (**nobody gains life**) | **4** | 2 |
| Pyrohemia (per {R}) | **4** | 1 |
| **Per turn cycle** | **~40 each, ~120 across the table** | **~9–10** |

**That is roughly 12 to 1 in your favour**, so the self-damage is not a problem worth solving. They
die in about one full cycle once it is all online; you would need four.

**The real risk is a stalled game, not the arithmetic.** Your clock runs whether or not the engine
does. If Ojer is exiled and the pingers drop from 4 to 1, the punishers still take 9–10 off you per
cycle while doing a third as much to them. So **deploy the punishers when you can close**, not on
curve — and note that every extra mana rock cuts your own Manabarbs exposure.

## Deliberately excluded, and why

- **Torbran / Fiery Emancipation / Gratuitous Violence / Solphim** — the 616.1 ordering trap above.
- **Spellshock** ({2}{R}, 2 damage to a player per spell **they** cast) and **Magebane Lizard** — you
  are the player casting eight spells a turn. These point the wrong way in this deck specifically.
- **Geosurge** {R}{R}{R}{R} — seven red, but spendable only on **artifact or creature spells**.
  Rituals earn their slot here by casting *more instants and sorceries*, which trigger the pingers.
  Geosurge's mana cannot do that. Pyretic Ritual, Desperate Ritual and Seething Song can, and are in.
- **Curse of Opulence** — a fine political one-drop, but *"each opponent attacking that player does
  the same"* hands the aggressive players free Gold that taps for mana **without** triggering
  Manabarbs or Burning Earth. It partly undoes two of the deck's best cards. Close call, left out.

## Koth — legality

**Koth, the Geomancer** {2}{R} 3/2 (Reach; landfall — 1 damage to each opponent, and add {R} if the
land is a Mountain) is from **Reality Fracture**, released **2026-10-02**. It reads
`commander: not_legal` in `scryfall.db` only because the set was not out when this list was built.
**Swap in Fire Diamond** if a strictly-legal-today list is needed.

## Known weaknesses

- **No enchantment removal beyond one Chaos Warp.**
- **Without Ojer the pingers deal 1 instead of 4.** The recursion softens it, but the deck is far
  worse while the commander is answered. Same shape of risk as the Mindskinner build.
- **Card advantage is impulse-only** — you play off the top a great deal.
- **Red gets hated out early in pods**, and this build telegraphs itself the moment Manabarbs lands.

## Bracket

**Bracket 3, one slot free. 2 Game Changers:** Gamble, Jeska's Will. Verified against
`game_changers.md`.

## Mana base notes

**33 lands, 29 of them red-producing.** The four that are not — Nykthos, Shivan Gorge, Tyrite
Sanctum, War Room — are a mild tension against the 7 cards needing two or more red pips, which is
the reason not to add a fifth colourless utility land.

**Rocks matter more here than in most red decks.** Manabarbs and Burning Earth damage *you* whenever
*you* tap a land; mana rocks, rituals and Koth's landfall trigger all sidestep that entirely. The
deck runs **six rocks** — Sol Ring, Arcane Signet, Mind Stone, Fire Diamond, Liquimetal Torque,
Worn Powerstone — and **32 lands rather than 33**, deliberately: in this deck a rock is strictly
better than a land, because the land costs you life every time you tap it.

**Fellwar Stone was cut for Fire Diamond on 2026-09-29.** Fellwar taps for a colour an *opponent's*
land could produce, so against the mono-coloured decks in this collection it can produce nothing
castable. Fire Diamond always makes red. It enters tapped, which costs a turn and is the whole price.

## Four-colour pod sim — 2026-09-30, 24 games

`ojer` (red) vs `newmill` (blue) vs `deathtouch` (black) vs `kodama` (green). Five seeds, 5-game
batches, 24 decided games, 1 drawn, median kill turn 17. Par in a four-way pod is **25%**.

| Deck | Wins | Rate | 95% CI | vs par |
|---|---|---|---|---|
| deathtouch (black) | 11 | **45.8%** | [26%, 66%] | z = +2.36, **exact p = 0.021** |
| ojer (red) | 8 | 33.3% | [14%, 52%] | z = +0.94, p = 0.23 |
| kodama (green) | 3 | 12.5% | [0%, 26%] | z = −1.41, p = 0.12 |
| newmill (blue) | 1 | **4.2%** | [0%, 12%] | z = −2.36, **exact p = 0.009** |

**Only two of the four results are real.** Black is significantly above par and blue significantly
below, on exact binomial tests. Red and green are both inside the noise — red finishing second
means nothing at this sample size.

**Method note:** a single unattended 45-game run is not possible in this environment. The harness
caps background jobs at 10 minutes, and detaching with `setsid` does not survive either, because the
container is reclaimed when the session idles. These 24 games came from 5-game batches run inside
live turns; one batch timed out and produced nothing.

## Deck statistics

100 cards · 32 lands (25 Mountain) · 20 creatures · 6 mana rocks · 27 instants and sorceries ·
13 card-advantage sources · 1 tutor · average CMC 2.51 · zero off-colour · all commander-legal except the Koth release date above.

# Cards Reference — Virtus the Veiled mono-black deathtouch

**Status: BUILT AND OWNED. All 10 outstanding cards acquired — owner confirmed 2026-10-27.**
Designed Sept 28, 2026. **The owner confirmed the deck was fully built and this list matched his
physical deck right up until the 2026-10-22 nine-card swap.** As of 2026-10-27 the owner has every
card in the 100 in hand, including all ten from the 10-22 and 10-26 swaps.

**ACQUIRED 2026-10-27 (10) — these are the cards going INTO the paper deck:**

```
Aetherflux Reservoir      Grave Pact
Ayara, First of Locthwain Skullclamp
Blood Artist              South Wind Avatar
Enduring Tenacity         Stensian Sanguinist // Exsanguinate
Erebos, God of the Dead   Tergrid, God of Fright // Tergrid's Lantern
```

**Coming out, back to the collection (10) — pair each with its replacement:**

| Out | In |
|---|---|
| Archetype of Finality | Tergrid, God of Fright // Tergrid's Lantern |
| Black Market | Erebos, God of the Dead |
| Gonti, Lord of Luxury | South Wind Avatar |
| Ravening Warg | Aetherflux Reservoir |
| Thrill-Kill Assassin | Enduring Tenacity |
| Arcane Signet | Ayara, First of Locthwain |
| Hired Poisoner | Blood Artist |
| Burrog Banemaker | Stensian Sanguinist // Exsanguinate |
| Case of the Gorgon's Kiss | Skullclamp |
| Bojuka Bog | Grave Pact |

**Thornbite Staff is on neither list — do NOT pull it.** It was cut and restored in the same
session on 2026-10-22, so it never actually left the deck.

Earlier status lines on this file were wrong and are superseded: "No cards acquired, nothing
sleeved" and "this is a shopping list, not a deck" were stale from the September design pass, and
the 2026-10-21 "build state unconfirmed" note has now been answered.

**Archidekt:** https://archidekt.com/decks/26876893/deathtouch_mono_black — verified card-for-card
against this list on 2026-09-28 (100 cards, zero differences, Virtus correctly set as commander).
The only textual variance is naming: Archidekt writes the Adventure card as
`Foulmire Knight // Profane Insight`, this list uses the front-face name `Foulmire Knight`.

**Every card below was resolved against `scryfall.db`.** Colour identity was checked on all 100
(zero off-colour), and every card has a Forge card script, so the deck is simulatable.

**Note on double-faced and Adventure cards.** This list stores front-face names only. The sim
harness handles that (it splits on `//`), but a naive lookup against `scryfall.db` will silently
fail to resolve `Foulmire Knight`, which is stored as `Foulmire Knight // Profane Insight`. Any
script counting theme density must fall back to a `LIKE 'name //%'` match or it will undercount.
Foulmire Knight does have deathtouch; the verified count is **28 of 100, 44% of non-land cards**.

## Commander

**Virtus the Veiled** — {2}{B} — Legendary Creature — Azra Assassin — **1/1**
"Partner with Gorm the Great. Deathtouch. Whenever Virtus deals combat damage to a player, that
player loses half their life, rounded up."

Do NOT run Gorm the Great — he is green and would break mono-black.

## What the deck does

Three axes that feed each other:

1. **Everything has deathtouch.** 22 creatures have it printed; Archetype of Finality covers the
   rest and turns it OFF for opponents. Nobody can block profitably and nobody wants to attack.
2. **Deathtouch plus a ping equals removal.** Any damage from a deathtouch creature is lethal, so
   Viridian Longbow ({T}, free) or Thornbite Staff ({2},{T}, and it UNTAPS whenever any creature
   dies) kills anything on board. Basilisk Collar grants deathtouch AND lifelink to any body.
3. **Lifegain converts to damage.** Many deathtouch creatures also have lifelink. Vito turns all of
   it into drain, and Exquisite Blood / Bloodthirsty Conqueror close the loop.

## The kill — complete combo grid, rebuilt 2026-10-26

**Four independent kill engines, 11 two-card assemblies between them.** Rebuilt from a full scan of
the 100 after the 2026-10-22 nine-card swap and the 2026-10-26 Grave Pact swap. **Engine 4 was
added 2026-10-27** after it won a game outright and turned out not to be in this file at all.

### ENGINE 1 — the life loop. Side A x Side B = 8 assemblies.

**Side B** — *"whenever an opponent loses life, you gain that much life"*:

| Card | Cost | Notes |
|---|---|---|
| **Exquisite Blood** | {4}{B} | Also half of Engine 2 — see below |
| **Bloodthirsty Conqueror** | {3}{B}{B} | 4/4 flying deathtouch body |

**Side A** — *"whenever you gain life, an opponent loses life"*:

| Card | Cost | Notes |
|---|---|---|
| **Vito, Thorn of the Dusk Rose** | {2}{B} | Targeted, loses *that much*. Also `{3}{B}{B}`: mass lifelink — **the best spark in the deck**, see below |
| **Enduring Tenacity** | {2}{B}{B} | Targeted, loses *that much*. Recurs itself as an enchantment when it dies |
| **Marauding Blight-Priest** | {2}{B} | Each opponent loses **1**, not that much — still infinite, just slower per iteration |
| **South Wind Avatar** | {3}{B} | Each opponent loses 1. Deathtouch body, **and its own spark** (gain life when another creature dies) |

Any Side A + any Side B = **8 infinite assemblies**. Vito and Enduring Tenacity scale with the
amount; Blight-Priest and South Wind Avatar tick 1 at a time but still loop forever, and ticking
one opponent to 0 just moves the loop to the next.

**Vito does three jobs on one card — confirmed in play 2026-10-27.** It is Side A, it is a spark
source, and its `{3}{B}{B}` mass-lifelink ability turns **any** creature into a spark on demand.
That last part is the one to remember: with Vito and a Side B card already down, five mana and a
single point of combat damage from anything you control starts the loop. You do not need to draw a
spark — Vito *is* the spark button.

**More than one Side A out at once makes the loop faster, not redundant.** Each Side B lifegain
triggers every Side A card you control. With Vito and Marauding Blight-Priest both out
(2026-10-27), the targeted opponent took 2 per iteration while the other two took 1.

**Side B is the bottleneck.** Exquisite Blood and Bloodthirsty Conqueror are the ONLY two cards in
all of mono-black with that text. There are four Side A cards and only two Side B cards, so **the
five tutors should fetch Side B.**

**The loop does NOT self-start.** Both halves on the battlefield still do nothing until one
life-change event happens. **22 cards in the deck can be that spark:**

- *You gain life:* Aetherflux Reservoir (every spell cast), Arnyn Deathbloom Botanist, Ayara First
  of Locthwain, Basilisk Collar (grants lifelink), Blood Artist, Crypt Ghast (extort), Exsanguinate,
  Gifted Aetherborn, Gray Merchant of Asphodel, Hooded Blightfang (on ATTACK, not on damage),
  Nighthawk Scavenger, Qarsi Revenant, Sheoldred the Apocalypse (every card you draw), South Wind
  Avatar, **The Darkness Crystal** (2 life every time *any* opponent's nontoken creature dies —
  including in combat between two other players, confirmed 2026-10-29), Vampire Nighthawk,
  Vampire of the Dire Moon, Vito (mass lifelink).
- *An opponent loses life:* Virtus the Veiled (half their life), Quietus Spike (half their life),
  Torment of Hailfire, Tergrid's Lantern, **Hooded Blightfang** (each opponent loses 1 on attack),
  **Crypt Ghast** (extort — each opponent loses 1 per spell cast).

**Two cards appear in both lists on purpose — Hooded Blightfang (amended 2026-10-28) and Crypt
Ghast (amended 2026-10-29).** Extort reads *"each opponent loses 1 life and you gain that much
life"* — one trigger, both events — so the Ghast sparks Side A and Side B alike, **on every spell
you cast**, which makes it the most reliably available spark in the deck once it is down.

**Hooded Blightfang appears in both lists on purpose — amended 2026-10-28 after the 11th game.**
Its single attack trigger is simultaneously a lifegain event and a life-loss event on every
opponent, so it sparks Side A *and* Side B — **it does not matter which half of the engine you
drew** (Crypt Ghast above is the other card with this property; an earlier version of this line
called Blightfang the only one, which was true until 2026-10-29). It also
triggers on declaring the attack, not on damage, so blockers and post-blocker removal cannot
stop it.

That is 22 **distinct cards**. An earlier line in this file counts "32" — that figure counts
trigger instances, since several of these cards provide more than one. Both are correct; this one
is the card count.

**In practice, opponents spark it for you — this is the deck's most underrated property.** Three
logged wins so far were sparked from outside this deck entirely:

- **2026-10-21** — one opponent attacked another opponent with Avacyn, Angel of Hope for 10.
- **2026-10-26 (turn-4 win)** — an opponent's own **Wretched Anurid** (*"whenever another creature
  enters, you lose 1 life"*) triggered off Bloodthirsty Conqueror entering. Their punisher card
  killed their whole table.
- **2026-10-29** — Brady's **Scrawling Crawler** (*"at the beginning of your upkeep, each player
  draws a card; whenever an opponent draws a card, that player loses 1 life"*) made Gabrielle draw
  and lose 1 on Brady's own upkeep. Exquisite Blood saw it, Blight-Priest saw the lifegain, and
  the loop killed both of them.

**Any symmetrical drain, punisher or forced-draw on the table is a live spark**, and it fires on
their turn, when nobody is holding up an answer.

**ANY** life-change event anywhere at the table starts the loop: an opponent's lifelink attack, a
shockland, a Phyrexian Arena, a fetchland crack, a Wretched Anurid, two other players fighting.
Four-player pods generate these constantly without you doing anything.

So treat "the loop does not self-start" as a note about the two cards **in isolation**, not as a
real liability in a pod. Once both halves are down, the game is usually over on the next life-change
event at the table, whoever causes it.

**Stensian Sanguinist // Exsanguinate is NOT a spark from hand.** It is a preparation card; the
Exsanguinate half can only be cast off the prepared creature, not from hand.

### ENGINE 2 — Aetherflux Reservoir x Side B = 2 assemblies. Confirmed in play 2026-10-26.

**Aetherflux Reservoir** ({4}, Artifact) — *"Pay 50 life: This artifact deals 50 damage to any
target."*

Pairs with **either** Side B card — Exquisite Blood **or** Bloodthirsty Conqueror. Same wording,
same result.

**This engine does not use Side A at all.** Damage dealt to a player IS life loss (CR 120.3c), and
life totals go below zero, so the loss is NOT capped at the target's remaining life. Shoot a player
at 3 life for 50 and they lose **50**, which Side B refunds in full. **Every activation after the
first pays for itself**, so one Reservoir kills the entire table in a single turn at instant speed,
for zero net life.

**THE FLOOR IS 51 LIFE, NOT 50. Corrected 2026-10-27 — an earlier version of this section said
"50+", which is wrong in the direction that loses the game.** Paying life happens during
*activation*, not resolution. The order is: pay 50 -> ability goes on the stack -> **state-based
actions are checked** -> ability resolves -> opponent loses 50 -> Side B refunds. Side B cannot pay
you back at the payment step because nothing has dealt damage yet.

- CR 119.4 — a player may pay an amount of life only if their life total is **greater than or equal
  to** the payment. So at exactly 50 you *can* pay, and you go to 0.
- CR 704.5a — a player at 0 or less life loses the game, checked before anyone gets priority.
- **At exactly 50, you pay, hit 0, and lose before the Reservoir ability ever resolves.**

At 51: pay 50 -> 1 life -> survive the check -> resolve -> opponent loses 50 -> Side B returns you
to 51. Repeat as many times as there are legal targets. Note you cannot hold two activations on the
stack from a low total — at 51 you only have the life for one, so let each resolve and take the
refund before firing again.

Observed 2026-10-26: three activations, 150 life paid, life total ended exactly where it started
(93 -> 43 -> 93 -> 43 -> 93 -> 43).

**Owner's own report, 2026-10-27: this engine fires reliably in play whenever Aetherflux Reservoir
and Exquisite Blood are both out, and he rates it highly.** The games logged in this file
under-represent it — in most of them he was racing and never near 51. Do not read the logs as a
measure of how often this engine works.

**Three ways it fizzles, each of which breaks the refund and strands you at 1 life:** damage
prevention or protection on the target, a hexproof opponent, or pointing it at a creature or
planeswalker instead of a player.

If Side A is *also* out, the first shot just starts Engine 1 and you never need the second
activation.

### ENGINE 3 — Viridian Longbow + Thornbite Staff. Not a drain loop — a board wipe.

Both Equipment on **one** creature. Longbow grants `{T}: deal 1 damage to any target` (free).
Thornbite grants *"whenever a creature dies, untap this creature."* With deathtouch, every ping
kills. Ping a creature -> it dies -> Thornbite untaps -> ping the next. **Destroys every opposing
creature in one turn, at instant speed, for zero mana.**

**Thornbite attaches FREE to a Shaman as it enters** — **Vampire Nighthawk is a Vampire Shaman**
with flying, deathtouch and lifelink — skipping the {4} equip. **Confirmed in play 2026-10-28:**
Nighthawk was cast turn 33 and Thornbite attached itself on the enters trigger.

**ENGINE 3 + double Side A is a drain engine, not just removal — found 2026-10-28.** With
**Vampire Nighthawk** carrying Thornbite and **Enduring Tenacity** plus **South Wind Avatar** on
the battlefield, each iteration is:

1. Pay {2}, tap Nighthawk, ping a creature.
2. **Deathtouch** kills it.
3. **Lifelink** gains 1 life.
4. That gain triggers **Enduring Tenacity** (target opponent loses 1) **and South Wind Avatar**
   (each opponent loses 1).
5. The creature dying **untaps Nighthawk** via Thornbite. Repeat.

Not infinite — it costs {2} per ping and needs a legal creature to kill — but it is removal and a
clock at instant speed on the same activation. Ran five times across two turns in the game below.

**With Crypt Ghast out, Thornbite is a ONE-CARD lock — found 2026-10-27.** Thornbite's own granted
ability is `{2}, {T}: deal 1 damage to any target`, and **Crypt Ghast makes every Swamp tap for
{B}{B}**, so a single Swamp pays for each ping. The Longbow is what makes the pings free; it is not
what makes the lock work. In the 2026-10-27 game below, four creatures died to Thornbite alone on
turn 21, four turns before the Longbow was cast.

This does NOT loop at a player's face: a creature must die to untap, and pinging a player kills
nothing. It is removal, not a kill. But each ping that kills gains 2 off **The Darkness Crystal**
and triggers **Blood Artist**, both of which are Engine 1 sparks.

### ENGINE 4 — Virtus the Veiled + Commander's Plate. Added 2026-10-27 after it won a game.

**Commander's Plate** {1} — *"Equipped creature gets +3/+3 and has protection from each color
that's not in your commander's color identity."* Equip commander {3}.

The commander is **mono-black**, so the Plate grants **protection from white, blue, red and green**.
Against a table with no black creatures, **Virtus is simply unblockable** — and Virtus reads
*"whenever Virtus deals combat damage to a player, that player loses half their life, rounded up."*

A 1/1 becomes a 4/4 that connects every turn and halves. The halving scales off **their** life
total, so the first swing is always the biggest: 40 -> 36 on combat damage -> **18** on the trigger.
Four or five connects kill anyone from 40, and nothing has to be drawn, tutored or assembled beyond
two cards.

**Total cost is {1} to cast plus {3} to equip the commander — the cheapest kill in the deck.**

**The +3/+3 is almost irrelevant — the protection is the whole card.** Virtus's halving does not
scale with power at all. In the 2026-10-28 game below, Virtus was a **1/1 the entire game** with
only Basilisk Collar on it, dealt exactly **1 combat damage** per connect, and still took three
opponents from 40 -> 19, 36 -> 17 and 31 -> 15. One point of damage connecting is the entire
requirement.

**THE CAVEAT — CORRECTED 2026-10-28. An earlier version of this entry said the hole was black
creatures. That was wrong and too narrow.**

Commander's Plate grants protection from each colour **not in your commander's colour identity** —
for mono-black that is white, blue, red and green. **Colourless is not a colour.** So two kinds of
blocker get through:

- **Black creatures**, as originally noted.
- **Colourless creatures** — artifact creature tokens (Thopters, Germs, Constructs, Phyrexian
  Mites), Eldrazi, manlands. In the 2026-10-28 game below, Gai had 1/1 **colourless Thopter tokens**
  on the board that could legally have blocked Virtus all game; he simply chose not to.

**CONFIRMED IN PLAY, 2026-10-28 (9th game).** Ethan blocked Plate-equipped Virtus with **Blight
Herder**, a {5} colourless Eldrazi Processor 4/5. Protection from W/U/R/G did nothing; the block
was legal and the 1/1 commander died to it. An opponent has now actually taken this block.

Colourless artifact tokens are far more common than a black deck at most tables, so treat this as a
real limitation rather than an edge case. Against either, fall back to **Dauthi Embrace**
({B}{B}: target creature gains shadow — shadow ignores colour entirely) or **Rogue's Passage**
({4}, {T}: target creature can't be blocked).

**Quietus Spike** ({3}, equip {3}) has the same halving text and grants deathtouch, so it is the
same engine on a non-commander body — but it does not grant evasion, which is the half that
matters. Plate on Virtus is strictly the better version when the table is not black.

### Engines 1 and 2 overlap on purpose

Exquisite Blood is now in **both** engines; Bloodthirsty Conqueror is in both as well. That is 10
assemblies off 7 cards, plus Engine 4's one off two more. **Sanguine Bond stays in the MAYBEBOARD** — not because it is redundant
(redundancy is the point), but because adding a ninth Side A x Side B assembly pushes the bracket
assessment from 3 to 4.

### Not infinite, but these are the value engines that win the long games

- **Grave Pact + Tergrid** — your creature dies, each opponent sacrifices, Tergrid puts every
  nontoken one they sacrifice onto **your** battlefield. One blocked one-drop can net three
  creatures.
- **Grave Pact + Ayara** — `{T}, sacrifice another black creature: draw a card` is a free
  repeatable sac outlet. Tap, sac, draw, whole table sacrifices. Every turn.
- **Grave Pact + Skullclamp** — {1} to kill a 1-toughness body, draw two, force three sacrifices.
- **Skullclamp + Arnyn** — the clamped creature has toughness 1 or less when it dies, so Arnyn
  drains 2 and gains 2 on top of the two cards. The gain is an Engine 1 spark.
- **Skullclamp + Avacyn, Angel of Horror** — Avacyn returns the clamped nontoken creature at the
  next end step, so the same body can be clamped again.
- **Sheoldred + any draw** — *"whenever you draw a card, you gain 2 life."* With Side A out, every
  single card you draw drains the table. The deck has 9 draw sources.
- **Tergrid + Torment of Hailfire** — Hailfire is sacrifice-or-discard-or-lose-3; Tergrid takes
  everything they give up.
- **Erebos, God of the Dead** — *"your opponents can't gain life."* Does not combo, but it locks
  lifegain decks out of racing the loop and makes the Reservoir math certain.
- **Witch of the Moors** — at your end step, if you gained life this turn, each opponent sacrifices
  a creature and you return a creature from the graveyard to hand. Any Engine 1 spark turns it on.

Exsanguinate and Gray Merchant are fine on their own as big drain, and both start the loop.

## Why the deck needs tutors

Only THREE cards in all of mono-black care about having deathtouch creatures: Hooded Blightfang,
Black Widow, and White Widow. That is the entire payoff pool. Hooded Blightfang in particular is
the deck's clock -- it triggers on ATTACK, not on damage, so blockers do not stop it. With a wide
board, every attack drains each opponent for the number of deathtouch attackers.

Five tutors (Demonic, Vampiric, Grim, Diabolic Intent, Sidisi) exist to find it. This is not a
power choice, it is load-bearing.

## Mana

Cabal Coffers + Urborg is the engine -- Urborg makes every land a Swamp, so Coffers taps for the
whole land count. Crypt Ghast and Nirkana Revenant double Swamps; Crypt Ghast's extort also gains
life, which feeds Vito. Deserted Temple untaps Coffers. Nykthos is live because the list is
wall-to-wall {B} and {B}{B} permanents -- the same devotion Gray Merchant reads.

Exsanguinate and Torment of Hailfire are the sinks that convert that mana into a win.

NOTE: Cabal Stronghold counts BASIC Swamps only, so Urborg does nothing for it. It is the weaker
Coffers and is in the list as redundancy, not as an equal.

## Game Changers — rechecked 2026-10-22

**3 Game Changers: Demonic Tutor, Vampiric Tutor, and TERGRID, GOD OF FRIGHT.**
**The deck is now exactly at the Bracket 3 cap. There is no free slot. Do not add a fourth.**

**Parser warning for future checks.** Tergrid's entry in `game_changers.md` reads
``- Tergrid, God of Fright — in the database as `Tergrid, God of Fright // Tergrid's Lantern` ``.
A naive parser that takes everything after `- ` as the card name **will miss it**, and a naive
parser will also miss nothing else — Tergrid is the only list entry with an explanatory suffix.
Split the line on the em dash before matching, and match the deck entry on both the full
`A // B` name and the front face. All eight other decks were re-counted with the corrected parser
on 2026-10-22 and none of their counts changed.

Sol Ring is NOT a Game Changer -- game_changers.md says so explicitly. An earlier draft of this
file wrongly listed it after a sloppy substring match hit that very sentence. Archidekt's bracket
checker independently returns the same two names.

## Bracket: 3 (Upgraded)

Assessed 2026-09-28 against the rules in game_changers.md. Archidekt estimates 4; this deck is
recorded as 3, deliberately.

- **Game Changers: 2 of 3 allowed.** Under the cap.
- **No mass land denial, no chained extra turns.**
- **The combo is not "cheap and early."** Cheapest assembly is EIGHT mana across two cards --
  Vito {2}{B} plus Exquisite Blood {4}{B} -- and it needs a third life-change event to start.
  Realistic assembly is turn 6-8, which is inside the "late game, around turn 6+, is fine" window
  the bracket rules allow.

Archidekt guesses 4 because it counts combo PIECES without weighing their cost. The honest
counter-argument for 4 is the five tutors, which make assembly far more consistent than a deck
hoping to topdeck it.

**Move this to Bracket 4 if** Sanguine Bond comes in from the maybeboard, or if in practice the
tutors assemble the kill by turn 5-6 consistently. Either way, say it out loud at the table: a
turn-7 combo nobody was warned about is the actual problem, not the label.

## Rejected during design — do not re-propose

- **Cecil, Dark Knight** — ILLEGAL here. Its back face (Cecil, Redeemed Paladin) is white, so its
  colour identity is B/W.
- **Damocles Base, Sword of Kang** — 5/5 flying deathtouch, but **Crew 3** in a deck of 1/1s and
  2/2s means tapping two or three creatures to attack with one. Those are the same bodies Hooded
  Blightfang wants attacking.
- **Whispersilk Cloak** — grants SHROUD, so you cannot target the creature with Kaya's Ghostform,
  Commander's Plate or Basilisk Collar. It fights the rest of the equipment.
- **Death Cloud** — symmetrical; each player sacrifices X creatures and X lands. This deck is the
  one with the wide board and the Coffers.
- **Thieving Varmint** — reads as a {1}{B} deathtouch lifelink body that taps for two mana, but
  the mana is "only to cast spells you don't own." Useless as ramp.
- **Mari, the Killing Quill / tribal builds** — rejected because the owner did not want to be
  locked into Assassins, Mercenaries and Rogues.
- **Epicure of Blood, Tetzimoc Primal Death** — cut for curve reasons, see git history.

## Swap 2026-10-22 (9 cards) — owner approved

The biggest change to the deck so far, aimed at two problems the owner named from play: **not
enough card draw**, and **sitting on Cabal Coffers mana with nothing to spend it on.**

| In | Out | Why |
|---|---|---|
| **Tergrid, God of Fright // Tergrid's Lantern** {3}{B}{B} 4/5 menace — **GAME CHANGER** | Archetype of Finality {4}{B}{B} | "Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may put that card from a graveyard onto the battlefield under your control." **Both enablers are already in the deck: Torment of Hailfire** (each opponent loses 3 *unless they sacrifice a nonland permanent or discard*) hands you everything they give up, and **Witch of the Moors** makes each opponent sacrifice a creature at your end step whenever you gained life. The back face, **Tergrid's Lantern**, is a repeatable mana sink — {T} to force sac-or-discard-or-lose-3, {3}{B} to untap — and that 3 life loss is itself a combo spark. Archetype was 6 mana to grant deathtouch where 22 creatures already have it printed. |
| **Erebos, God of the Dead** {3}{B} | Black Market {3}{B}{B} | {1}{B}, pay 2 life: draw. **Sheoldred refunds the 2**, so it is a free repeatable draw engine and a mana sink. Indestructible, and **"your opponents can't gain life"** shuts off the lifegain decks that can outrun the drain plan. Black Market's mana exists **only in your precombat main phase** and it enters with zero counters — the least flexible mana in the deck, in a deck already flooding. |
| **South Wind Avatar** {3}{B} 3/4 | Gonti, Lord of Luxury {2}{B}{B} | Deathtouch, "whenever another creature you control dies, you gain life equal to its toughness", "whenever you gain life, each opponent loses 1 life." A combo half, a deathtouch body, and **its own spark** on one card. Gonti's steal is one card once on ETB; Tinybones does it repeatedly and costs {B}, so Tinybones was kept instead (owner's call — he has used both). |
| **Aetherflux Reservoir** {4} | Ravening Warg {1}{B} | Lifegain **on every spell cast**, scaling within a turn — the combo's one documented weakness is that it does not self-start, and this sparks it every turn forever. The pay-50 mode is a real one-card kill at this deck's life totals, but the top line is the reason it is here. |
| **Enduring Tenacity** {2}{B}{B} 4/3 | Thrill-Kill Assassin {1}{B} | Vito's exact text on a body, **one mana cheaper than Sanguine Bond**, and when it dies it **returns as an enchantment** — wipe-resistant. Thrill-Kill's Unleash counter stops it blocking, and this deck blocks, so its only printed ability was one the owner would decline every game. |
| **Ayara, First of Locthwain** {B}{B}{B} 2/3 | Arcane Signet {2} | Spark on **every black creature you cast** (all of them are black), **plus** "{T}, sacrifice another black creature: draw a card" — a spark and a draw outlet in one, and three black pips for devotion. Arcane Signet was a 2-mana rock behind 36 lands and eight mana engines. |
| **Blood Artist** {1}{B} 0/1 | Hired Poisoner {B} | "Whenever this creature **or another creature** dies, target player loses 1 life and you gain 1 life." Any creature anywhere, including everything the deathtouchers kill and creatures that die between two opponents — and it is a **double-ended spark**, hitting both halves of the grid. Hired Poisoner was the only creature in the deck with no text at all beyond deathtouch; the other three one-drops all have upside. (**Thornbite Staff was cut here first and put straight back — see the correction below.**) |
| **Stensian Sanguinist // Exsanguinate** {1}{B} 2/2 | Burrog Banemaker {B} | On attack it grants **deathtouch to a target creature**, which is most of what Archetype did, for 2 mana instead of 6. Burrog's {1}{B} pump is near-worthless on a deathtoucher, which only ever needs 1 damage. |
| **Skullclamp** {1} | Case of the Gorgon's Kiss {B} | Equip {1}, +1/-1, draw two when the creature dies. **Six 1-toughness bodies** die to it instantly, and each death triggers **Arnyn** (drain 2 / gain 2 = a spark) while **Avacyn returns nontoken creatures to the battlefield**. Gorgon's Kiss is weaker than it reads — see the ruling note below. |

**Result after the correction below: 100 cards · 36 lands · 32 creatures · 21 printed
deathtouch · avg MV 2.78 · 3 of 3 Game Changers.** (The 2026-10-26 Grave Pact swap later moved this
to 35 lands; everything else is unchanged.)
Draw sources went from 6 to 9, and three of the new ones are repeatable rather than one-shot.

### CORRECTION, same day — Thornbite Staff put back, Hired Poisoner cut instead

Thornbite Staff was cut in the swap above on the argument that the Longbow lock "needed three cards
and about ten mana to do what the deathtouch blockers already do." **That was wrong on both counts
and the cut was reversed within the hour.**

**The lock, stated properly.** Put **Viridian Longbow** and **Thornbite Staff** on one deathtouch
creature. Tap via **Longbow's** ability (free — Thornbite's own ping costs {2}, so never use it):
1 damage, deathtouch makes it lethal, the creature dies, and Thornbite's *"whenever a creature dies,
untap this creature"* untaps you. Repeat. **You destroy every creature your opponents control in one
turn, at instant speed, for zero mana.** It is bounded by creatures dying, so it is unlimited kills,
not infinite face damage.

**Why it is cheap, which the cut argument missed:** Thornbite reads *"Whenever a Shaman creature
enters, you may attach this Equipment to it."* **Vampire Nighthawk is a Vampire Shaman** with flying,
deathtouch **and lifelink** already in the deck — so with Thornbite on the battlefield first, it
attaches **free**, skipping the {4} equip. Each ping then also gains 1 life, which is a combo spark,
so Nighthawk plus both Equipment plus an assembled grid wins on the spot.

**Caveats:** the ability costs {T}, so the creature cannot be summoning-sick — **Swiftfoot Boots'
haste fixes that**. Equipping is sorcery speed; the activations are not. Thornbite must be down
*before* the Shaman enters for the free attach. Basilisk Collar substitutes for native deathtouch.

**Do not propose cutting Thornbite Staff or Viridian Longbow again.** The owner had never tried this
line; it is now a documented part of the deck.

### Cards the owner protected in this pass — DO NOT re-suggest as cuts
- **Dauthi Embrace** — his only confirmed connect against a **black** deck, where Commander's Plate's protection does nothing.
- **Quietus Spike + Rancid Rats** — Spike grants deathtouch but **no power boost**, so the Rats stays 1/1 and **skulk** keeps working. A near-unblockable "half their life, rounded up" on a one-drop; effectively a second Virtus.
- **Dire Fleet Poisoner** — its Pirate ETB is dead text (only Pirate in the deck), but **flash** on a deathtoucher is unconditional value: ambush blocker, and it dodges sorcery-speed wipes from hand. Better than Ravening Warg, which was cut instead.
- **Swiftfoot Boots** — **haste is the one thing Commander's Plate cannot grant.** Cast Virtus, equip for {1}, attack the same turn instead of giving the table a full turn cycle to answer him. No game log shows it unused; the two logs on file simply never drew it.
- **Bubbling Muck, Nirkana Revenant, Cabal Ritual, Culling the Weak, Dark Ritual** — the owner wants the mana flood. Do not cut mana.
- **Village Rites** — cutting it would cost a draw source.
- **Kaya's Ghostform** — recursion, and the only protection for Liliana.
- **Exsanguinate and Torment of Hailfire** — both have won games. Never propose cutting them.
- **Blightwing Bandit** — offered by the owner and declined by him; 1 of only 6 fliers and a deathtoucher.
- **Tinybones** — kept over Gonti. Repeatable steal on a one-drop, and Skullclamp fodder.
- **Viridian Longbow and Thornbite Staff** — both kept. They are the board-wipe lock; see the correction above.
- The three removal spells (Go for the Throat, Snuff Out, Feed the Swarm).

### Grave Pact — ADDED 2026-10-26. Cut: Bojuka Bog.

**Grave Pact** — {1}{B}{B}{B} — Enchantment — *"Whenever a creature you control dies, each other
player sacrifices a creature of their choice."* **Not a Game Changer**, so the 3-of-3 count is
unchanged.

Approved in principle 2026-10-22, cut found and swap approved 2026-10-26.

**Why it is the highest-value slot in the deck — it is not the Pact alone, it is what it plugs into:**
- **+ Tergrid** — every opponent sacrifice is a nontoken permanent Tergrid puts onto **your**
  battlefield. One blocked one-drop can net three creatures.
- **+ Ayara** — `{T}, Sacrifice another black creature: Draw a card` is a free, repeatable sac
  outlet. Tap, sac, draw, and the whole table sacrifices. Every turn.
- **+ Skullclamp** — {1} to kill a 1-toughness body, draw two, and force three sacrifices.
- **+ Blood Artist** — every death is also a drain, which is a combo spark.

It also matches how the owner actually plays the deck: *"a lot of the time I just leave the
creatures up and don't do much damage, only for blocks."* With 21 printed deathtouchers, every one
of those blocks becomes a four-for-one.

**Grave Pact does not need recursion to work.** It is not a sacrifice engine you have to feed — it
is a tax on trading. The deathtouchers were already dying in combat; the Pact just makes each of
those deaths cost the table a creature apiece. Raised by the owner 2026-10-26 and checked: the deck
also has more recursion than it looks. **Avacyn, Angel of Horror** is a blanket — *"Whenever Avacyn
or another nontoken creature you control dies, return that card to the battlefield under your
control at the beginning of the next end step"* — so with her out, your side of a Grave Pact trade
is free. Behind her: **Witch of the Moors** (which already forces each opponent to sacrifice *and*
returns a creature to hand), **Qarsi Revenant** renew, **Kaya's Ghostform**, **Tergrid**.

**The cut — Bojuka Bog.** Audited all eight nonbasic lands. The Bog was the only one without a job:
- **Not Swamp-typed** (`Land`, no subtype), so **Cabal Coffers, Cabal Stronghold and Extraplanar
  Lens cannot see it** — unless Urborg is already out, which makes every land a Swamp anyway.
- **Enters tapped.**
- Its only payoff is a one-shot ETB exiling one player's graveyard.
- Every other nonbasic has a job: Coffers (engine), Stronghold (second Coffers), Urborg (makes all
  lands Swamps), Deserted Temple (untaps Coffers), Nykthos (devotion), Rogue's Passage (the one
  piece of evasion that beats other black decks).

Land count 36 → 35. Swamp-typed count is **unchanged at 29**, so the Coffers/Stronghold/Lens engine
is untouched. Simulation delta is negligible: 36 lands gave 5.76 lands in play by turn 10, 35 gives
5.58.

**Known cost of the cut, flagged to the owner and accepted:** Bojuka Bog was the deck's **only
graveyard hate**. A Meren / Muldrotha / Karador deck at the table now recurs unchecked. Revisit if
graveyard decks become common in the owner's pod.

Alternatives considered for the slot, all checked and none a Game Changer:
- **Dictate of Erebos** {3}{B}{B} — identical text with **flash**, one mana more.
- **Butcher of Malakir** {5}{B}{B} — same effect on a 5/5 flier, 7 mana.
- **Fleshbag Marauder** / **Plaguecrafter** {2}{B} — one-shot, each player sacrifices on ETB.

### Two other gaps found in the 2026-10-22 audit

**Artifact removal: ZERO — and the owner has ruled this is fine, 2026-10-22.** Nothing in the 100
destroys an artifact; Feed the Swarm covers enchantments only. Recorded as a known, accepted gap:
the deck wins fast enough that answering artifacts is not worth a slot. **Do not re-propose it.**
(If it ever does come up, Unstable Obelisk {3} is the best mono-black option — a mana rock first,
{7} to destroy any permanent.)

**Board wipe — CORRECTED 2026-10-22: the deck HAS one. It is Torment of Hailfire.** An earlier note
here said the deck ran no wipe; the owner pointed out that is wrong. For a large X, Torment forces
each opponent to sacrifice a nonland permanent or discard on every iteration — it **strips boards and
hands while never touching this deck's own 32 creatures.** It is a one-sided wipe, and **with Tergrid
out every permanent they sacrifice comes to you.** Do not propose adding a board wipe; a symmetrical
one would be strictly worse here. **Artifact removal is also a non-issue per the owner — the deck
bursts quickly enough that it does not need to answer artifacts.**

### Speed analysis of the 2026-10-22 swap — measured, not guessed

**Slower to start, roughly 2.4x faster to assemble the kill.**

- **Plays at MV 2 or less: 33 -> 30**, and Arcane Signet is gone, so there is no turn-two rock.
  Turns 1-3 are emptier and there are fewer early Hooded Blightfang triggers.
- **Life-change spark sources: 27 -> 32.** New ones: Blood Artist, Ayara, Aetherflux Reservoir,
  Enduring Tenacity, South Wind Avatar, Stensian, Tergrid's Lantern. Lost: Case of the Gorgon's
  Kiss, Ravening Warg.
- **Combo grid 2x2 -> 2x4** and **draw 6 -> 9 sources**, three of them repeatable.

Probability of holding **both** halves, hypergeometric over 99 with this deck's draw rate:

| turn | before | after |
|---|---|---|
| 5 | 5.2% | 10.7% |
| 8 | 7.9% | 18.5% |
| 10 | 9.9% | 23.7% |
| 12 | 12.2% | 29.0% |
| 15 | 15.7% | 38.0% |

**THE BOTTLENECK IS SIDE B.** Exquisite Blood and Bloodthirsty Conqueror are the **only two cards in
mono-black** with "whenever an opponent loses life, you gain that much life" — the whole database was
searched. Side A is now four cards and finds itself; Side B is still two. **Tutor for Side B.**
Demonic Tutor, Vampiric Tutor, Grim Tutor, Diabolic Intent and Sidisi should all go get Exquisite
Blood or Bloodthirsty Conqueror unless something is actively lethal. By 21 cards seen you are only
38% to have found one on your own.

Both logged wins were turn 25-26. Expect this build to land closer to **turn 18-22**, with a
slightly higher chance of a clunky turn 3.

### Benched, still live candidates
**Starscape Cleric** {1}{B} — Blight-Priest's text one mana cheaper on a flier with Offspring, but
**"this creature can't block"** fights a deck whose cheap creatures exist to block. Benched.
Also still open: **Profane Command**, **Grim Haruspex**, **Black Market Connections**,
**Dark Prophecy**, **Twilight Prophet**, **Thrull Parasite**, **Vraan**, **Zulaport Cutthroat**,
**Bontu's Monument**.

### Rejected with reasons
- **Sanguine Bond** — identical text to Vito at two more mana with no body; **Enduring Tenacity is the same effect one mana cheaper on a 4/3 that comes back from wipes.**
- **Necropotence** (Game Changer) — it exiles and puts into hand rather than drawing, so **Sheoldred never triggers**; cards arrive at your *next* end step so you cannot dig mid-turn; and with no hand-size fixer the cleanup discards get exiled.
- **Ancient Tomb** (Game Changer) — **not Swamp-typed**, so Cabal Coffers, Cabal Stronghold and Extraplanar Lens cannot see it. Same flaw that made Bojuka Bog the weakest land, and the reason it was the cut for Grave Pact on 2026-10-26. **Mana Vault** (Game Changer) is the same problem as an artifact. **Imperial Seal** (Game Changer) is a sixth tutor that is sorcery-speed and puts the card on top of the library, costing a draw.
- **Death Cloud** — symmetrical; it would wreck this deck's own board and 36 lands.
- **Skullclamp objection, resolved.** The owner's first reaction was that clamping kills his own creatures. True, but deaths are not pure loss here: Arnyn drains on them, **Avacyn returns nontoken creatures to the battlefield**, and Witch of the Moors returns one to hand.

## Swap 2026-10-19 — Liliana back in, owner approved

| In | Out | Why |
|---|---|---|
| Liliana of the Dark Realms {2}{B} | Cover of Darkness {1}{B} | Owner wanted Blightwing Bandit AND Liliana both in the 100. Blightwing's cut was already paid (it took Liliana's slot in commit 72a8959), so re-adding Liliana cost exactly one more card. Cover of Darkness grants **fear**, which black creatures block — the weakest of the deck's four evasion effects, next to Commander's Plate (protection from W/U/R/G, unblockable at most tables), Rogue's Passage (unconditional) and Dauthi Embrace (shadow). It also cannot cover Virtus and the Vampires at once: Virtus is an **Azra Assassin**, so naming Vampire leaves the commander out and naming Assassin covers 5 creatures instead of 10. And it feeds none of the connect-dependent payoffs it would need to justify a slot — no White Widow counter, no Black Widow draw, no lifelink connection for Vito or Marauding Blight-Priest. |

**Process note, recorded deliberately.** Commit `72a8959` (Liliana out, Blightwing in; Charcoal
Diamond out, Extraplanar Lens in) was **pushed without approval** — "Y lil" was read as "yes,
Liliana" when it meant "why Liliana". The swaps survived on their merits after the owner reviewed
them, but the push itself was a mistake. Confirm before editing.

### Correction to the reasoning above, 2026-10-19
An earlier version of this entry claimed Cover of Darkness "triggers none of the deathtouch payoffs —
**no Hooded Blightfang drain**." That was wrong. Blightfang reads *"Whenever a creature you control
with deathtouch **attacks**, each opponent loses 1 life and you gain 1 life"* — it fires on the
declaration of attackers, not on connecting, so **evasion is irrelevant to it** and it was never an
argument for or against Cover of Darkness. The White Widow, Black Widow, Quietus Spike, Tinybones and
lifelink-into-Vito lines do all require combat damage to a player, so those parts stand.

**Re-examined on the numbers and the cut still holds, but narrowly.** The deck has 10 Vampires, and
**4 of them already fly** (Bloodthirsty Conqueror, Nighthawk Scavenger, Qarsi Revenant, Vampire
Nighthawk). Naming Vampire therefore only added evasion to 6 ground bodies, of which only 2 have
lifelink (Gifted Aetherborn, Vampire of the Dire Moon) — the part that converts a connection into a
drain. Naming Assassin covers 5 and does include Virtus, but Commander's Plate already makes him
unblockable against any non-black deck while giving +3/+3, and Rogue's Passage is unconditional.

**The one condition that would reverse this:** against a pod light on black, fear is live and Cover
of Darkness is a 2-mana permanent that switches on a whole tribe every combat for free, where Dauthi
Embrace charges {B}{B} per creature per turn. If the owner's regular table is mostly non-black, put
it back. The honest alternative cut in that case is **Hired Poisoner** ({B} 1/1 deathtouch, no text),
the lowest-impact card in the 100 — kept because 26 of 31 creatures have deathtouch and the cheap
bodies are the engine's fuel, so cutting the cheapest one costs real consistency.

**Alternate cut considered and not taken:** Ravening Warg — its Ferocious lifegain needs a power-4
creature and the deck has only about six.

## Rules notes added 2026-10-22

- **Stensian Sanguinist is a PREPARATION card, not a split card.** Ruling: *"Preparation cards can
  only be cast with their base characteristics."* **You cannot cast Exsanguinate from hand off it.**
  From hand it is only a {1}{B} 2/2. The Exsanguinate half is reached by: cast the creature, attack,
  its trigger grants a creature deathtouch, **that creature must deal combat damage to a player**,
  then Stensian becomes prepared and a copy of Exsanguinate is created in exile, which you may cast
  for its full {X}{B}{B}. It is a repeatable Exsanguinate *engine*, **not a second copy in hand** —
  which is exactly why plain Exsanguinate stays in the deck.
- **Stensian's deathtouch grant comes too late for Hooded Blightfang.** Both trigger on declaring
  attackers; Blightfang checks for deathtouch at that moment, and Stensian's grant resolves after.
  Point the grant at a creature that does **not** already have deathtouch and that you expect to
  connect.
- **Case of the Gorgon's Kiss does NOT auto-solve at end of turn** — the reminder text misleads.
  Ruling: *"To Solve — [condition]" means "At the beginning of your end step, **if [condition]** and
  this Case is not solved, it becomes solved."* and *"If the condition isn't true at the beginning of
  your end step, the ability won't trigger at all."* It needed **three creature cards** into
  graveyards in one turn, and **tokens don't count**. Its ETB also only kills a creature *already
  dealt damage this turn*, which your deathtouchers have already finished off. This is why it was cut.
- **Tergrid + Torment of Hailfire is the deck's new haymaker.** Torment forces each opponent to lose
  3 **unless they sacrifice a nonland permanent or discard a card** — with Tergrid out, every one of
  those sacrifices and every discarded permanent card comes to you. X=5 into three opponents can hand
  you a dozen permanents.
- **Attack more.** The owner reported holding creatures back as blockers. **Hooded Blightfang
  triggers on ATTACK, not on connecting** — declaring three deathtouchers drains each opponent for 3
  and gains 3 before blockers are declared, and that lifegain is a combo spark. Blocking a deathtoucher
  is a bad trade for the opponent, so cheap attackers usually get through or trade up.

## Open items

- **Acquisitions logged 2026-10-21: Commander's Plate, Avacyn Angel of Horror, Blightwing Bandit.**
  Blightwing was already in the 100 (commit `72a8959`); Avacyn and Commander's Plate were already in
  the list as well, so these three close real gaps rather than changing the decklist.
- **Full build state unknown.** The old "nothing acquired / shopping list" line was stale — the deck
  has been played and at least these cards plus the snow-covered Swamps are in hand. A full
  owned-versus-needed pass has never been done for this deck; it is the obvious next thing to ask
  the owner for, the way it was done for Kodama and White Angel.
- Sanguine Bond maybeboard decision.
- Playtested, not formally tested. **Sixteen logged four-player wins and two logged losses** (2026-10-21,
  four on 2026-10-26, four on 2026-10-27, seven wins and both losses on 2026-10-28) — but see the caveat
  heading the logged-games section: these are pasted games, not the full record. Fastest win is own
  turn 4; slowest is own turn 13. **Both losses are written up in full below — read them before assuming
  the deck has no weaknesses.**


## Creature (32)

**Archetype of Finality** — {4}{B}{B} — Enchantment Creature — Gorgon — **2/3**
"Creatures you control have deathtouch. | Creatures your opponents control lose deathtouch and can't have or gain deathtouch."

**Avacyn, Angel of Horror** — {5}{B}{B}{B} — Legendary Creature — Angel — **8/8**
"Flying, deathtouch | Whenever Avacyn or another nontoken creature you control dies, return that card to the battlefield under your control at the beginning of the next end step."

**Black Widow, Deadly Hunter** — {2}{B} — Legendary Creature — Human Assassin Hero — **3/3**
"Deathtouch | Whenever a creature you control with deathtouch deals combat damage to a player, you draw a card and lose 1 life."

**Blightwing Bandit** — {3}{B} — Creature — Faerie Rogue — **2/2**
"Flying, deathtouch | Whenever you cast your first spell during each opponent's turn, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled, and mana of any type can be spent to cast it."
Back in after being cut on 09-30. The cut reasoning was that the rider rarely fires; in the 10-14
game it fired off Snuff Out, stole Will of the Sultai, and that card won the game. It is also a
SIXTH flying deathtoucher, which is the deck's scarcest blocker type.

**Bloodthirsty Conqueror** — {3}{B}{B} — Creature — Vampire Knight — **5/5**
"Flying, deathtouch | Whenever an opponent loses life, you gain that much life. (Damage causes loss of life.)"

**Crypt Ghast** — {3}{B} — Creature — Spirit — **2/2**
"Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.) | Whenever you tap a Swamp for mana, add an additional {B}."

**Dire Fleet Poisoner** — {1}{B} — Creature — Human Pirate — **2/2**
"Flash | Deathtouch | When this creature enters, target attacking Pirate you control gets +1/+1 and gains deathtouch until end of turn."

**Dire Fleet Ravager** — {3}{B}{B} — Creature — Orc Pirate Wizard — **4/4**
"Menace, deathtouch | When this creature enters, each player loses a third of their life, rounded up."

**Foulmire Knight // Profane Insight** — {B} // {2}{B} — Creature — Zombie Knight // Instant — Adventure — **1/1**
"Foulmire Knight -- {B} | Creature — Zombie Knight | Deathtouch | // | Profane Insight -- {2}{B} | Instant — Adventure | You draw a card and you lose 1 life. (Then exile this card. You may cast the creature later from exile.)"

**Gifted Aetherborn** — {B}{B} — Creature — Aetherborn Vampire — **2/3**
"Deathtouch, lifelink"

**Gonti, Lord of Luxury** — {2}{B}{B} — Legendary Creature — Aetherborn Rogue — **2/3**
"Deathtouch | When Gonti enters, look at the top four cards of target opponent's library, exile one of them face down, then put the rest on the bottom of that library in a random order. You may cast that card for as long as it remains exiled, and mana of any type can be spent to cast that spell."

**Gray Merchant of Asphodel** — {3}{B}{B} — Creature — Zombie — **2/4**
"When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost this way. (Each {B} in the mana costs of permanents you control counts toward your devotion to black.)"

**Hired Poisoner** — {B} — Creature — Human Assassin — **1/1**
"Deathtouch"

**Hooded Blightfang** — {2}{B} — Creature — Snake — **1/4**
"Deathtouch | Whenever a creature you control with deathtouch attacks, each opponent loses 1 life and you gain 1 life. | Whenever a creature you control with deathtouch deals damage to a planeswalker, destroy that planeswalker."

**Marauding Blight-Priest** — {2}{B} — Creature — Vampire Cleric — **3/2**
"Whenever you gain life, each opponent loses 1 life."

**Nighthawk Scavenger** — {1}{B}{B} — Creature — Vampire Rogue — **1+*/3**
"Flying, deathtouch, lifelink | Nighthawk Scavenger's power is equal to 1 plus the number of card types among cards in your opponents' graveyards."

**Nirkana Revenant** — {4}{B}{B} — Creature — Vampire Shade — **4/4**
"Whenever you tap a Swamp for mana, add an additional {B}. | {B}: This creature gets +1/+1 until end of turn."

**Pharika's Chosen** — {B} — Creature — Snake — **1/1**
"Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)"

**Qarsi Revenant** — {1}{B}{B} — Creature — Vampire — **3/3**
"Flying, deathtouch, lifelink | Renew — {2}{B}, Exile this card from your graveyard: Put a flying counter, a deathtouch counter, and a lifelink counter on target creature. Activate only as a sorcery."

**Rancid Rats** — {1}{B} — Creature — Zombie Rat — **1/1**
"Skulk (This creature can't be blocked by creatures with greater power.) | Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)"

**Sheoldred, the Apocalypse** — {2}{B}{B} — Legendary Creature — Phyrexian Praetor — **4/5**
"Deathtouch | Whenever you draw a card, you gain 2 life. | Whenever an opponent draws a card, they lose 2 life."

**Sidisi, Undead Vizier** — {3}{B}{B} — Legendary Creature — Zombie Snake — **4/6**
"Deathtouch | Exploit (When this creature enters, you may sacrifice a creature.) | When Sidisi exploits a creature, you may search your library for a card, put it into your hand, then shuffle."

**Thrill-Kill Assassin** — {1}{B} — Creature — Human Assassin — **1/2**
"Deathtouch | Unleash (You may have this creature enter with a +1/+1 counter on it. It can't block as long as it has a +1/+1 counter on it.)"

**Tinybones, the Pickpocket** — {B} — Legendary Creature — Skeleton Rogue — **1/1**
"Deathtouch | Whenever Tinybones deals combat damage to a player, you may cast target nonland permanent card from that player's graveyard, and mana of any type can be spent to cast that spell."

**Typhoid Rats** — {B} — Creature — Rat — **1/1**
"Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)"

**Vampire Nighthawk** — {1}{B}{B} — Creature — Vampire Shaman — **2/3**
"Flying | Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.) | Lifelink (Damage dealt by this creature also causes you to gain that much life.)"

**Vampire of the Dire Moon** — {B} — Creature — Vampire — **1/1**
"Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.) | Lifelink (Damage dealt by this creature also causes you to gain that much life.)"

**Virtus the Veiled** — {2}{B} — Legendary Creature — Azra Assassin — **1/1**
"Partner with Gorm the Great (When this creature enters, target player may put Gorm into their hand from their library, then shuffle.) | Deathtouch | Whenever Virtus deals combat damage to a player, that player loses half their life, rounded up."

**Vito, Thorn of the Dusk Rose** — {2}{B} — Legendary Creature — Vampire Cleric — **1/3**
"Whenever you gain life, target opponent loses that much life. | {3}{B}{B}: Creatures you control gain lifelink until end of turn."

**White Widow, Yelena Belova** — {1}{B} — Legendary Creature — Human Assassin Villain — **1/2**
"Deathtouch | Whenever a creature you control with deathtouch deals combat damage to a player, put a +1/+1 counter on it."


## Artifact (11)

**Arcane Signet** — {2} — Artifact
"{T}: Add one mana of any color in your commander's color identity."

**Basilisk Collar** — {1} — Artifact — Equipment
"Equipped creature has deathtouch and lifelink. (Any amount of damage it deals to a creature is enough to destroy it. Damage dealt by this creature also causes you to gain that much life.) | Equip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)"

**Extraplanar Lens** — {3} — Artifact
"Imprint — When this artifact enters, you may exile target land you control. | Whenever a land with the same name as the exiled card is tapped for mana, its controller adds one mana of any type that land produced."
Imprint a SNOW-COVERED SWAMP. The 29 basics are snow specifically so this is one-sided -- imprint a
plain Swamp and every opponent on Swamps gets doubled mana too. Cost: the imprinted land is exiled
permanently and does not come back if the Lens is destroyed.

**Commander's Plate** — {1} — Artifact — Equipment
"Equipped creature gets +3/+3 and has protection from each color that's not in your commander's color identity. | Equip commander {3} | Equip {5}"

**Quietus Spike** — {3} — Artifact — Equipment
"Equipped creature has deathtouch. | Whenever equipped creature deals combat damage to a player, that player loses half their life, rounded up. | Equip {3}"

**Sol Ring** — {1} — Artifact
"{T}: Add {C}{C}."

**Swiftfoot Boots** — {2} — Artifact — Equipment
"Equipped creature has hexproof and haste. (It can't be the target of spells or abilities your opponents control. It can attack and {T} no matter when it came under your control.) | Equip {1} ({1}: Attach to target creature you control. Equip only as a sorcery.)"

**The Darkness Crystal** — {2}{B}{B} — Legendary Artifact
"Black spells you cast cost {1} less to cast. | If a nontoken creature an opponent controls would die, instead exile it and you gain 2 life. | {4}{B}{B}, {T}: Put target creature card exiled with The Darkness Crystal onto the battlefield tapped under your control with two additional +1/+1 counters on it."

**Thornbite Staff** — {2} — Kindred Artifact — Shaman Equipment
"Equipped creature has "{2}, {T}: This creature deals 1 damage to any target" and "Whenever a creature dies, untap this creature." | Whenever a Shaman creature enters, you may attach this Equipment to it. | Equip {4}"

**Viridian Longbow** — {1} — Artifact — Equipment
"Equipped creature has "{T}: This creature deals 1 damage to any target." | Equip {3} ({3}: Attach to target creature you control. Equip only as a sorcery.)"


## Enchantment (5)

**Dauthi Embrace** — {2}{B} — Enchantment
"{B}{B}: Target creature gains shadow until end of turn. (It can block or be blocked by only creatures with shadow.)"

**Exquisite Blood** — {4}{B} — Enchantment
"Whenever an opponent loses life, you gain that much life."

**Grave Pact** — {1}{B}{B}{B} — Enchantment
"Whenever a creature you control dies, each other player sacrifices a creature of their choice."

**Kaya's Ghostform** — {B} — Enchantment — Aura
"Enchant creature or planeswalker you control | When enchanted permanent dies or is put into exile, return that card to the battlefield under your control."

**Phyrexian Arena** — {1}{B}{B} — Enchantment
"At the beginning of your upkeep, you draw a card and you lose 1 life."


## Planeswalker (1)

**Liliana of the Dark Realms** — {2}{B} — Legendary Planeswalker — Liliana — **starting loyalty 3**
"+1: Search your library for a Swamp card, reveal it, put it into your hand, then shuffle. | −3: Target creature gets +X/+X or -X/-X until end of turn, where X is the number of Swamps you control. | −6: You get an emblem with 'Swamps you control have {T}: Add {B}{B}{B}{B}.'"
Back in 2026-10-19. **The +1 is not generic ramp here — it is a Swamp**, and Cabal Coffers, Cabal
Stronghold, Nirkana Revenant and Crypt Ghast all scale off Swamp count, while Extraplanar Lens is
imprinted on a Snow-Covered Swamp. The emblem is a kill, not value: 29 Snow-Covered Swamps plus
Urborg making every other land a Swamp means ten lands tap for forty mana, which is Torment of
Hailfire for X=38.
**Known cost, decided and accepted:** she enters at 3, so the −3 kills her the turn it is used, and
the ultimate needs three full turn cycles of +1 undefended at a four-player table. **Kaya's Ghostform
enchants a creature OR a planeswalker you control** and is the only protection in the deck for her;
she returns at base loyalty 3.

## Sorcery (9)

**Bubbling Muck** — {B} — Sorcery
"Until end of turn, whenever a player taps a Swamp for mana, that player adds an additional {B}."

**Demonic Tutor** — {1}{B} — Sorcery
"Search your library for a card, put that card into your hand, then shuffle."

**Diabolic Intent** — {1}{B} — Sorcery
"As an additional cost to cast this spell, sacrifice a creature. | Search your library for a card, put that card into your hand, then shuffle."

**Exsanguinate** — {X}{B}{B} — Sorcery
"Each opponent loses X life. You gain life equal to the life lost this way."

**Feed the Swarm** — {1}{B} — Sorcery
"Destroy target creature or enchantment an opponent controls. You lose life equal to that permanent's mana value."

**Grim Tutor** — {1}{B}{B} — Sorcery
"Search your library for a card, put that card into your hand, then shuffle. You lose 3 life."

**Night's Whisper** — {1}{B} — Sorcery
"You draw two cards and lose 2 life."

**Read the Bones** — {2}{B} — Sorcery
"Scry 2, then draw two cards. You lose 2 life. (To scry 2, look at the top two cards of your library, then put any number of them on the bottom and the rest on top in any order.)"

**Torment of Hailfire** — {X}{B}{B} — Sorcery
"Repeat the following process X times. Each opponent loses 3 life unless that player sacrifices a nonland permanent of their choice or discards a card."


## Instant (7)

**Cabal Ritual** — {1}{B} — Instant
"Add {B}{B}{B}. | Threshold — Add {B}{B}{B}{B}{B} instead if there are seven or more cards in your graveyard."

**Culling the Weak** — {B} — Instant
"As an additional cost to cast this spell, sacrifice a creature. | Add {B}{B}{B}{B}."

**Dark Ritual** — {B} — Instant
"Add {B}{B}{B}."

**Go for the Throat** — {1}{B} — Instant
"Destroy target nonartifact creature."

**Snuff Out** — {3}{B} — Instant
"If you control a Swamp, you may pay 4 life rather than pay this spell's mana cost. | Destroy target nonblack creature. It can't be regenerated."

**Vampiric Tutor** — {B} — Instant
"Search your library for a card, then shuffle and put that card on top. You lose 2 life."

**Village Rites** — {B} — Instant
"As an additional cost to cast this spell, sacrifice a creature. | Draw two cards."


## Land (35)

**Cabal Coffers** — Land — Land
"{2}, {T}: Add {B} for each Swamp you control."

**Cabal Stronghold** — Land — Land
"{T}: Add {C}. | {3}, {T}: Add {B} for each basic Swamp you control."

**Deserted Temple** — Land — Land
"{T}: Add {C}. | {1}, {T}: Untap target land."

**Nykthos, Shrine to Nyx** — Land — Legendary Land
"{T}: Add {C}. | {2}, {T}: Choose a color. Add an amount of mana of that color equal to your devotion to that color. (Your devotion to a color is the number of mana symbols of that color in the mana costs of permanents you control.)"

**Rogue's Passage** — Land — Land
"{T}: Add {C}. | {4}, {T}: Target creature can't be blocked this turn."

29x Snow-Covered Swamp (Basic Snow Land — Swamp). Snow basics so Extraplanar Lens/Caged Sun-style
effects can be imprinted on a land type opponents do not share. They are still Swamps, so Cabal
Coffers, Cabal Stronghold (basic Swamp), Crypt Ghast, Nirkana Revenant, Bubbling Muck, Snuff Out
and Liliana all read them normally.
**Urborg, Tomb of Yawgmoth** — Land — Legendary Land
"Each land is a Swamp in addition to its other land types."

## Simulation

Registered in the `mtg-sim` harness as deck key **`deathtouch`** (aka virtus, monoblack, black).
Results to date, Forge AI piloting both sides:

- **Heads-up vs the blue mill deck: 43-7 (86%)**, decided=50, median kill turn 9. Heads-up strips
  the blue deck's pod multiplier, so this number flatters this deck considerably.
- **Three-way pod vs blue mill and Kodama: 38.4%** over 73 decided games across 3 seeds, 95% CI
  [27.2%, 49.5%]. Par is 33.3% and the interval contains it, so all three decks are statistically
  indistinguishable.

### READ THIS BEFORE DRAWING CONCLUSIONS FROM THE GAMES BELOW

**These are games the owner pasted into a chat session. They are NOT a complete play record.** He
plays far more games than he pastes, and which ones get pasted is arbitrary.

**Do not infer that a card is underperforming because it does not appear here, or appears rarely.**
That mistake was made on 2026-10-27 about both Grave Pact and Aetherflux Reservoir and had to be
withdrawn in both cases. Absence from this section is evidence of nothing. The owner's own report
of how a card plays outranks anything counted off these logs.

What this section IS good for: concrete sequences, rules interactions, exact mana counts, and
things that actually happened. What it is NOT good for: frequency, win rate, or whether a card is
pulling its weight.

### THE OWNER'S RULE, 2026-10-28: "Every card has a purpose for when the time arrives."

**This is the single most-repeated mistake made against this deck, and it has been made five times.
Do not make it a sixth.** A card is not graded on how often it appears in a sample of logs. It is
graded on what it does in the game where it is the answer.

| Card | What was claimed | What actually happened |
|---|---|---|
| **Viridian Longbow + Thornbite Staff** | Argued as a cut, 2026-10-22 | Became ENGINE 3; broke a Cloudsteel Kirin "you can't lose the game" lock that nothing else in the 100 answers |
| **Grave Pact** | "Has not yet been the reason a game was won" | Withdrawn — drawn from a biased sample |
| **Aetherflux Reservoir** | "The pay-50 kill rarely fires" | Owner: it fires reliably whenever it and Exquisite Blood are both out |
| **Stensian Sanguinist** | "The preparation half has produced zero value" | Owner: "I use it when I can" — a Forge AI limitation, not a card problem |
| **Rogue's Passage** | "The slot is low-impact, not worth chasing an upgrade" | Activated three turns running to push Virtus and then Sidisi through for the kill, 2026-10-28 |

**The rule that follows:** absence from a log is not evidence. A card that does nothing in nine
games and wins the tenth has done its job. Before describing any card in this deck as
underperforming, check whether the claim rests on anything other than how often it showed up in
logs the owner happened to paste — and if it does not, do not make the claim.

This sits alongside the repo rule in CLAUDE.md that **redundancy is consistency, not waste**. Both
exist because the deck is a 99-card singleton: the question is never "how often" but "is the answer
in there when it is needed."

### INDEX OF ALL LOGGED GAMES — 32 games, 28-4, last updated 2026-10-29

Every game the owner has pasted, in order. Turn numbers are **sleepy's own turns**, not Forge's
log turns. "Won by" is the thing that actually ended the game, not everything that mattered in it.

| # | Date | Result | Own turn | Clock | Won / lost by |
|---|---|---|---|---|---|
| 1 | 10-21 | **W** | 13 | 4m44s | Engine 1 — sparked by an **opponent's** Avacyn attack |
| 2 | 10-26 | **W** | 13 | 19m08s | **Aetherflux Reservoir + Exquisite Blood** — first recorded |
| 3 | 10-26 | **W** | 4 | 7m38s | Engine 1 — Blight-Priest × Conqueror. **Fastest by turns** |
| 4 | 10-26 | **W** | 9 | 9m37s | **Torment of Hailfire X=20**. Won from behind at 11 life |
| 5 | 10-26 | **W** | 11 | 19m04s | **Torment of Hailfire X=22** off eight Swamps |
| 6 | 10-27 | **W** | 10 | 8m18s | Engine 1 — **South Wind Avatar sparked its own combo** |
| 7 | 10-27 | **W** | 10 | 11m13s | **Virtus + Commander's Plate** — Engine 4 discovered here |
| 8 | 10-27 | **W** | 11 | 13m33s | **Engine 3** — Viridian Longbow + Thornbite, 20-turn lock |
| 9 | 10-27 | **W** | 9 | 26m31s | Engine 1 — comboed off at **8 life**, closest call in a win |
| 10 | 10-28 | **W** | 9 | 4m40s | **Sheoldred** killed two opponents on their own draw steps |
| 11 | 10-28 | **W** | 9 | 6m52s | **Dauthi Embrace** + Virtus halvings |
| 12 | 10-28 | **W** | 6 | 18m43s | Engine 1 — leanest kill yet |
| 13 | 10-28 | **W** | 11 | 28m08s | Thornbite auto-attach. Rematch vs. the loss-1 pod |
| — | 10-28 | **L** | died t41 | — | **Mass exile + protection** (Marcus, W/G Angels) |
| — | 10-28 | **L** | died t43 | — | **Elesh Norn −2/−2 + Farewell** (Marcus, mono-white) |
| 14 | 10-28 | **W** | 10 | 7m40s | **Witch of the Moors + Tergrid** stole eight creatures |
| 15 | 10-28 | **W** | 16 | 1h08m42s | **Hooded Blightfang** grind |
| 16 | 10-28 | **W** | 13 | 44m37s | **Stensian Sanguinist + White Widow**, grew 2/2 → 8/8 |
| 17 | 10-28 | **W** | 11 | 7m18s | Engine 1 — six lands, **commander never cast** |
| 18 | 10-28 | **W** | 19 | 20m10s | Virtus/Plate + **Hooded Blightfang for exactly 1** |
| 19 | 10-28 | **W** | 24 | **1h21m09s** | Three different kills: Exsanguinate, Aetherflux, combat |
| 20 | 10-28 | **W** | 13 | 10m00s | Engine 1 — **Blightfang sparked both halves** |
| — | 10-28 | **L** | died t5 | 2m41s | **21 commander damage** — Ishai + Bruse Tarl double strike |
| 21 | 10-28 | **W** | 8 | 14m06s | **Hailfire X=8 + Darkness Crystal**; two Aetherflux fires |
| 22 | 10-28 | **W** | 10 | 10m02s | **Thornbite on Virtus** (Lens-paid) + Gray Merchant for 9 |
| 23 | 10-29 | **W** | 7 | **3m29s** | Engine 1 — sparked by an **opponent's Scrawling Crawler** |
| 24 | 10-29 | **W** | 7 | 5m14s | Engine 1 — Vito × Exquisite Blood, **finished on 143 life** |
| 25 | 10-29 | **W** | 11 | 13m36s | Engine 1 — sparked by **Crypt Ghast extort** |
| 26 | 10-29 | **W** | 7 | 14m28s | Engine 1 — Vito × Exquisite Blood **ticking at 2** |
| 27 | 10-29 | **W** | 8 | 10m57s | Engine 1 — sparked by an opponent's **Vandalblast** |
| — | 10-29 | **L** | died t11 | 1h04m32s | **Six answers + a 92-damage flying strike** (Picumar) |
| 28 | 10-29 | **W** | 7 | 6m50s | Engine 1 — **Enduring Tenacity × Conqueror, ticking at 5** |

**Current extremes.** Fastest by turns: **own turn 4** (game 3). Fastest by clock: **3m29s**
(game 23). Longest: **1h21m09s** / own turn 24 (game 19). Lowest life in a win: **8**
(game 9). Highest life: **143** (game 24). Shortest loss: eliminated on **turn 5** (loss 3).

**Individual entries below carry superlatives that were true when written** — several say "fastest
on record" or "longest on record" and have since been beaten. This table is the authority on
which game holds what.

**How the wins break down:** Engine 1 (Side A × Side B) closed **15**; Torment of Hailfire **3**;
Virtus combat/halving **3**; Aetherflux Reservoir **2**; and one each for Sheoldred's draw
punishment, Engine 3's Longbow lock, Witch + Tergrid, Stensian + White Widow, and Blightfang's
grind. **Four of the Engine 1 wins were sparked by a card an opponent controlled.**

**How the losses break down:** two to **exile-based sweepers the deck cannot rebuild through**,
one to **a fast evasive commander** the deck could neither block nor race. See "What the losses
have in common" above.

### Logged win — 2026-10-21, four-player pod, won turn 25 (round 13), 4m44s

sleepy 1 — Collin Goofgrumble 0, Douglas 0, Jezzine 0. Finished at **87 life**.

**The combo fired off an opponent's attack on another opponent, not off anything this deck did.**
Worth recording because it is the opposite of how the kill is usually described.

- **Turn 24 (own turn), assembly:** land, **Marauding Blight-Priest** ({2}{B}), then **Culling the
  Weak** sacrificing **Gonti, Lord of Luxury** for {B}{B}{B}{B} to deploy **Bloodthirsty Conqueror**
  the same turn. Gonti had already cashed his ETB on turn 20, so the sacrifice cost an empty shell.
  Culling the Weak is what made it a one-turn assembly instead of two.
- **Turn 25 (Collin's turn), the spark:** Collin attacked **Douglas** with Avacyn, Angel of Hope for
  10. An opponent lost life → Conqueror gained 10 (40 → 50) → Blight-Priest drained each opponent 1
  → three more opponents losing life → Conqueror again → loop. It ran roughly 38 iterations until
  Collin bottomed out from 38 to 0. Jezzine and Douglas died earlier in the same loop.
- **No action required from this deck once both halves were down.** Any life-loss event at the table
  starts it, including one between two other players.

**Hired Poisoner earned its slot, and this is the evidence.** It attacked on turns 8 and 12; each
attack triggered **Hooded Blightfang** for 1 life from each of three opponents plus 1 gained — six
life of swing from a one-mana 1/1 that never dealt more than 1 combat damage. See the Cover of
Darkness correction above, where Hired Poisoner was the alternate cut considered and kept.

**The deck attacked exactly twice all game** (turns 8 and 12, same creature) and won anyway.
**Mass Calcify** on turn 17 destroyed Hooded Blightfang and Hired Poisoner — all nonwhite creatures
— and the deck simply rebuilt and comboed off seven turns later.

**Caveat on this log: the simulated deck may be stale.** The log prints `Swamp`, not
`Snow-Covered Swamp`, and none of Liliana, Blightwing Bandit, Extraplanar Lens or Ferocity of the
Hunt appear. If Forge is not abbreviating the name, the list being simmed predates commit `580c045`
and everything after it. Re-export `deathtouch_decklist.txt` into Forge before weighting these
results.

### Logged win — 2026-10-26 (1st game), four-player pod, won on own turn 13 (log turn 49), 19m08s

sleepy 1 — Amy Loafknock 0, Zyneste 0, Ochala 0. Finished at **43 life**, having peaked at **100**.

**Won with Aetherflux Reservoir + Exquisite Blood, not with the Side A / Side B grid.** This is the
first recorded use of the Reservoir line and it is the reason the section above was added.

- **The kill turn:** topdecked and cast **Aetherflux Reservoir** off a Snow-Covered Swamp and Sol
  Ring in the postcombat main, then activated it three times in the same turn. Amy (14 -> -36),
  Zyneste (2 -> -48), Ochala (3 -> -47). Exquisite Blood refunded all 50 each time.
- Exquisite Blood had been out since turn 41; the Reservoir was the last piece.

**What got him there:**
- **The Widows are doing their job.** On the final alpha strike, **Black Widow, Deadly Hunter**
  (draw a card per deathtouch connect) and **White Widow, Yelena Belova** (+1/+1 counter per
  connect) each triggered **eight times** off one attack. Eight cards from a single combat step.
- **Virtus + Viridian Longbow is the removal suite.** Used four separate times at instant speed for
  free, killing **Sheoldred**, **Raphael Fiendish Savior**, **Angelic Sell-Sword** and **Bronze
  Bombshell** — all without Thornbite Staff to untap it.
- **Erebos** was cast turn 13 and the `{1}{B}, pay 2 life: draw a card` ability was activated five
  times across the game. The nine-card swap's draw package is working.
- **Witch of the Moors** fired its end-step edict three times, stripping a creature from each
  opponent each time.
- **Avacyn, Angel of Horror** recurred Black Widow and Dhund Operative after they died.

**Disruption he played through and still won:**
- **Strip Mine destroyed Cabal Coffers** on turn 36.
- **Grindstone** milled seven relevant cards: Commander's Plate, Vampiric Tutor, Basilisk Collar,
  Phyrexian Arena, Sheoldred the Apocalypse, The Darkness Crystal, Gray Merchant of Asphodel.
- **Public Execution** killed Sidisi; **Inferno Fist** killed Virtus on turn 19 (Kaya's Ghostform
  brought him back later).

**Deck version:** this game was run on the post-9-swap list — Erebos, Aetherflux Reservoir,
Enduring Tenacity and Snow-Covered Swamps all appear in the log. Grave Pact had not been added yet.

### Logged win — 2026-10-26 (2nd game), four-player pod, won on own turn 4 (log turn 16), 7m38s

sleepy 1 — Amy Loafknock 0, Zyneste 0, Ochala 0. Finished at **78 life**, from 38.

**Fastest recorded win by a wide margin, and the deck cast four relevant spells all game.** Engine 1,
Marauding Blight-Priest x Bloodthirsty Conqueror.

| Own turn | Log turn | Play |
|---|---|---|
| 2 | 8 | Sol Ring, **Marauding Blight-Priest** (Side A) |
| — | 7 (Ochala's end step) | **Vampiric Tutor** |
| 3 | 12 | **Demonic Tutor**, Quietus Spike |
| 4 | 16 | **Bloodthirsty Conqueror** off Sol Ring + 3 Snow-Covered Swamps |

**The spark was an opponent's own card.** Zyneste controlled **Wretched Anurid** — *"whenever
another creature enters, you lose 1 life."* Bloodthirsty Conqueror entering triggered **their**
Anurid, Zyneste lost 1, Conqueror gained sleepy 1, Blight-Priest drained each opponent 1, Conqueror
again, loop. Roughly 40 iterations. sleepy 38 -> 78 while the table went to 0. Zyneste died first,
having spent the whole game chipping themself with the Anurid; Ochala and Amy hit 0 on the same
iteration.

**sleepy never attacked, never used removal, and activated nothing.** He cast a creature and won.

**This validates the Side B tutoring rule.** Side A arrived on its own by turn 2 — there are four of
them. Both tutors were then spent finding Side B, which is only two cards deep. That is the grid
working exactly as written above.

**Quietus Spike was cast on turn 3 and never mattered.** Noted only so the log is not read as
evidence for it.

### Logged win — 2026-10-26 (3rd game), four-player pod, won on own turn 9 (log turn 33), 9m37s

sleepy 1 — Amy Loafknock 0, Zyneste 0, Ochala 0. Finished at **11 life** — the lowest of any
logged win, and the first one won from behind.

**Won with Torment of Hailfire X=20**, cast turn 31 off Sol Ring + 5 Snow-Covered Swamps + Cabal
Coffers + Cabal Stronghold, with **Crypt Ghast and Extraplanar Lens both doubling**. Ochala, out of
permanents and cards, went 12 -> **-48**. This is the "sitting on Coffers mana with nothing to
spend it on" complaint finally converted into a win condition.

**Viridian Longbow broke a "can't lose the game" lock — the deck has no other answer.** Ochala had
**Cloudsteel Kirin** attached to Micromancer: *"Equipped creature has flying and 'You can't lose
the game and your opponents can't win the game.'"* That is why the log is a wall of
`Replacement Effect: You can't lose the game` — Ochala sat at -48 and would not die. A free
instant-speed **South Wind Avatar** deathtouch ping off the Longbow killed Micromancer, the Kirin
came off, and Ochala and Zyneste died on the spot. **Without the Longbow this game is not won.**
Second log in a row it has carried; see the 2026-10-22 correction above where it was nearly cut.

**Crypt Ghast extort + South Wind Avatar is a 6-point swing per spell cast** — extort drains 1 from
each opponent and gains 3, and South Wind Avatar sees that gain and drains 1 more from each.

- **Aetherflux Reservoir** was cast turn 23 and never reached the pay-50 mode; sleepy hovered at
  11-25 life all game. The Engine 2 kill needs 50 life and this game never got there.
- **Ochala cast Quietus Spike**, equipped Micromancer, and halved sleepy 22 -> 11.

### Logged win — 2026-10-26 (4th game), four-player pod, won on own turn 11 (log turn 44), 19m04s

sleepy 1 — Amy Loafknock 0, Zyneste 0, Ochala 0. **The first game closed by a single card.**

**Torment of Hailfire X=22 killed all three at once**, off **eight Snow-Covered Swamps and nothing
else**. Extraplanar Lens and Nirkana Revenant each add a {B} per Swamp tapped, so 8 lands produced
**24 mana** — exactly {22}{B}{B}. The table went from 34 / 30 / 23 to **-17 / -18 / -22**.

**There was no Cabal Coffers this game.** Nykthos, Cabal Ritual and Bubbling Muck were all milled
out. Eight basics and two doublers paid for it alone.

**Witch of the Moors was the MVP: five end-step triggers, roughly 13 creatures destroyed** across
the table (Boneyard Aberration, Wicked Wolf, Ohabi Caleria twice, Living Conundrum, Bloodroot
Apothecary, Selhoff Occultist, three Reassembling Skeletons and more).

**Witch also recurred a card the deck had been milled.** Nirkana Revenant was milled turn 17,
returned to hand by Witch turn 32, cast turn 36, and became one of the two doublers that paid for
the Hailfire. Ochala milled sleepy 11 cards and handed one back.

**Stensian Sanguinist's first appearance, and it worked.** Turn 28 it triggered on attack, gave
Witch of the Moors deathtouch, Witch connected with Ochala for 4, and Stensian **became prepared**.
It died to Wicked Wolf's fight trigger turn 34 before the free Exsanguinate copy was cast, so the
preparation was wasted — but the card did what it says.

**Two costs worth recording:**
- **Feed the Swarm cost 12 life.** Ochala had mutated Mindleecher onto Emblazoned Golem; Feed the
  Swarm charges the permanent's mana value, and a mutate pile's is the whole stack. 31 -> 19 to
  kill one creature.
- **3 poison counters** from Zyneste's Inkmoth Nexus across three attacks. Not close to 10, but
  poison is a clock this deck cannot interact with or undo.

Grave Pact was not drawn.

### Logged win — 2026-10-27 (1st game), four-player pod, won on own turn 10 (log turn 39), 8m18s

sleepy 1 — Amy Loafknock 0, Zyneste 0, Ochala 0. Engine 1, and a **new pairing: South Wind Avatar
x Exquisite Blood.**

**South Wind Avatar sparked its own combo — exactly as the grid predicts.** Black Widow (3/3)
attacked Zyneste, Sigiled Sentinel blocked, both died. South Wind Avatar's first ability (*"whenever
another creature you control dies, you gain life equal to its toughness"*) gained 3, which
triggered its **second** ability (*"whenever you gain life, each opponent loses 1 life"*), which
Exquisite Blood refunded, which triggered it again. About 36 iterations. Zyneste died first at 20,
then Amy at 28, then Ochala at 36 — confirming that ticking one opponent to 0 just moves the loop
to the next.

**The spark was a deathtoucher trading in combat.** With 21 printed deathtouchers whose job is
exactly that, this is the most repeatable spark the deck has.

**The deck won through a Sunder.** Ochala cast **Sunder** turn 22 — *"Return all lands to their
owners' hands"*, at instant speed, every land on the table including a freshly played Cabal
Coffers. sleepy was over hand size at cleanup and discarded **Cabal Stronghold, three Snow-Covered
Swamps, Exsanguinate and Gray Merchant**. Coffers was never replayed. From turn 23 the deck
rebuilt one land a turn off basics and still assembled and killed the table by turn 39. **This is
the 35-land count earning its keep** — a deck that is almost all Swamps refuels from a mass land
bounce.

- **Phyrexian Arena** ticked every upkeep from turn 15 — nine cards.
- **Black Widow attacked five times** for 3, drawing a card each time.
- **Witch of the Moors** got two end-step edicts.

### Logged win — 2026-10-27 (2nd game), four-player pod, won on own turn 10 (log turn 35), 11m13s

sleepy 1 — Omarn 0, Daisy 0, Randy 0. Finished at **31 life**. A new pod (Omarn, Daisy, Randy
rather than the usual three).

**Won with Virtus + Commander's Plate, which was not in this file until this game.** See ENGINE 4
above, added because of this log. None of the three opponents controlled a black creature — the
pod was W/G, W/U/R and mono-G — so the Plate's protection from white, blue, red and green made
Virtus unblockable for the entire game.

| Own turn | Log turn | Target | Combat | After the halving |
|---|---|---|---|---|
| 15 | 15 | Omarn | 40 -> 36 | **18** |
| 19 | 19 | Randy | 41 -> 37 | **18** |
| 23 | 23 | Omarn | 18 -> 14 | **7** |
| 27 | 27 | Daisy | 22 -> 18 | **9** |
| 33 | 33 | Omarn | 6 -> 0 | dead (Virtus 4 + Crypt Ghast 2) |
| 35 | 35 | Daisy | 7 -> 1 | **0** |

**Six connects, blocked zero times.** Commander's Plate was cast turn 3 and sat waiting; Virtus
landed turn 11 and was equipped turn 15.

**Rogue's Passage was in play all game and never needed.** The Plate's protection already provided
the evasion, for free, every turn.

**Torment of Hailfire was only X=9** this game (turn 33) — against X=20 and X=22 in the two games
before it. No Cabal Coffers and no doublers; six lands and extort. It stripped Omarn's and Daisy's
boards rather than killing, which was enough.

- **Exquisite Blood landed on the last turn** and gained 6 off the final halving, but no Side A was
  out, so Engine 1 never came online. It was not needed.
- **Daisy killed Randy, not sleepy** — her five-creature board took Randy 3 -> -4 on turn 29. The
  deck only had to kill two opponents.
- **The deck took real damage:** Daisy's turn-32 alpha strike put sleepy 36 -> 24, and **Aberrant**
  destroyed **Phyrexian Arena** with its Heavy Power Hammer trigger.
- Grave Pact was not drawn.

### Logged win — 2026-10-27 (3rd game), four-player pod, won on own turn 11 (log turn 40), 13m33s

sleepy 1 — Nadeer 0, Dominic 0, Zessfar 0. Lowest life all game was 36 — never seriously threatened.

**The first logged game where ENGINE 3 actually fired, and it locked the table out for twenty
turns.** Viridian Longbow + Thornbite Staff, both on **Virtus**, killed roughly **21 creatures**,
most of them on their controller's own turn as they resolved:

Elephant Token, Barbara Wright, Tireless Provisioner, The Odd Acorn Gang (x2), Nut Collector,
The Twelfth Doctor (x2), Breeches Eager Pillager, Impulsive Pilferer, Lightning-Rig Crew,
Steamcore Scholar, Moon-Blessed Cleric, Gilded Goose, Windreader Sphinx, **Jin-Gitaxias**,
Inquisitive Glimmer, Defiler of Dreams, Warden of Evos Isle, Storm Fleet Aerialist, Spectral Sailor.

**Jin-Gitaxias had Ward {2} and the ward was simply paid.**

**Thornbite worked four turns before the Longbow arrived, because Crypt Ghast was out.** Thornbite
grants `{2}, {T}: deal 1 damage`, Crypt Ghast makes each Swamp tap for {B}{B}, so one Swamp paid
for one ping. Four kills on turn 21 that way; Longbow landed turn 25 and made the pings free. See
the ENGINE 3 note above, which was updated because of this game.

**Avacyn blanked a board wipe.** Dominic cast **The Night of the Doctor** on turn 39 — *"Destroy
all creatures"* — killing Witch of the Moors, Avacyn, Vampire of the Dire Moon, Virtus and Crypt
Ghast. Avacyn triggers on *"Avacyn or another nontoken creature you control"* dying, **including
herself**, so all five triggers went on the stack and **all five creatures returned at the next end
step.** The wipe cost nothing. sleepy untapped and cast Torment of Hailfire for X=14 to finish
Dominic and Nadeer.

**Engine 4 ran alongside it.** Commander's Plate equipped turn 17; Virtus halvings on turns 21, 25,
29 and 37 — Zessfar 40 -> 18, Dominic 37 -> 16, Nadeer 39 -> 17, then Zessfar 16 -> 0.

**The Engine 4 caveat was live this game.** Zessfar was B/G and could legally have blocked Virtus;
the Plate's protection only covered Dominic (W/U/R) and Nadeer (U/R). Forge chose not to block, but
a black opponent at the table is exactly the case the Engine 4 entry warns about.

- **Rishadan Brigand made sleepy sacrifice Skullclamp** on turn 19, before it ever equipped anything.
- Grave Pact was not drawn. (See the caveat at the top of this section.)

### Logged win — 2026-10-27 (4th game), four-player pod, won on own turn 9 (log turn 33), 26m31s

sleepy 1 — Nadeer 0, Dominic 0, Zessfar 0. **Comboed off at 8 life** — the closest the deck has come
to losing in any logged game. Finished at **47**.

**What nearly killed him:** Dominic ran **Cleon, Merry Champion** (double strike) with **Kediss,
Emberclaw Familiar** — *"Whenever a commander you control deals combat damage to an opponent, it
deals that much damage to each other opponent."* On turn 24 Cleon was pumped with Invigorated
Rampage and connected for 6 twice through double strike; sleepy went 24 -> 18 -> 8 in one combat,
and Kediss dealt 24 of collateral to each of Nadeer and Zessfar at the same time.

**The spark was Vito's activated ability, bought on purpose.** Exquisite Blood, Vito and Marauding
Blight-Priest were all on the battlefield with no life-change event to start the loop. sleepy paid
`{3}{B}{B}` for **Vito's mass lifelink**, used **Rogue's Passage** to make Virtus unblockable, and
attacked for **1 damage**. Lifelink gained 1 life, and that was the whole spark.

**Two Side A cards doubled the rate.** Each Exquisite Blood lifegain triggered both Vito (targeted,
loses that much) and Blight-Priest (each opponent loses 1), so Dominic took 2 per iteration and the
others 1. Roughly 40 iterations — Nadeer died first at 9, then Zessfar, then Dominic from 40.

This game is why the Engine 1 section above now calls Vito the spark button rather than just a
Side A card.

- **Viridian Longbow went on Dire Fleet Poisoner**, not Virtus, on turn 17 — no Thornbite this game,
  so one ping per turn, which still killed Wick the Whorled Mind, Urabrask and Cleon twice.
- **Kaya's Ghostform returned Virtus** after it traded with an Elemental Token on turn 25, which is
  the only reason Virtus was available to spark the kill four turns later.
- **Siege Smash destroyed Extraplanar Lens** on turn 23. It has **split second**, so there was no
  responding to it.
- Grave Pact was not in this log. (See the caveat at the top of this section.)

**The takeaway: Engine 1 does not care about the board.** sleepy was at 8 life facing a board
producing 12+ damage a turn, and the kill cost five mana and one point of lifelink damage.

### Logged win — 2026-10-28 (1st game), four-player pod, won on own turn 9 (log turn 34), 4m40s

sleepy 1 — Nathaniel 0, Gai 0, Katelyn 0. Fastest game on the clock so far.

**Sheoldred killed two of the three opponents on their own draw steps**, not in combat. *"Whenever
an opponent draws a card, they lose 2 life."* She landed turn 12 and ticked every opponent for 2
every turn for ten turns, while gaining sleepy 2 on each of his own draws.

- **Gai died turn 30** — draw step, 2 -> 0.
- **Katelyn died turn 31** — draw step, 1 -> -1.

sleepy went *up* from 40 to 47 despite taking 11 from Tezzeret. Gai's own **Tezzeret, Master of the
Bridge** hit the table for 11 each, dropping Katelyn to 3 — he set up Sheoldred to finish both
himself and his neighbour.

**Engine 4 ran alongside it.** Commander's Plate on Virtus turn 16; halvings on turns 21, 25, 29
and 33 (Gai 34 -> 15, Katelyn 32 -> 14, Gai 11 -> 2, Nathaniel 18 -> 7).

**This is the game that exposed the colourless hole in Engine 4.** Gai controlled 1/1 **colourless**
Thopter tokens, which the Plate's protection from W/U/R/G does nothing about. They could have
blocked Virtus at any point. See the corrected caveat in ENGINE 4 above.

**Rogue's Passage was never drawn or played.**

### Logged win — 2026-10-28 (2nd game), four-player pod, won on own turn 9 (log turn 29), 6m52s

sleepy 1 — Nathaniel 0, Gai 0, Katelyn 0. **A Dauthi Embrace showcase, and the game that settled
the Minas Morgul question.**

**Dauthi Embrace was cast turn 14 and used every turn after.** Virtus connected turns 18, 22, 26,
27 and 29 and was never blocked once:

| Turn | Target | After the halving |
|---|---|---|
| 18 | Katelyn | 40 -> **19** |
| 22 | Gai | 36 -> **17** |
| 26 | Nathaniel | 31 -> **15** |
| 27 | Nathaniel | 15 -> **6** |

**On the kill turn sleepy paid {B}{B} three times** — shadow on Virtus, Sheoldred *and* Gray
Merchant — and alpha-struck. **Minas Morgul could not have done that**: one shadow counter at a
time at {3}{B} each. The winning turn required three creatures unblockable simultaneously.

**Virtus was a 1/1 all game.** No Commander's Plate; Basilisk Collar went on turn 18, which grants
deathtouch and lifelink but no power. One combat damage per connect, and the halving did all the
work. This is the evidence behind the "+3/+3 is almost irrelevant" note in ENGINE 4 above.

**Nathaniel killed two opponents for sleepy.** Katelyn died turn 23 and Gai turn 26 to Nathaniel's
Phyrexian board (Phyrexian Vindicator, Elesh Norn, Essence of Orthodoxy, Incubator tokens). sleepy
only had to kill one player.

**Elesh Norn** taxed every point of damage sleepy dealt — *"whenever a source an opponent controls
deals damage to you or a permanent you control, that source's controller loses 2 life unless they
pay {1}"* — and sleepy paid the {1} rather than take it.

Sheoldred carried the draw-step drain again. Grave Pact was not drawn in either game.

### Logged win — 2026-10-28 (3rd game), four-player pod, won on own turn 6 (log turn 23), 18m43s

sleepy 1 — Nathaniel 0, Gai 0, Katelyn 0. **Second-fastest win on record** (the turn-4 game is still
the fastest), and the leanest Engine 1 kill yet.

**Everything sleepy cast all game:** Black Widow (turn 11), Nighthawk Scavenger (turn 15),
Marauding Blight-Priest and Dire Fleet Poisoner (turn 19), Exquisite Blood (turn 23).

**Both earlier threats had already been answered.** Nathaniel's **Rise of the Witch-king** forced
everyone to sacrifice a creature on turn 12 and took Black Widow; Gai's **Assassin's Trophy** killed
Nighthawk Scavenger on turn 17. None of it mattered.

**The kill turn:** cast Exquisite Blood, attack Nathaniel with a **2/2 Dire Fleet Poisoner** for 2.
Exquisite Blood saw an opponent lose 2 -> gained 2 -> Blight-Priest drained each opponent 1 ->
Exquisite Blood again. Roughly 40 iterations. sleepy went **40 -> 81**; Nathaniel died first, then
Katelyn and Gai together from 40 each.

**sleepy had two creatures on the board and was behind.** This is the third consecutive Engine 1
win where the spark was just a small creature connecting — Black Widow trading, Virtus for 1 off
Vito's lifelink, and now an unblocked 2/2. **The loop does not care what the board looks like.**

Rogue's Passage was in play from turn 15 and, for the third game running, was never used for
evasion.

### Logged win — 2026-10-28 (4th game), four-player pod, won on own turn 11 (log turn 38), 28m08s

sleepy 1 — Kylie 0, Amadeus 0, Marcus 0. **Rematch against the exact pod that handed the deck its
only logged loss, and the longest game on record.** Record 13-1.

**Thornbite Staff auto-attached for the first time in any log.** Vampire Nighthawk cast turn 33,
Thornbite attached free off the Shaman trigger. See the ENGINE 3 note above, which was expanded
because of this game — with Enduring Tenacity and South Wind Avatar already out, each {2} ping
killed a creature, gained 1 off lifelink, drained the table twice, and untapped Nighthawk. Ran five
times across turns 35-38, eating Tomik Izzet Sparkmage, Sawblade Scamp, an Elemental token, a
Goblin token and **Hellrider**.

**Grave Pact earned its slot here.** Cast turn 22. On turn 33 Virtus died blocking Generous
Plunderer and Grave Pact made **all three opponents sacrifice a creature**, while South Wind Avatar
turned Virtus's own death into life that then drained. This is the card doing what was argued for
when it was added.

**Virtus halved three times before dying** — Amadeus 34 -> 16, Marcus 40 -> 19, Marcus 8 -> 4 — and
was a **1/1 the whole time**. No Commander's Plate this game.

**Three permanents were answered in the first nine turns and it did not matter:**
- **Vandalblast** destroyed Skullclamp (turn 7).
- **Swords to Plowshares** exiled Tinybones (turn 9).
- **Aang, Swift Savior** airbended Vampire of the Dire Moon into exile (turn 9).

**Two opponents died to each other.** Marcus died turn 31 to Kylie's attack; Amadeus died turn 37
to Kylie's **Hellrider** and **Raid Bombardment** attack triggers. sleepy killed only Kylie, on
turn 38. **Third consecutive game where the deck only had to kill one player** — a recurring
pattern worth noting: in a four-player pod this deck often wins the last fight rather than all
three.

### LOGGED LOSS — 2026-10-28, four-player pod. Marcus won; sleepy died turn 41 at -8.

**The first recorded loss, and the only data this file has on how the deck actually loses.** Worth
more attention than any single win. Marcus was W/G Angels; Kylie was B/R pirates/sacrifice; Amadeus
was W/B lifegain.

**Order of events:**

1. **Virtus was exiled on turn 10** by Kylie's **Epic Downfall** (*"Exile target creature with mana
   value 3 or greater"*). Exile, so **Kaya's Ghostform did nothing**. Virtus was not recast until
   turn 33 — **six of sleepy's own turns with no commander**, and Engine 4 offline for most of the
   game.
2. **Vito died to a Lightning Strike** on turn 22. Side A gone.
3. **Blasphemous Act** on turn 26 dealt 13 to every creature and wiped sleepy's board.
4. **Both instant-speed removal spells fizzled on the same creature.**
5. **Side B was never drawn.** No Exquisite Blood, no Bloodthirsty Conqueror anywhere in the log.
   Engine 1 was never live.

### The removal problem — the most important thing in this log

**Radiant, Serra Archangel** — *"Tap another untapped creature you control with flying: Radiant
gains protection from the color of your choice until end of turn."* Marcus had a board full of
Angels, so the ability was **free and repeatable**.

- **Snuff Out** ("destroy target **nonblack** creature") — he made Radiant black. Fizzled, and the
  4 life was already paid.
- **Go for the Throat** ("destroy target **nonartifact** creature") — fizzled the same way.

**Every removal spell in this deck says "destroy target," and all three die to protection:** Snuff
Out, Go for the Throat, **Feed the Swarm**. Against a creature that can grant itself protection on
demand, the deck has no answer at all.

### Structural weaknesses this loss exposes

- **No fliers to block with, and no board wipe that hit his side.** Marcus ended on **119 life**
  off Lyra Dawnbringer (gives all other Angels lifelink), Archangel of Thune, Victory's Herald and
  Ajani. Torment of Hailfire was never drawn.
- **Deathtouch blocking does not stop first strike.** Lyra Dawnbringer is a 5/5 flying **first
  strike** lifelinker — it kills a deathtouch blocker before the blocker deals any damage. The
  deck's main defensive plan is simply off against first strike.
- **Exiling Virtus answers two of the four engines at once** (Engine 4 and the Virtus halving), and
  the deck has **no way to return a creature from exile**. Kaya's Ghostform covers dies-or-exiled
  for the enchanted creature only, and it was not attached at the time.
- **Engine 1 needs Side B, and Side B is two cards.** Every logged win that used Engine 1 had one
  of them. This game did not, and the file already flags Side B as the bottleneck — this is what
  that bottleneck looks like when it bites.

**No changes are being proposed off one loss.** The record is 12-1 and Marcus drew extremely well.
This entry exists so the failure modes are written down rather than inferred from a wall of wins.

### LOGGED LOSS #2 — 2026-10-28, four-player pod. Marcus won; sleepy died turn 43 at -3.

**Second loss, same opponent as the first (Marcus), different deck — mono-white legends/Praetors.**
Record 13-2. This one is a different failure mode from loss #1 and worth reading alongside it.

**ELESH NORN, GRAND CENOBITE IS THE SINGLE WORST CARD THIS DECK CAN FACE.**
*"Other creatures you control get +2/+2. Creatures your opponents control get -2/-2."* Cast turn 36.
With avg MV 2.78 and a deck full of 1/1s and 2/2s, **-2/-2 kills most of the list on arrival**:
- It immediately killed Virtus (1/1) and three of Kylie's creatures on resolution.
- **Marauding Blight-Priest** (3/2) was cast turn 37 and **died instantly**.
- **Virtus was recast on turns 40 AND 42 and died instantly both times.** Three casts, three deaths,
  no damage dealt.

There is no answer to it in the 100 — Go for the Throat and Snuff Out can target it, but it was
never removed, and the deck's own creatures cannot survive to block.

**FAREWELL wiped everything to EXILE.** Turn 24, Marcus chose all four modes: exile all artifacts,
creatures, enchantments and graveyards. sleepy lost **Virtus, Nighthawk Scavenger, Stensian
Sanguinist, Sol Ring and Swiftfoot Boots** in one card. Because it is **exile**, neither Avacyn nor
Kaya's Ghostform could recover any of it — the same hole loss #1 exposed, hit far harder.

**Thalia, Heretic Cathar** (turn 31) — *"Creatures and nonbasic lands your opponents control enter
tapped"* — meant every creature sleepy cast from turn 31 on **arrived tapped and could not block**,
while Marcus built a lethal board.

**Torment of Hailfire was countered by Spell Pierce** on turn 31. sleepy had tapped six Swamps for
X and could not pay the {2}. **The deck's biggest mana sink is a noncreature spell with no
protection.**

**Amadeus's Ruin Crab milled roughly 18 cards** off the top across the game, including **Cabal
Coffers, Nykthos, Erebos, Exsanguinate, Read the Bones, Thornbite Staff, South Wind Avatar,
Viridian Longbow, Foulmire Knight and Rancid Rats**.

**Commander's Plate was destroyed by Witch Enchanter** on turn 19, one turn after it was equipped,
and **Enduring Tenacity by Loran of the Third Path** on turn 41.

### Observation: Forge does not cast Stensian Sanguinist's prepared copy — THE OWNER DOES

Stensian Sanguinist's attack trigger made a creature prepared **four separate times** in this game
(turns 10, 14, 18 and 22) and the free Exsanguinate copy was never cast. Same in the 2026-10-26
game.

**Owner's correction, 2026-10-28: "I use it when I can."** This is a **Forge AI limitation, not a
card problem.** The preparation half works fine in his hands. Do not read the sim logs as evidence
about this card, and do not propose it as a cut on that basis.

**SETTLED, 2026-10-28 (7th game): Forge did cast it, and it killed a player.** Two Exsanguinates
resolved in a deck that holds one standalone copy plus Stensian's half — X=8 killed Gabrielle, X=9
killed Ethan. In the same game Stensian grew itself from 2/2 to 8/8 with White Widow and dealt the
killing blow. The card is not a liability; the earlier write-ups were wrong.

### What the losses have in common

**Losses #1 and #2** were both lost to **mass exile / mass removal that the deck cannot rebuild
through**, plus a permanent the removal suite could not answer. Loss #1 was protection (Radiant);
loss #2 was a static -2/-2 (Elesh Norn) and an exile wipe. The recurring theme there is that **the
deck recovers from spot removal easily and from exile-based sweepers not at all.**

**Losses #3 and #4 are a different axis and do not fit that pattern** — nothing of sleepy's was
removed all game. It was an evasive commander (Ishai, flying, growing off every opponent's spell)
with a free double-strike grant, killing sleepy with 24 commander damage on his fifth turn. See
LOGGED LOSS #3 below. Two distinct ways the deck loses, not one:

1. **Exile-based sweepers**, which it cannot rebuild through.
2. **A fast evasive clock**, which its deathtouch blockers do not deter and its three-mana curve
   does not race. **LOSS #4 is this again at scale** — six fliers under True Conviction and
   Akroma for 92 damage in one combat.
3. **Being answered piece by piece** (LOSS #4). Six removal spells and two counterspells meant
   Side A and Side B were never on the battlefield at the same time. **The engines are
   unprotected two-card assemblies** — no counter backup, no hexproof — so one opponent holding
   up blue mana is enough to stop the Conqueror resolving.

### Logged win — 2026-10-28 (5th game), four-player pod, won on own turn 10 (log turn 33), 7m40s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. **Tergrid's best game by far, and the first log
showing the Witch of the Moors + Tergrid engine actually running.** Record 14-2.

**WITCH OF THE MOORS + TERGRID STOLE EIGHT CREATURES.** Witch forces each opponent to sacrifice a
creature at sleepy's end step whenever he gained life that turn; Tergrid puts every nontoken
permanent they sacrifice onto **his** battlefield. It fired four end steps running:

| Turn | Sacrificed, and taken by Tergrid |
|---|---|
| 18 | Mondrak Glory Dominus, Norin Swift Survivalist |
| 22 | Akiri Line-Slinger, Alora Merry Thief, Kellan the Kid |
| 26 | Queen of Ice |
| 29 | Professional Face-Breaker, Picklock Prankster |

By the final turn sleepy was attacking with **ten creatures, five of them stolen** — Mondrak,
Professional Face-Breaker, Norin, Kellan and Queen of Ice all swung for him. Gabrielle went
**1 -> -27**.

**AYARA IS WHAT TURNS WITCH OF THE MOORS ON, EVERY TURN.** Witch needs "if you gained life this
turn." Ayara reads *"whenever Ayara or another black creature you control enters, each opponent
loses 1 life and you gain 1 life"* — and **every creature in this deck is black**. Casting any
creature guarantees the Witch trigger. That pairing is more reliable than any lifelink attack and
should be treated as the default way to switch Witch on.

**Ayara -> Vito was the second engine.** Ayara's 1 life per black creature became a targeted drain
off Vito (*"whenever you gain life, target opponent loses that much life"*), on top of the 1 each
Ayara already took. Several creatures cost the table 2-3 life just by arriving.

**Virtus was Path to Exile'd on turn 5** and recast later; the deck did not need him this game.

**Grave Pact was cast turn 21 and never triggered** — no creature of sleepy's died after it
resolved.

### Logged win — 2026-10-28 (6th game), four-player pod, won on own turn 16 (log turn 44), 1h08m42s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. **By far the longest game on record** and a
grind, not a combo. Record 15-2.

**Hooded Blightfang was the engine.** *"Whenever a creature you control with deathtouch attacks,
each opponent loses 1 life and you gain 1 life."* It triggers **on attack, not on damage**, so it
paid out every single combat regardless of blocks, and with **Exquisite Blood** out each of those
three separate life losses fed another gain. No Side A was ever drawn, so this was pure incremental
value rather than Engine 1 — and it was enough.

**ROGUE'S PASSAGE EARNED ITS KEEP HERE — a correction to the running assumption.** Across the
previous several logs it was never used for evasion, and the Minas Morgul discussion concluded the
slot was low-impact. **In this game it was activated on three consecutive turns (42, 43, 44)** to
push Virtus and then Sidisi through a board sleepy could not get past otherwise. The final kill was
an unblockable Sidisi. Do not treat the slot as dead weight on the strength of the earlier logs.

**sleepy killed two of the three.** Gray Merchant of Asphodel's ETB on turn 30 took **Brady Nitnumb
3 -> -1**; the final unblockable Sidisi swing took **Gabrielle 1 -> -3**. **Ethan died to
Gabrielle's commander**, Akiri Line-Slinger, on accumulated commander damage (3 + 16 off a Boros
Charm double strike + 8 = 27).

**Torment of Hailfire for X=8** on turn 27 stripped Brady and Gabrielle of six permanents between
them.

**Disruption played through:**
- **An Offer You Can't Refuse countered Aetherflux Reservoir** (turn 25).
- **Chandra's Ignition** had Akiri deal 8 to each opponent and each other creature, killing Gifted
  Aetherborn and taking sleepy 38 -> 30.
- **Swords to Plowshares exiled Blightwing Bandit** (turn 29).
- **Gabrielle's own Bojuka Bog exiled sleepy's graveyard** on turn 35 — the same card that was cut
  from this deck for Grave Pact.

**Viridian Longbow moved twice** — onto Blightwing Bandit, then Hooded Blightfang — and sniped
Akiri Line-Slinger off the board on two separate turns.

### Logged win — 2026-10-28 (7th game), four-player pod, won on own turn 13 (log turn 45), 44m37s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 16-2. **This game is the direct answer to
the owner's rule above: it was won by Stensian Sanguinist, the card this file twice described as
producing nothing.**

**STENSIAN SANGUINIST + WHITE WIDOW = A SELF-GROWING CREATURE. New finding, not previously in this
file.** Stensian's attack trigger can **target itself**, giving itself deathtouch — which then
qualifies it for White Widow, Yelena Belova's *"whenever a creature you control with deathtouch
deals combat damage to a player, put a +1/+1 counter on it."*

It attacked on seven separate turns, targeting itself every time, and grew:

**2/2 -> 3/3 -> 4/4 -> 5/5 -> 6/6 -> 7/7 -> 8/8** — and dealt the killing blow, 8 damage to Brady
Nitnumb.

No equipment, no auras, no tutoring. Two cards that were both already in the deck.

**BOTH EXSANGUINATES WERE CAST. The preparation half finally paid off.** The deck contains exactly
one standalone **Exsanguinate** and one **Stensian Sanguinist // Exsanguinate**. Two Exsanguinates
resolved this game:

- **X=8** on turn 35 — killed **Gabrielle, 5 -> -3**.
- **X=9** on turn 41 — killed **Ethan, 2 -> -7**.

Two resolutions from a deck holding one standalone copy means Stensian's half was cast. Stensian
became prepared on nearly every attack from turn 12 onward. **The preparation mechanic produced a
second Exsanguinate and it killed a player.**

**The Darkness Crystal reanimated two opponents' creatures — first time shown in a log.** Its
replacement exiles opposing nontoken creatures as they die; its {4}{B}{B} ability then puts them
onto sleepy's battlefield with two +1/+1 counters. **Lurrus of the Dream-Den** (turn 28) and
**Bastion Protector** (turn 32) both came back on sleepy's side and attacked for him.

**Disruption played through:** Path to Exile took Tinybones (turn 13) and Virtus (turn 35);
Swords to Plowshares exiled Bloodthirsty Conqueror (turn 30); Merciless Executioner and Accursed
Marauder each forced a sacrifice that took Virtus and Lurrus.

Bloodthirsty Conqueror was on the battlefield for a stretch but no Side A was ever drawn, so
Engine 1 never came online. This was all combat and Exsanguinate.

### Logged win — 2026-10-28 (8th game), four-player pod, won on own turn 11 (log turn 22), 7m18s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 17-2. **Engine 1 killed all three
opponents in a single trigger chain, from a six-land board, with the commander never cast.**

**Virtus the Veiled was never played.** The name does not appear anywhere in this log. The deck
won without its commander.

**Six lands, all game.** Snow-Covered Swamp (t2), Snow-Covered Swamp (t6), Snow-Covered Swamp
(t10), Rogue's Passage (t14), Snow-Covered Swamp (t18), Snow-Covered Swamp (t22) — one per turn
cycle, no Coffers, no Lens, no Crypt Ghast, no Sol Ring. Every spell cast was paid at exactly the
mana available that turn. The curve did the work the ramp usually does.

**The kill — ENGINE 1, Marauding Blight-Priest x Bloodthirsty Conqueror:**

| Own turn | Log turn | Play |
|---|---|---|
| 1 | 2 | Swamp, **Commander's Plate** (it costs **{1}** — the cheap cast, expensive equip) |
| 3 | 6 | Swamp, **Dire Fleet Poisoner** |
| 5 | 10 | Swamp, **Black Widow, Deadly Hunter** |
| 7 | 14 | Rogue's Passage, **Liliana of the Dark Realms**, +1 for a Swamp |
| 9 | 18 | Swamp, **Bloodthirsty Conqueror** (Side B) |
| 11 | 22 | Swamp, **Marauding Blight-Priest** (Side A), **Torment of Hailfire X=1**, alpha strike |

On turn 22 both halves were finally down. Torment X=1 stripped one permanent from each opponent
(Brady's Power Boost, Ethan's **Sol Ring**, Gabrielle's Clue — all three chose to sacrifice rather
than take 3). Then Conqueror (5/5), Black Widow (3/3) and Dire Fleet Poisoner (2/2) all attacked
Brady unblocked for **10**, 33 -> 23.

That 10-point loss was the spark. Conqueror saw it and gained sleepy 10 (43 -> 53), Blight-Priest
saw the lifegain and drained each opponent 1, Conqueror saw each of those three separate losses and
gained again — and the loop never stopped. Deaths in order: **Brady, then Ethan, then Gabrielle.**
sleepy finished at **87 life**.

**Why three opponents makes this loop faster, not just longer:** Blight-Priest drains *each*
opponent, so one iteration produces **three separate life-loss events**, each of which is its own
Conqueror trigger, each of which is its own lifegain, each of which triggers Blight-Priest again.
The chain branches per opponent instead of ticking once. Against a single opponent it is 1 per
iteration; here it was 3, which is why the whole table died inside one combat step.

**Black Widow, Deadly Hunter is why the combo was in hand.** It drew **5 cards** across turns 10,
14 and 18 (one per deathtouch connection, 1 life each), for a total self-inflicted cost of 5 life
that was refunded 50x over. The Conqueror came off the top of a deck being dug through by the
Black Widow triggers.

**Commander's Plate was never equipped** — no commander to equip it to, and {5} for a non-commander
equip was never worth a turn. It cost one mana on turn 1 and sat there. Noting what happened, not a
verdict on the card: the game it is the answer to is the one where Virtus shows up into a board of
white and blue blockers.

**Log-reading note so this doesn't confuse anyone later:** Gabrielle's **"Liliana of the Dark
Realms (342)"** that attacked Ethan is **Sarah Jane Smith wearing Psychic Paper**, which lets its
controller choose a creature card name. sleepy's actual Liliana is card (83) and was killed on
turn 16 by Dauntless Scrapbot + Viconia after going to 4 loyalty.

**sleepy took 1 point of damage from an opponent all game** (Emry, Lurker of the Loch, turn 16).
Brady did essentially nothing — Jessica Jones on turn 15 and a Power Boost. Ethan built a UB
artifact engine (Emry, Etherium Sculptor, Ashnod's Altar, Talisman, Junk Diver) and never pointed
it at sleepy. Gabrielle spent the game hitting Ethan. **Dauntless Scrapbot exiled every opponent's
graveyard on turn 12**, which would have mattered against the Tergrid/Ghostform lines and did not
here.

### Logged win — 2026-10-28 (9th game), four-player pod, won on own turn 19 (log turn 38), 20m10s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 18-2. **The Engine 4 colourless-blocker
caveat was confirmed live in this game — see below. It is no longer theoretical.**

No Engine 1 and no Engine 2 piece was ever drawn. This was **Virtus + Commander's Plate, Vito's
lifelink turn, and a Hooded Blightfang grind**, and all three mattered.

**Build-up:**

| Own turn | Log turn | Play |
|---|---|---|
| 2 | 3 | Swamp, **Commander's Plate** ({1}) |
| 6 | 11 | Swamp, **Grim Tutor** (−3 life) |
| 8 | 15 | Swamp, **Extraplanar Lens**, imprinting a Snow-Covered Swamp |
| 10 | 19 | Swamp, **Qarsi Revenant**, **Ayara, First of Locthwain** |
| 12 | 23 | Swamp, **Virtus the Veiled**, **Plate equipped** (equip commander {3}), **Vito** |
| 14 | 27 | Swamp, Vito's **{3}{B}{B} mass lifelink**, swing |
| 16 | 31 | **Black Widow, Deadly Hunter**, alpha strike — **Brady dies** |
| 17 | 34 | Swamp, swing at Gabrielle, **Nighthawk Scavenger** / Nykthos the turn before |
| 18 | 36 | **Sol Ring**, **Hooded Blightfang**, swing — Virtus dies to a colourless blocker |
| 19 | 38 | Swing — **Hooded Blightfang kills Ethan with 1 combat damage** |

**THE COLOURLESS HOLE IN COMMANDER'S PLATE JUST HAPPENED. Turn 36: Ethan blocked Plate-equipped
Virtus with BLIGHT HERDER — a {5} Eldrazi Processor, 4/5, colours `[]`.** Protection from white,
blue, red and green did nothing. Virtus dealt 4 deathtouch damage and killed it; Blight Herder
dealt 4 back and killed the 1/1 commander. This is the exact failure mode written into the
corrected Engine 4 caveat on 2026-10-28, and this is the first log in which an opponent actually
took the block. **Colourless blockers are not an edge case.**

Before that, the Plate did its job for four turns and three halvings:

- **Turn 27** — Virtus unblocked on Gabrielle for 4, halving **27 -> 13**.
- **Turn 31** — Virtus unblocked on Brady; Vito's drain took him 4 -> 1, then the halving took
  **1 -> 0**. **Virtus killed Brady.**
- **Turn 34** — Virtus unblocked on Gabrielle for 8, halving **4 -> 2**.

**Ethan's own two cards aimed sleepy's commander at Gabrielle and doubled him doing it.**
**Baeloth Barrityl, Entertainer** (2/5) goads every opposing creature with power under 2 — that
is Virtus, Vito and Hooded Blightfang — forcing them to attack and to attack *someone other than
Ethan*. **Death Kiss** then reads *"whenever a creature an opponent controls attacks one of your
opponents, double its power until end of turn."* So on turn 34 Virtus was goaded onto Gabrielle
and swung as an **8/8**. Ethan set up the hit that put her to 2, then killed her himself with
**Fireball X=2** on turn 35. sleepy killed one player directly; the pod did the second.

**Vito's mass-lifelink turn is the play to remember.** Turn 27, {3}{B}{B}: Qarsi Revenant hit Brady
for 3 and Virtus hit Gabrielle for 4, and because Vito reads *"whenever you gain life, target
opponent loses that much life,"* the 7 life gained became **7 more life off Ethan** (33 -> 26) on
top of Virtus halving Gabrielle. One activation, three opponents hit, one combat.

**Hooded Blightfang finished the game by itself.** It attacks alongside deathtouchers and reads
*"whenever a creature you control with deathtouch attacks, each opponent loses 1 life and you gain
1 life"* — note **attacks**, not connects, so blocking does not stop it. Turn 38, four deathtouch
attackers = four triggers, Ethan **5 -> 1** before blockers. Ethan blocked Qarsi, Black Widow and
Nighthawk and left the 1/4 Snake unblocked. **1 combat damage, Ethan 1 -> 0.**

**Snow-Covered Swamps paid for themselves.** Extraplanar Lens imprinted one on turn 15 and no
opponent ran a single snow land — Ethan on Mountains/Forests, Gabrielle on Plains, Brady on
Forest/Mountain/Breeding Pool. The whole table's basics were live for a normal Lens and dead
against this one.

**Natural lifelink carried the life total, not a single drain engine.** Qarsi Revenant, Nighthawk
Scavenger and Gifted Aetherborn all have lifelink printed. sleepy went 40 -> 77 without Exquisite
Blood, Bloodthirsty Conqueror or Aetherflux Reservoir ever appearing.

Tutors used: **Grim Tutor** turn 11, **Diabolic Intent** turn 36 (sacrificing the Gifted Aetherborn
cast the same turn). **Night's Whisper** turn 36 for two more.

### Logged win — 2026-10-28 (10th game), four-player pod, won on own turn 24 (log turn 47), 1h21m09s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 19-2. **Longest game on record**, beating
the 1h08m42s grind. **Three opponents, three completely different kills, in three consecutive own
turns** — and the commander was never cast for the second game running.

| Player | Killed by | Own turn |
|---|---|---|
| **Ethan** | **Exsanguinate X=9** (5 -> −4) | 19 |
| **Gabrielle** | **Aetherflux Reservoir, pay 50** (3 -> −47) | 24 |
| **Brady Nitnumb** | **Seven-creature alpha strike**, 12 damage (2 -> −10) | 24 |

**EREBOS, GOD OF THE DEAD WAS THE WHOLE GAME.** Cast turn 18 and it attacked or drew cards almost
every turn after. Three separate parts of the card mattered:

- **Indestructible.** Gabrielle's **Elspeth, Sun's Champion −3** (destroy all creatures with power
  4 or greater) on turn 43 killed Kodama of the East Tree, Craterhoof Behemoth, Michelangelo and
  **sleepy's own Tergrid** — and did nothing to a 5/7 Erebos. The deck's answer to a wrath was
  already on the battlefield.
- **"Your opponents can't gain life."** Brady tapped **The Great Henge** (*"{T}: Add {G}{G}. You
  gain 2 life"*) on turns 43 and 45 and gained nothing both times.
- **{1}{B}, pay 2 life: draw a card.** Used at least five times, including **three activations in
  a row on the final turn** (81 -> 75) to dig for the Reservoir.

Erebos wore **Basilisk Collar** (deathtouch + lifelink, turn 26) and later **Quietus Spike**
(halving, turn 41). Collar is what turned every connect into 5 life, which is how the life total
got high enough for the Reservoir at all. Spike halved Gabrielle **25 -> 12** on turn 41 through
**Rogue's Passage**, which made the god unblockable for {4}.

**AETHERFLUX RESERVOIR KILLED SOMEONE WITH NO SIDE B ON THE BATTLEFIELD.** No Exquisite Blood, no
Bloodthirsty Conqueror. sleepy was simply at **75 life** from Collar lifelink, Ayara, Blight-Priest
and a 27-point Exsanguinate, cast the Reservoir for {4} and immediately **paid 50 (75 -> 25)** to
kill Gabrielle. The engine-2 combo is the self-refunding version; **this game is the reminder that
the raw mode is live on its own the moment the deck is past 51**, which this deck gets to on
lifelink alone.

**TORMENT OF HAILFIRE X=6, TURN 30 — the biggest single spell in any logged game.** Six iterations
against three opponents. The table paid it off almost entirely in permanents and cards:

- **Gabrielle** lost Felisa, Fang of Silverquill, Aron Benalia's Ruin, Hagra Constrictor and
  Phyrexian Arena, and discarded Evolving Wilds.
- **Ethan** lost Talisman of Hierarchy, a Phyrexian Golem token and **five Treasure tokens**.
- **Brady** lost The Gitrog Ravenous Ride, Bloated Contaminator and Falthis, and discarded Honest
  Rutstein, Beast Whisperer and Nyxbloom Ancient.

**TERGRID MISSED IT BY TWO OWN TURNS.** Hailfire resolved on **turn 30**; Tergrid, God of Fright
was cast on **turn 34**. Every one of those sacrifices and discards above would have been put onto
sleepy's battlefield under Tergrid's trigger. Tergrid then died to Elspeth on turn 43 without ever
triggering. Nothing to fix in the list — this is a **sequencing note**: when both are in hand, the
god comes down first and the Hailfire waits a turn.

**AYARA + MARAUDING BLIGHT-PRIEST IS 2 PER OPPONENT PER BLACK CREATURE.** On the turn-44 rebuild,
four black creatures entered — Nighthawk Scavenger, Marauding Blight-Priest, Dire Fleet Poisoner,
Blood Artist. Each ETB triggers Ayara (*each opponent loses 1, you gain 1*), and that lifegain then
triggers Blight-Priest (*each opponent loses 1*). **Brady went 13 -> 7 and Gabrielle 12 -> 7 in one
main phase**, off creatures that cost five mana in total. Worth remembering as a value line
independent of any combo.

**What the opponents took off sleepy:**

- **Rite of Oblivion** exiled **Vampire Nighthawk** (turn 17) and, on flashback, **Gifted
  Aetherborn** (turn 21). Exile again — the recurring hole.
- **Heritage Reclamation** destroyed **Quietus Spike** (turn 45), after it had already halved
  Gabrielle once.
- **Elspeth** took Tergrid.

**Diabolic Intent's sacrifice handed an opponent a creature.** Turn 10, sleepy sacrificed Gifted
Aetherborn to Diabolic Intent; turn 11, **Brady cast Reanimate on it** and took it off sleepy's
graveyard. Recording the interaction, not arguing the card — Intent tutored what it was cast for
and a reanimator opponent happened to be sitting downstream of the graveyard.

### Logged win — 2026-10-28 (11th game), four-player pod, won on own turn 13 (log turn 25), 10m00s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 20-2. **ENGINE 1 off Exquisite Blood +
Marauding Blight-Priest, and the spark was Hooded Blightfang's attack trigger. That trigger fires
BOTH halves of the engine by itself — see the correction below.**

| Own turn | Log turn | Play |
|---|---|---|
| 1 | 1 | Swamp |
| 3 | 5 | Swamp, **Thornbite Staff** |
| 5 | 9 | Rogue's Passage, **Hooded Blightfang** |
| 7 | 13 | Urborg, **Liliana of the Dark Realms**, +1 for a Swamp |
| 9 | 17 | Swamp, **Tergrid**, Blightfang swings at Gabrielle |
| 11 | 21 | Swamp, **Exquisite Blood** (Side B), Blightfang swings again |
| 13 | 25 | Swamp, **Diabolic Intent**, **Marauding Blight-Priest** (Side A), swing — **loop** |

**The kill.** Both halves were down for the first time on turn 25. Hooded Blightfang attacked Brady
alone, and its trigger — *"whenever a creature you control with deathtouch attacks, each opponent
loses 1 life and you gain 1 life"* — did everything at once: the **1 life gained** triggered
Blight-Priest, and the **1 lost by each of three opponents** triggered Exquisite Blood three times.
From there it never stopped. Deaths in order: **Ethan, Gabrielle, Brady.** sleepy finished at
**76 life** from 36.

**CORRECTION TO THE SPARK LIST ABOVE — Hooded Blightfang belongs in BOTH halves of it, not just
"you gain life."** Its one trigger is simultaneously a lifegain event (fires Side A: Vito, Enduring
Tenacity, Blight-Priest, South Wind Avatar) and a life-loss event on every opponent (fires Side B:
Exquisite Blood, Bloodthirsty Conqueror). **It is the only card in the deck that sparks the engine
from either direction, so it does not care which half you drew.** It also triggers on **declaring
the attack**, not on damage, so no blocker, removal-at-instant-speed-after-blockers or fog stops
it once attackers are declared. The spark list has been amended.

**Three more things this game establishes about Blightfang:** it has now been the finisher
(2026-10-28 9th game, killed Ethan for 1 combat damage), the grind engine (6th game), and the
combo spark (this one). One {2}{B} 1/4.

**Exquisite Blood sat alone for one full turn cycle and did nothing but gain life.** Cast turn 21,
it turned the Blightfang trigger into +3 and the combat damage into +1 — the engine is genuinely
inert without a Side A, exactly as the grid says.

**Tergrid was Chaos Warped one turn after landing.** Cast turn 17, shuffled into the library by
Brady on turn 18. She has now been removed in three consecutive logged games — Elspeth, arriving
after the Hailfire, and now Chaos Warp — without a trigger. Recording what happened; nothing here
argues about the card.

**Thornbite Staff was cast turn 5 and never attached** — no Shaman was cast all game, and the
{2}-to-attach only happens on a Shaman's ETB. Noted for the record.

**Liliana of the Dark Realms got +1 once (fetching a Swamp) and died on turn 16** to Mausoleum
Wanderer and Siren Stormtamer, two 1/1 fliers, from 4 loyalty.

**Diabolic Intent's sacrifice paid for itself this time.** Turn 25, sacrificing **Blood Artist** to
cast it triggered Blood Artist's own death ability (Gabrielle −1, sleepy +1), which Exquisite Blood
then turned into another +1. The tutor cost one card and drained the table on the way out.

**Gabrielle mulliganed to five** on a mono-blue fliers deck and still hit sleepy for 9 on turn 24
with Siren Stormtamer, Ray Fillet and Vulture — the only real damage sleepy took all game.

### LOGGED LOSS #3 — 2026-10-28, four-player pod. Gabrielle won; sleepy died to COMMANDER DAMAGE.

Record 20-3. **A new failure mode. The first two losses were life totals going to zero against mass
exile. This one was 24 commander damage in two swings from a flier, and sleepy got five turns.**

Match ran 2m41s. Gabrielle **mulliganed to five** and still won. sleepy was eliminated on log turn
20 — Gabrielle's fifth turn — at 11 life, with the game-loss flag reading *"accumulation of 21
damage from generals."* Brady Nitnumb went the same way; Ethan was the only player who died to a
life total.

**ISHAI, OJUTAI DRAGONSPEAKER IS THE CARD.** {2}{W}{U}, 1/1, **flying**, *"whenever an opponent
casts a spell, put a +1/+1 counter on Ishai."* In a four-player pod that is three opponents feeding
it. Cast on log turn 12 as a 1/1:

| Log turn | Ishai's power | Event |
|---|---|---|
| 16 | 3 | Attacks sleepy with **double strike** (Bruse Tarl) — **3 + 3 = 6** |
| 20 | 9 | Attacks sleepy with double strike — **9 + 9 = 18**, total **24**, sleepy dead |
| 23 | 11 | Attacks Brady — 11 |
| 26 | 13 | Attacks Brady — 13, total 24, Brady dead |
| 28 | 14 | Attacks Ethan with double strike — 14 + 14, Ethan 27 -> −7 |

**Bruse Tarl, Boorish Herder is the multiplier.** *"Whenever Bruse Tarl enters or attacks, target
creature you control gains double strike and lifelink until end of turn."* It doubled Ishai every
single combat and gained Gabrielle the damage back — she finished on **114 life**. Ishai alone is a
slow clock; Ishai plus a free double-strike grant is a two-turn commander kill.

**sleepy's own spells fed it.** Rancid Rats, Exquisite Blood and Snuff Out each put a counter on
Ishai. There is no way to play around this short of not casting spells.

**RULES NOTE — Kediss's redirect is NOT commander damage.** Kediss, Emberclaw Familiar reads
*"whenever a commander you control deals combat damage to an opponent, it deals that much damage
to each other opponent."* The log labels that as **non-combat damage**, and the 21-damage rule
counts **combat damage only** (CR 903.10a). So Kediss's 13 to Ethan on turn 26 hit his life total
but added nothing to any commander-damage tally. Everything that killed sleepy and Brady was real
combat damage from Ishai.

**WHAT ACTUALLY WENT WRONG — the deck had no answer to a flier, and its one answer got countered.**

sleepy's entire game, five turns:

| Own turn | Log turn | Play |
|---|---|---|
| 1 | 1 | Swamp |
| 2 | 5 | Swamp, **Demonic Tutor** |
| 3 | 9 | Swamp, **Swiftfoot Boots**, **Tinybones, the Pickpocket** |
| 4 | 13 | Swamp, **Rancid Rats**, Boots onto Rancid Rats |
| 5 | 17 | **Cabal Coffers**, **Exquisite Blood**, attack Gabrielle for 2 |

- **Snuff Out was the correct answer and it was countered.** On log turn 20, with Ishai already at
  18 commander damage, sleepy cast Snuff Out on **Bruse Tarl** — paying the alternative cost of 4
  life, which is exactly right, since killing the double-strike granter halves the clock.
  Gabrielle's **An Offer You Can't Refuse** countered it for {U}. That was the game.
- **Nothing on sleepy's board could block a flier.** The board was Tinybones (1/1) and Rancid Rats
  (1/1 with skulk), both ground creatures. The deck's fliers — Nighthawk Scavenger, Qarsi Revenant,
  Vampire Nighthawk, Hooded Blightfang's deathtouch wall — simply were not drawn in five turns.
  **Deathtouch is a blocking deterrent and a flying commander ignores it entirely.** A 1/1 flier
  that grows every time anyone casts anything is the clean counter to a deck whose defence is
  "attacking into me is a bad trade."
- **Exquisite Blood landed with no Side A again** (own turn 5) and gained 2 life before sleepy
  died.

**This loss is not the exile problem.** Nothing of sleepy's was destroyed or exiled all game. The
board was intact at death. The deck lost because **a 24-point evasive clock arrived faster than
five turns of a deck that curves out at three mana**, and the single instant that could have
slowed it was answered by a one-mana counterspell.

### Logged win — 2026-10-28 (12th game), four-player pod, won on log turn 32 (own turn 8), 14m06s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 21-3. **This is the rematch against the
deck that won LOSS #3 — Gabrielle's Ishai / Bruse Tarl / Kediss. All three of her commanders got
exiled in one spell.** Also the first game in which **Aetherflux Reservoir fired twice**.

| Own turn | Log turn | Play |
|---|---|---|
| 3 | 11 | Nykthos, **Vampire Nighthawk** |
| 4 | 15 | Swamp, **Sheoldred, the Apocalypse** |
| 5 | 19 | Swamp, **Nirkana Revenant** |
| 6 | 23 | Night's Whisper, **The Darkness Crystal**, **Virtus**, **Kaya's Ghostform**, **Aetherflux Reservoir** |
| 7 | 27 | Swamp, **Black Widow**, swing (Virtus halves Ethan 24 -> 12), **White Widow** |
| 8 | 31 | **The storm turn** — seven spells, Hailfire X=8, Reservoir for 50 |

**THE STORM TURN, SPELL BY SPELL.** Sheoldred (recast after a Cyclonic Rift), Village Rites, Grim
Tutor, Bubbling Muck, Dark Ritual, Torment of Hailfire, Erebos — seven spells. Aetherflux
Reservoir's *"whenever you cast a spell, you gain 1 life for each spell you've cast this turn"*
paid **1+2+3+4+5+6+7 = 28 life**, taking sleepy from 47 to **98**. Then **pay 50: Brady Nitnumb
30 -> −20**.

**THE MANA — Nirkana Revenant + Bubbling Muck means each Swamp taps for THREE black.** Nirkana
reads *"whenever you tap a Swamp for mana, add an additional {B}"* and Bubbling Muck adds another
{B} on top until end of turn. Two Swamps therefore produced **6**, Dark Ritual added **3**, for 9
available. Torment of Hailfire at X=8 costs {8}{B}{B} = 10 — and **The Darkness Crystal's "black
spells you cast cost {1} less"** brought it to exactly **9**. Three cards lining up to make the X
spell castable to the mana, with nothing spare.

**TORMENT OF HAILFIRE X=8 + THE DARKNESS CRYSTAL IS A ONE-SIDED EXILE WIPE. New interaction, not
previously in this file.** The Crystal reads *"if a nontoken creature an opponent controls would
die, instead exile it and you gain 2 life."* Every creature the table sacrificed to Hailfire was
therefore **exiled instead of dying, and each one gained sleepy 2 life**. Eleven creatures went:

**Ishai, Ojutai Dragonspeaker · Bruse Tarl, Boorish Herder · Kediss, Emberclaw Familiar** ·
Flaming Tyrannosaurus · Leela, Sevateem Warrior · The War Doctor · Kutzil, Malamet Exemplar ·
Araña, Heart of the Spider · The Eleventh Doctor · Drix Fatemaker · Jace, Vryn's Prodigy

That is **22 life gained** on top of the storm count, plus Whirlwind of Thought, Ghostly Prison,
Blackblade Reforged, Swiftfoot Boots, two Signets, Stone of Erech and a Vibranium token to
graveyards, plus five discards. **The deck's answer to the Ishai problem turned out to be the
Hailfire it already runs.**

**Rules caveat on those three commanders:** CR 903.9a lets a commander's owner move it to the
command zone instead of being exiled. Forge left Ishai, Bruse Tarl and Kediss in exile; **in paper
Gabrielle could have put all three back in the command zone and recast them.** The sacrifice to
Hailfire still happens either way, but do not count on exile being permanent against a commander.

**SHEOLDRED WAS THE CLOCK NOBODY BLOCKED.** *"Whenever you draw a card, you gain 2 life. Whenever
an opponent draws a card, they lose 2 life."* With three opponents drawing every turn — and Ethan
looting with Jace, Vryn's Prodigy and The Great Mound on top of that — Sheoldred alone took Ethan
from 39 to 29 and Gabrielle from 36 to 22 **before a single attack**, while paying sleepy 2 life
per draw in the other direction. Black Widow's deathtouch draws each gained 2 as well.

**Cyclonic Rift bounced Sheoldred and it simply came back.** Gabrielle cast it **unoverloaded** on
log turn 30 for a single target. sleepy recast Sheoldred on turn 31 as the first spell of the storm
turn, which also made it storm spell #1. **Bounce is the removal this deck shrugs off** — worth
setting next to the exile problem in the losses section: the same card overloaded, or an exile
effect, is the version that actually costs the deck a game.

**Two Aetherflux activations in one game, which is new.** 98 -> 48 killing Brady on turn 31, then
sleepy climbed back to 53 on Sheoldred draw triggers and deathtouch connects and fired again on
**Gabrielle's turn 32 during her draw step**: 53 -> 3, Gabrielle 5 -> −45. The deck's life total
regenerated 5 points in one round cycle, which was all it needed.

**Kaya's Ghostform went on Virtus on turn 23 and never had to fire** — nobody killed the commander
this game. Virtus connected twice, halving Ethan 24 -> 12 on turn 27 and Gabrielle 11 -> 5 on
turn 31, the second one setting up the lethal Reservoir.

**Brady's Stone of Erech exiled sleepy's White Widow** when she was sacrificed to Village Rites —
*"if a creature an opponent controls would die, exile it instead"* cuts both ways, and it meant no
Blood Artist-style death value and nothing for The Darkness Crystal to reanimate later.

### Logged win — 2026-10-28 (13th game), four-player pod, won on own turn 10 (log turn 38), 10m02s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 22-3. **THORNBITE STAFF FINALLY WENT OFF,
on Virtus, and Extraplanar Lens is what paid for it. Also the biggest single Virtus halving on
record: Gabrielle 76 -> 38.**

**THORNBITE STAFF + VIRTUS + EXTRAPLANAR LENS — the machine gun, with the mana worked out.**

Thornbite Staff grants *"{2}, {T}: this creature deals 1 damage to any target"* **and** *"whenever
a creature dies, untap this creature."* Put it on a deathtouch body and every ping kills, every
kill untaps, so **{T} is never the limit — mana is.** The Lens, imprinted on a Snow-Covered Swamp
on turn 11, makes every Swamp tap for {B}{B}, so:

- **Cast the Staff, {2}** — one Swamp.
- **Equip {4}** — two Swamps. (Virtus is an **Azra Assassin**, not a Shaman, so the free
  attach-on-Shaman-ETB clause did not apply and the full equip was paid.)
- **Each ping, {2}** — **one Swamp, one dead creature.**

It fired on three separate turns and killed **eight creatures** without Virtus ever being blocked
or leaving the board:

| Own turn | Log turn | Pinged to death |
|---|---|---|
| 7 | 27 | Robot Token, Spider-Bot |
| 8 | 31 | Vision Spectral Synthezoid, **Lyra Dawnbringer**, Robot Token |
| 9 | 35 | **Lyra Dawnbringer** (second copy), Diversion Unit, Ellyn Harbreeze |

**Lyra Dawnbringer, a 5/5 flying lifelink first-striker, died twice to one black mana.** This is
the same lock the file already records for Crypt Ghast — *each Swamp taps for {B}{B}, exactly
paying Thornbite's {2}* — and **Extraplanar Lens is now confirmed as the second enabler of it.**

**VIRTUS HALVED 76 TO 38 ON TURN 23 — the largest single halving logged.** Gabrielle was on an
Angel lifegain build (Bishop of Wings, Seraph Sanctuary, Angelic Field Marshal, Lyra, Battle
Angels of Tyr) and had climbed to **80**. One unblocked point of damage from a 1/1 took half of it.
**Virtus gets better against lifegain, not worse** — the halving scales off their total, so every
point they gain is a point he takes back on the next connect. He halved four times this game:
76 -> 38, 34 -> 17, 10 -> 5, and Ethan 9 -> 4.

**WHITE WIDOW TURNED THE WHOLE TEAM INTO A CLOCK.** *"Whenever a creature you control with
deathtouch deals combat damage to a player, put a +1/+1 counter on it"* — permanent growth on
every connect, across every deathtoucher at once. Hooded Blightfang went **1 -> 2 -> 3 -> 4**
damage over four swings and Virtus **1 -> 2 -> 3 -> 4**. The final alpha strike was 4+4+3+5 = **16**
from creatures that cost nine mana in total.

**Hooded Blightfang's attack trigger ran every combat from turn 20 on** — four swings, each
draining all three opponents 1 and gaining 1. That is where most of Brady's life went while sleepy
was busy with the other two.

**Torment of Hailfire X=8 on turn 23** — the second X=8 in two games. It took Chronicle of Victory,
Memory Guardian, Ellyn Harbreeze, Henchbots, Mechanized Production, Angelic Field Marshal, Big
Mother Mouser, Stridehangar Automaton, **Lyra Dawnbringer**, Automated Artificer, Clan Crafter,
Battle Angels of Tyr, Falcon's Wing Harness, Swiftfoot Boots, Bishop of Wings, Clockwork Droid and
**Sol Ring**, plus six discards. **The Darkness Crystal was not out this time**, so these went to
graveyards rather than exile — the difference between this Hailfire and the previous game's.

**GRAY MERCHANT FOR 9 KILLED ETHAN AND GAINED 18.** Devotion to black was **9** on turn 38. Each
opponent lost 9 (Ethan 3 -> −6, Brady 16 -> 7) and sleepy gained **the total life lost, not X** —
two living opponents, so **+18** (38 -> 56). Worth stating plainly: Gary's lifegain multiplies by
the number of opponents still alive, so casting it *before* the table thins out is worth more.

**Phyrexian Arena ran from turn 15 to the end** — an extra card every upkeep for 1 life, six
draws across the game, in a deck that wants to hit land drops and keeps gaining the life back.

Deaths in order: **Gabrielle** on turn 35 (Erebos, 2 -> −3), **Ethan** on turn 38 (Gray Merchant,
3 -> −6), **Brady** on turn 38 (alpha strike, 4 -> −12).

### Logged win — 2026-10-29, four-player pod, won on log turn 24 (sleepy's 7th turn), 3m29s

sleepy 1 — Brady Nitnumb 0, Ethan 0, Gabrielle 0. Record 23-3. **sleepy never attacked once. Zero
combat damage dealt all game.** Engine 1 off **Exquisite Blood + Marauding Blight-Priest**, and
**the spark was an opponent's own card, on an opponent's turn, pointed at a third opponent.**

sleepy's entire game, seven turns, seven spells:

| Own turn | Log turn | Play |
|---|---|---|
| 1–3 | 1, 5, 9 | Swamp, Swamp, Swamp |
| 4 | 13 | Swamp, **South Wind Avatar** — Chaos Warped away the next turn |
| 5 | 17 | Swamp, **Night's Whisper**, **Demonic Tutor** |
| 6 | 20 | Swamp, **Marauding Blight-Priest** (Side A), **Snuff Out** on Wingnut, **Virtus** |
| 7 | 23 | Swamp, **Exquisite Blood** (Side B) |

**BRADY BUILT THE IGNITION INTO HIS OWN BOARD.** On log turn 24, Brady's upkeep, his **Scrawling
Crawler** triggered: *"At the beginning of your upkeep, each player draws a card. Whenever an
opponent draws a card, that player loses 1 life."* Gabrielle drew, Gabrielle lost 1 — and that is
an opponent of sleepy's losing life, so **Exquisite Blood** gained sleepy 1, which **Marauding
Blight-Priest** turned into 1 off each opponent, which Exquisite Blood saw again. The loop never
stopped. Brady 30 -> 0, Gabrielle 31 -> 0, sleepy 22 -> 52.

**Brady then accelerated it.** Mid-loop he sacrificed two Goblins to **Siege-Gang Lieutenant**,
pinging Gabrielle for 1 each time — two more life-loss events, two more Exquisite Blood triggers,
two more Blight-Priest rounds. He was feeding the engine that was killing him.

**This is the third logged win where the spark came from outside the deck**, and the cleanest
example yet: a symmetrical draw-and-drain artifact, firing on its controller's own upkeep, aimed
at someone else entirely. The spark list above is what the deck brings; **the table usually brings
one too.**

**Brady killed Ethan, not sleepy.** A Goblin swarm with **Legion Warboss**, **Wingnut, Bat on the
Belfry** (+1/+0 to every other attacker) and **Combat Celebrant** (untap all other creatures,
extra combat phase) hit Ethan for 21 across two combats on log turn 18: **28 -> 7 -> −14**. The
pod did a third of the work again.

**Two one-mana answers cost sleepy two permanents:**

- **Chaos Warp** (Gabrielle, log turn 14) shuffled away **South Wind Avatar** the turn after it
  landed. That is a Side A card — the loop would have been live four turns earlier with it.
  Chaos Warp has now taken a key permanent in two consecutive games (Tergrid, then this).
- **Siege-Gang Lieutenant's {2}, sacrifice a Goblin: 1 damage** killed **Virtus** on log turn 21.
  A 1/1 commander dies to any ping at all, and a Goblin deck has an unlimited supply of them.

**Snuff Out resolved this time**, paying 4 life (28 -> 24) to destroy Wingnut, Bat on the Belfry —
worth setting against LOSS #3, where the same card on the same kind of target was countered by An
Offer You Can't Refuse. Same card, same read, different result.

**3m29s is the fastest match clock logged.** The previous shortest was 4m40s.

### Logged win — 2026-10-29 (2nd game), four-player pod, won on own turn 7 (log turn 25), 5m14s

sleepy 1 — Lacspor 0, Iona 0, Feturn 0. Record 24-3. **A new pod — Lacspor on mono-red Goblins,
Iona on mono-blue, Feturn on white weenies.** Engine 1 off **Exquisite Blood + Vito, Thorn of the
Dusk Rose**, sparked by **Ayara** off Sidisi entering. **sleepy declared no attackers all game, for
the second game running, and finished on 143 life — the highest total in any log.**

| Own turn | Log turn | Play |
|---|---|---|
| 1 | 1 | Swamp, **Foulmire Knight** — Swords to Plowshares'd on turn 4 |
| 2 | 5 | Swamp |
| 3 | 9 | Swamp, **Ayara, First of Locthwain** — Cyclonic Rifted on turn 11 |
| 4 | 13 | Swamp, **Liliana of the Dark Realms**, +1 for a Swamp — killed on turn 14 |
| 5 | 17 | Swamp, **Ayara recast** |
| 6 | 21 | Swamp, **Hooded Blightfang**, **Vito** (Side A) |
| 7 | 25 | Cabal Coffers, **Exquisite Blood** (Side B), **Sidisi, Undead Vizier** — **loop** |

**The spark was Ayara off a creature ETB.** Sidisi entered, Ayara fired (*each opponent loses 1,
you gain 1*), Vito saw the lifegain and drained a target opponent, Exquisite Blood saw the loss and
gained it back, and round it went. **Ayara is a one-card spark in this deck specifically because
every creature in the 99 is black** — any creature you cast is the ignition.

**VITO'S LOOP KILLS SEQUENTIALLY; BLIGHT-PRIEST'S KILLS IN PARALLEL. Worth knowing which Side A
you have.** Vito reads *"whenever you gain life, **target** opponent loses that much life"* — one
player per iteration — so the loop emptied **Iona** first (35 -> 0), then **Feturn** (29 -> 0),
then **Lacspor** (35 -> 0), in that order. Marauding Blight-Priest hits *each* opponent per
iteration and takes the whole table down together. Both are lethal and neither can be responded to
once it starts, but against a pod the Blight-Priest version is faster in real time, and Vito's
version walks the table one seat at a time.

**sleepy ended on 143 life.** Previous high in this file was 98. Nothing was spent on it — no
Aetherflux, no Exsanguinate, just the loop running past lethal.

**Three answers were used on sleepy and only one stuck:**

- **Swords to Plowshares** (Feturn, turn 4) exiled **Foulmire Knight**. Exile again — the only
  permanent answer anyone found, and it was spent on a one-drop.
- **Cyclonic Rift** (Iona, turn 11) bounced **Ayara**, **unoverloaded**, for a single target. She
  was recast on turn 17 and went on to spark the kill. **That is the third logged game where an
  unoverloaded Rift cost the deck nothing** (Sheoldred in the 12th game, Ayara here) — bounce is
  the removal this deck shrugs off, and the overloaded version is a different card entirely.
- **Lacspor's Goblins** killed **Liliana of the Dark Realms** on turn 14 after one +1 activation.

**Mystic Remora taxed sleepy all game and changed nothing.** Iona cast it turn 8 and paid
cumulative upkeep for six turns; it triggered on Liliana, Exquisite Blood and every opponent's
noncreature spell. The deck's threats are creatures, so the Remora largely taxed the rest of the
table on sleepy's behalf.

**Sidisi's exploit was not used** — she entered, nothing was sacrificed, and the search never
happened. She was cast as a five-mana black creature to trigger Ayara, and that was enough.

### Logged win — 2026-10-29 (3rd game), four-player pod, won on own turn 11 (log turn 40), 13m36s

sleepy 1 — Alicia 0, Eli 0, Picumar 0. Record 25-3. Another new pod — **Alicia** on R/G Impact
Tremors stompy, **Eli** on U/R artifacts, **Picumar** on W/B equipment. Engine 1 off **South Wind
Avatar × Exquisite Blood**, and **the spark was Crypt Ghast's extort.**

**CRYPT GHAST'S EXTORT IS A DOUBLE-SIDED SPARK, like Hooded Blightfang.** *"Whenever you cast a
spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life."* One
trigger, two events: the **gain** fires Side A, the **loss on every opponent** fires Side B. It
also triggers on **every spell**, not just creatures, so with the Ghast out the deck is holding
the ignition in hand at all times. The spark list has been amended to carry it in both halves.

On the final turn sleepy cast five spells — Erebos, Demonic Tutor, Culling the Weak, Exquisite
Blood, and the extort payments on each — and once Exquisite Blood resolved, the next extort was
the loop: extort gained 2 → South Wind Avatar drained each opponent 1 → Exquisite Blood gained it
back → South Wind Avatar again. **Picumar died first, then Eli.** sleepy finished at **67**.

**COMMANDER'S PLATE WAS DESTROYED — the first time anyone has answered it.** Equipped to Virtus on
turn 15; **Untimely Malfunction** (Alicia, {1}{R} instant, "destroy target artifact") killed it on
turn 16. One turn of protection. Engine 4 has now been beaten two different ways in the logs: a
colourless blocker (9th game, 2026-10-28) and plain artifact removal.

**Virtus still did the work without it.** He connected on turn 19 and halved **Alicia 38 → 19**,
then again on turn 27 for **14 → 6**. He died twice to chump blocks — **Darkstar** (turn 31) and
**Chrome Dome** (turn 37) — because a 1/1 with no Plate trades with anything. Recast once in
between. Two halvings off two connects is the whole card; the body is irrelevant.

**South Wind Avatar did both of its jobs.** It is Side A (*whenever you gain life, each opponent
loses 1*) **and** a lifegain source (*whenever another creature you control dies, you gain life
equal to its toughness*), so every chump-blocked Virtus and every lifelink connection off Vampire
Nighthawk and Vampire of the Dire Moon fed it. Before the loop even started it was draining the
table 1–2 per combat.

**Three permanents taken off sleepy, all by different answers:**

- **Untimely Malfunction** → Commander's Plate (turn 16).
- **Henchbots** → **Tinybones** exiled on ETB, "until this creature leaves the battlefield"
  (turn 25). Not permanent, but it never came back.
- **Chaos Warp** → **Qarsi Revenant** shuffled away (turn 28). **That is Chaos Warp taking a
  permanent in three consecutive logged games** — Tergrid, then South Wind Avatar, now Qarsi.

**Picumar killed Alicia**, not sleepy — Kingpin, Cloud and Hardened Tactician swung her out at
4 → −1 on turn 31, right after she had landed a 10/10 Primeval Protector. **Fourth logged game
where an opponent removed an opponent for us.**

**Alicia's Impact Tremors pinged sleepy twice** for 1 each as she built her board. In a deck that
gains life every combat it never mattered, but it is the kind of card that would matter against
the Aetherflux plan, where every point below 51 is a turn of delay.

### Logged win — 2026-10-29 (4th game), four-player pod, won on own turn 7 (log turn 27), 14m28s

sleepy 1 — Alicia 0, Eli 0, Picumar 0. Record 26-3. Same three names as the previous game but
**three different decks** — Alicia on **W/B infect/toxic**, Eli on W/G Sidar Kondo + Keleth horses,
Picumar on Bant legends. Engine 1 off **Vito × Exquisite Blood**, sparked by a lifelink connection.
sleepy peaked at **120**.

**THE VITO LOOP TICKS AT WHATEVER SIZE THE SPARK WAS. New mechanical note.** Gifted Aetherborn
connected for **2** with lifelink. Vito reads *"whenever you gain life, target opponent loses
**that much** life"* and Exquisite Blood reads *"whenever an opponent loses life, you gain **that
much** life"* — both preserve the amount, so the loop ran at **2 per iteration**, not 1. Alicia
26 → 0, Eli 24 → 0, Picumar 32 → 0, all in twos.

That is twice the speed of the Marauding Blight-Priest version, which is locked to 1 per iteration
by its own text. **Spark the Vito loop with the biggest lifegain event available** — a lifelink
hit from a 2- or 3-power creature, an Exsanguinate, a Gray Merchant — and it resolves in half the
iterations. It does not grow, but it never shrinks below the spark either.

**ALICIA WAS ON INFECT, AND THE DECK'S ENTIRE DEFENCE DOES NOTHING ABOUT POISON.** sleepy finished
the game on **three poison counters** while at 120 life:

- **Infectious Inquiry** (turn 17) — each opponent gets a poison counter.
- **Blightbelly Rat** dying (turn 22) — proliferate, a second counter.
- **Norn's Decree** (turn 27) — *"whenever one or more creatures an opponent controls deal combat
  damage to you, that opponent gets a poison counter."* **Attacking Alicia is what gave sleepy
  the third one.**

Three is a long way from ten and this game was never in danger. Recording it because it is a
threat axis nothing in the deck touches: **no amount of lifegain, no Exquisite Blood, no
Aetherflux buffer interacts with poison at all**, and Norn's Decree specifically punishes the one
thing this deck does every turn. A faster toxic draw is worth watching for.

**DUSK KILLED WHITE WIDOW — and the deck's small bodies are normally the reason it survives
sweepers.** Eli cast **Dusk** (*destroy all creatures with power 3 or greater*) on turn 13. It hit
exactly one of sleepy's creatures, and only because she had been **pumped to 4/5**: a symmetric
"each player may put two +1/+1 counters on a creature they control" trigger from Picumar's board
had let sleepy grow her, then her own connect added a third counter.

**Power-based and toughness-based sweepers cut in opposite directions for this deck.** Dusk,
Elspeth's −3 and Mass Calcify-style effects mostly miss a board of 1/1s and 2/3s. Elesh Norn,
Grand Cenobite's **−2/−2** (LOSS #2) kills nearly all of it on sight. The deck's low curve is
simultaneously its best sweeper protection and its worst.

**ELESH NORN, MOTHER OF MACHINES LANDED ONE TURN BEFORE THE KILL.** Picumar cast her on turn 26:
*"Permanents entering don't cause abilities of permanents your opponents control to trigger."*
That **switches off Ayara, Gray Merchant of Asphodel, Blood Artist's ETB value and every
enters-the-battlefield drain in the deck.** It did not matter here because the spark was combat
damage, not an ETB — but **the Ayara and Gary lines would have been dead on the spot.** Worth
knowing by name: this is the one white Praetor that beats the deck's ETB engines without removing
a single permanent.

**Picumar was running Quietus Spike** (turn 15) — the deck's own Virtus-halving equipment, pointed
the other way. It never connected.

**Log-reading note:** the trigger the log attributes to Picumar's "The Eleventh Doctor (504)" —
*"each player may put two +1/+1 counters on a creature they control"* — is not the text on the
card of that name in `scryfall.db`, which is the {1}{W}{U} Time Lord with "I. AM. TALKING!" The
same text appears on Picumar's **Leela, Sevateem Warrior** in the same log, so Forge appears to be
rendering one ability under two names. The counters themselves certainly happened.

### Logged win — 2026-10-29 (5th game), four-player pod, won on own turn 8 (log turn 33), 10m57s

sleepy 1 — Alicia 0, Eli 0, Picumar 0. Record 27-3. Alicia/Eli/Picumar again on a **third set of
decks** — Alicia on R/W Bloomburrow mice, Eli on R/W tokens, Picumar on white legends. Engine 1
with **two Side A cards and Bloodthirsty Conqueror**, and **the spark was an opponent's
Vandalblast — the same spell that destroyed the card doing the sparking.**

**THE KILL, EXACTLY.** On log turn 33 Eli cast **Vandalblast overloaded** — *destroy each artifact
you don't control*. That simultaneously destroyed sleepy's **The Darkness Crystal** and **Sol
Ring**, and Picumar's **Adaptive Automaton**, which is an **artifact creature**. The Crystal's
replacement effect — *"if a nontoken creature an opponent controls would die, instead exile it and
you gain 2 life"* — still applied to the Automaton, because a replacement effect is locked in as
the event happens and the Crystal was still on the battlefield at that moment. **It exiled the
Automaton and gained sleepy 2 life on its own way to the graveyard**, and that lifegain was the
spark:

**+2 life → Marauding Blight-Priest** (each opponent loses 1) **and Vito** (target opponent loses
2) **→ Bloodthirsty Conqueror** (gain that much) **→ round again.** Eli died first, then Alicia,
then Picumar. sleepy finished at **84**.

**THE DARKNESS CRYSTAL IS A PASSIVE SPARK GENERATOR, AND IT FIRES ON OTHER PEOPLE'S COMBAT.** This
is the part worth keeping. The Crystal turns **every opponent's nontoken creature death** into a
2-life gain for sleepy — not just creatures sleepy kills. It fired three times this game:

| Log turn | What died | How |
|---|---|---|
| 23 | **Valley Questcaller** | Blocked sleepy's Dire Fleet Poisoner |
| 30 | **Aurora Champion** | Died in **Picumar's attack on Eli** — nothing to do with sleepy |
| 33 | **Adaptive Automaton** | Killed by **Eli's own Vandalblast** |

Two of those three were events sleepy had no part in. With a Side A and a Side B down, **the
Crystal means any creature dying anywhere at the table starts the loop.** It belongs in the spark
list not as a card that gains life but as one that converts the whole table's combat into sparks.

**TWO SIDE A CARDS AT ONCE — second logged instance.** Marauding Blight-Priest (turn 19) and Vito
(turn 27) were both out when Bloodthirsty Conqueror finally landed on turn 31, so every iteration
took **1 off each opponent plus 1 more off whoever Vito targeted**. The grid's note that stacked
Side A makes the loop faster rather than redundant now has a second game behind it.

**Side A was down twelve log turns before Side B.** Blight-Priest on turn 19, Conqueror on turn
31. For six of sleepy's own turns the deck was holding half an engine and doing almost nothing
with it — two Dire Fleet Poisoner attacks is the entire combat record of the game. **That is the
normal shape of these wins and it is why the deck does not need to race.**

**Deserted Temple untapped Cabal Coffers for a double activation on turn 31** — *"{1}, {T}: untap
target land"* on *"{2}, {T}: add {B} for each Swamp you control."* That one land is what paid for
Bloodthirsty Conqueror (5) and Virtus (3) in the same turn, and it is the turn the game was won on.

**What the table took off sleepy:** **Stroke of Midnight** killed Blightwing Bandit (turn 30);
**Vandalblast** took The Darkness Crystal and Sol Ring (turn 33) — and cost Eli the game doing it.
Nobody touched Marauding Blight-Priest, Vito or the Conqueror.

**Swords to Plowshares and Path to Exile were both cast this game and neither was aimed at sleepy**
— Eli and Alicia each spent one on Picumar's Suki, Kyoshi Captain. The deck's creatures are
individually unthreatening enough that premium white removal went elsewhere.

### LOGGED LOSS #4 — 2026-10-29, four-player pod. Picumar won; sleepy died at −45 to a flying alpha strike.

Record 27-4. 1h04m32s. **The first loss in which the deck's engine was taken apart piece by piece
rather than simply outpaced — six separate answers, including two counterspells — and the first
loss with a kill of its own on the board (Exsanguinate took Eli out).**

**SIX ANSWERS, AND THEY HIT EVERY RELEVANT CARD:**

| Own turn | Log turn | Answer | What it took |
|---|---|---|---|
| 2 | 7 | **Wear** (Alicia) | **Viridian Longbow** — Engine 3, gone the turn after it landed |
| 3 | 10 | **Path to Exile** (Eli) | **Marauding Blight-Priest** — **Side A, exiled on the turn it was cast** |
| 4 | 15 | **Vandalblast** (Alicia) | **Extraplanar Lens** |
| 5 | 19 | **Chaos Warp** (Alicia) | **Nighthawk Scavenger** |
| 6 | 22 | **Counterspell** (Picumar) | **Bloodthirsty Conqueror — Side B, countered on the stack** |
| 9 | 33 | **Negate** (Picumar) | **Snuff Out**, aimed at Windreader Sphinx |

**Engine 1 never had both halves on the battlefield at any point in the game.** Side A was exiled
on turn 10; Side B was countered on turn 22. That is the whole story of the loss in two lines.

**SNUFF OUT HAS NOW BEEN COUNTERED IN TWO OF THE FOUR LOSSES** — An Offer You Can't Refuse in
LOSS #3, Negate here. It is the deck's only instant-speed removal and it is a **noncreature
spell**, which is precisely what cheap blue counterspells are held for. Both times it was pointed
at the card that went on to kill sleepy.

**HOW PICUMAR ACTUALLY KILLED HIM — 92 damage in one combat.** Mono-W/U fliers, stacked three
deep:

- **True Conviction** — *creatures you control have double strike and lifelink.*
- **Akroma, Vision of Ixidor** — *at the beginning of each combat, each other creature you control
  gets +1/+1 for each of flying, first strike, double strike, lifelink, vigilance…* On a board
  where everything flies and everything has double strike and lifelink from True Conviction, that
  is **+3/+3 or more to the whole team, every combat**.
- **Kangee, Sky Warden** — *whenever Kangee attacks, attacking creatures with flying get +2/+0.*

Six fliers attacked on log turn 42. First-strike damage was **13 + 9 + 8 + 8 + 8 = 46**, taking
sleepy 47 → 1. Then the same creatures dealt it **again** in the regular damage step: 1 → **−45**.
Picumar gained all of it twice over and finished on **218 life**, from 40.

**This is LOSS #3's failure mode with more copies of it.** Loss #3 was one evasive flier
(Ishai) killing sleepy with commander damage. This is six, with double strike. **The deck has no
answer to a wide flying board**: deathtouch deters blocks, not attacks; the only fliers in the 99
are Nighthawk Scavenger, Qarsi Revenant, Vampire Nighthawk and Hooded Blightfang's reach-less
wall, and two of those were answered.

**BAELOTH BARRITYL GOADED THE DECK'S UTILITY CREATURES INTO DYING.** Alicia's Baeloth goads every
opposing creature with power under 2 — which in this deck is most of the board. **Vito (1/3) was
goaded into attacking Eli on turn 30 and died to a Kasla block. Blood Artist (0/1) was goaded on
turn 34 and died to a Thopter block.** Goad is a hard counter to a deck built out of small
creatures that want to sit still and drain: it does not kill them, it makes sleepy kill them.
Add **Ghostly Prison** (turn 16) taxing the attacks sleepy actually wanted to make, and the deck
was being pushed into bad combat from both directions at once.

**What did work:** **Exsanguinate X=6** on turn 38 killed Eli (6 → 0) and took sleepy 29 → 47,
which is the only reason he survived turn 40 at all. **Blood Artist** drained Eli for 1 six
separate times off other players' creatures dying — a reminder that it works off the whole
table's combat, not just sleepy's.

**What this loss adds to the pattern.** The three earlier losses were about effects the deck
cannot rebuild through (exile sweepers) or cannot race (an evasive clock). This one is about
**being answered on the stack and at sorcery speed, repeatedly, by three players at once**. The
deck's engines are two- and three-card assemblies with no protection — no counterspell backup, no
hexproof, nothing that makes Side A or Side B resilient. Against one opponent holding up blue
mana, the Conqueror simply does not resolve.

### Logged win — 2026-10-29 (6th game), four-player pod, won on own turn 7 (log turn 27), 6m50s

sleepy 1 — Alicia 0, Eli 0, Picumar 0. Record 28-4. **Immediate rematch after LOSS #4, same three
opponents, and the answer was the fastest loop the deck has produced.** Engine 1 off **Enduring
Tenacity × Bloodthirsty Conqueror**, **ticking at 5 per iteration**.

**FIRST LOGGED GAME WHERE ENDURING TENACITY IS THE CARD THAT CLOSES.** It has been on the
battlefield in earlier games (and was destroyed by Loran in the 16th) but had never been the Side
A that ended one. Both halves were cast on the **same turn** — Bloodthirsty Conqueror for 4, then
Enduring Tenacity for 3, seven mana off seven Swamps — and then Erebos attacked.

**WITH BLOODTHIRSTY CONQUEROR AS SIDE B, ANY DAMAGE YOU DEAL SETS THE LOOP'S TICK RATE.** This is
the sharp version of the note from the 26th game. The chain was:

1. **Erebos connects for 5.** Picumar 20 → 15.
2. **Conqueror** — *whenever an opponent loses life, you gain that much life* — gains sleepy **5**.
3. **Enduring Tenacity** — *whenever you gain life, target opponent loses **that much** life* —
   takes **5** off Picumar.
4. Conqueror sees it, gains **5**. Back to step 3.

Both halves preserve the amount, so **the loop runs at whatever the first hit was**. Five is the
highest tick rate logged; the Vito version in the 26th game ran at 2 off a Gifted Aetherborn
connection, and Marauding Blight-Priest is permanently locked to 1. **Pair Vito or Tenacity with
the Conqueror and the correct spark is the biggest single hit available** — Erebos at 5/7 is the
best body in the deck for it. Picumar fell from 15 in three iterations, Alicia from 30 in six.
sleepy finished on **85**.

**sleepy attacked exactly once all game** — the Erebos swing that started the loop.

**THE DARKNESS CRYSTAL GAINED 6 LIFE OFF THREE DEATHS, TWO OF WHICH WERE OTHER PLAYERS' REMOVAL.**
Second game running that confirms it as a table-wide passive engine:

| Log turn | Creature exiled | Killed by |
|---|---|---|
| 20 | **Yoshimaru, Ever Faithful** | sleepy's own Snuff Out |
| 23 | **Cid, Freeflier Pilot** | **Eli's** Hell to Pay, aimed at Picumar |
| 25 | **Esper Sentinel** | **Alicia's** V.A.T.S., aimed at Picumar |

**PICUMAR KILLED ELI WITH 21 COMMANDER DAMAGE** — Ardenn, Intrepid Archaeologist loaded with
Wrecking Ball Arm, Mithril Coat and Bitterthorn, connecting for 7 on three consecutive turns
(log 16, 20, 24). **Fifth logged game where an opponent removed an opponent**, and the second time
commander damage has decided a seat — the first was against sleepy in LOSS #3.

**V.A.T.S. killed Virtus, and it is a card to know.** {2}{B}{B} instant, **split second**, *choose
any number of target creatures with equal toughness, destroy them.* Split second means no response
is possible at all — not Snuff Out, not anything. It took Virtus (1/1) alongside Picumar's Esper
Sentinel on turn 25. A 1/1 commander shares toughness with half of every board in the format, so
this is a clean one-card answer to Virtus that cannot be interacted with.

**Esper Sentinel taxed sleepy all game** — *whenever an opponent casts their first noncreature
spell each turn, draw a card unless that player pays {X}*. It triggered on The Darkness Crystal,
Liliana and Snuff Out, and Picumar drew off each. The deck casts a noncreature spell most turns,
so the Sentinel was effectively a Phyrexian Arena pointed at sleepy specifically. It died to
Alicia's V.A.T.S., not to anything sleepy did.

**Snuff Out resolved this time**, paying 4 life to kill Yoshimaru on turn 20 — set against the two
losses where it was countered (An Offer You Can't Refuse, Negate). Three of the four most recent
castings have now resolved; the two that did not both cost the deck a game.

**Liliana of the Dark Realms got one +1 activation and died on turn 21** to Caesar and Paladin
Elizabeth Taggerdy. That is now three consecutive games in which Liliana has fetched exactly one
Swamp and then been attacked off the board.

### Grave Pact — running record (added 2026-10-27)

Added 2026-10-26, cutting Bojuka Bog, on the argument that 21 deathtouchers trading constantly plus
Tergrid / Ayara / Skullclamp would make it fire often. Tracking it honestly:

| Game | Drawn? | Triggers | Notes |
|---|---|---|---|
| 2026-10-26 (3rd) | Cast turn 19 | **1** (turn 29) | Dire Fleet Poisoner died blocking; all three opponents sacrificed a **token**. Tergrid was not out, so nothing was stolen. |
| 2026-10-26 (4th) | Not drawn | — | |
| 2026-10-27 | Cast turn 39 | **1** (turn 39) | Fired the same turn, on the Black Widow trade that sparked the kill — an edict on all three at the moment the loop went off. |
| 2026-10-27 (2nd) | Not drawn | — | |
| 2026-10-27 (3rd) | Not drawn | — | |
| 2026-10-27 (4th) | Not drawn | — | |
| 2026-10-28 (1st) | Not drawn | — | |
| 2026-10-28 (2nd) | Not drawn | — | |
| 2026-10-28 (3rd) | Not drawn | — | |
| 2026-10-28 (loss) | Not drawn | — | |
| 2026-10-28 (4th) | Cast turn 22 | **1** (turn 33) | Virtus died blocking; all three opponents sacrificed a creature, at the moment the drain engine came online. |
| 2026-10-28 (loss 2) | Not drawn | — | |
| 2026-10-28 (5th) | Cast turn 21 | **0** | Nothing of sleepy's died after it resolved. |
| 2026-10-28 (6th) | Not drawn | — | |
| 2026-10-28 (7th) | Not drawn | — | |
| 2026-10-28 (8th) | Not drawn | — | |
| 2026-10-28 (9th) | Not drawn | — | |
| 2026-10-28 (10th) | Not drawn | — | |
| 2026-10-28 (11th) | Not drawn | — | |
| 2026-10-28 (loss 3) | Not drawn | — | |
| 2026-10-28 (12th) | Not drawn | — | |
| 2026-10-28 (13th) | Not drawn | — | |
| 2026-10-29 | Not drawn | — | |
| 2026-10-29 (2nd) | Not drawn | — | |
| 2026-10-29 (3rd) | Not drawn | — | |
| 2026-10-29 (4th) | Not drawn | — | |
| 2026-10-29 (5th) | Not drawn | — | |
| 2026-10-29 (loss 4) | Not drawn | — | |
| 2026-10-29 (6th) | Not drawn | — | |

**This table covers LOGGED games only, which are a subset of the games actually played.** The owner
pastes some match logs into these sessions and not others, so a blank row means "not in a log I
saw", not "did not happen".

**Owner's correction, 2026-10-27: Grave Pact has been used and has performed in games not captured
here.** An earlier version of this section read the logged sample as evidence the card was
underperforming and said it "has not yet been the reason a game was won." That conclusion was drawn
from a biased sample and is withdrawn. The per-game rows below are still accurate as far as they
go; they just do not support a verdict either way.

## Swaps from collection, 2026-09-30

Four one-for-one swaps, matched on mana value, all from cards the owner already had in hand — no
purchases. **The deck's engine is lifegain, not just deathtouch:** Hooded Blightfang gains 1 life per
deathtouch attacker, Vito turns lifegain into an opponent losing that much, and Marauding
Blight-Priest adds 1 to each opponent on top. Cards that gain life are damage multipliers here.

| In | Out | |
|---|---|---|
| **Arnyn, Deathbloom Botanist** {2}{B} 2/2 | Blightwing Bandit {3}{B} 2/2 | Engine with 11 live targets, for a 2/2 whose rider rarely turns on |
| **Burrog Banemaker** {B} 1/1 | Pharika's Chosen {B} 1/1 | Same body plus `{1}{B}: +1/+1`, so not a dead late topdeck |
| **Ravening Warg** {1}{B} 2/2 | Typhoid Rats {B} 1/1 | Bigger body, gains 2 on attack — and lifegain is damage here |
| **Witch of the Moors** {3}{B}{B} 4/4 | Dire Fleet Ravager {3}{B}{B} 4/4 | Repeating edict on the whole table |

### Two cuts I got wrong first, corrected the same day

**Black Widow, Deadly Hunter was almost cut for Arnyn. That was a mistake.** Black Widow draws a card
whenever a deathtoucher connects, and **Sheoldred is in this deck** — so the draw gains 2 life, which
Vito converts to 2 loss and Blight-Priest to 1 more per opponent. **It feeds the same lifegain engine
that justified Arnyn, and draws a card on top.** It is also a 3/3 to Arnyn's 2/2, and its trigger
matches how the deck already plays: Hooded Blightfang rewards attacking with deathtouchers, so you
are attacking regardless. With only **6 card-draw sources** in the deck, draw is the scarce resource,
not damage. **Blightwing Bandit** was the right cut instead — its rider needs a first spell cast on
an opponent's turn, and of the deck's 8 instants three are rituals you would never hold up.

**Rancid Rats was almost cut for Ravening Warg. Also wrong.** Rancid Rats has **skulk**, so only 0/X
and 1/X creatures can block it — it connects nearly every swing, which is a reliable Hooded
Blightfang drain and a Black Widow draw. The vanilla 1/1 deathtouchers have no such upside, so
**Typhoid Rats** went instead. Hired Poisoner is the identical remaining vanilla body if another
1-drop ever needs to go.

**Arnyn is an engine, not a body.** *"Whenever a creature you control with power or toughness 1 or
less dies, target opponent loses 2 and you gain 2."* **Eleven creatures in the deck qualify** —
Hired Poisoner, Rancid Rats, Foulmire Knight, Vampire of the Dire Moon, Thrill-Kill Assassin,
Tinybones, White Widow, Hooded Blightfang, Vito, Virtus and Burrog Banemaker — **11 after the swaps**.
Chump-blocking with a 1/1 deathtoucher is what this deck does every turn, and with Arnyn out each one
that dies is:

| | |
|---|---|
| Arnyn | opponent −2, **you +2** |
| Vito, off that lifegain | opponent −2 |
| Marauding Blight-Priest | **each** opponent −1 |
| **Per 1/1 that dies** | **6 across a four-pod** |

**Witch of the Moors** — *"at your end step, if you gained life this turn, each opponent sacrifices a
creature and you return a creature card from your graveyard to your hand."* Blightfang gains life
every combat, so the condition is close to automatic and the edict repeats every turn. Dire Fleet
Ravager's ETB was one big hit that also hit us.

**Honest note on two of these.** Black Widow drew a card on every deathtouch connection and mono-black
needs draw; Rancid Rats' skulk made it near-unblockable and a reliable Blightfang trigger. Both are
real trades rather than free upgrades.

**Considered and rejected from the same batch:** Crossbones (needs Villains; the deck has one),
Dauthi Trapper, Lord of the Forsaken, Abyssal Harvester and Scathing Shadelock (no deathtouch, so
Blightfang and Archetype don't see them), Canyon Crawler (the 6-slot is Archetype and Nirkana
Revenant), and Grimdancer, Fell Stinger, Gutless Plunderer, Ninja of the Hand, Pirate Peddlers,
Sidisi Regent and The Master of Lake-town (playable, not better than the slot). **Dreaded Bat-Cloud**
{4}{B} 4/2 flying deathtouch, usually costing {1}{B}, was offered as an optional fifth and not taken.

## Legality flag — Avacyn, Angel of Horror

**Avacyn, Angel of Horror** {5}{B}{B}{B} 8/8 flying deathtouch is from **Reality Fracture Commander,
released 2026-10-02**. It reads `commander: not_legal` in `scryfall.db` only because the set is not
out yet; it has been in the deck since it was built on 2026-09-28. Same situation as Koth in `ojer`.

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

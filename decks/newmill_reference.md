# Cards Reference — The Mindskinner voltron mill, REBUILD (`newmill`)

**Status: EXPERIMENTAL, NOT BUILT.** Rebuilt 2026-09-29 from `oldmill`, which is kept intact for
A/B testing. Sim harness key: **`newmill`**.

**Every card resolved against `scryfall.db`** — all 100 checked for colour identity (zero
off-colour) and Commander legality.

## Commander

**The Mindskinner** — {U}{U}{U} — Legendary Enchantment Creature — Nightmare — **10/1**
"Can't be blocked. If a source you control would deal damage to an opponent, **prevent** that damage
and **each opponent** mills that many cards."

## The thesis change

`oldmill` was mill-goodstuff: 33 cards containing the word "mill", winning by accumulating spells.
**This build treats the commander as the mill engine and voltrons him.** Every point of power on an
unblockable body becomes mill to *each* opponent, so pumping him scales far harder than adding mill
spells — and double strike doubles it outright.

| Setup (10 lands on board) | Per opponent | Table total (3 opponents) |
|---|---|---|
| Bare 10/1 | 10 | 30 |
| + Commander's Plate | 13 | 39 |
| + Blackblade Reforged | 23 | 69 |
| **+ Fireshrieker (double strike)** | **46** | **138** |
| **+ Genji Glove instead** | **92** | **276** |
| + one Helm of the Host copy | 184 | 552 |

**Decking three opponents takes 297 total mill.** For comparison, Fractured Sanity — one of the
best mill spells in the format — is 42 total, once, and it is a three-mana card.

Mill-word count is **23**, down from 33, and that is intended. The metric stopped measuring the
deck's output the moment the commander became the engine.

## THE RULING — read this before adding any copy effect

Official Gatherer ruling, 2024-09-20:

> "If you somehow control more than one of The Mindskinner, the multiple replacement effects will
> have no effect. **Damage dealt to an opponent by a source you control will be replaced only
> once** with that opponent milling that many cards."

**The reading this deck is built on:** the ruling means *one damage instance is replaced once*. It
answers "I control two Mindskinners, does my 1/1's damage mill 2?" — no, it mills 1. The second
Mindskinner's ability is redundant **on that instance**.

But two Mindskinner bodies attacking are **two separate sources dealing two separate damage
instances**, each replaced once, independently — so 20 + 20 = **40 per opponent**.

**A published article (coolstuffinc, Wischkaemper, 2024-10-24) reads it the other way**, stating
that two Mindskinners each hitting for 20 means each opponent mills only 20. If that reading is
correct, **Helm of the Host, Auton Soldier and Irenicus's Vile Duplication are all near-worthless**
and this deck should be pure single-creature voltron instead.

The counter-argument for this deck's reading: if a second body contributed nothing, then Zellix
tokens and Vantress Gargoyle would contribute nothing while Mindskinner is out, and they clearly do.

**Confidence is high but not absolute. Worth a judge call or a playgroup agreement before buying
the copy package.** The copy package is deliberately kept to three cards so the deck still functions
if the other reading prevails.

## What does and does not work under the prevent clause

The damage is **prevented**, so it is never *dealt*. Anything keyed on damage being dealt is dead.

**WORKS:**
- **Double strike** — two separate combat damage steps, two separate prevention events, two mills.
  This is the single biggest gain in the rebuild.
- **Extra combat phases** — Genji Glove untaps and grants another combat.
- **Annihilator** — triggers on *attack*, not on damage.
- **Attack triggers** generally.
- **More bodies** — each is its own damage source (subject to the ruling above).

**DEAD — do not add these:**
- **Sword of Body and Mind** — its mill clause is "deals combat damage to a player". Never fires.
- **Quietus Spike** — halve-life never fires.
- **Loxodon Warhammer** — lifelink gains nothing off players.
- **Mindcrank** — no damage means no life loss.
- Crosstown Courier, Towering-Wave Mystic, Shriekgeist, Mindscour Dragon, infect.

**USELESS:**
- **Trample** — he is unblockable, so there is never excess damage to assign. That is most of
  Loxodon Warhammer's text and part of Eldrazi Conscription's.

**AND:** because he can never deal combat damage to a player, **The Mindskinner can never kill via
the 21-commander-damage rule.** Mill is the only route while he is on the battlefield.

## The equipment package

| Card | Cost + equip | Why |
|---|---|---|
| **Genji Glove** {5} | equip {3} | Double strike **plus untap plus an extra combat phase** — effectively quadruple |
| **Fireshrieker** {3} | equip {2} | Cheapest double strike, the five-mana on-ramp |
| **Blackblade Reforged** {2} | **equip legendary {3}** | +1/+1 per land. Built for commanders; that equip cost is the cheap one |
| **Commander's Plate** {1} | equip commander {3} | +3/+3 and protection from blue, black, red, green |
| **Accorder's Shield** {0} | equip {3} | Free to cast; +0/+3 fixes the 10/**1** toughness |
| **Lavaspur Boots** {1} | equip {1} | Haste and **ward {1}** for two mana total |

**Strata Scythe was rejected**: same job as Blackblade Reforged at the same equip cost, but it
counts only Islands (29) rather than all lands (35), and needs an ETB search to set up.

## Finding the payoff — four tutors

Genji Glove is the card the deck is built around, so it is findable four ways, two of which cost no
spell slot:

- **Whir of Invention** {X}{U}{U}{U} — any artifact **onto the battlefield**, and **improvise** lets
  you tap from your 19 artifacts to pay X. Finds Genji Glove and skips its 5-mana cast entirely.
- **Fabricate** {2}{U} — any artifact, to hand.
- **Inventors' Fair** (land) — {4}, {T}, sac: any artifact.
- **Urza's Saga** (land) — artifact MV <=1 onto the battlefield: Sol Ring, Commander's Plate,
  Accorder's Shield, Lavaspur Boots, Altar of the Brood.

## The copy package (three cards)

- **Auton Soldier** {4}{U}{U} — enters as a copy of any creature, non-legendary, **with myriad**.
  Copy the commander and each attack spawns a token copy attacking *each other opponent*.
- **Irenicus's Vile Duplication** {3}{U} — token copy, non-legendary, with flying.
- **Helm of the Host** {4}, equip {5} — a new non-legendary hasty copy **every combat**, accumulating.

Note the copies do **not** get the Equipment — they are 10/1s, not 13/4s, and die to any ping.

## Interaction and protection

**Six counterspells:** Swan Song {U}, An Offer You Can't Refuse {U}, Three Steps Ahead {U} (spree:
counter *or* copy a creature *or* draw two), Counterspell {U}{U}, **Didn't Say Please** {1}{U}{U}
(counters *and* mills three), Fierce Guardianship (free with the commander out).

**One-mana removal:** Pongify, Rapid Hybridization.

**Protecting the commander:** Commander's Plate (protection from four colours), Lavaspur Boots
(ward), Spellskite, Vodalian Illusionist (repeatable phase-out), Slip Out the Back, Teferi's Time
Twist, Fool's Demise, and the immediate blinks (Essence Flux, Siren's Ruse, Blur, Ghostly Flicker).

**Altar of Dementia** doubles as the escape hatch: sacrifice the commander in response to exile and
mill equal to his power on the way out; he returns to the command zone.

## What was deliberately removed, and why

- **Silent Arbiter** — caps *every* player at one attacker, which kills myriad and every Helm of the
  Host token. It was correct for the old build and is wrong for this one.
- **Screaming Swarm** — wanted a wide attack.
- **Fleet Swallower, Sphinx Mindbreaker, Jace's Mindseeker, Akroma's Memorial** — 6-7 mana each, all
  competing for the turns this deck needs to cast and equip.
- **Traumatize, Realmbreaker, Hedron Crab, Thought Scour, Increasing Confusion, Drown in Dreams** —
  slow or single-target mill, which is a third as efficient as "each opponent" in a pod.

## Known weaknesses

- **Thirteen creatures.** Thin. The flier problem documented in `oldmill_reference.md` — 81% of
  incoming damage came from fliers across ten logged four-pod games — gets **worse** here, not
  better. This build's answer is to win before it matters, which is coherent but fragile.
- **All eggs in one basket.** An exile effect on the commander leaves the equipment as dead
  cardboard. The protection suite is good but not airtight, and Commander's Plate does not stop
  white or colourless removal, non-targeted wipes, -X/-X, or edicts.
- **Equipment does nothing alone.** Every one is blank without the commander on the battlefield.

## Bracket

**Bracket 3, at the cap. 3 Game Changers:** Rhystic Study, Fierce Guardianship, Cyclonic Rift.
Verified against `game_changers.md`. No room for a fourth.

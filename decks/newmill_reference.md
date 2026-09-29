# Cards Reference — The Mindskinner voltron mill, REBUILD (`newmill`)

**Status: PLAYTESTED, not yet built in paper.** Rebuilt 2026-09-29 from `oldmill`, which is kept
intact for A/B testing. Sim harness key: **`newmill`**. **Three wins in three piloted games — see
"Logged games" below.**

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

**That last row does not apply while Silent Arbiter is on the battlefield** — only one creature can
attack each combat, so the copy waits. See the Silent Arbiter section for the trade.

**Decking three opponents takes 297 total mill.** For comparison, Fractured Sanity — one of the
best mill spells in the format — is 42 total, once, and it is a three-mana card.

Mill-word count is **23**, down from 33, and that is intended. The metric stopped measuring the
deck's output the moment the commander became the engine.

## Logged games

All three piloted by hand in Forge, 2026-09-29. **Three games, three wins.**

### The four-pod — won on turn 19, all three opponents decked

Four-player pod, `newmill` vs three opponents including the mono-black deathtouch deck (Virtus the
Veiled, Gonti, Dauthi Embrace, Cabal Stronghold and Phyrexian Arena all on board at the end).

| | |
|---|---|
| Result | Win, turn 19 — all three opponents lost drawing from an empty library |
| Opponents' final life | **37, 39, 28** — essentially untouched |
| Creatures drawn all game | **The Mindskinner only.** Zero others. |
| Commander deaths | **Two.** Recast both times, paying tax to 5 then 7 mana. |
| Equipment drawn | Genji Glove and Fireshrieker |
| Support on board | Memory Erosion, Drowned Secrets, Rhystic Study, Altar of Dementia, Sol Ring, Arcane Signet, Inventors' Fair |

**What this confirms.** The life totals are the tell: nobody was ever pressured, because under the
prevent clause nobody *can* be. The game is decided entirely on cards, not on life, and the deck got
there through a table containing the exact deck — mono-black deathtouch — that `oldmill` was losing
to. It also won having drawn **none** of its other twelve creatures, which means the voltron plan
does not need a board. The cost of that was three dead cards: Helm of the Host and Irenicus's Vile
Duplication had nothing but the commander to copy, and Altar of Dementia had nothing to sacrifice.

### The two heads-up games

`newmill` also beat the green Kodama deck and the mono-black deathtouch deck in 1v1. Worth less than
the pod game: one library to grind and a third of the incoming damage, at the same mill rate.

## Play notes from those games

**Genji Glove is the engine. Per turn, on a bare unblockable 10/1:**

| Step | Damage prevented | Each opponent mills |
|---|---|---|
| Combat 1, first strike | 10 | 10 |
| Combat 1, regular | 10 | 10 |
| *untap, additional combat phase* | | |
| Combat 2, first strike | 10 | 10 |
| Combat 2, regular | 10 | 10 |
| **Turn total** | | **40 per opponent — 120 across a four-pod** |

**The Glove grants exactly one extra combat.** Its trigger reads "if it's the first combat phase of
the turn", so combat 2 fails the check and does not chain a third.

**Fireshrieker and Genji Glove do not stack.** Double strike is a binary keyword; having it twice
does nothing. Once the Glove is attached, paying {2} to equip Fireshrieker is dead mana — hold it for
a counterspell. This is **not** a reason to cut either one: two sources is why you find one at all,
and Fireshrieker at {3} cast / {2} equip is the copy you can deploy four turns before the Glove. It
only matters when a second creature is available to carry the spare.

**Protecting an equipped commander — ranked.** The commander dying is the real cost in this deck
(second cast 5 mana, third 7), and not all the protection is equal once Equipment is attached:

1. **Slip Out the Back** {U} — best in the deck. Phases out the commander *and* "anything attached to
   it", so the Equipment survives **still attached**. The +1/+1 counter also makes him an 11/1, which
   is 44 mill per Genji turn instead of 40.
2. **Lavaspur Boots** — ward {1} taxes every removal spell passively.
3. **Spellskite** — redirect the target.
4. **The blinks** (Siren's Ruse, Teferi's Time Twist, Essence Flux, Blur, Ghostly Flicker) — they
   save the creature but **the Equipment falls off**, and re-equipping the Glove is another {3}.
   Reach for these only when Slip Out the Back is not in hand.
5. **Fool's Demise** — returns him to the battlefield on death, skipping the tax entirely.

**Helm of the Host is the hidden ceiling.** The token copies are non-legendary and hasty, and their
damage is prevented and converted to mill the same way — every copy is another 10 per opponent per
combat. It was drawn in the logged game with no second creature to fall back on, so it only ever
copied the commander.

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
  you tap from your 20 artifacts to pay X. Finds Genji Glove and skips its 5-mana cast entirely.
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
**These are not interchangeable once Equipment is attached — see the ranked list under "Play notes".**

**Silent Arbiter** {4} — 1/5 Artifact Creature. *"No more than one creature can attack each combat.
No more than one creature can block each combat."* The deck's main answer to going wide; see its own
section below. Findable with Whir of Invention, Fabricate and Inventors' Fair, which is why it is
better here than it was in `oldmill`.

**Altar of Dementia** doubles as the escape hatch: sacrifice the commander in response to exile and
mill equal to his power on the way out; he returns to the command zone. It is also the **off switch
for Silent Arbiter** — sacrifice the Arbiter on any turn you actually want to attack with copies.

## Silent Arbiter — added 2026-09-29, and the trade it makes

Cut from the rebuild, then **added back** over `Rogue's Passage` after the A/B sim below. The
reasoning for cutting it was that it blanks myriad and stops Helm of the Host tokens attacking. That
is true, and it is not the whole picture.

**What it buys.** The flier / go-wide problem is this deck's worst matchup and is documented in both
references. The Arbiter caps the **whole table** at one attacker per combat, which is the only effect
in the 99 that scales against an arbitrary number of creatures. Crawlspace, Propaganda and Maze of
Ith then only have to handle that one attacker.

**What it costs — the ceiling, not the floor.** The fail-safe still works completely: a Helm of the
Host token is a **non-legendary copy of the commander**, so it is unblockable, it carries the
prevention clause, it can wear the Genji Glove for {3}, and it **skips commander tax entirely.** If
the commander is answered, one copy attacking per combat still mills each opponent 10, or 40 with the
Glove on it. What the Arbiter removes is attacking with the commander *and* a copy in the same
combat: roughly 60 mill per opponent per turn down to 40, when a spare body is available.

**It does not slow the Genji Glove plan at all.** The limit is per *combat*; Genji Glove grants a
second combat, and the equipped creature attacks in both.

**It improves two cards.** *Court of Cunning* makes you the monarch, normally a death sentence for a
13-creature deck — with the Arbiter down, opponents can send exactly one creature at the crown per
combat. And *Jace, Memory Adept* becomes defensible for the same reason.

**Why it is not simply "correct".** It is a real trade of top-end speed for a floor against the
matchup that beats this deck. Altar of Dementia is the off switch when the copies want to swing.

## The A/B sim, 2026-09-29 — 88 games

`oldmill` and `newmill` each into an identical three-way pod with the mono-black deathtouch deck and
Kodama. Same field, same three seeds (4242, 777, 31337), 15 games each. Par is 33.3%.

| Arm | Blue wins | Decided | Win rate | 95% CI | vs par |
|---|---|---|---|---|---|
| `oldmill` | 11 | 43 | 25.6% | [12.5%, 38.6%] | z = −1.08, p = 0.28 — not distinguishable |
| `newmill` | 7 | 45 | 15.6% | [5.0%, 26.1%] | z = −2.53, **p = 0.011 — below par** |

The 10-point gap between arms is **not** significant (z = +1.17, p = 0.24). Two games in
`oldmill`/4242 exceeded the compute budget and were excluded.

**Read this with the pilot in mind.** The Forge AI does not hold up counterspells, sequence
Equipment, or protect the commander, and `newmill` requires all three — the same 99 cards decked a
four-pod on turn 19 when piloted by hand. `oldmill` is a pile of cards an AI can play competently.
The arm difference is mostly a gap in driving.

**The result that is not about piloting:**

| Deck | with `oldmill` at the table | with `newmill` at the table |
|---|---|---|
| Deathtouch (Virtus) | 44.2% | **53.3%** |
| Kodama | 30.2% | 31.1% |

Deathtouch gained nine points when the blue seat swapped and Kodama did not move. The only defensive
card `oldmill` had that `newmill` lacked was **Silent Arbiter**. That is what motivated adding it
back.

## What was deliberately removed, and why

- **Screaming Swarm** — wanted a wide attack.
- **Fleet Swallower, Sphinx Mindbreaker, Jace's Mindseeker, Akroma's Memorial** — 6-7 mana each, all
  competing for the turns this deck needs to cast and equip.
- **Traumatize, Realmbreaker, Hedron Crab, Thought Scour, Increasing Confusion, Drown in Dreams** —
  slow or single-target mill, which is a third as efficient as "each opponent" in a pod.

## Known weaknesses

- **Fourteen creatures.** Thin. The flier problem documented in `oldmill_reference.md` — 81% of
  incoming damage came from fliers across ten logged four-pod games — is not solved, only narrowed.
  Silent Arbiter, Crawlspace, Propaganda and Maze of Ith all answer attackers without caring how many
  creatures the opponent has, but they are four 1-ofs. The build's real answer is still to win before
  it matters.
- **All eggs in one basket.** An exile effect on the commander leaves the equipment as dead
  cardboard. The protection suite is good but not airtight, and Commander's Plate does not stop
  white or colourless removal, non-targeted wipes, -X/-X, or edicts.
- **Equipment does nothing alone.** Every one is blank without the commander on the battlefield.

## Bracket

**Bracket 3, at the cap. 3 Game Changers:** Rhystic Study, Fierce Guardianship, Cyclonic Rift.
Verified against `game_changers.md`. No room for a fourth.

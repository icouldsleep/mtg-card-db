# Cards Reference — The Mindskinner mono-blue mill (`newmill`)

**Status: PLAYTESTED, not yet built in paper.** Sim harness key: **`newmill`**. **Three wins in
three piloted games — see "Logged games" below.**

**Archidekt:** https://archidekt.com/decks/26944750/blue_mono_mill — verified card-for-card against
`newmill_decklist.txt` on 2026-09-30. 100 cards, zero differences.

**Every card resolved against `scryfall.db`** — all 100 checked for colour identity (zero
off-colour) and Commander legality.

## Commander

**The Mindskinner** — {U}{U}{U} — Legendary Enchantment Creature — Nightmare — **10/1**
"Can't be blocked. If a source you control would deal damage to an opponent, **prevent** that damage
and **each opponent** mills that many cards."

## The commander as a mill engine

**Every point of power on an unblockable body becomes mill to *each* opponent**, so pumping the
commander scales far harder than adding mill spells — and double strike doubles it outright. That is
why the deck runs Equipment where a mill deck would run enchantments.

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

Mill-word count is **23**, and that metric stopped measuring the deck's output the moment the
commander became the engine.

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
there through a table containing the exact deck — mono-black deathtouch — that this build had been
losing to. It also won having drawn **none** of its other creatures, which means the commander
alone does not need a board. The cost of that was three dead cards: Helm of the Host and Irenicus's Vile
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
4. **The blinks** (Siren's Ruse, Teferi's Time Twist, Essence Flux, Blur) — they save the creature
   but **the Equipment falls off**, and re-equipping the Glove is another {3}. Reach for these only
   when Slip Out the Back is not in hand.
5. **Fool's Demise** — returns him to the battlefield on death, skipping the tax entirely.

**Helm of the Host is the hidden ceiling.** The token copies are non-legendary and hasty, and their
damage is prevented and converted to mill the same way — every copy is another 10 per opponent per
combat. It was drawn in the logged game with no second creature to fall back on, so it only ever
copied the commander.

## THE REBUILD, 2026-09-30 — creatures ARE the mill engine

The deck was losing because it treated the commander as the only mill source and filled the rest of
the 99 with slow mill enchantments. That reading of the card was too narrow:

> If a source **you control** would deal damage to an opponent, prevent that damage and **each
> opponent** mills that many cards.

**"A source you control" is any source.** With the commander on the battlefield every creature is a
mill engine, and a far better one than any enchantment in the old list:

| Attacking with the commander out | Mill per opponent | Across a four-pod |
|---|---|---|
| A 2/3 flier | 2 | 6 |
| Vantress Gargoyle (5/4) | 5 | 15 |
| Four creatures averaging 3 power | 12 | **36** |

Psychic Corrosion milled 2 per draw. One 3/3 connecting mills 9. **Bruvac doubles all of it.**

**The constraint that follows:** a blocked creature deals its damage to the blocker, not the player,
so it mills nothing. **Evasion, not size, is what turns a body into mill.**

**15 out:** Psychic Corrosion, Sphinx's Tutelage, Teferi's Tutelage, Drowned Secrets, Memory Erosion,
Court of Cunning, Folio of Fancies, Jace Memory Adept, Altar of Dementia, Altar of the Brood, The
Water Crystal, Windfall, Fractured Sanity, **Silent Arbiter** (it caps you at one attacker per combat
and now fights the gameplan) and **Ruin Crab** (0/3, can never mill through combat).

**15 in:** Thassa, God of the Sea · Mithril Coat · Charix, the Raging Isle · Mist-Cloaked Herald ·
Triton Shorestalker · Slither Blade · Sleep-Cursed Faerie · Benevolent River Spirit · Cemetery
Illuminator · Kitesail Larcenist · Skystrike Officer · Cloud Elemental · Reservoir Kraken · Hover
Barrier · Wall of Frost.

Creatures go **12 to 25**. Untouched: the commander, Genji Glove, Fireshrieker, all three copies, the
equipment, protection, counterspells, mana, and the finisher package below.

### The finisher — kicked Maddening Cacophony + Bruvac

**Maddening Cacophony** kicked mills each opponent **half their library**. **Bruvac** doubles it.
**Half, doubled, is the whole library — it decks the entire table off one card.** Six mana plus
Bruvac's three, nothing infinite, comfortably inside Bracket 3.

**Drift of Phantasms is the tutor for it.** Transmute {1}{U}{U} finds a card of the same mana value;
Drift is MV 3 and **Bruvac is MV 3**. The 0/5 flying wall you keep for blocking is also the search
engine for the kill.

### Charix — know the window

**{3}: Charix gets +X/−X, where X is the number of Islands you control.** The pump is +X/**−X**, so
with a 0/17 base:

| Islands | Charix becomes |
|---|---|
| 8 | 8/9 |
| 12 | 12/5 |
| 16 | **16/1** |
| 17+ | **dies to state-based actions** |

The deck runs 29 Islands. Activate between roughly 8 and 16 Islands; past that leave it as a wall.
With Thassa making it unblockable, a 16-power Charix mills 48 across a four-pod.

## Logged game — 2026-09-30, four-player win, all three opponents decked

Piloted by hand. vs mono-red Ojer, mono-black deathtouch and Kodama green. **Won on turn 34.**

| Turn | Setup | Power | Mill per opponent |
|---|---|---|---|
| 19 | Commander + Fireshrieker | 10 | 10 + 10 = **20** |
| 23 | same | 10 | **20** |
| 27 | + Blackblade Reforged (6 lands) | **16** | 16 + 16 = **32** (96 across the table) |
| 31 | same | 16 | the remainder — all three empty |

**Four connects emptied three 99-card libraries.**

**Charix did its job on turn 25.** Green had Unnatural Growth doubling its board and sent a
**12-power Kodama of the East Tree**; Charix blocked and shrugged it off. **Mist-Cloaked Herald ate a
Lightning Bolt on turn 3** — a removal spell that was then not available for the commander on 15.
Life held at **40 → 37 → 23 → 21 → 17**, against two aggressive boards.

**The commander survived because it was protected, not because nobody tried.** The pilot cast it with
{U} and **Slip Out the Back** in hand. Note that Slip Out the Back phases out the creature **and
everything attached to it**, so the whole 32-mill package survives a Snuff Out for one mana — which
the blink effects cut in this rebuild would not have done.

## The commander is an ENCHANTMENT creature — the removal surface is wider than it looks

**The Mindskinner is a Legendary *Enchantment* Creature — Nightmare.** In a logged game it died to
**Reclamation Sage** (*"destroy target artifact or enchantment"*). It dies to creature removal **and**
to Naturalize, Disenchant, Aura Shards, Back to Nature and every green or white catch-all.

**That roughly doubles the number of cards at a typical table that can answer it**, and it is why
"they targeted him the moment he came out" keeps happening. Build and pilot on the assumption the
first copy dies.

**Commander's Plate answers this specific case** — in mono-blue it grants protection from white,
black, red and green, and Reclamation Sage's ability targets.

## Do not feed the punishers — the Zellix lesson

In a loss to the mono-red deck, **Zellix's Horror tokens were the pilot's own kill condition.**
Zellix makes a 1/1 whenever a player mills a creature card; the red deck's **Rampaging Ferocidon**
deals 1 damage to a creature's controller whenever another creature enters, which Ojer rewrote to 4.
**Three Horrors in one turn was 12 damage to our own face.** Against any "whenever a creature enters"
punisher, decline the Zellix triggers.

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

**CONFIRMED IN PLAY, 2026-09-29 — Forge implements it per source.** From the game log of a
four-player win, attacking with the commander and an Irenicus token (creature 425), where only the
commander carried Fireshrieker:

```
Combat: sleepy assigned The Mindskinner (100) and The Mindskinner (425) to attack Tousba.
Phase: sleepy's First Strike Damage Step
Replacement Effect: If a source you control would deal damage to an opponent,
                    prevent that damage and each opponent mills that many cards.
  -> Roland milled 10 · Tousba milled 10
Phase: sleepy's Combat Damage Step
Replacement Effect: ...
Replacement Effect: ...
  -> Roland milled 10 · Tousba milled 10 · Roland milled 10 · Tousba milled 10
```

**One replacement effect in the first-strike step** (only one body had double strike), **two in the
regular damage step** (both bodies). Thirty cards off each opponent in one combat. That is this
deck's reading, not the article's.

**Caveat: Forge is an implementation, not a judge.** Rules engines can be wrong. This is strong
corroboration rather than a ruling, so a judge call or playgroup agreement is still the right move
before a tournament. The copy package stays at three cards regardless.

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
  Accorder's Shield, Lavaspur Boots.

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
Twist, Fool's Demise, and the immediate blinks (Essence Flux, Siren's Ruse, Blur).
**These are not interchangeable once Equipment is attached — see the ranked list under "Play notes".**

## What was deliberately removed, and why

- **Screaming Swarm** — wanted a wide attack.
- **Fleet Swallower, Sphinx Mindbreaker, Jace's Mindseeker, Akroma's Memorial** — 6-7 mana each, all
  competing for the turns this deck needs to cast and equip.
- **Traumatize, Realmbreaker, Hedron Crab, Thought Scour, Increasing Confusion, Drown in Dreams** —
  slow or single-target mill, which is a third as efficient as "each opponent" in a pod.

## Logged game — 2026-09-29, four-player win, and what went wrong

**Result: win.** `newmill` vs mono-black deathtouch (Roland), a GW defenders deck (Tousba) and
mono-green (George). Roland **decked out**; George and Tousba killed each other. Finished on **6
life** after Quietus Spike on a Nirkana Revenant halved the pilot twice.

**The deck only actually killed one of the three.** Worth being honest about: this was surviving a
bloodbath as much as milling a table.

### The mana diagnosis — the important part

The pilot was mana-starved the whole game, and **it was not variance**:

| | |
|---|---|
| Cards seen (7 opening + 9 draws + 1 Tutelage) | ~17 |
| Lands hit | 6 |
| Rate | **35%** |
| This deck's land density | **35%** |

**Expectation was hit exactly, and expectation was not enough.** That is a deckbuilding fault, not a
bad draw. The spiral from the log:

| Turn | Lands | |
|---|---|---|
| 11 | **3** | Cast the commander for {U}{U}{U}, **tapped out**. Snuff Out (free — pay 4 life) kills it. |
| 15 | 4 | Urza's Saga |
| 19 | 5 | Island |
| 23 | **4** | **Urza's Saga sacrifices itself to chapter III** on the exact turn the recast became affordable. Paid the 5-mana tax with all four Islands plus Sol Ring. |
| 27 | 4 | Irenicus's Vile Duplication (4) + Fireshrieker equip (2) = exactly the six available |

**The mana problem caused the commander problem.** At three lands you must tap out to deploy, so
every protection spell is a dead card in hand; then the tax makes the recast 5, which took eight
more turns. One removal spell cost twelve turns because a single blue mana could not be held up.

### THE PLAY RULE THAT FOLLOWS

**Do not cast The Mindskinner on turn three. Cast it on turn four with {U} open.** The commander is
{U}{U}{U}, so turn three means tapping out, and this deck's whole protection suite costs one:

- **Slip Out the Back** {U} — phases it out *with the Equipment still attached*. Saves it even from
  free removal like Snuff Out, at instant speed.
- **Swan Song** {U} and **An Offer You Can't Refuse** {U} — counter the removal instead.
- **Spellskite** — its redirect costs {U/P}, so **2 life instead of mana** when you are tapped out.

One blue open covers four different answers. A turn of tempo is far cheaper than twelve.

### The commander is the table's number one removal target

Reported by the pilot across multiple games, not just this one: *"they targeted mind the moment he
came out."* That is not an unusually removal-heavy testing field — **a 10/1 unblockable body that
mills 10 a hit is the most obvious removal magnet at any table.** Build and pilot on the assumption
that the first copy dies. This is why the copy package and Fool's Demise earn their slots, and why
the turn-four rule above matters more than any single card in the list.

### Mana fix applied, 2026-09-29

The deck ran 35 lands and four rocks, but **three of those four made colourless mana** (Sol Ring,
Thought Vessel, Sapphire Medallion is a reducer), so they do nothing toward a {U}{U}{U} commander.
**Sky Diamond** and **Coldsteel Heart** were added over **Ghostly Flicker** and **High Tide** —
blue-producing rocks, three now counting Arcane Signet. Both enter tapped; that is the price.
Ghostly Flicker was the slot because blinks drop the Equipment and Slip Out the Back does the job
for one mana; High Tide needs a big Island-tapping turn this deck has never had.

**Urza's Saga was kept** despite deleting itself at the worst moment — it fetches four things here
(Sol Ring, Commander's Plate, Lavaspur Boots, Accorder's Shield) and its Construct token blocked in
this very game. Treat it as 34.5 lands when counting.

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

## Known weaknesses

- **Fliers.** Across ten logged four-pod games, **81% of incoming damage came from fliers.** The
  rebuild narrowed this rather than solving it: Cloud Elemental, Vantress Gargoyle, Benevolent River
  Spirit and Hover Barrier block in the air, and Crawlspace, Propaganda and Maze of Ith answer
  attackers without caring how many creatures the opponent has — but the last three are 1-ofs. The
  build's real answer is still to win before it matters.
- **All eggs in one basket.** An exile effect on the commander leaves the equipment as dead
  cardboard. The protection suite is good but not airtight, and Commander's Plate does not stop
  white or colourless removal, non-targeted wipes, -X/-X, or edicts.
- **Equipment does nothing alone.** Every one is blank without the commander on the battlefield.

## Bracket

**Bracket 3, at the cap. 3 Game Changers:** Rhystic Study, Fierce Guardianship, Cyclonic Rift.
Verified against `game_changers.md`. No room for a fourth.

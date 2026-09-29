# Cards Reference — The Mindskinner mono-blue mill (NEW / UNBUILT)

**Status: EXPERIMENTAL, NOT BUILT.** Designed Sept 28, 2026. No cards acquired, nothing sleeved.
This is a paper design, not a record of a physical deck. Do not treat it like the other reference
files that describe decks the owner actually owns.

**Archidekt:** https://archidekt.com/decks/26888106/blue_mono_mill — verified card-for-card against
this list on 2026-09-28 (100 cards, zero differences, The Mindskinner correctly set as commander).

**Every card below was resolved against `scryfall.db`.** All 100 were checked for colour identity
(zero off-colour) and Commander legality.

**Note on the two different "mill" counts.** Archidekt's Mill *category* reads 28 — that counts
cards manually tagged as mill. The figure used throughout this file is **34**, which counts every
card whose oracle text literally contains the word "mill", and that is the number the owner's
density goal tracks. The difference is cards filed under other categories that still say mill:
Altar of Dementia (Sac Outlet), Drift of Phantasms (Tutor), Vantress Gargoyle, Realmbreaker and
others.

## Commander

**The Mindskinner** — {U}{U}{U} — Legendary Enchantment Creature — Nightmare — **10/1**
"The Mindskinner can't be blocked. If a source you control would deal damage to an opponent,
**prevent** that damage and **each opponent** mills that many cards."

## What the deck does

**Opponent-mill only. This deck does not self-mill** — that was an explicit design constraint from
the owner. Stitcher Geralf was cut for exactly this reason ("each player mills three" includes you).
Vantress Gargoyle's `{T}: each player mills a card` is the only self-mill left and it is optional;
you would rather be attacking with it.

Three axes:

1. **The commander converts damage into pod-wide mill.** Any damage you would deal to an opponent
   becomes mill *to every opponent*. In a four-player game that is 3x value on every point of power.
   A 13/4 Mindskinner (with Commander's Plate) swings for **13 mill to each opponent = 39 a turn**.
2. **Go wide off Zellix.** Zellix, Sanity Flayer makes a 1/1 Horror every time a player mills one or
   more creature cards. Commander decks are ~30% creatures, so milling 20 a turn produces multiple
   Horrors a turn. Each Horror is another point of power feeding axis 1.
3. **Mill multipliers.** Bruvac doubles every opponent mill. The Water Crystal adds +4 to every mill
   instance. Both are replacement effects on the same event, so **the milling player chooses the
   order** and will pick the cheaper one — off one damage that is 6 per opponent, not 10.

## THE PREVENT CLAUSE — read this before adding any card

Mindskinner **prevents** the damage. Prevented damage is never dealt. So every card whose trigger
reads "deals combat damage to a player" or "an opponent loses life" **does nothing while your own
commander is on the battlefield.** These are traps and were all deliberately excluded:

- Crosstown Courier, Towering-Wave Mystic, Merfolk Windrobber, Shriekgeist, Reef Pirates
- Mindscour Dragon, Screeching Silcaw, Undead Alchemist
- **Mindcrank** (no damage means no life loss)
- Quietus Spike's halve-life trigger, Sword of Body and Mind's mill trigger
- Blighted Agent (infect damage is prevented too, so no poison counters)
- Daring Saboteur (its loot trigger is damage-based)

**What to add instead:** attack-triggered, ETB, upkeep, cast-triggered, draw-triggered and landfall
mill. Those all work. Screaming Swarm ("whenever you attack with one or more creatures") and
Veteran Ice Climber ("whenever this creature attacks") are attack triggers, not damage triggers,
which is why they are in and the list above is not.

Damage to **creatures** is NOT prevented — only damage to an opponent (a player). That is why
deathtouch would still function here, if you ever wanted it.

## The commander is also your biggest liability

While Mindskinner is out **you can never deal damage to a player.** Your 10/1 cannot kill anybody.
That matters against Elixir of Immortality, Feldon's Cane, Gaea's Blessing, or an opponent at 3 life
with 40 cards left.

**The toggle:** only two of your five blink/phase effects can turn the prevention off for a combat.

| Card | Wording | Toggles it off? |
|---|---|---|
| **Slip Out the Back** {U} | "it **phases out**" — gone until your next turn | **YES** |
| **Teferi's Time Twist** {1}{U} | returns "at the beginning of the next **end step**" | **YES** — after the damage step |
| Essence Flux {U} | "exile, **then return**" — same resolution | No, he is back before damage |
| Siren's Ruse {1}{U} | same | No |
| Blur {2}{U} | same | No |

**The line:** swing wide, leave Mindskinner at home, then Slip Out the Back on him during declare
blockers. All your other damage lands as real damage. Do NOT attack with him and then phase him —
a phased or exiled attacker is removed from combat and deals nothing.

**Vodalian Illusionist** ({U}{U}, {T}: target creature phases out) is the repeatable version of both
this toggle and the protection.

## Where blinking actually multiplies mill

The immediate blinks want to point at the ETB-mill creatures, not the commander:

- **Essence Flux {U} on Sphinx Mindbreaker = each opponent mills 10 again.** With Bruvac that is 20
  each, so **60 mill across the table for one blue mana.**
- Jace's Mindseeker (mill 5 + cast a free instant/sorcery off the top)
- Manic Scribe (3 each), Homarid Explorer-style ETBs, Wall of Lost Thoughts (4),
  Overwhelmed Apprentice (2 each)
- **Ghostly Flicker {2}{U}** blinks two targets — Sphinx Mindbreaker + Jace's Mindseeker in one card.

## Commander's Plate — the best version of this card that exists

`Equipped creature gets +3/+3 and has protection from each color that's NOT in your commander's
color identity. Equip commander {3}, Equip {5}.`

Mono-U means protection from **White, Black, Red AND Green** — four of five colours. Mindskinner
becomes **13/4**, and the jump from 1 to 4 toughness fixes his single real weakness (a 10/1 dies to
any ping: Orcish Bowmasters, a stray Shock, Pestilence).

Protection covers **D**amage, **E**nchant/equip, **B**locking, **T**argeting. So Swords, Path,
Murder, Doom Blade, Beast Within, Krosan Grip and Chaos Warp all bounce off, and
**Blasphemous Act does not kill him.**

**Its three holes — this is why the blinks stay in:**
1. **Blue removal.** Pongify, Rapid Hybridization, Cyclonic Rift, counterspells. Blue is in your
   identity, so no protection from it.
2. **Colourless.** Karn, Ugin, All Is Dust, Ulamog.
3. **Non-targeted wipes and edicts.** Damnation, Toxic Deluge (-X/-X — Deluge for 4 still gets him),
   Farewell, sacrifice effects.

Plate and the blinks are complements, not redundancy. Plate blanks four colours permanently; the
blinks cover what Plate cannot touch.

## Tutoring — three tutors, one spell slot

- **Drift of Phantasms** {2}{U} 0/5 flying defender — transmute {1}{U}{U} finds any **MV 3** card.
  That is **21 cards in this deck**, including **Bruvac**, Court of Cunning, Fractured Sanity, all
  three draw-engine enchantments, Memory Erosion, Zellix and Fierce Guardianship. MV 3 is where this
  deck lives. It is also the best blocker in the deck.
- **Urza's Saga** (land) — chapter III searches for an artifact MV <=1 and puts it **onto the
  battlefield**: **Commander's Plate**, Sol Ring, or Altar of the Brood. Chapter II makes Constructs
  that get +1/+1 per artifact — real bodies for the go-wide plan and Altar of Dementia fuel.
- **Inventors' Fair** (land) — `{4}, {T}, sac: search your library for an artifact`. Any artifact,
  so Commander's Plate or The Water Crystal. Plus 1 life a turn with 3+ artifacts (you run 10).

Two of the three cost no spell slot. **Mystical Tutor and Gifts Ungiven were rejected: both are
Game Changers** (see `game_changers.md`) and the deck is already at the Bracket 3 cap.

## Mana — measured, not guessed

40,000-game Monte Carlo on this exact mana base (36 lands, 32 blue sources, 4 rocks):

| | |
|---|---|
| Commander down by turn 3 | **75%** |
| Mana-screwed (<=2 mana on turn 4) | **6.7%** |
| Lands stranded in hand on turn 7 | **0.06** |
| Mean mana available T4 / T6 / T8 | **3.9 / 5.1 / 6.0** |

**Screw is not a problem and flood is essentially zero — 36 lands is correct, not excessive.**

**More ramp does not help.** A fourth mana rock is worth **+0.14 mana on turn 8** and cuts screw by
0.9%. Even 38 lands plus a 4th rock only buys +0.35 mana by turn 8. You get one land drop a turn and
games end around turn 8; you cannot ramp past that.

**What does help is untap effects and cost reduction**, which is why the deck runs:
- **High Tide** {U} — every Island taps for an extra {U} this turn. You have **31 Islands** (30
  basics + Mystic Sanctuary, which is an Island). Six Islands out = **12 mana for one mana.** Dead
  when your hand is empty; it is an "I have four spells and six lands" card.
- **Frantic Search** {2}{U} — draw 2, discard 2, untap three lands. Net free, and the two draws
  trigger Psychic Corrosion + Sphinx's Tutelage + Teferi's Tutelage for **up to 12 mill per opponent
  off a free spell.**
- **Sapphire Medallion** + **The Water Crystal** stack for **{2} off every blue spell.**

**Treasure tokens were considered and rejected.** Mono-blue's best treasure makers are Sailor of
Means and Corsair Captain — one treasure for three mana is bad ramp. Note that
**An Offer You Can't Refuse gives its two treasures to the OPPONENT** ("its controller creates").

**Do not count on The Water Crystal's `{4}{U}{U}` tap ability.** That is 6 mana; you will average
6.0 on turn 8. Play that card for the static text (+4 to every mill, blue spells cost {1} less), not
the activation. Same for Rogue's Passage {4} and Inventors' Fair {4}+sacrifice — late game or never.

**Your protection is nearly free, which is what saves the deck.** Fierce Guardianship costs {0} with
the commander out; Slip Out the Back, Swan Song, An Offer You Can't Refuse and Essence Flux are all
{U}. Holding up protection while deploying is what normally breaks a mana-hungry blue deck.

## Theme density

| Deck | Cards saying the word | % of all 100 | **% of non-land cards** |
|---|---|---|---|
| Black deathtouch | 28 | 28% | 44% |
| **This deck ("mill")** | **37** | **37%** | **57%** |

36 of the 100 cards are lands and cannot say "mill". Of the 65 that could, 37 do.

## Bracket

**Bracket 3, exactly at the cap. 3 Game Changers:** Rhystic Study, Fierce Guardianship,
Cyclonic Rift. Verified against `game_changers.md` card by card. **No room for a fourth** without
moving to Bracket 4. Commander's Plate, High Tide, Sapphire Medallion and Urza's Saga are all
confirmed NOT Game Changers.

No mass land denial, no chained extra turns, no cheap early two-card infinite combo.
**Caution: do not add Isochron Scepter** — with Dramatic Reversal that is a cheap two-card infinite
and would break Bracket 3. (Dramatic Reversal is not currently in the deck either.)

## Cards rejected, and why

- **Nephalia Drownyard** — a land that mills 3, looks perfect, but its ability costs {1}{U}{B} so its
  colour identity is {B}{U}. **Illegal in mono-blue.**
- **Tasha's Hideous Laughter** — *exiles* rather than mills. Does not say the word, does not fill
  graveyards, and starves Zellix of creature cards.
- **Mindcrank** and the whole damage-triggered mill package — see THE PREVENT CLAUSE above.
- **Mystical Tutor, Gifts Ungiven** — Game Changers, deck is at the cap.
- **Thassa, God of the Sea** — devotion to blue 5 is unrealistic here.
- **Whirler Rogue** — Mindskinner is already unblockable.
- **Roadkill Rodney / Gorgon Flail** — the only real deathtouch-plus-go-wide options in the colour
  identity. Left out because deathtouch is the black deck's theme, but both are legal and would work
  (damage to creatures is not prevented). Rodney's Squad makes multiple 2/1 deathtouchers.
- **Every Ulamog.** All nine were checked. **Not one contains the word "mill"** — they all *exile* or
  annihilate. Ulamog, the Ceaseless Hunger reads "defending player **exiles** the top twenty cards",
  which means **Bruvac does not double it, The Water Crystal does not add to it, and Zellix makes no
  Horrors from it.** It breaks all three engines at once, the same trap as Tasha's Hideous Laughter.
  It is also {10} and **colourless**, so neither Sapphire Medallion nor The Water Crystal discounts it
  (both read "**blue** spells cost {1} less"). Enablers would be Eldrazi Temple and Eye of Ugin, both
  lands, but they cost blue sources and are blank without Ulamog in hand.
- **Cut Your Losses** — replaced by Fleet Swallower on 2026-09-28. Three cards did "half a library"
  (Traumatize MV5, Cut Your Losses MV6, Fleet Swallower MV7) and the deck averages 6.0 mana on turn 8,
  so two of them compete for the same single turn. Cut Your Losses had the worst rate of the three:
  Traumatize plus a mana, still rounds **down**, and its casualty 2 wants a creature with power 2+,
  which the 1/1 Zellix Horrors cannot pay.

## Fleet Swallower — the top-end finisher

**Fleet Swallower** {5}{U}{U} 6/6 Fish — "Whenever this creature attacks, target player mills half
their library, rounded **up**."

- It is an **attack** trigger, so it works under the prevent clause.
- It is **blue**, so Sapphire Medallion + The Water Crystal drop it to **{3}{U}{U}, five mana**.
- **With Bruvac out, "half their library" doubles into their whole library.** One-card kill.
- Under Mindskinner its 6 damage also converts to 6 mill for each opponent, on top of the half-library.

Backup option not included: **Terisian Mindbreaker** {7} colourless 6/4, same half-library attack
trigger, with **unearth {1}{U}{U}{U}** for an immediate hasty swing. Says mill, but colourless so no
cost reduction applies.

## Fliers and evasion census

Unblockable: The Mindskinner (13/4 with Plate), Slither Blade, Veteran Ice Climber, plus
Rogue's Passage.
Fliers: Vantress Gargoyle (**5/4 for {1}{U}** — can't attack unless the defender has 7+ cards in
graveyard, which in a mill deck is permanently true by turn 3), Screaming Swarm, Sphinx Mindbreaker,
Jace's Mindseeker. Drift of Phantasms is a 0/5 flying **defender** and cannot attack.

Unblockable beats flying here: flying still gets blocked by fliers and reach, and in a three-opponent
pod somebody always has one.

## Combat posture — do NOT hold creatures back as blockers

Measured over a 3-way pod (deathtouch / this deck / Kodama), 12 games with full logs:

- **Blue lost to life total 0 in 10 of 12 games. It never once lost to an empty library.**
- In those same 12 games it **decked four opponents** (Virtus twice, Kodama twice) but converted
  only two into wins.

The mill is already lethal. The deck dies before it can collect. That is why the answer is not
"keep blockers home" — every creature held back is mill you did not deal, and under the commander a
creature's damage mills **every** opponent, so attacking is worth roughly 3x blocking in a pod.

**Attack with everything. The defence is non-combat:**

- **Crawlspace** {3} — no more than two creatures can attack you each combat. Does **not** restrict
  your own attacks. Guts a go-wide board without ever blocking.
- **Aetherize** {3}{U} — return all attacking creatures to hand. A fog that also undoes their board.
- **Propaganda** {2}{U} — taxes {2} per attacker.
- **Cyclonic Rift** overloaded — bounces the table.

**The only creatures that should ever be home are the ones that cannot attack anyway:**

| Card | Why it is the designated blocker |
|---|---|
| **Drift of Phantasms** 0/5 flier | **Defender** — literally cannot attack, so it costs the attack plan nothing |
| **Wall of Lost Thoughts** 0/4 | **Defender** — same |
| **Veteran Ice Climber** 1/3 | **Vigilance** — attacks *and* blocks, so it is never a choice |

Vantress Gargoyle can't block unless you hold 4+ cards in hand (Reliquary Tower, Thought Vessel and
Folio of Fancies make that easy, but it is an attacker first).

Two more outs that make blocking unnecessary: **Altar of Dementia** converts a creature that is
about to die into mill equal to its power at instant speed, and **Vodalian Illusionist** phases a
creature out to save it.

**Against a deathtouch deck specifically, blocking is always a losing action** — deathtouch makes
any amount of damage lethal, so toughness is irrelevant and a 0/5 Wall trades with a 1/1. This is
why high-toughness blockers were rejected in favour of Crawlspace and Aetherize.

## Pod vs heads-up — the format matters enormously

| | Heads-up vs deathtouch | 3-way pod (73 decided games, 3 seeds) |
|---|---|---|
| This deck's win rate | **14%** | **28.8%**, 95% CI [18.4%, 39.2%] |
| Median kill turn | 9 | 15 |

Par in a 3-way pod is 33.3%, and the confidence interval contains it — this deck, the deathtouch
deck (38.4%) and Kodama (32.9%) are **statistically indistinguishable**. The heads-up result was a
format artifact: "each opponent mills that many" is a 3x multiplier that does not exist in 1v1, and
~99 cards from one library in 9 turns is out of reach.

Seed variance was large enough that a single pod run is worthless: Kodama scored 48% on one seed and
21.7% on another, over the same matchup. Always run several seeds.

Key cards resolved more often in longer pod games than heads-up: Bruvac 10% -> 33%,
Commander's Plate 20% -> 25%, Traumatize 15% -> 25%.

**Unresolved: Court of Cunning resolved 0 times in 32 logged games**, against an expected ~20% per
game. That is roughly a 1-in-1000 outcome, so it is probably not variance — the likeliest
explanation is that Forge's AI never casts it, possibly because it does not evaluate the monarch.
Sphinx's Tutelage also came in 0/12. **Do not read either as a card-quality signal**; on paper Court
of Cunning is still the strongest card in the deck.

## The commander has NO ETB trigger — blinking him mills nothing

The Mindskinner's text is entirely static: "can't be blocked" plus the damage-prevention
replacement effect. **There is nothing that triggers on entering the battlefield.** Blinking or
recasting him mills zero. His mill comes from converting damage, which requires him to **attack**.

So the flicker suite is protection only, which is what it was picked for. Two cautions:

- **If he is attacking and you blink or phase him, he is removed from combat and deals no damage** —
  saving him mid-combat costs that swing's mill.
- Point the immediate blinks (Essence Flux, Siren's Ruse, Blur, Ghostly Flicker) at the **ETB-mill
  creatures** instead: Sphinx Mindbreaker (each opponent mills 10, so 20 each with Bruvac),
  Jace's Mindseeker (5 + a free spell), Manic Scribe (3 each), Wall of Lost Thoughts (4),
  Overwhelmed Apprentice (2 each).

**To actually pick him up and recast him, use Altar of Dementia.** Sacrifice Mindskinner, mill equal
to his power (10, or 13 with Commander's Plate), and he returns to the command zone. Instant speed,
so it dodges exile and sacrifice edicts that Commander's Plate cannot stop, and it converts him into
mill on the way out. Commander tax applies: {U}{U}{U} plus {2} per recast.

## Accorder's Shield — why a {0} Equipment earns a slot

`{0}` Artifact — Equipment. Equipped creature gets **+0/+3** and has **vigilance**. Equip {3}.

The vigilance is the smaller half. **Mindskinner is a 10/1, and toughness 1 is his real weakness** —
he dies to any incidental ping (Orcish Bowmasters, a stray Shock, Pestilence, a Goblin
Sharpshooter). Accorder's Shield costs nothing to cast and makes him a **10/4 without needing
Commander's Plate**, then a 13/7 with it. Equipment stack, so both can sit on him.

The vigilance does matter in one specific spot: a Plated Mindskinner has protection from white,
black, red and green, and **protection prevents damage from sources of those colours**. So he blocks
any non-blue creature, takes zero damage, and deals 13. With vigilance he attacks for 13 mill *and*
blocks for free every turn.

Rejected alternative: **Angel's Trumpet** {3} grants vigilance to **all** creatures including
opponents', and damages you for each of your creatures that did not attack — it punishes exactly the
posture this deck sometimes needs.

## Akroma's Memorial — vigilance is the point, and it is a DEFENSIVE card

`{7}` Legendary Artifact. Creatures you control have flying, first strike, **vigilance**, trample,
haste, **and protection from black and from red.**

This was initially filed as win-more. That was wrong. The pod diagnostic says the mill is already
lethal — four opponents decked across twelve games — while every loss was at life 0. **The deck does
not need more mill, it needs more turns alive.** Vigilance buys turns at zero cost to the mill plan,
because it removes the choice between swinging and blocking. Equipment cannot deliver that; it
equips one creature. This is the **only** team-wide vigilance grant in the colour identity.

It stacks three more answers onto the same problem:
- **Protection from black and red** — blockers cannot be damaged or targeted by either colour.
  Against the mono-black deathtouch deck that is total immunity, which fixes the one matchup where
  blocking genuinely was a losing action.
- **Flying** on every Zellix Horror token: evasion, so more mill.
- **Haste**: tokens attack the turn they are created.

There are real bodies to protect: **9 of 19 creatures have toughness 4 or more**, including two
6/6s, a 5/4 and two 4/4s.

**The cost, plainly:** it is **colourless**, so neither Sapphire Medallion nor The Water Crystal
discounts it — both read "**blue** spells cost {1} less". That is the same trap that disqualified
Ulamog. A true undiscounted 7 mana in a deck averaging 6.0 on turn 8, so it lands turn 8-9 and will
sometimes sit in hand. High Tide is the realistic enabler.

**The curve is not the objection.** Even with it this deck is the cheapest of the eleven in this
repo at avg CMC 2.62 with 8 cards at 5+. Old Toph ran 3.74 with 18 at 5+ and 12 at 6+ — and old
Toph's failure was never its curve, it was the AI declining to cast its commander while holding the
mana (81% of its whiff games had a red land out). This deck casts its commander in 95% of games at a
median of its own turn 3.

## Four-player pod result, and an upside worth knowing

Added to the 4-way pod (this deck, black deathtouch, white Lyra Angels, Kodama), 59 decided games
over three seeds:

| Deck | Rate | vs par (25%) |
|---|---|---|
| White Lyra | 55.9% | significantly above |
| Black deathtouch | 18.6% | not distinguishable |
| Kodama | 13.6% | significantly below |
| **This deck** | **11.9%** | **significantly below (z = -2.33)** |

This deck was at par (28.8%) in the 3-way pod. **Adding a fourth opponent gave it one more library
to mill and one more attacker pointed at it, and the second clearly outweighed the first** — which
matches the earlier diagnostic finding that it dies at life 0 rather than running out of time. One
excluded game hit the compute clock, and those are the long games this deck is likeliest to win, so
11.9% is very slightly pessimistic.

**The upside: this deck attacks the white deck's plan better than anything else at the table.** Log
entries from the white-deck diagnostic show it milling white's win conditions straight out of the
library:

```
Ai(3)-Lyra ... milled Grasp of Fate, Felidar Sovereign and Righteous Valkyrie
Ai(3)-Lyra ... milled Plains and Felidar Sovereign
Ai(3)-Lyra ... milled ... Court of Grace, Aetherflux Reservoir and Felidar Sovereign
```

Felidar Sovereign and Aetherflux Reservoir are 1-ofs in that deck. Milling them removes the plan,
not just cards. Worth remembering when choosing a mill target in a pod: the lifegain deck's win
conditions are in its library, not on its board.

## Open items

- Not built. No cards acquired.
- Never simulated as of this writing.
- Optional adds discussed but not included: Belltower Sphinx (2/5 flier, defensive),
  Soratami Mindsweeper (land-bounce mill, re-triggers Hedron/Ruin Crab), Mindeye Drake,
  Cloud of Faeries (free 1/1 flier, untaps 2 lands), Snap, Turnabout, Fabricate, Mind Stone.

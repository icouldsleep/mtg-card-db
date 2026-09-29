# Cards Reference — Ojer Axonil, Deepest Might (`ojer`)

**Status: NEW, NOT BUILT.** Created 2026-09-29. Sim harness key: **`ojer`**.

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

## Deck statistics

100 cards · 32 lands (25 Mountain) · 19 creatures · 6 mana rocks · 28 instants and sorceries ·
average CMC 2.41 · zero off-colour · all commander-legal except the Koth release date above.

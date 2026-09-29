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
- **Enchantments:** **Chaos Warp, and only Chaos Warp.** This is mono-red's structural hole and no
  list fixes it. Mulligan toward it against blue or white.

## The self-damage ledger — the deck's real cost

Five cards hurt you as well, and they stack:

| Card | To you, per turn cycle |
|---|---|
| Manabarbs | ~5 (one per land you tap) |
| Burning Earth | 1–2 — you run 25 Mountains, so it is **mostly one-sided** |
| Roiling Vortex | 1 |
| Sulfuric Vortex | 2, **and you cannot gain life** |
| Pyrohemia | 1 per activation, plus 1 to each of your own creatures |

With all of them out that is roughly **9–10 life a turn cycle off your own 40 — about four turns of
clock on yourself.** That is the bargain, not a flaw: this build closes fast rather than grinding.
Sulfuric Vortex is the single biggest tax if it ever needs trimming.

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

## Deck statistics

100 cards · 33 lands (25 Mountain) · 30 instants and sorceries · average CMC 2.51 · zero off-colour ·
all commander-legal except the Koth release date above.

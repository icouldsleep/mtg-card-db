# Cards Reference — Virtus the Veiled mono-black deathtouch (NEW / UNBUILT)

**Status: BUILT AND OWNED, with 9 cards outstanding (confirmed by the owner 2026-10-22).**
Designed Sept 28, 2026. **The owner confirmed the deck was fully built and this list matched his
physical deck right up until the 2026-10-22 nine-card swap.** Everything in the 100 is in hand
except the nine cards that swap added.

**TO ACQUIRE (9):**

```
Aetherflux Reservoir      Erebos, God of the Dead
Ayara, First of Locthwain Skullclamp
Blood Artist              South Wind Avatar
Enduring Tenacity         Stensian Sanguinist // Exsanguinate
                          Tergrid, God of Fright // Tergrid's Lantern
```

**Coming out, back to the collection (9):** Arcane Signet, Archetype of Finality, Black Market,
Burrog Banemaker, Case of the Gorgon's Kiss, Gonti Lord of Luxury, Hired Poisoner, Ravening Warg,
Thrill-Kill Assassin. Thornbite Staff is **not** on either list — it was cut and restored in the
same session, so it never left the deck.

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

## The kill

  Exquisite Blood OR Bloodthirsty Conqueror    ("opponent loses life -> you gain that much")
                    x
  Vito, Thorn of the Dusk Rose OR
  Marauding Blight-Priest                      ("you gain life -> opponent(s) lose life")

**FOUR assemblies, all infinite.** Marauding Blight-Priest IS a combo piece, not a lesser backup:
opponent loses 1 -> Exquisite Blood gains you 1 -> Blight-Priest drains each opponent -> loop.
An earlier draft of this file wrongly called it "non-infinite backup"; Archidekt's bracket checker
flagged it correctly and the claim was withdrawn.

**Sanguine Bond stays in the MAYBEBOARD.** With four assemblies already, it is redundancy the deck
does not need, and adding it pushes the bracket assessment toward 4.

Exsanguinate and Gray Merchant both start the loop and are fine on their own as big drain. Note the
pair does NOT self-start -- once both halves are down you still need one life-change event (a
lifelink attack, Crypt Ghast extort) to kick it off.

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
deathtouch · avg MV 2.78 · 3 of 3 Game Changers.**
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

### NEXT ADD — Grave Pact. Approved in principle 2026-10-22, waiting on a cut.

**Grave Pact** — {1}{B}{B}{B} — Enchantment — *"Whenever a creature you control dies, each other
player sacrifices a creature of their choice."* **Not a Game Changer**, so it does not disturb the
3-of-3 count.

This is the highest-value open slot in the deck and the reason is **Tergrid**. The deck runs **21
deathtouch creatures** whose job is trading in combat. With Grave Pact out, **every trade strips a
creature from all three opponents — and Tergrid puts all three onto your battlefield.** One blocked
one-drop can net three creatures. Skullclamp makes it worse for them: {1} to draw two cards *and*
force the table to sacrifice.

Alternatives in the same slot, all checked and none a Game Changer:
- **Dictate of Erebos** {3}{B}{B} — identical text with **flash**, one mana more. Ambush it mid-combat.
- **Butcher of Malakir** {5}{B}{B} — same effect on a 5/5 flier, 7 mana.
- **Fleshbag Marauder** / **Plaguecrafter** {2}{B} — one-shot, each player sacrifices on ETB.
  Plaguecrafter also hits planeswalkers.

**No cut has been identified.** The pool is tight — see the protected list above. Revisit with the
owner.

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
- **Ancient Tomb** (Game Changer) — **not Swamp-typed**, so Cabal Coffers, Cabal Stronghold and Extraplanar Lens cannot see it. Same flaw that makes Bojuka Bog the weakest land. **Mana Vault** (Game Changer) is the same problem as an artifact. **Imperial Seal** (Game Changer) is a sixth tutor that is sorcery-speed and puts the card on top of the library, costing a draw.
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
- Playtested, not formally tested. See the logged 2026-10-21 four-player win below.


## Creature (30)

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


## Artifact (10)

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


## Enchantment (6)

**Black Market** — {3}{B}{B} — Enchantment
"Whenever a creature dies, put a charge counter on this enchantment. | At the beginning of your first main phase, add {B} for each charge counter on this enchantment."

**Case of the Gorgon's Kiss** — {B} — Enchantment — Case
"When this Case enters, destroy up to one target creature that was dealt damage this turn. | To solve — Three or more creature cards were put into graveyards from anywhere this turn. (If unsolved, solve at the beginning of your end step.) | Solved — This Case is a 4/4 Gorgon creature with deathtouch and lifelink in addition to its other types."

**Dauthi Embrace** — {2}{B} — Enchantment
"{B}{B}: Target creature gains shadow until end of turn. (It can block or be blocked by only creatures with shadow.)"

**Exquisite Blood** — {4}{B} — Enchantment
"Whenever an opponent loses life, you gain that much life."

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


## Land (36)

**Bojuka Bog** — Land — Land
"This land enters tapped. | When this land enters, exile target player's graveyard. | {T}: Add {B}."

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

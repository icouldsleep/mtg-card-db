# Cards Reference — Virtus the Veiled mono-black deathtouch (NEW / UNBUILT)

**Status: EXPERIMENTAL, NOT BUILT.** Designed Sept 28, 2026. No cards acquired, nothing sleeved.
This is a paper design, not a record of a physical deck. Do not treat it like the other eight
reference files, which describe decks the owner actually owns.

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

## Game Changers — checked against game_changers.md on 2026-09-28

**2 Game Changers: Demonic Tutor, Vampiric Tutor.**

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

## Open items

- Nothing acquired. This is a shopping list, not a deck.
- Sanguine Bond maybeboard decision.
- Untested. The owner has flagged the whole thing as experimental.


## Creature (30)

**Archetype of Finality** — {4}{B}{B} — Enchantment Creature — Gorgon — **2/3**
"Creatures you control have deathtouch. | Creatures your opponents control lose deathtouch and can't have or gain deathtouch."

**Avacyn, Angel of Horror** — {5}{B}{B}{B} — Legendary Creature — Angel — **8/8**
"Flying, deathtouch | Whenever Avacyn or another nontoken creature you control dies, return that card to the battlefield under your control at the beginning of the next end step."

**Black Widow, Deadly Hunter** — {2}{B} — Legendary Creature — Human Assassin Hero — **3/3**
"Deathtouch | Whenever a creature you control with deathtouch deals combat damage to a player, you draw a card and lose 1 life."

**Blightwing Bandit** — {3}{B} — Creature — Faerie Rogue — **2/2**
"Flying, deathtouch | Whenever you cast your first spell during each opponent's turn, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled, and mana of any type can be spent to cast it."

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

**Charcoal Diamond** — {2} — Artifact
"This artifact enters tapped. | {T}: Add {B}."

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


## Enchantment (7)

**Black Market** — {3}{B}{B} — Enchantment
"Whenever a creature dies, put a charge counter on this enchantment. | At the beginning of your first main phase, add {B} for each charge counter on this enchantment."

**Case of the Gorgon's Kiss** — {B} — Enchantment — Case
"When this Case enters, destroy up to one target creature that was dealt damage this turn. | To solve — Three or more creature cards were put into graveyards from anywhere this turn. (If unsolved, solve at the beginning of your end step.) | Solved — This Case is a 4/4 Gorgon creature with deathtouch and lifelink in addition to its other types."

**Cover of Darkness** — {1}{B} — Enchantment
"As this enchantment enters, choose a creature type. | Creatures of the chosen type have fear. (They can't be blocked except by artifact creatures and/or black creatures.)"

**Dauthi Embrace** — {2}{B} — Enchantment
"{B}{B}: Target creature gains shadow until end of turn. (It can block or be blocked by only creatures with shadow.)"

**Exquisite Blood** — {4}{B} — Enchantment
"Whenever an opponent loses life, you gain that much life."

**Kaya's Ghostform** — {B} — Enchantment — Aura
"Enchant creature or planeswalker you control | When enchanted permanent dies or is put into exile, return that card to the battlefield under your control."

**Phyrexian Arena** — {1}{B}{B} — Enchantment
"At the beginning of your upkeep, you draw a card and you lose 1 life."


## Planeswalker (1)

**Liliana of the Dark Realms** — {2}{B}{B} — Legendary Planeswalker — Liliana
"+1: Search your library for a Swamp card, reveal it, put it into your hand, then shuffle. | −3: Target creature gets +X/+X or -X/-X until end of turn, where X is the number of Swamps you control. | −6: You get an emblem with "Swamps you control have '{T}: Add {B}{B}{B}{B}.'""


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

29x Swamp.
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

# Cards Reference — Lyra Dawnbringer mono-white Angel lifegain (NEW / UNBUILT)

**Status: EXPERIMENTAL.** Designed Sept 28, 2026, as an upgrade to a mono-white Angel precon the
owner is acquiring. **Every card was resolved against `scryfall.db`** — all 100 checked for colour
identity (zero off-colour) and Commander legality.

## Commander

**Lyra Dawnbringer** — {3}{W}{W} — Legendary Creature — Angel — **5/5**
"Flying, first strike, lifelink. **Other Angels you control get +1/+1 and have lifelink.**"

## What the deck does

**Life total is the win condition, not a resource.** Commander starts you at 40, which makes the
threshold cards far better than they read:

| Life | What turns on |
|---|---|
| **40** (start) | **Felidar Sovereign** — *you win the game* at upkeep. Live at baseline |
| **47** (+7) | **Righteous Valkyrie** gives the team +2/+2 · **Speaker of the Heavens** makes free 4/4 Angels |
| **50** (+10) | **Test of Endurance** — *you win the game* · **Doctor Strange** gives +2/+2 and vigilance |
| **55** (+15) | **Angel of Destiny** — *each player it attacked this turn loses the game* |

**Serra Ascendant** deserves its own line: at 30+ life it gets +5/+5 and flying, so in Commander it
is a **6/6 flying lifelinker for one mana, from turn one.**

### The engine loop

**Bishop of Wings + Angelic Accord.** An Angel enters, Bishop gains you 4 life, that satisfies
Angelic Accord's "gained 4 or more life this turn", which makes a free 4/4 flying Angel at end step,
which triggers Bishop again. **Righteous Valkyrie** stacks on top (gain life equal to each entering
Angel's or Cleric's toughness) and **Angel of Vitality** adds +1 to every lifegain instance.

**Archangel of Thune** converts all of it into +1/+1 counters on your whole board.

## Lifelink triggers on BLOCKING — this is why vigilance matters so much here

Lifelink reads "damage dealt by this creature also causes you to gain that much life." It is not
restricted to combat damage to a player. It triggers on damage dealt **while blocking**, while being
blocked, and to creatures.

Lyra gives every Angel lifelink. So **vigilance means the team attacks for life AND blocks for
life — two lifegain events per turn cycle.** In this deck vigilance is not merely defensive, it is a
win-condition accelerator: every extra lifegain event pushes you up the threshold ladder and feeds
Angelic Accord, Resplendent Angel, Well of Lost Dreams and Archangel of Thune.

Lyra herself is a 5/5 **first strike** lifelinker — she blocks a 4/4, kills it before it deals
damage, and you gain 5.

### Vigilance sources — 6 grant it to others, 5 have it themselves

**Grant it to the team:**

| Card | Condition |
|---|---|
| **Brave the Sands** {1}{W} | Unconditional, **and every creature can block an additional creature** |
| **Always Watching** {1}{W}{W} | Unconditional, **nontoken only**, +1/+1 |
| **Thraben Watcher** {2}{W}{W} | Unconditional, **other nontoken only**, +1/+1. Also a 2/2 Angel flier |
| **Rinoa, Angel Wing** {2}{W} | Your combat only, **creatures with flying**, +1/+1. Also recursion |
| **Angelic Field Marshal** {2}{W}{W} | Requires you control your commander |
| **Doctor Strange, Surgeon** {4}{W} | Requires 50+ life (+10 over starting) |

**Have it themselves:** Giada, Font of Hope · Metropolis Reformer · Serra Avenger ·
Speaker of the Heavens · Felidar Sovereign. Resplendent Angel's tokens also enter with it.

**Watch the "nontoken" clause.** This deck makes a lot of 4/4 Angel tokens (Angelic Accord,
Resplendent Angel, Speaker of the Heavens), and **Always Watching and Thraben Watcher do not touch
them.** Brave the Sands, Rinoa and Angelic Field Marshal do. That is what makes Brave the Sands the
best of the six despite costing the least.

**Rinoa does not give herself vigilance** — she grants it to creatures with flying and she is a
2/4 Human Rebel Warlock with no evasion.

## Rinoa, Angel Wing — two cards in one

`{2}{W}` 2/4. At the beginning of combat on your turn, creatures you control **with flying** get
+1/+1 and gain vigilance until end of turn. Whenever one or more **attacking** creatures you control
die, you may return one of them to the battlefield tapped with a flying counter. Once each turn.

The deck is nearly all fliers, so the first ability is a team anthem plus team vigilance every
combat for three mana. The second is the only recursion in the deck that triggers off losing
attackers — a free rebuy every turn you trade in combat, and real insurance against blockers and
wipes.

## Gift of Immortality — and a trap

Best targets are **Lyra** (a recurring 5/5 flying first-strike lifelinker) or **Felidar Sovereign**
(a win condition that will not stay dead).

**Do NOT put it on Academy Rector.** Both are death triggers you control, so you choose the order,
but they cancel each other out: exile Rector for its enchantment tutor and Gift finds nothing in the
graveyard to return; return Rector with Gift and the tutor fizzles because the card has left the
graveyard. You get one or the other, never both.

## Tutoring for Aetherflux Reservoir

- **Enlightened Tutor** {W} — artifact **or** enchantment, so it finds Aetherflux Reservoir,
  Test of Endurance *or* Angelic Accord. **This is a Game Changer.**
- **Inventors' Fair** — a **land**, so it costs no spell slot. `{4}, {T}, sac: search for any
  artifact.` Also gains 1 life a turn with 3+ artifacts, and the deck runs 11.
- **Idyllic Tutor** {2}{W} — enchantment only; gets Test of Endurance.
- **Academy Rector** {3}{W} — dies, puts an enchantment **onto the battlefield** free.

**Wishclaw Talisman is black** and therefore illegal here, despite being the obvious one-mana
any-card tutor.

## Aetherflux Reservoir — an alternate route, not the main plan

Its lifegain clause ("gain 1 life for each spell you've cast **this turn**") is a storm payoff. An
Angel deck with a real curve casts one or two spells a turn, so it gains 1–3 life a turn. Modest.

Its value is the **50-damage button**. Note the tension: you need 50+ life to pay 50 (you cannot pay
life you do not have), and paying it drops you below both Test of Endurance's 50 and Felidar's 40.
In a three-opponent pod it kills one player, not the table. Treat it as the backup for when your
upkeep triggers keep getting removed.

**Synergy worth knowing:** **Herald of Eternal Dawn** says "you can't lose the game and your
opponents can't win the game." At exactly 50 life you can fire the Reservoir, go to 0, and survive.

## What was cut from the precon, and why

**Actively fought the plan:** Day of Judgment and Cleansing Nova (destroy all creatures — this *is*
the creature deck), Sunblast Angel (destroys all tapped creatures, i.e. your own attackers),
Search the Premises (rewards being attacked, but Archangel of Tithes discourages that).

**Handed opponents cards:** Secret Rendezvous ("you **and target opponent** each draw three"),
Cut a Deal.

**Too expensive or too weak:** Reya Dawnbringer (9 mana), Emeria Shepherd, Austere Command (6 mana,
awkward for a go-wide deck), Temple of the False God (cannot tap until you control five lands),
Marble Diamond, Radiant Fountain, Segovian Angel, Norn's Choirmaster, Vanguard Seraph.

**Conditional filler:** Angelic Sleuth, Merchant of Truth, Wojek Investigator, Metallic Mimic,
Angel of Finality, Destroy Evil, Heraldic Banner, Patchwork Banner.

**Thraben Watcher was cut and then restored.** It was dropped for overlapping Always Watching, which
is the wrong reasoning in a singleton deck — two copies of anthem-plus-vigilance means you actually
draw one. It is also an Angel and a flier, so Lyra pumps it and gives it lifelink.

## Commander's Plate — every mono-coloured deck should run it

`{1}` Equipment. Equipped creature gets **+3/+3** and has **protection from each color that's not in
your commander's color identity**. Equip commander {3}, Equip {5}.

Mono-white means protection from **blue, black, red and green** — four of the five colours, the most
this card can ever give. On Lyra she becomes an **8/8 flying, first-strike, lifelinking** threat that:

- **cannot be blocked by any non-white creature** (protection stops blocking, not just damage)
- cannot be targeted by their removal
- takes no damage from any of those colours

For this deck the number that matters is **8 life per connection** — 40 to 48 in a single swing, or
**16 with Doctor Strange** doubling it. Two hits clears Test of Endurance's 50.

**What protection does not stop:** white removal, colourless removal (Karn, Ugin, All Is Dust),
non-targeted wipes (Damnation, Farewell), -X/-X effects, and sacrifice edicts. That is why
Teferi's Protection, Flawless Maneuver, Swiftfoot Boots and Gift of Immortality stay — they cover
what the Plate cannot.

Swiftfoot Boots is not made redundant: Equipment stack, and haste is the one thing the Plate does
not provide.

## Bracket

**Bracket 3, exactly at the cap. 3 Game Changers:** Enlightened Tutor, Smothering Tithe,
Teferi's Protection. Verified against `game_changers.md` card by card. **No room for a fourth.**

**Serra's Sanctum** was rejected — it taps for {W} per enchantment and the deck runs few.

## Mana

40,000-game Monte Carlo on this mana base (37 lands, 33 white sources, 4 rocks):

| | |
|---|---|
| Lyra castable ({3}{W}{W}) by turn 5 | **61%**, by turn 6 **71%** |
| Mana-screwed (<=2 mana on turn 4) | **6.0%** |
| Lands stranded in hand, turn 7 | **0.07** |

The model **understates** the deck, because it cannot see the cost reducers: **Starnheim Aspirant**
(Angel spells cost {2} less), **Herald of War** ({1} less), and **Giada** tapping for {W} toward
Angel spells.

## Open items

- Not built. Precon not yet in hand as of writing.
- Never simulated.
- **Interaction is thin** — 3 sorceries and 7 instants. Swords to Plowshares, Fateful Absence,
  Exorcise, Invoke the Divine and Grasp of Fate are the answers. This is the first place to look if
  the deck underperforms in a Bracket 3 pod.
- Options considered and not included: **Serra's Blessing** {1}{W} (a third unconditional team
  vigilance grant, strictly worse than Brave the Sands at the same cost), **Aang, Air Nomad**
  {3}{W}{W} 5/4 (flying, vigilance, grants team vigilance — but a Human Avatar Ally, so Lyra does
  **not** pump him or give him lifelink), **Sigil of the Empty Throne** (4/4 flying Angel per
  enchantment cast — left out deliberately to keep this deck distinct from the Killian aura deck).

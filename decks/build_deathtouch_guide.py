"""Build the Virtus the Veiled mono-black play guide as a single PDF.

Written 2026-10-21. Content is drawn from decks/deathtouch_reference.md and
every card's oracle text was re-read from scryfall.db while writing it.
Style matches build_toph_guide.py so the three guides look like one set.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

ss = getSampleStyleSheet()
TITLE = ParagraphStyle('TITLE', parent=ss['Heading1'], fontSize=19, spaceAfter=2, leading=23)
SUB   = ParagraphStyle('SUB', parent=ss['BodyText'], fontSize=10.5,
                       textColor=colors.HexColor('#444444'), spaceAfter=10)
H2    = ParagraphStyle('H2', parent=ss['Heading2'], fontSize=13, spaceBefore=14, spaceAfter=6,
                       textColor=colors.HexColor('#1a1a1a'))
H3    = ParagraphStyle('H3', parent=ss['Heading3'], fontSize=10.5, spaceBefore=10, spaceAfter=4)
BODY  = ParagraphStyle('BODY', parent=ss['BodyText'], fontSize=9.5, leading=13.2, spaceAfter=5)
BULL  = ParagraphStyle('BULL', parent=BODY, leftIndent=13, bulletIndent=3, spaceAfter=3)
NUM   = ParagraphStyle('NUM', parent=BODY, leftIndent=15, bulletIndent=3, spaceAfter=3)
QUOTE = ParagraphStyle('QUOTE', parent=BODY, leftIndent=12, rightIndent=12,
                       fontName='Helvetica-Oblique', textColor=colors.HexColor('#333333'),
                       spaceBefore=4, spaceAfter=7)
CELL  = ParagraphStyle('CELL', parent=BODY, fontSize=8.5, leading=11, spaceAfter=0)
CELLB = ParagraphStyle('CELLB', parent=CELL, fontName='Helvetica-Bold')

GRID = TableStyle([
    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#ece7f2')),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
])

def h2(t):  return Paragraph(t, H2)
def h3(t):  return Paragraph(t, H3)
def p(t):   return Paragraph(t, BODY)
def q(t):   return Paragraph(t, QUOTE)
def b(t):   return Paragraph(t, BULL, bulletText='•')
def n(t, i):return Paragraph(t, NUM, bulletText=f'{i}.')
def table(rows, widths):
    data = [[Paragraph(c, CELLB if r == 0 else CELL) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1); t.setStyle(GRID); return t

W = 7.0 * inch
S = lambda h=6: Spacer(1, h)
F = []

# ---------------------------------------------------------------- page 1
F += [Paragraph('Virtus the Veiled — Mono-Black Deathtouch Drain', TITLE),
      Paragraph('Play guide · rebuilt 2026-10-22 · 100 cards, 36 lands · Bracket 3, '
                '<b>3 of 3 Game Changers</b> (Demonic Tutor, Vampiric Tutor, Tergrid) — at the cap', SUB)]

F += [h2('The commander'), q(
    '<b>Virtus the Veiled</b> — {2}{B} — Legendary Creature — Azra Assassin — <b>1/1</b><br/>'
    'Partner with Gorm the Great · Deathtouch<br/>'
    'Whenever Virtus deals combat damage to a player, <b>that player loses half their life, '
    'rounded up.</b>')]
F += [p('He is a <b>1/1</b>. The half-life trigger does not care how much damage he deals, only '
        'that he connects. <b>Never spend a card pumping him.</b> Every resource goes into making '
        'him unblockable and keeping him alive. Two connections put almost anyone in burn range; '
        'from 40 that is 40 → 20 → 10.'),
      p('Gorm the Great is not in the deck, so the Partner line does nothing. Ignore it.')]

F += [h2('What the deck actually does'),
      p('It is not a creature deck that happens to drain. It is a <b>drain engine</b> with 26 '
        'deathtouch bodies acting as both defence and triggers. Three overlapping plans:'),
      n('<b>Combo.</b> A two-card loop that kills the whole table at once. See the next page.', 1),
      n('<b>Commander damage by halves.</b> Virtus or Quietus Spike connecting, repeatedly.', 2),
      n('<b>Big black finishers.</b> Torment of Hailfire for a large X, Exsanguinate, or '
        'Gray Merchant of Asphodel off a high devotion count.', 3)]

F += [PageBreak()]

# ---------------------------------------------------------------- page 2
F += [h2('The kill — the 2×4 grid')]
F += [p('Any <b>Side A</b> card plus any <b>Side B</b> card is an <b>infinite loop</b> that drains '
        'every opponent to zero. <b>Eight</b> two-card combinations, which is why it assembles so '
        'often. Single-target versions still kill the whole table — you choose a new target each '
        'iteration, so you kill one player, then the next.')]
F += [table([
    ['Side A — "whenever you GAIN life"', 'Side B — "whenever an opponent LOSES life, you gain that much"'],
    ['<b>Vito, Thorn of the Dusk Rose</b> {2}{B} — target opponent loses that much<br/>'
     '<b>Marauding Blight-Priest</b> {2}{B} — <b>each</b> opponent loses 1<br/>'
     '<b>Enduring Tenacity</b> {2}{B}{B} — target opponent loses that much; returns as an '
     'enchantment when it dies<br/>'
     '<b>South Wind Avatar</b> {3}{B} — each opponent loses 1 (and gains you life when your '
     'creatures die, so it sparks itself)',
     '<b>Exquisite Blood</b> {4}{B}<br/><br/><b>Bloodthirsty Conqueror</b> {3}{B}{B} — 5/5 flier '
     'with deathtouch<br/><br/>These are the only two in mono-black. There is no third; all future '
     'redundancy has to come from Side A.'],
], [3.5*inch, 3.5*inch])]
F += [S(8)]
F += [h3('The loop does NOT self-start'),
      p('Both halves on the battlefield do nothing by themselves. You need <b>one life-change '
        'event</b> to spark it, and then it runs on its own. This is the single most important '
        'thing to know about the deck.'),
      b('<b>Extort</b> off Crypt Ghast — pay {W/B} on any spell. One mana, the cheapest spark.'),
      b('Any lifelink creature connecting.'),
      b('A fetch-style life payment, Read the Bones, Night\'s Whisper, Grim Tutor, Vampiric Tutor.'),
      b('<b>The Darkness Crystal</b> — any nontoken creature an opponent controls dying gains you 2.'),
      b('<b>Blood Artist</b> — <b>any</b> creature dying anywhere, including between two opponents. '
        'Drains and gains in one trigger, so it starts the loop from either side.'),
      b('<b>Ayara, First of Locthwain</b> — every black creature you cast, and all of yours are black.'),
      b('<b>Aetherflux Reservoir</b> — every spell you cast, scaling within the turn.'),
      b('<b>Erebos</b> or <b>Skullclamp</b> — any draw you pay life for, refunded by Sheoldred.'),
      b('<b>Tergrid\'s Lantern</b> — {T} to make a player lose 3 (or sacrifice, or discard).'),
      b('<b>An opponent attacking another opponent.</b> Any life loss at the table counts.')]
F += [S(6), q('<b>Logged 2026-10-21:</b> the loop fired on an <i>opponent\'s</i> turn, when Collin '
              'attacked Douglas with Avacyn for 10. Conqueror gained 10, Blight-Priest drained, and '
              'the table died over roughly 38 iterations. The deck did nothing on the turn it won. '
              'Final life total 87.')]

F += [PageBreak()]

# ---------------------------------------------------------------- page 3
F += [h2('Evasion — the only thing Virtus needs')]
F += [table([
    ['Card', 'What it does for Virtus', 'Cost'],
    ['<b>Commander\'s Plate</b>', '+3/+3 and <b>protection from white, blue, red and green</b> — '
     'every colour not in your identity. Unblockable by any non-black creature, and untargetable '
     'by four colours of removal.', '{1}, equip commander {3}'],
    ['<b>Rogue\'s Passage</b>', 'Unconditionally unblockable. Works against black decks, which the '
     'Plate does not.', '{4}, {T}'],
    ['<b>Dauthi Embrace</b>', 'Shadow — effectively unblockable, and repeatable on any creature.',
     '{B}{B} per activation'],
    ['<b>Quietus Spike</b>', 'A second copy of the half-life trigger that can ride a creature they '
     'are less afraid of.', '{3}, equip {3}'],
], [1.35*inch, 4.25*inch, 1.4*inch])]
F += [S(8)]
F += [h3('Protection is DEBT — what it actually stops'),
      p('Protection from a colour stops four things from sources of that colour: <b>D</b>amage, '
        '<b>E</b>nchanting/Equipping, <b>B</b>locking, and <b>T</b>argeting. It does <b>not</b> '
        'stop sacrifice effects, -X/-X, board wipes that say "destroy all", or exile that does not '
        'target. Commander\'s Plate is colourless, so it can still equip a creature it protects.')]
F += [h3('Black opponents are the hole'),
      p('The Plate gives no protection from black and black creatures can block through it. Against '
        'a black deck, Rogue\'s Passage or Dauthi Embrace is the answer, not the Plate.')]

F += [PageBreak()]

# ---------------------------------------------------------------- page 4
F += [h2('Deathtouch payoffs — read the trigger condition carefully')]
F += [table([
    ['Card', 'Triggers on', 'Needs to connect?'],
    ['<b>Hooded Blightfang</b>', 'A deathtouch creature you control <b>ATTACKS</b>', '<b>No.</b> '
     'Fires on declaring attackers. Blocking it does not stop the drain.'],
    ['<b>White Widow, Yelena Belova</b>', 'Deathtouch creature deals combat damage to a player',
     'Yes'],
    ['<b>Black Widow, Deadly Hunter</b>', 'Deathtouch creature deals combat damage to a player',
     'Yes'],
    ['<b>Arnyn, Deathbloom Botanist</b>', 'A creature you control with power <b>or</b> toughness 1 '
     'or less dies', 'No — it wants your small bodies to trade'],
    ['<b>Virtus / Quietus Spike</b>', 'Combat damage to a player', 'Yes'],
], [1.6*inch, 2.5*inch, 2.9*inch])]
F += [S(8)]
F += [p('<b>The Blightfang line is the one that gets misplayed.</b> Attacking with three small '
        'deathtouchers drains each opponent for 3 and gains you 3 <i>before blockers are even '
        'declared</i> — and that lifegain is a combo spark. Attack with everything even into a wall '
        'of blockers.')]
F += [h3('Why the one-mana bodies are in the deck'),
      p('Hired Poisoner is a vanilla 1/1 deathtoucher and looks like filler. In the logged game it '
        'attacked twice and generated <b>six life of swing</b> through Blightfang while never '
        'dealing more than 1 damage. 26 of 31 creatures have deathtouch; the cheap ones are the '
        'engine\'s fuel, not padding.')]
F += [h3('THE BOARD-WIPE LOCK — Viridian Longbow + Thornbite Staff'),
      p('Put <b>both</b> on one deathtouch creature. Tap using <b>Longbow\'s</b> ability (free — '
        'Thornbite\'s own ping costs {2}, never use it): 1 damage, deathtouch makes it lethal, the '
        'creature dies, and Thornbite\'s <i>"whenever a creature dies, untap this creature"</i> '
        'untaps you. Repeat. <b>You destroy every creature your opponents control in one turn, at '
        'instant speed, for zero mana.</b> It is bounded by creatures dying — unlimited kills, not '
        'infinite face damage.'),
      p('<b>Put it on Vampire Nighthawk.</b> He is a Vampire <b>Shaman</b>, and Thornbite reads '
        '"whenever a Shaman creature enters, you may attach this Equipment to it" — so with the '
        'Staff already down it attaches <b>free</b>, skipping the {4} equip. He has flying, '
        'deathtouch and <b>lifelink</b>, so every ping also gains 1 life, which is a combo spark.'),
      b('The ability costs {T}, so the creature can\'t be summoning-sick — <b>Swiftfoot Boots\' '
        'haste fixes that.</b>'),
      b('Equipping is sorcery speed; the activations are instant speed, so you can wipe their '
        'attackers or blockers on their turn.'),
      b('Thornbite must be on the battlefield <b>before</b> the Shaman enters for the free attach.'),
      b('<b>Basilisk Collar</b> substitutes for native deathtouch, and adds lifelink.')]
F += [h3('Skullclamp — your draw engine, added 2026-10-22'),
      p('Equip {1}, the creature gets <b>+1/-1</b>, and when it dies you <b>draw two</b>. Six bodies '
        'have 1 toughness and die on the spot: Hired Poisoner, Rancid Rats, Foulmire Knight, '
        'Tinybones, Vampire of the Dire Moon — and Virtus, who you should <b>never</b> clamp. Each '
        'death also triggers <b>Arnyn</b> (drain 2, gain 2 — a spark), and <b>Avacyn returns '
        'nontoken creatures to the battlefield</b>, so with her out you draw two and keep the body.')]

F += [PageBreak()]

# ---------------------------------------------------------------- page 5
F += [h2('Mana — 29 Snow-Covered Swamps and why')]
F += [p('Every basic in the deck is a <b>Snow-Covered Swamp</b>. Its type line is '
        '"Basic Snow Land — Swamp", so it is still a Swamp for every card that checks, including '
        'Cabal Stronghold\'s "basic Swamp".')]
F += [table([
    ['Card', 'Scales off'],
    ['<b>Cabal Coffers</b>', '{2}, {T}: Add {B} for each <b>Swamp</b> you control'],
    ['<b>Cabal Stronghold</b>', '{3}, {T}: Add {B} for each <b>basic Swamp</b> you control'],
    ['<b>Crypt Ghast</b> / <b>Nirkana Revenant</b>', 'Whenever you tap a Swamp for mana, add an '
     'additional {B} — these stack with each other'],
    ['<b>Nykthos, Shrine to Nyx</b>', 'Your devotion to black (77 black pips in the deck)'],
    ['<b>Urborg, Tomb of Yawgmoth</b>', 'Makes every land a Swamp, so all of the above count them'],
    ['<b>Deserted Temple</b>', 'Untaps Cabal Coffers for a second activation'],
], [2.1*inch, 4.9*inch])]
F += [S(8)]
F += [h3('Extraplanar Lens — imprint on a Snow-Covered Swamp'),
      q('Imprint — When this artifact enters, you may exile target land you control.<br/>'
        'Whenever a land with <b>the same name</b> as the exiled card is tapped for mana, '
        '<b>its controller</b> adds one mana of any type that land produced.'),
      p('Because your basics are snow, the name it matches is "Snow-Covered Swamp" — which nobody '
        'else is running. Imprint it on a plain Swamp by mistake and you double every opponent\'s '
        'Swamps too. <b>The imprinted land is exiled permanently.</b>')]
F += [h3('Liliana of the Dark Realms'),
      p('Enters at <b>3 loyalty</b>, so the −3 kills her the turn you use it. The +1 fetches a '
        '<b>Swamp</b>, which makes Coffers, Stronghold, Nirkana and Crypt Ghast all better — it is '
        'not generic ramp. The −6 emblem gives every Swamp "{T}: Add {B}{B}{B}{B}": ten lands '
        'becomes forty mana, which is Torment of Hailfire for X=38. It needs three full turn '
        'cycles undefended. <b>Kaya\'s Ghostform enchants a creature OR a planeswalker</b> and is '
        'the only protection in the deck for her.')]

F += [PageBreak()]

# ---------------------------------------------------------------- page 6
F += [h2('Misplays to avoid')]
F += [b('<b>Pumping Virtus.</b> He is a 1/1 and the trigger is half their life regardless. Spend on '
        'evasion instead.'),
      b('<b>Forgetting Blightfang fires on attack.</b> Attack with every deathtoucher even into '
        'blockers — the drain and the lifegain happen before blocks.'),
      b('<b>Holding the combo waiting for a "safe" turn.</b> The loop needs a spark, and sparks '
        'come from the whole table. Deploy both halves and let someone else start it.'),
      b('<b>Imprinting Extraplanar Lens on a non-snow land.</b> That hands the doubling to any '
        'opponent running Swamps.'),
      b('<b>Taking the command zone when Virtus dies while enchanted by Kaya\'s Ghostform.</b> '
        'The replacement is a choice — decline it, let him hit the graveyard, and Ghostform '
        'returns him with no commander tax.'),
      b('<b>Using Liliana\'s −3 as removal early.</b> It kills her. Only do it if the board demands '
        'it or you have already given up on the emblem.'),
      b('<b>Blocking with a deathtoucher and then sacrificing it before damage.</b> Blocked stays '
        'blocked (CR 509.1h) — the attacker deals no damage, but you also deal none, so the '
        'deathtouch is wasted unless you needed the body elsewhere.'),
      b('<b>Trying to cast Exsanguinate off Stensian Sanguinist from your hand.</b> You cannot. It '
        'is a <b>preparation card</b> — "preparation cards can only be cast with their base '
        'characteristics." From hand it is only a {1}{B} 2/2. You get the Exsanguinate copy only '
        'after it becomes prepared, which needs the creature it gave deathtouch to <b>connect</b>.'),
      b('<b>Pointing Stensian\'s deathtouch grant at a creature that already has it.</b> Both it '
        'and Hooded Blightfang trigger on declaring attackers, and the grant resolves after '
        'Blightfang checks — so it never adds a Blightfang drain. Give it to Vito, Blight-Priest, '
        'Gray Merchant, Crypt Ghast or Nirkana Revenant instead.'),
      b('<b>Clamping Virtus.</b> He is 1/1. Skullclamp kills your commander.'),
      b('<b>Sitting back and never attacking.</b> Hooded Blightfang fires on <b>declaring '
        'attackers</b>. Three deathtouchers attacking drains each opponent 3 and gains you 3 before '
        'blockers exist — and that is a combo spark. Blocking a deathtoucher is a bad trade for '
        'them, so cheap attackers usually get through or trade up.')]
F += [h2('Opening hand — what to keep'),
      p('Keep anything with <b>three lands and a one- or two-drop deathtoucher</b>. The deck is 36 '
        'lands with heavy ritual support (Dark Ritual, Cabal Ritual, Culling the Weak, Bubbling '
        'Muck), so two-landers with a ritual and a tutor are keepable. Mulligan hands with no black '
        'source by turn two or with three cards costing five-plus.'),
      p('<b>Tutor priority early:</b> a mana engine (Cabal Coffers or Crypt Ghast) beats a combo '
        'half. You find combo pieces faster off a big mana turn than off a turn-three Vito.')]

F += [PageBreak()]

# ---------------------------------------------------------------- page 7
F += [h2('Tergrid — the haymaker, added 2026-10-22')]
F += [q('<b>Tergrid, God of Fright</b> — {3}{B}{B} — 4/5 Menace<br/>'
        'Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may '
        'put that card from a graveyard onto the battlefield under your control.<br/>'
        '<b>Tergrid\'s Lantern</b> — {3}{B} — Legendary Artifact<br/>'
        '{T}: Target player loses 3 life unless they sacrifice a nonland permanent or discard a '
        'card. · {3}{B}: Untap Tergrid\'s Lantern.')]
F += [b('<b>Torment of Hailfire</b> forces each opponent to lose 3 <i>unless they sacrifice a '
        'nonland permanent or discard a card</i>. With Tergrid out, <b>everything they give up '
        'comes to you.</b> X=5 into three opponents can hand you a dozen permanents.'),
      b('<b>Witch of the Moors</b> makes each opponent sacrifice a creature at your end step '
        'whenever you gained life. With Tergrid, you keep all three — every turn.'),
      b('The <b>Lantern</b> side is a mana sink for flood turns, and the 3 life loss is a spark.')]
F += [h2('Reference numbers')]
F += [table([
    ['', ''],
    ['Deck size', '100 — 36 lands (29 Snow-Covered Swamp + 7 nonbasic), 64 spells'],
    ['Creatures', '33, of which <b>22 have deathtouch printed</b>'],
    ['Curve', 'avg MV 2.77 — 1:15 · 2:15 · 3:16 · 4:10 · 5:6 · 6:1 · 8:1'],
    ['Black pips', '77 — relevant for Nykthos and Gray Merchant of Asphodel'],
    ['Game Changers', '<b>3 of 3 — Demonic Tutor, Vampiric Tutor, Tergrid. AT THE CAP; do not add '
                      'a fourth.</b>'],
    ['Draw', '9 sources — Phyrexian Arena, Black Widow, Read the Bones, Night\'s Whisper, Village '
             'Rites, Profane Insight, plus <b>Erebos, Ayara and Skullclamp</b> (all repeatable)'],
    ['Removal', '3 dedicated (Go for the Throat, Snuff Out, Feed the Swarm), plus Witch of the '
                'Moors and The Darkness Crystal'],
    ['Tutors', '4 — Demonic Tutor, Vampiric Tutor, Grim Tutor, Diabolic Intent, plus Sidisi'],
], [1.4*inch, 5.6*inch])]
F += [S(10)]
F += [h2('Cards whose text people get wrong'),
      b('<b>Snow-Covered Swamp</b> is a Swamp. Everything that says Swamp, including "basic Swamp", '
        'reads it normally.'),
      b('<b>Extort</b> triggers once per spell you cast, and you may pay once per trigger. Two '
        'extort creatures means two separate triggers on the same spell.'),
      b('<b>Gray Merchant of Asphodel</b> counts <b>devotion</b>, which is black mana symbols on '
        'permanents you control — not cards, not Swamps.'),
      b('<b>The Darkness Crystal</b> replaces an opponent\'s nontoken creature dying with exile and '
        '<b>gains you 2 life</b>. That is a combo spark every time one of their creatures dies, and '
        'it shuts off their recursion.'),
      b('<b>Witch of the Moors</b> checks at your end step whether you gained life <i>that turn</i>. '
        'Any extort payment or lifelink hit turns it on.'),
      b('<b>Torment of Hailfire</b> gives each opponent the choice each iteration. Against a board '
        'full of permanents a small X does very little; it is a finisher, not a value spell.')]
F += [S(10), Paragraph('Built from decks/deathtouch_reference.md. Every card\'s oracle text '
                       're-read from scryfall.db on 2026-10-21.', SUB)]

doc = SimpleDocTemplate('decks/deathtouch_play_guide.pdf', pagesize=LETTER,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.7*inch, bottomMargin=0.7*inch,
                        title='Virtus the Veiled — Mono-Black Deathtouch Drain Play Guide',
                        author='mtg-card-db')
doc.build(F)
print('built decks/deathtouch_play_guide.pdf')

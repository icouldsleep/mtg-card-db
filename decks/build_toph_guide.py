"""Rebuild the Toph play guide as a single PDF.

Faithful reproduction of the Sept 21 nine-page guide, with tables restored
(they did not survive text extraction from the original), plus two sections it
never covered: the fetchland/landfall package and the Forge AI finding.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

ss = getSampleStyleSheet()
TITLE = ParagraphStyle('TITLE', parent=ss['Heading1'], fontSize=19, spaceAfter=2, leading=23)
SUB   = ParagraphStyle('SUB', parent=ss['BodyText'], fontSize=10.5, textColor=colors.HexColor('#444444'), spaceAfter=10)
H2    = ParagraphStyle('H2', parent=ss['Heading2'], fontSize=13, spaceBefore=14, spaceAfter=6, textColor=colors.HexColor('#1a1a1a'))
H3    = ParagraphStyle('H3', parent=ss['Heading3'], fontSize=10.5, spaceBefore=10, spaceAfter=4)
BODY  = ParagraphStyle('BODY', parent=ss['BodyText'], fontSize=9.5, leading=13.2, spaceAfter=5)
BULL  = ParagraphStyle('BULL', parent=BODY, leftIndent=13, bulletIndent=3, spaceAfter=3)
NUM   = ParagraphStyle('NUM', parent=BODY, leftIndent=15, bulletIndent=3, spaceAfter=3)
QUOTE = ParagraphStyle('QUOTE', parent=BODY, leftIndent=12, rightIndent=12, fontName='Helvetica-Oblique',
                       textColor=colors.HexColor('#333333'), spaceBefore=4, spaceAfter=7)
CELL  = ParagraphStyle('CELL', parent=BODY, fontSize=8.5, leading=11, spaceAfter=0)
CELLB = ParagraphStyle('CELLB', parent=CELL, fontName='Helvetica-Bold')
NOTE  = ParagraphStyle('NOTE', parent=BODY, fontSize=8, textColor=colors.grey)

def T(rows, widths):
    data = [[Paragraph(c, CELLB if i == 0 else CELL) for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#ececec')),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#a0a0a0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 5), ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7f7f7')]),
    ]))
    return t

def b(txt):  return Paragraph(txt, BULL, bulletText='•')
def n(i, txt): return Paragraph(txt, NUM, bulletText=f'{i}.')
def p(txt):  return Paragraph(txt, BODY)

S = []
W = 6.5 * inch

S.append(Paragraph("Toph, the First Metalbender", TITLE))
S.append(Paragraph("Naya land-creature combat deck &mdash; Bracket 3 &mdash; how to actually play it", SUB))
S.append(Paragraph('"Nontoken artifacts you control are lands in addition to their other types. (They don\'t gain '
                   'the ability to {T} for mana.) At the beginning of your end step, earthbend 2."', QUOTE))

S.append(Paragraph("The one sentence version", H2))
S.append(p("Your commander turns your artifacts into lands, and earthbend turns lands into creatures. So your "
           "mana base is your army, your artifacts are your mana base, and both of them grow every single end "
           "step for free. <b>Nothing else in the deck matters until Toph resolves</b> &mdash; deploy her turn 3 "
           "or 4, every game."))

S.append(Paragraph("Earthbend, exactly", H2))
S.append(Paragraph('"Earthbend N": Target land you control becomes a 0/0 land creature with haste in addition to '
                   'its other types. Put N +1/+1 counters on it. When it dies or is exiled, return it to the '
                   'battlefield tapped under your control.', QUOTE))
for x in [
  "<b>Haste is automatic.</b> Without it an animated land could not tap for mana, attack, or be sacrificed the turn you animate it.",
  "<b>No duration.</b> An earthbent land stays a creature permanently.",
  "<b>It grants the land type itself.</b> This is the important one: an artifact you have already earthbent stays a land creature even if Toph dies. Spend your early earthbends on artifacts, not on real lands &mdash; your real lands are already lands.",
  "<b>It returns from graveyard or exile ONLY.</b> Bounce and tuck are permanent losses, earthbent or not.",
  "<b>Sacrificing counts as dying</b>, which is what makes Zuran Orb an engine instead of a lifegain card.",
  "<b>Earthbends stack.</b> Counters accumulate; the base 0/0 reset is a no-op after the first.",
  "It does not give the land a colour, and it does not remove abilities &mdash; an earthbent Ornithopter still flies.",
]: S.append(b(x))
S.append(Spacer(1,4))
S.append(p("<b>MDFC trap.</b> Bala Ged Sanctuary has only its front face in the graveyard, and that face is a "
           "Sorcery. A sorcery cannot be put onto the battlefield, so earthbend's return does nothing for it. "
           "<b>Never feed a modal double-faced land to Zuran Orb.</b>"))

S.append(Paragraph("What Toph does and does not trigger", H2))
for x in [
  "<b>Nontoken artifacts entering DO trigger landfall</b>, because the type change applies as they enter. Casting one does not use your land drop.",
  "<b>A permanent already on the battlefield becoming a land triggers nothing.</b> When Toph resolves and converts your existing artifacts, you get no landfall burst. Same when Gift of Immortality returns her.",
  "<b>The parenthetical is reminder text.</b> Artifacts can gain mana abilities from elsewhere &mdash; Chromatic Lantern and Great Divide Guide both grant them to lands, and your artifacts are lands.",
  "<b>Tokens are never lands:</b> Clues, Treasures, Food, Cats, Beasts, Plants, Spiders, Insects, Constructs.",
]: S.append(b(x))

S.append(PageBreak())

S.append(Paragraph("The fetch package &mdash; six fetches, seven landfall payoffs", H2))
S.append(p("<b>Every fetch is two landfall triggers</b>: once when the fetch itself enters, once when the land it "
           "finds enters. That is why a fetch beats a basic in this deck, and why you never cut one for a basic."))
S.append(T([["Fetch","The fetch itself","The land it finds"],
            ["Arid Mesa","enters untapped","<b>untapped</b>"],
            ["Prismatic Vista","enters untapped","<b>untapped</b>"],
            ["Windswept Heath","enters untapped","<b>untapped</b>"],
            ["Wooded Foothills","enters untapped","<b>untapped</b>"],
            ["Grasslands","<b>enters tapped</b>","<b>untapped</b>"],
            ["Mountain Valley","<b>enters tapped</b>","<b>untapped</b>"]],
           [1.7*inch, 2.4*inch, 2.4*inch]))
S.append(Spacer(1,6))
S.append(p("<b>Grasslands and Mountain Valley are the ones that get misread.</b> The land itself enters tapped, "
           "but what it <i>fetches</i> comes in untapped &mdash; their search text has no tapped clause. Slower to "
           "deploy, not slower to pay off."))
S.append(p("<b>Seven landfall payoffs see both triggers:</b> Avenger of Zendikar, Evolution Sage, Felidar Retreat, "
           "Lotus Cobra, Rampaging Baloths, Scute Swarm, and Toph, Earthbending Master."))
S.append(p("<b>Traveling Chocobo doubles both halves.</b> Its text: <i>\"If a land or Bird you control entering the "
           "battlefield causes a triggered ability of a permanent you control to trigger, that ability triggers an "
           "additional time.\"</i> Each of the two landfall events becomes two, so <b>one fetch is four landfall "
           "triggers</b>. With Scute Swarm out at six or more lands, every one of those four makes a <i>copy of "
           "Scute Swarm</i> &mdash; a single fetch is four new Swarms."))

S.append(Paragraph("Only 6 of your 16 artifacts make mana", H2))
S.append(p("Sol Ring, Arcane Signet, The Mind Stone, Chromatic Lantern, Thran Dynamo, Twitching Doll. The other ten "
           "are lands for landfall and earthbend purposes only. <b>Chromatic Lantern and Great Divide Guide are the "
           "highest-leverage permanents in the deck</b> because they turn that whole pile into real mana."))

S.append(Paragraph("Getting more than one earthbend a turn", H2))
S.append(p("Toph gives you earthbend 2 at your end step. That is the floor, not the ceiling."))
S.append(Paragraph("Only two cards multiply Toph's end step", H3))
S.append(T([["Card","What it does"],
            ["Annie Joins Up","If a triggered ability of a legendary creature you control triggers, it triggers an additional time. Free, automatic, every turn. Also deals 5 damage to a creature on entry."],
            ["Strionic Resonator","{2}, {T}: copy a triggered ability already on the stack. Once per turn cycle."]],
           [1.7*inch, 4.8*inch]))
S.append(Spacer(1,6))
S.append(p("Both out is <b>earthbend 2 three separate times</b>, each with its own target. They are separate "
           "instances, not one earthbend 6. Total counters come out the same either way because your boosters apply "
           "per event &mdash; the choice is bodies versus size. Two medium land creatures beat one big one most "
           "turns, because Toski and Ohran Frostfang draw per creature that connects."))
S.append(Paragraph("Using Strionic Resonator correctly", H3))
for i, x in enumerate([
  "<b>Beginning of your end step.</b> Toph's ability triggers and you choose its target land now.",
  "<b>Hold priority.</b> Activate the Resonator, targeting that trigger on the stack.",
  "The copy resolves first with a new target, then the original resolves."], 1):
    S.append(n(i, x))
S.append(Spacer(1,3))
S.append(p("You cannot pre-activate it &mdash; the trigger must already be on the stack. That means holding up {2} "
           "through your whole turn, which competes directly with The Stasis Coffin's {2}."))
S.append(Paragraph("Annie doubles more than the commander", H3))
S.append(p("Every legendary creature you control: Toph Hardheaded Teacher (earthbend 2 per spell cast instead of 1), "
           "Toph Earthbending Master, Toph Greatest Earthbender, Avatar Kyoshi and Bumi Unleashed."))
S.append(Paragraph("Two cards that look like they should double Toph and do not", H3))
S.append(p("<b>Traveling Chocobo</b> only fires when a land or Bird enters. Toph's end step trigger is not caused by "
           "a land entering, so Chocobo never touches it. Chocobo doubles your landfall package only &mdash; which, "
           "as above, is still a great deal across six fetches."))
S.append(p("<b>What else to point them at.</b> They hit different pools. Annie only sees legendary creatures, but "
           "she is free and always on. The Resonator sees any triggered ability you control, but costs {2} and a "
           "tap, once per turn cycle."))

S.append(PageBreak())

S.append(Paragraph("Annie's best non-Toph targets", H2))
S.append(T([["Legendary creature","Doubled, it becomes"],
 ["Kodama of the East Tree","Two free permanents out of your hand per permanent entering. Under Toph every artifact you cast is a permanent entering, so casting Sol Ring drops two more things free. <b>The biggest one on the list.</b>"],
 ["Bumi, Unleashed","Two extra combat phases, and untaps all your lands twice. Often just lethal."],
 ["Toski, Bearer of Secrets","2 cards per creature that connects. Six attackers is 12 cards."],
 ["The Earth King","Twice as many basics fetched when power-4 creatures attack &mdash; twice the landfall."],
 ["Avatar Kyoshi","Earthbend 8 twice each combat, two separate targets, untapping both lands."],
 ["Toph, Hardheaded Teacher","Earthbend 2 per spell you cast instead of 1."],
 ["Toph, Earthbending Master","Two experience counters per land drop, so his attack earthbend grows twice as fast."]],
 [1.9*inch, 4.6*inch]))

S.append(Paragraph("Strionic Resonator's best targets", H2))
S.append(p("These are the ones Annie cannot reach, ranked by what the copy is actually worth:"))
S.append(T([["Trigger","The copy gives you"],
 ["Kalonian Hydra attacks","It doubles counters on each creature you control, so copying it quadruples them. A board of 20/20 lands becomes 80/80 each, and Toph Greatest Earthbender's double strike counts that twice. <b>Hold the Resonator for this.</b>"],
 ["Craterhoof Behemoth ETB","+X/+X twice, X being your creature count each time. With eight creatures that is +16/+16 to the board instead of +8/+8. Craterhoof is not legendary, so Annie never sees it &mdash; the Resonator is your only way to double it."],
 ["Avenger of Zendikar ETB","Double the Plants, one per land twice. Each Plant is also an Aura Shards trigger and a Kodama trigger."],
 ["Evolution Sage landfall","A second proliferate, which through the full counter stack is another 16 counters on every permanent you pick."],
 ["Aura Shards","Destroy two artifacts or enchantments off one creature entering."],
 ["Scute Swarm landfall","An extra copy of Scute Swarm once you are at six or more lands."],
 ["Terrasymbiosis","A second draw batch in a turn it has already fired."],
 ["Sylvan Library draw step","Two more cards on top of the two, at 4 life each to keep."]],
 [1.9*inch, 4.6*inch]))
S.append(Spacer(1,6))
S.append(p("<b>Not worth copying.</b> The Ozolith &mdash; the bank is empty after the first move. Gift of "
           "Immortality &mdash; the creature is already back. Haywire Mite's death trigger is 2 life. Lotus Cobra "
           "is one mana. Spend the {2} on the Coffin instead."))
S.append(Spacer(1,4))
S.append(p("With both out, Toph's end step gives you <b>THREE</b> instances, not four. Annie makes it trigger twice "
           "&mdash; two separate abilities on the stack &mdash; and the Resonator copies one of them. Same for "
           "Hardheaded Teacher and everything else Annie touches."))

S.append(PageBreak())

S.append(Paragraph("Every repeatable earthbend source", H2))
S.append(T([["Source","Rate"],
 ["Toph, the First Metalbender","Earthbend 2 at your end step, free"],
 ["Toph, Hardheaded Teacher","Earthbend 1 per spell you cast, free &mdash; the highest volume source"],
 ["Toph, Earthbending Master","Earthbend X per attack, X = your experience counters"],
 ["Avatar Kyoshi, Earthbender","Earthbend 8 at each combat, then untaps that land"],
 ["Ba Sing Se","{2}{G}, {T}: earthbend 2, sorcery speed, every turn"]],
 [2.3*inch, 4.2*inch]))
S.append(Spacer(1,6))
S.append(p("One-shots on top of that: Solid Ground, Earthbending Student, Badgermole Cub, Bumi Unleashed, "
           "Rockalanche, and the two Tophs' enter-the-battlefield triggers."))
S.append(p("<b>Bumi, Unleashed is the sleeper.</b> Combat damage untaps all your lands and gives you an additional "
           "combat phase where only land creatures can attack. That re-triggers Toph Earthbending Master's attack "
           "earthbend and Avatar Kyoshi's combat trigger a second time &mdash; and Annie doubles both again."))

S.append(Paragraph("The three loops", H2))
S.append(p("All three work the same way: earthbend it, use it up, earthbend returns it."))
S.append(Paragraph("The Stasis Coffin &mdash; take zero damage every turn", H3))
S.append(Paragraph('"{2}, {T}, Exile The Stasis Coffin: You gain protection from everything until your next turn."', QUOTE))
S.append(p("Exiling is part of the cost, so on its own it is one use. Under Toph it is a land, so earthbend it and "
           "the delayed trigger returns it from exile."))
for i, x in enumerate([
  "Your turn: the Coffin is earthbent from last end step and untapped.",
  "Attack with everything. You do not need blockers.",
  "Post-combat: {2}, tap, exile. It returns tapped. You gain protection.",
  "Beginning of your end step: Toph's earthbend 2 re-arms it.",
  "Opponents' turns: you take zero damage.",
  "Your untap step: it untaps, already earthbent. Repeat."], 1):
    S.append(n(i, x))
S.append(Spacer(1,3))
S.append(p("<b>What it does not stop:</b> your creatures still die, life loss that is not damage, non-targeted "
           "effects (\"each player sacrifices\"), and your own permanents being destroyed. It protects you, not the "
           "board. Commander damage and infect are both damage, so both are prevented."))
S.append(Paragraph("Ichor Wellspring &mdash; two cards a turn", H3))
S.append(Paragraph('"When this artifact enters or is put into a graveyard from the battlefield, draw a card." '
                   'One trigger, two conditions, both fire every time.', QUOTE))
S.append(p("Earthbend it, then sacrifice it to Zuran Orb (it is a land, so Zuran Orb can): draw 1 plus 2 life, "
           "earthbend returns it, it enters so draw 1 plus a landfall trigger. Re-earthbend at end step and repeat. "
           "<b>It must be earthbent before you sacrifice it</b>, or it stays in the graveyard and you are down a card."))
S.append(Paragraph("Zuran Orb &mdash; a landfall engine, not a lifegain card", H3))
S.append(p("{0} to cast, free to activate, instant speed. Sacrifice an earthbent land: 2 life, it returns tapped, "
           "landfall trigger. Once per earthbend. Doubled by Traveling Chocobo. It is also the right response to a "
           "blocker that is about to die &mdash; you keep the land and gain the life. <b>Only sacrifice things that "
           "are currently earthbent.</b> An un-earthbent artifact dies for good."))

S.append(PageBreak())

S.append(Paragraph("Counter math &mdash; always add before you double", H2))
S.append(p("Five cards modify counters as they are placed. They are replacement effects and <b>you</b> choose the "
           "order (CR 616.1)."))
S.append(T([["Card","Effect","Applies to"],
 ["Hardened Scales","+1","+1/+1 counters on a creature"],
 ["Solid Ground","+1","+1/+1 counters on a permanent"],
 ["Ozolith, the Shattered Spire","+1","+1/+1 counters on an artifact or creature"],
 ["Branching Evolution","x2","+1/+1 counters on a creature"],
 ["Doubling Season","x2","any counter type on a permanent, plus tokens"]],
 [2.1*inch, 0.8*inch, 3.6*inch]))
S.append(Spacer(1,7))
S.append(Paragraph("Earthbend 2 with all five out: &nbsp; <b>2 &rarr; 3 &rarr; 4 &rarr; 5 &rarr; 10 &rarr; 20</b>",
                   ParagraphStyle('MATH', parent=BODY, fontSize=11, alignment=1, spaceAfter=7)))
S.append(p("<b>Take the three plus-ones first, then both doublers.</b> Reversing the order gives you 5 instead of 20."))
for x in [
  "Only Doubling Season touches non-+1/+1 counters, so it is the one that doubles Twitching Doll's nest counters. Neither it nor the others touch experience counters, which sit on you, not a permanent.",
  "<b>Proliferate is affected by all five.</b> Evolution Sage proliferates on every land drop, and proliferate puts counters &mdash; so one proliferate on a creature that already has a counter becomes 16 through the full stack, on every permanent you choose at once.",
  "<b>Kalonian Hydra is not a sixth multiplier.</b> The five above modify counters as they are placed. Hydra doubles counters already on every creature you control when it attacks. Nothing else does that.",
]: S.append(b(x))

S.append(Paragraph("Twitching Doll &mdash; turning the counter pile into a board", H2))
S.append(Paragraph('"{T}: Add one mana of any colour. Put a nest counter on this creature."<br/>'
                   '"{T}, Sacrifice: Create a 2/2 green Spider with reach for each counter on it."', QUOTE))
S.append(p("It says <b>each counter</b>, not each nest counter. So every +1/+1 counter earthbend put on it becomes a "
           "Spider. A Doll sitting on 20 counters cashes in for twenty 2/2 reach Spiders, forty with Doubling Season "
           "doubling the tokens. Sacrificing is dying, so earthbend returns the Doll to do it again. Every Spider "
           "entering is also an Aura Shards trigger."))

S.append(Paragraph("Urza's Saga", H2))
S.append(p("Chapter II makes Constructs that get +1/+1 for each artifact you control, and you run 16. Chapter III "
           "finds a card with actual <b>mana cost</b> {0} or {1}, not mana value &mdash; your five legal targets are "
           "Zuran Orb, Ornithopter, Sol Ring, The Ozolith and Haywire Mite. Ozolith the Shattered Spire at {1}{G} "
           "does not qualify."))
S.append(p("<b>Earthbend it before chapter III resolves.</b> The Saga sacrifices itself, sacrificing is dying, and "
           "earthbend returns it as a fresh object with zero lore counters. It restarts at chapter I. Without an "
           "earthbend on it, it is a land that deletes itself in three turns."))

S.append(Paragraph("The earthbend-target bottleneck", H2))
S.append(p("Four cards want a target every turn. Toph gives you one, Annie two, Strionic Resonator three, Ba Sing Se "
           "a fourth for {2}{G}. Rank them by what you need that turn:"))
S.append(T([["Spend it on","You get"],
 ["The Stasis Coffin","Take zero damage until your next turn"],
 ["Ichor Wellspring","2 cards"],
 ["Urza's Saga","Restart the Saga for another tutor and more Constructs"],
 ["Ornithopter","A flying attacker that costs no mana to swing with"]],
 [2.1*inch, 4.4*inch]))

S.append(PageBreak())

S.append(Paragraph("Card draw &mdash; what actually draws", H2))
S.append(p("Half your draw needs combat damage. Know which half."))
S.append(Paragraph("Needs combat damage to a player", H3))
S.append(T([["Card","Rate"],
 ["Toski, Bearer of Secrets","per creature that connects"],
 ["Ohran Frostfang","per creature that connects, and attackers gain deathtouch"],
 ["Kutzil, Malamet Exemplar","once per player, batched &mdash; <b>NOT</b> per creature"]],
 [2.3*inch, 4.2*inch]))
S.append(Spacer(1,6))
S.append(p("Kutzil uses the \"whenever one or more creatures\" template, so six attackers into one opponent draws "
           "<b>one</b> card. It triggers separately per player, so a three-way alpha strike draws three. Its real "
           "value is the top line: <b>\"your opponents can't cast spells during your turn\"</b> &mdash; a Silence "
           "protecting every attack you make."))
S.append(p("<b>Toph, Greatest Earthbender gives land creatures DOUBLE STRIKE</b>, which is two combat damage steps. "
           "All three of these trigger twice. Six land creatures with her out is twelve Toski cards in one combat."))
S.append(Paragraph("Does not need combat", H3))
S.append(T([["Card","Rate"],
 ["Terrasymbiosis","Draw = counters placed, once per turn. Toph's free end step alone is 2"],
 ["Sylvan Library","2 extra at your draw step, 4 life each to keep"],
 ["Ichor Wellspring","2 per loop cycle"],
 ["Garruk's Uprising","On a power-4 creature entering, not attacking"]],
 [2.3*inch, 4.2*inch]))
S.append(Spacer(1,6))
S.append(p("<b>Garruk's draw is weaker than it looks.</b> Earthbent lands do not trigger it &mdash; they were "
           "already on the battlefield and never \"enter.\" Live triggers are Rampaging Baloths' Beasts, The Earth "
           "King's Bear, Kodama's drops, Bumi, Avatar Kyoshi, Craterhoof and Kalonian Hydra. Its trample clause is "
           "the main reason it is in the deck."))

S.append(Paragraph("Removal and Aura Shards", H2))
S.append(T([["Type","Cards"],
 ["Artifact / enchantment","Haywire Mite, Chaos Warp, Beast Within, Aura Shards"],
 ["Creature (spot)","Path to Exile, Swords to Plowshares, Beast Within, Chaos Warp, Annie Joins Up"],
 ["Board wipe","Planar Outburst &mdash; the only one, and nothing can tutor it"],
 ["Land","Strip Mine, Wasteland"]],
 [1.9*inch, 4.6*inch]))
S.append(Spacer(1,6))
S.append(p("<b>Planar Outburst destroys all NONLAND creatures.</b> Your earthbent lands are land creatures. They "
           "live, everyone else's board dies. It is a one-sided wrath in this deck."))
S.append(p("<b>Aura Shards</b> destroys an artifact or enchantment whenever a creature you control enters. Avenger "
           "of Zendikar entering with eight lands is eight destroy triggers on one card. A Twitching Doll on twenty "
           "counters is twenty. Earthbent lands do not trigger it &mdash; a permanent already on the battlefield "
           "becoming a creature does not enter."))

S.append(PageBreak())

S.append(Paragraph("Protecting the board, and protecting Toph", H2))
S.append(p("These are two different problems and the deck is good at one of them."))
S.append(Paragraph("Board protection &mdash; nine pieces", H3))
S.append(T([["Card","Covers"],
 ["Heroic Intervention","Hexproof and indestructible on ALL permanents, lands included"],
 ["Flawless Maneuver","Free with a commander out; indestructible on creatures"],
 ["The Stasis Coffin","Protection from everything, repeatable via the loop"],
 ["Iroas, God of Victory","Prevents all damage to attackers; indestructible; not a creature, so it dodges creature removal"],
 ["Akroma's Memorial","Protection from black and red, plus flying, first strike, vigilance, trample, haste"],
 ["Lightning Greaves","Shroud &mdash; stops your own targeting too, unlike hexproof"],
 ["Gift of Immortality","Recurs a creature &mdash; see the trap below"],
 ["Kutzil","Opponents cannot cast spells during your turn"],
 ["Earthbend itself","Every animated land returns from graveyard or exile"]],
 [1.9*inch, 4.6*inch]))
S.append(Spacer(1,6))
S.append(p("<b>Cyclonic Rift overloaded barely touches you.</b> It returns each nonland permanent. Under Toph your "
           "artifacts are lands and your earthbent lands are lands, so Sol Ring, Thran Dynamo, The Ozolith, "
           "Twitching Doll and Akroma's Memorial all stay. Toph herself is a creature and does get bounced."))
S.append(Paragraph("The Gift of Immortality trap", H3))
S.append(p("The commander rule is a <b>may</b>: \"if your commander would be put into a zone other than the stack or "
           "battlefield, you may put it into the command zone instead.\" Take that option and Toph never dies, Gift "
           "never triggers, and you pay +2 tax."))
S.append(p("<b>Decline the command zone and let her hit the graveyard.</b> Gift returns her to the battlefield "
           "immediately, at no tax, and Gift itself comes back attached at the next end step. It recurs forever."))
S.append(p("It does not cover exile. Swords to Plowshares and Path to Exile still get her, and only Heroic "
           "Intervention and Lightning Greaves stop those. <b>Two cards in 99 &mdash; the deck's biggest structural "
           "risk.</b>"))

S.append(PageBreak())

S.append(Paragraph("How to play the deck", H2))
S.append(p("In order, every game."))
for i, x in enumerate([
  "<b>Deploy Toph as fast as possible.</b> Everything scales off her. Turn 3-4 is the target. You have eleven accelerants at two mana or less &mdash; 57% of opening sevens have one, 71% by turn three on the draw.",
  "<b>Earthbend artifacts, not real lands.</b> Earthbend grants the land type itself, so an animated artifact survives Toph dying. Ornithopter first &mdash; it flies, and swinging with it costs you nothing because it makes no mana.",
  "<b>Spread by default, concentrate to close.</b> Wide boards feed Toski and Ohran (per creature), The Earth King (per attacker) and Aura Shards (per token). One giant land is a single removal spell away from nothing.",
  "<b>Hold up {2} if Strionic Resonator or The Stasis Coffin is out.</b> They compete for the same mana &mdash; you usually only afford one per turn.",
  "<b>Alpha strike behind the Coffin.</b> Swing with everything, then exile it post-combat. You take zero damage until your next turn, so you never need blockers."], 1):
    S.append(n(i, x))

S.append(Paragraph("The kill turn", H2))
S.append(p("Concentration is the finish, not the build-up. When you are going for it:"))
for x in [
  "<b>Kalonian Hydra</b> attacks and doubles the counters already on every creature you control.",
  "<b>Toph, Greatest Earthbender</b> gives land creatures double strike, so every counter counts twice.",
  "<b>Craterhoof Behemoth</b> gives trample and +X/+X where X is your creature count.",
  "<b>Bumi Unleashed</b> connecting untaps all your lands and gives an extra combat with land creatures only.",
  "<b>Sphere Grid</b> means anything with a counter already has trample and reach.",
]: S.append(b(x))

S.append(Paragraph("Mulligan guide", H2))
S.append(p("34 land-capable cards in 99. 23.5% of opening sevens have 0-1 lands, 45.3% have three or more. A keepable "
           "hand is three lands, or two lands plus an accelerant &mdash; that is <b>64.5% of hands</b>."))
for x in [
  "Mulligan hands with <b>no green source</b>. Green is 51 of your 68 pips.",
  "Mulligan hands with <b>no play before turn four</b>. Toph costs 4 and nothing works without her.",
  "<b>Remember the artifacts are not lands in your opening hand.</b> Before Toph resolves, Ornithopter is a 0/2 and Sol Ring is a mana rock. The 50 effective-land figure is a turn-six number.",
  "Planar Outburst at {3}{W}{W} is your only awkward cast &mdash; white is 15 sources.",
]: S.append(b(x))

S.append(Paragraph("Three things people get wrong at the table", H2))
for x in [
  "<b>Bouncing or tucking an earthbent land loses it permanently.</b> Earthbend only returns things from the graveyard or exile. Do not assume it is safe from everything.",
  "<b>Annie gives you two separate earthbends, not one bigger one.</b> Choose targets separately. You can split or stack.",
  "<b>Sacrificing an un-earthbent artifact to Zuran Orb kills it for good.</b> Earthbend first, always.",
]: S.append(b(x))

S.append(Spacer(1,14))
S.append(Paragraph("All card text verified against scryfall.db. Bracket 3 confirmed against "
                   "game_changers.md &mdash; three Game Changers: Aura Shards, Enlightened Tutor, "
                   "Smothering Tithe. Last revised Sept 28 2026.",
                   NOTE))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.75*inch, 0.45*inch,
        "Toph, the First Metalbender play guide  -  all card text verified against scryfall.db")
    canvas.drawRightString(LETTER[0]-0.75*inch, 0.45*inch, str(doc.page))
    canvas.restoreState()

doc = SimpleDocTemplate("decks/toph_play_guide.pdf", pagesize=LETTER,
    leftMargin=0.75*inch, rightMargin=0.75*inch, topMargin=0.7*inch, bottomMargin=0.75*inch,
    title="Toph, the First Metalbender - play guide", author="mtg-card-db")
doc.build(S, onFirstPage=footer, onLaterPages=footer)
import os
print("wrote decks/toph_play_guide.pdf:", os.path.getsize("decks/toph_play_guide.pdf"), "bytes")

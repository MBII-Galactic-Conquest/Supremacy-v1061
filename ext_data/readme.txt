This is the readme for properly indexing our classes for the Galactic Conquest.

EXAMPLE: s_1ra_sold

SO far, there is currently 10 eras in the handbook.
1, will be used for the Galactic Civil War.

"s_" = Supremacy
"1ra" = Era 1, Rebel Alliance(Team)
"1em" = Era 1, Galactic Empire(Team)
"sold" = class name, this is the common soldier


Eras:
1 - Galactic Civil War (ra/em)
2 - Clone Wars (Phase I) (ca/da)
3 - Mandalorian Wars (or/mf)
4 - Jedi Civil War (or/re)
5 - Darth Malgus' Sith Empire (or/me)
6 - EU/Legends Thrawn's Ascendancy // Imperial Remnants (nr/eh)
7 - EU/Legends Fall of The Black Sun // Criminal Syndicates VS New Republic (nr/bs)
8 - Rise of the First Order // Disney Canon (re/fo)
9 - Rise of the Exile // KOTOR II Dark Wars (ex/st)
10 - Rise of the Empire // Andor Early GCW Era (an/em)
11 - Lego Star Wars // Clones vs Stormtroopers (lca/lem)
12 - Shadows of Dathomir // Halloween Months Zombie Survival (su/zo)
13 - Hordes of the Yuuzhan Vong (ga/vo)
14 - Rise of Darth Krayt // Sith-Imperial War (fel/kr)
15 - Conquest of the Eternal Throne // SWTOR (et/or/se)
16 - Conquest of the Infinite Empire // Rakatan Conquest (ie/se)
17 - Clone Wars (Phase II) (ca/da)

bd1 - battle droid
bd2 - heavy Rocket
bd3 - mg droid
bd4 - ofc droid
bd5 - bd sniper
bd6 - flm droid

mg1 - magna guard ph1
pd1 - deka ph1
ps1 - sbd ph1

cs2 - clone heavy rocket
cs3 - clone heavy mg
cs4 - clone veteran longrifle
cs5 - clone veteran sharpshooter

s - soldier supplies
b - soldier bacta
g - soldier garrison
bg - soldier bacta & garrison
c - soldier combat shielding
sg - sold supplies & garrison
bs - sold bacta & supplies
cg - sold shielding & garrison
cs - sold shielding & supplies
bc - sold bacta & shielding
eb - soldier enhanced blasters
l - generic leader
x - named leader
m - soldier mvp

en - soldier energy boost
eng - soldier energy & garrison
ens - soldier energy & supplies
enb - soldier energy & bacta
enc - soldier energy & combat shielding 

Neutral Factions:

(Neutral Factions get soldier and officer only. 20:10 lives)

Era 3 & 4-
(Czerka)

Czerka Corporation (cz)

Era 6-
(Remnants)

Warlord Zsinj (wz)
Pentastar Alignment (pa)
Veer's Remnant (vr)
Eriadu Authority (ea)
Corporate Sector Authority (ca)
Operation Shadow Hand (sh)
Hapes Consortium (hc)
Greater Maldrood (gm)
Empire Reborn (er)

Era 7-
(Criminal Syndicates)

Pykes Syndicate (ps)
Hutt Cartel (hc)
Crimson Dawn (cd)
Crymorah Syndicate (cs)

Era 10-
(Corporations)

Corporate Sector Authority (ca)
Pre-Mor Enforcers (pm)

Siegeteam Specifics:

g_siegeteam1 "sup_good1" && g_siegeteam "sup_evil1"
/mbmode 4

Numerical index is based on the eras above.

Neutral Planet Siegeteam Specifics:

"Sup_NTat1"

Sup - Supremacy
N - Neutral/Planet Defense
Tat - Planet Name
1 - Era

Useful Binds:

+set fs_dirbeforepak "1" in command line of MBII launcher

/bind - timescale 1
/bind = timescale 10
/bind [ newround
/bind ] exec c

c.cfg
devmap mb2_duel_dantooine

Useful Information:

MBAssets3 (legends /ext_data/)
MBAssets2 (weapon models & hud)
MBAssets (character & weapon sounds)
MBModelsX (character models & sounds)

Base Classes:
(BH Kick given to soldiers, engineers, spies, jet troopers, and heavy troopers in eras 1, 2, 6, 7, 8)
(Vibroblades given to soldiers, engineers, spies, jet troopers, and heavy troopers in eras 3, 4, 5)
(Applicable to the 4 character limit bonus per team.)
(Unlocked with credits in the handbook.)

"sold" == Soldier (default, common, no limit)
Lives, 3

"eng" == Engineer (special unit)
Lives, 2

"spy" == Spy (special unit)
Lives, 1

"hvr" == Heavy Trooper, Rocket (special unit)
Lives, 2

"hvg" == Heavy Trooper, MG (special unit)
Lives, 2

"jet" == Jet Trooper, A280/T21, (special unit)
Lives, 2

"ofc" == Officer, Rally (special unit)
Lives, 2

Bonus Specific:

"solb" == Soldier, Bacta (default, common, no limit)
Lives, 3 - Given Small Bacta

"med" == Medic (special unit)
Lives, 1

"fw1" == Generic Force Wielder, Swordsman (special unit)
Lives, 1

"fw2" == Generic Force Wielder, Sorcerer (special unit)
Repulse
Lives, 1

"hr1" == Generic Hero, Sniper (leader)
Lives, 1

"hr2" == Generic Hero, Sustain (leader)
Lives, 1

"bh1" == Bounty Hunter, Sniper (leader)
Lives, 1

"bh2" == Bounty Hunter, Gadget (leader)
Lives, 1

Era Specific:

Era 2 - Clone Wars-

CA-

    Phase 1 -- Default Special Units

"pc1" - Clone, Phase 1, Soldier (default, common, no limit)
Lives, 2
EMP Nade 1
CR 1

"pc2" - Clone, Phase 1, Heavy Trooper, Rocket (special unit)
Lives, 1

"pc3" - Clone, Phase 1, Heavy Trooper, MG (special unit)
Lives, 1

"par" = Arc Trooper, Phase 1, Pistols (special unit)
EMP Nade 2
Lives, 1

    Phase 2 -- Blobs, Westar Arc Introduced

"cs1" - Clone, Phase 2, Soldier (default, common, no limit)
Lives, 3
EMP Nades 2
Blobs
CR 2

"cs2" - Clone, Phase 2, Heavy Trooper, Rocket (special unit)
EMP Nade 1
Lives, 2

"cs3" - Clone, Phase 2, Heavy Trooper, MG (special unit)
EMP Nade 1
Lives, 2

"ar1" - Arc Trooper, Phase 2, Pistols (special unit)
EMP Nade 1
Lives, 2

"ar2" - Arc Trooper, Phase 2, Westar (special unit)
EMP Nades 3
Lives, 2

CIS-

(Droids cannot use the bacta bonus)
(They have bonus lives, instead, but are weaker)

    Either Phases-

"bd1" == Battle Droid, Soldier (default, common, no limit)
Assemble
Lives, 6

"bd2" == Battle Droid, Heavy Trooper, Rocket (special unit)
Assemble
Lives, 3

"bd3" == Battle Droid, Heavy Trooper, MG (special unit)
Assemble
Lives, 3

"bd4" == Battle Droid, OOM Series, Officer (special unit)
Rally
Lives, 3

"bd5" == Battle Droid, Sniper (leader)
Lives, 2

    Phase 1 -- Default Special Units

"ps1" == SBD, Phase 1, Lower FP/Hull/Battery, Gadget (special unit)
Wrist Rocket
Lives, 1

"ps2" == SBD, Phase 1, Mid FP, No Gadget (special unit)
Lives, 1

"ps3" == SBD, Phase 1, Jetpack, Lowest FP/Hull/Battery, No Cortosis (special unit)
Lives, 1

"pd1" == Droideka, High Hull, Low Shields, Lowest FP, No Gadgets (special unit)
Lives, 1

    Phase 2 -- Blobs, Westar Arc Introduced

"sb1" == SBD, Phase 2, Mid FP/Hull/Battery, Gadget (special unit)
Wrist Rocket
Wrist Laser
Lives, 2

"sb2" == SBD, Phase 2, High FP, Blast & Magnetize (special unit)
Lives, 2

"sb3" == SBD, Phase 2, Jetpack, Mid FP/Hull/Battery, Cortosis (special unit)
Flamethrower
Lives, 2

"dr1" ==  Droideka, High Hull, Full Shields, Full FP, Power Management (special unit)
Lives, 2

"dr2" == Droideka, Med Hull, Full Shields, Low FP, Shield Repulse (special unit)
Lives, 2

"bx1" == Arc, Sniper (leader)
Arc Roll
Vibroblade
Rally
Lives, 1

"bx2" == Bounty Hunter, Gadget (leader)
Vibroblade
Lives, 1

Era 3 - Mandalorian Wars

"ma1" == Mandalorian, Jetpack Trooper, Med Fuel, EE4 (special unit)
Beskar 1 - Replaces Jet Trooper
Lives, 2

"ma2" == Mandalorian, Jetpack, Full Fuel, Westars, Wrist Laser (special unit)
Beskar 3
Lives, 1

"ma3" == Mandalorian, Jetpack, Med Fuel, EE-3, Flamethrower (special unit)
Beskar 2
Lives, 1

"ma4" == Mandalorian, Jetpack, Med Fuel, EE-3, Rocket (special unit)
Beskar 1
Lives, 1

"ma5" == Mandalorian, Jetpack, Med Fuel, EE-3, Whistling Birds (special unit)
Beskar 2
Lives, 1

Era 4 - Jedi Civil War

(Starforge Obtained)
(No Vibroblades)

"sd1" == Sentinel Droid, Soldier (default, common, no limit)
Beskar 1 - 50 HP - 125 Armor
Lives, 2

"sd2" == Sentinel Droid, Heavy Trooper, Rocket (special unit)
Beskar 2 - 70 HP - 125 Armor
Lives, 1

"sd3" == Sentinel Droid, Heavy Trooper, MG (special unit)
Beskar 2 - 70 HP - 125 Armor
Lives, 1

"rd1" == 'White' Rakatan Destroyer Droid, Droideka, Full FP, Full Shields, Power Management (special unit)
Lives, 1

Era 7 - Fall of the Black Sun

"bsd" == Black Sun B1, Soldier (default, common, no limit)
Beskar 1
Lives, 2

"bso" == Black Sun B1, Officer (special unit)
Beskar 1
Rally
Lives, 1

(Circumstantial Gains)

"cd1" == Crimson Dawn, Mandalorian, Med Fuel, EE4, Rocket (special unit)
Beskar 2
Lives, 1

"cd2" == Crimson Dawn, BX-Commando Droid (special unit)
Beskar 1
Arc Roll
Vibroblade
Rally
Lives, 2

"cd3" == Crimson Dawn, Red B1, Officer (special unit)
Beskar 2
Rally
Lives, 1

"cd4" == Crimson Dawn, SBD, Full FP/Battery/Hull, Cortosis (special unit)
Beskar 2
Wrist Rocket
Flamethrower
Lives, 1

"gam" == Gammorean Guard, Bounty Hunter (leader)
Axe, Saber Def 1
AOE Hit Knockback
Wookie Fury 2
Lives, 1

"pyk" == Pyke, Bounty Hunter (leader)
All Darts, Full BH Kit
Thermal Detonator
Lives, 1



Planet Specific:

Kashyyyk (most eras, either team)-

"wkf" == Wookie, Fury (republic) (special unit)
Lives, 1

"wkb" == Wookie, Bowcaster (republic) (special unit)
Lives, 1

"ewf" == Wookie, Fury, Enslaved (empire) (special unit)
Lives, 1

"ewb" == Wookie, Bowcaster, Enslaved (empire) (special unit)
Lives, 1

Droid Depot (Era 6)-

    Corporate Sector Authority-

"cd1" == CSA B1 (soldier, common, no limit)
Lives, 3

"cd2" == CSA B1, Heavy Trooper, Rocket (special unit)
Lives, 2

"cd3" == CSA B1, Heavy Trooper, MG (special unit)
Lives, 2

"cd4" == CSA b1, Sniper (leader)
Lives, 1 - Simulates Hero

"cd5" == CSA B1, Gadget (leader)
Lives, 1 - Simulates Hero

    Thrawn Possesses-

"td1" == Thrawn B1 (soldier, common, no limit)
Lives, 3

"td2" == Thrawn B1, Heavy Trooper, Rocket (special unit)
Lives, 2

"td3" == Thrawn B1, Heavy Trooper, MG (special unit)
Lives, 2

"td4" == Thrawn B1, Sniper (leader)
Lives, 1 - Simulates Bounty Hunter

"td5" == Thrawn B1, Gadget (leader)
Lives, 1 - Simulates Bounty Hunter

Droid Depot (Era 5)-

"md1" == Malgus Destroyer, Droideka, Full FP, Full Shields, Power Management (special unit)
Lives, 2

Clone Labs (Era 5)-
(No Vibroblades)

"oc1" == Old Republic Clone, Soldier (default, common, no limit)
Wookie Charge Melee (Fury 1)
EMP Nade 1
Lives, 3

"oc2" == Old Republic Clone, Heavy Trooper, Rocket (special unit)
EMP Nades 2
Wookie Fury 2
Lives, 2

"oc3" == Old Republic Clone, Heavy Trooper, MG (CR3) (special unit)
EMP Nades 2
Wookie Fury 2
Lives, 2
# Affix Deep

A mobile-first, 8-bit roguelite dungeon crawler that runs in the browser. Every monster and item can roll a **prefix** and a **suffix** (for example, *Aged Ant of Speed* or *Rusty Greatsword of Glass*), so the same base creature or sword plays differently from run to run.

## Play it

Open `index.html` in any modern browser. It's a single self-contained file: no build step, no server, no dependencies. Your progress saves in the browser's local storage.

### Host it free on GitHub Pages

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, pick `main` and `/ (root)`, and save.
4. After a minute the game is live at `https://<your-username>.github.io/affix-deep/`. On Android, open it in Chrome and choose **Add to Home screen** to launch it like an app.

## What's in the game

- **Music that follows the game:** generated live in the browser with Web Audio (no sound files), so it stays chiptune and adds nothing to the download. The town is light and airy, and every building you walk into has its own theme (a bouncy Shop, a jig in the Tavern, stately brass in the Guild Hall, a march in the Training Yard, organ, choir and bells in the Temple, hammer, grindstone and bellows in the Smithy, harp and bubbling flasks in the Apothecary, a ticking clock and clinking coins in the Bank, wandering pan flute in the Cartographer, and old stone humming in the cellar). The dungeon is a slow, grungy, distorted sludge riff and the Abyss is lower and heavier still. Every fight switches to fast, dark fight music, taking turns through four tunes (a gallop, a heavy chug, a frantic sprint and war drums), and champions get their own. Moods crossfade on their own, and the note button in the top bar turns music on or off (remembered per device). Browsers only allow sound after a tap, so music starts on your first one. Each mood is a small entry in `MOODS` inside `Music`.
- **A tutorial:** one-time tips appear the first time you reach each part of the game (town, buildings with quests, the tavern, exploring, fighting, loot, the stairs, leveling up, coming home and dying). Skip them all from any tip, or bring them back from the Guild Hall.
- **An opening story:** a new adventurer arrives in Emberhold as a stranger with no past, good or bad. The stories about the dungeon are true, the locals won't go near it, and the town gets by on outsiders. It plays once as tap-through narration over the town (text in `INTRO_STORY`).

- **Room-map dungeon floors:** each floor is a randomly generated web of connected rooms on a scrollable map. Tap a connected room to move (or a farther known room to travel there through safe rooms). Rooms can hold monsters, treasure chests (some trapped, some Mimics), trap rooms you disarm or dash through, shrines, campfires, a wandering merchant, locked vaults whose key one monster carries, cursed idols that offer a run-long bargain, armory racks where you pick one of three items, marked elites with a guaranteed rare drop, harvest spots for your current gathering quest, and the stairs down. On about three floors in ten, one room's tile on the map has a tiny crack on one edge. Nothing points it out; tap it once that room is cleared and it opens a hidden passage to a gold hoard, a library, an armory, a champion, a deadly trap or a teleport circle. Every room stays hidden until you step inside, along with where its doors lead, and fights start the moment you walk into a monster's room. Each run rolls one dungeon prefix and suffix that hold for every floor (Dark, Infested, Haunted, Flooded, of Riches, of Ambush, of Traps, of Echoes, and more), and every 10th floor always carries a harsh doom (Cursed, Lightless, Teeming or Starving; two of them from floor 30), with monsters two levels higher and a champion on the stairs.

- **104 monsters** across ants, spiders, flying insects, crawlers, rats, snakes, bears, humanoids (goblinoids, orcs, outlaws, warriors, spellcasters, beastfolk, archers, clerics), undead and dragons. Each has a species trait and an ability pool for its family.
- **Monster affixes:** 29 prefixes and 21 suffixes, good and bad, including humanoid-only prefixes (Dark, Evil, Hideous, Bulked, Avenged, Holy).
- **Gear in 8 slots** (weapon, shield, head, body, hands, feet, neck, ring), with cloth, light and heavy armor builds, two-handed weapons, and dozens of positive, negative and mixed item affixes.
- **Five attributes** (Strength, Dexterity, Vitality, Intelligence, Luck) with points to spend each level, and a Character screen that shows exactly what's affecting every stat.
- **Waystones** on every 10th floor: reach one and make it home alive, and the Dungeon Gate lets you start future runs on the floor just past it for a toll of 2 × floor² gold (triple in the Abyss).
- **A secret under the tavern** (spoilers): bring a strange stone home from below floor 20 and Big Hob calls you over, tells you what he knows in a tap-through conversation, and takes you down to the cellar. The Old Wall there has eight empty sockets. Eight stones are hidden in glimmering crevices below floor 20, rarer the shallower you are. Carry one home alive and set it in the wall, but until all eight are set any death empties the wall and every stone rolls back into the deep. Set all eight to permanently unlock **the Abyss**, a second dungeon about ten times harder (monsters 30 levels up) with far better loot (45 item levels up).
- **A Bestiary** in the Guild Hall: every species you've slain with its lore, trait, abilities and the affixes you've seen on it. Killing 100, 500, 1,000 and 10,000 of a species masters it, for 1%, 5%, 15% and 25% more damage against it.
- **Scrolls with affixes:** 11 scroll spells (Flame, Frost, Lightning, Venom, Hex, Sundering, Leech, Holy, Ward, Haste, Mending, plus Escape) that roll prefixes and suffixes like everything else, such as a Quickened Flame Scroll of Venom or a Volatile Lightning Scroll of Backlash.
- **Stacking consumables** (up to 10 per bag slot), plus a **potion bag** and a **scroll bag** that sit outside your inventory (expanded at the Apothecary). In fights, the Potions and Scrolls buttons open them.
- **A walkable isometric town:** a full-screen isometric pixel diorama of timber-framed shops, a thatched tavern, a stone guild keep, a marble bank, a temple with a bell tower and more, joined by dirt roads with lamp posts and ringed by forest. Tap a building to go inside; the Dungeon Gate is a pit sunk into the ground. The Shop, Training Yard, Temple, Apothecary, Smithy, Bank and Cartographer each sell modest permanent perks, and each, along with the Shop, has its own quest giver (Tess Quill, Sergeant Brakka, Sister Maren, Old Wenna, Durik Ironhand, Master Pell and Ysolde) offering easy, medium and hard quests. You can hold one quest at a time, quest materials only drop while you're on the quest that needs them, and progress only counts when you make it home alive. Completing quests earns reputation, which unlocks higher perk levels. The Smithy also reforges an item's prefix or suffix (each reforge on the same item costs 50% more than the last, and after two safe tries the item may shatter: 5%, 10%, 18%, 28%, 40%, 50%, then 60%), and the Guild Hall keeps your records: runs, deaths, biggest hit, damage dealt and taken, and every monster species you've slain.
- **Turn order driven by speed**, status effects (poison, burning, slowed, blinded, cursed, corroded), a loot screen with side-by-side item comparison, a shop, a tavern with a stash (the free stable bed works once per visit to town), and roguelite death rules.

## Project layout

```
index.html          The whole game: HTML, CSS, JavaScript and embedded pixel art
art-tools/          Python scripts that generate the 48x48 monster sprites
  pxlib.py          Shape masks, shading, outlines and sprite-sheet helpers
  monsters.py       Original fantasy monsters (also revise.py, final.py)
  bears.py, bugs.py, ratsnakes.py, ants.py
  hk.py             Character toolkit: stances, garments, faces, hair, capes, weapons
  folk1.py-folk3.py Hand-built humanoids, one function per character
  humans.py         Older template humanoid generator (also newfolk.py)
  dragons.py        Parametric dragon generator
  cut_wall.py       Cuts the Old Wall and its eight stones out of source-art/old-wall.jpg and finds the sockets
  cut_portraits.py  Cuts the townsfolk portraits out of source-art/portraits-set-1.jpg at their native pixel grid
  cut_buildings.py  Cuts town buildings out of an art sheet at their native pixel grid (python3 cut_buildings.py source-art/buildings-set-2.jpg sheet2 out.json)
  iso_scene2.py     Paints the town ground: grass, cobbled streets, plaza, trees, lamp posts
  iso.py            Isometric engine: textured walls, tiled and thatched roofs, props
  iso_town.py       The isometric town buildings; iso_scene.py lays out the town ground
  buildings2.py     Earlier flat town buildings (portraits.py draws the townsfolk faces)
  buildings.py      Older town buildings (plus townbg.py for the town backdrop, hero.py for your avatar, townfolk.py for the gate and quest givers)
  objects.py        Dungeon objects: chest, stairs, shrine, campfire, merchant (objects2.py: trap, entrance; objects3.py: vault, idol, armory, harvest)
```

## Adding content

Everything is data-driven inside `index.html`:

- **Monsters:** add an entry to `MONSTERS` (stats, family, first floor, trait, flavor text), and a sprite to `ART` under the same key. Optional `w` sets how often it appears (1 is normal, 0.1 is rare).
- **Monster affixes:** add to `MPRE` (prefixes) or `MSUF` (suffixes). Use `mul` for multipliers, `add` for flat bonuses, `flag` for special behaviors, and `only: ['humanoid']` to limit an affix to one monster type.
- **Species traits:** add to `TRAITS` and reference it from the monster.
- **Abilities:** add to `ABIL`, list it in a family's pool in `FAMILY`, and handle it in `useAbility()`.
- **Items and item affixes:** `IBASE`, `IPRE` and `ISUF`.

## Making sprites

The pixel art is generated, not hand-painted. To make new sprites:

```
cd art-tools
pip install -r requirements.txt
python dragons.py        # writes dragons.png (preview sheet) and dragons.json
```

Each script writes a preview sheet (`.png`) and a JSON file of base64 PNG data URIs. Paste those entries into the `ART` object in `index.html`. Set `pxlib.FLAT['on'] = True` (as `humans.py`, `newfolk.py` and `dragons.py` do) for the flatter, hand-drawn look.

Any sprite can also be swapped for your own 48x48 PNG by replacing its data URI.

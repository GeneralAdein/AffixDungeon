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

- **Room-map dungeon floors:** each floor is a randomly generated web of connected rooms on a scrollable map. Tap a connected room to move (or a farther known room to travel there through safe rooms). Rooms can hold monsters, treasure chests (some trapped, some Mimics), trap rooms you disarm or dash through, shrines, campfires, a wandering merchant, locked vaults whose key one monster carries, cursed idols that offer a run-long bargain, armory racks where you pick one of three items, marked elites with a guaranteed rare drop, harvest spots for your current gathering quest, and the stairs down. Every room stays hidden until you step inside, along with where its doors lead, and fights start the moment you walk into a monster's room. Each run rolls one dungeon prefix and suffix that hold for every floor (Dark, Infested, Haunted, Flooded, of Riches, of Ambush, of Traps, of Echoes, and more), and every 10th floor always carries a harsh doom: Cursed, Lightless, Teeming or Starving.

- **104 monsters** across ants, spiders, flying insects, crawlers, rats, snakes, bears, humanoids (goblinoids, orcs, outlaws, warriors, spellcasters, beastfolk, archers, clerics), undead and dragons. Each has a species trait and an ability pool for its family.
- **Monster affixes:** 29 prefixes and 21 suffixes, good and bad, including humanoid-only prefixes (Dark, Evil, Hideous, Bulked, Avenged, Holy).
- **Gear in 8 slots** (weapon, shield, head, body, hands, feet, neck, ring), with cloth, light and heavy armor builds, two-handed weapons, and dozens of positive, negative and mixed item affixes.
- **Five attributes** (Strength, Dexterity, Vitality, Intelligence, Luck) with points to spend each level, and a Character screen that shows exactly what's affecting every stat.
- **A Bestiary** in the Guild Hall: every species you've slain with its lore, trait, abilities and the affixes you've seen on it. Killing 100, 500, 1,000 and 10,000 of a species masters it, for 1%, 5%, 15% and 25% more damage against it.
- **Scrolls with affixes:** 11 scroll spells (Flame, Frost, Lightning, Venom, Hex, Sundering, Leech, Holy, Ward, Haste, Mending, plus Escape) that roll prefixes and suffixes like everything else, such as a Quickened Flame Scroll of Venom or a Volatile Lightning Scroll of Backlash.
- **Stacking consumables** (up to 10 per bag slot) and a **Potion Belt** that holds potions outside the bag, expanded at the Apothecary.
- **A walkable isometric town:** a full-screen isometric pixel diorama of timber-framed shops, a thatched tavern, a stone guild keep, a marble bank, a temple with a bell tower and more, joined by dirt roads with lamp posts and ringed by forest. Tap a building to go inside; the Dungeon Gate is a pit sunk into the ground. The Training Yard, Temple, Apothecary, Smithy, Bank and Cartographer each sell modest permanent perks, and each has its own quest giver (Sergeant Brakka, Sister Maren, Old Wenna, Durik Ironhand, Master Pell and Ysolde) offering easy, medium and hard quests. You can hold one quest at a time, quest materials only drop while you're on the quest that needs them, and progress only counts when you make it home alive. Completing quests earns reputation, which unlocks higher perk levels. The Smithy also reforges an item's prefix or suffix, and the Guild Hall keeps your records: runs, deaths, biggest hit, damage dealt and taken, and every monster species you've slain.
- **Turn order driven by speed**, status effects (poison, burning, slowed, blinded, cursed, corroded), a loot screen with side-by-side item comparison, a shop, a tavern with a stash, and roguelite death rules.

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
  cut_buildings.py  Cuts town buildings out of an art sheet (source-art/), removes the background and scales them to a town lot
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

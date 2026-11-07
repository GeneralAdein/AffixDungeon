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

- **First-person dungeon floors** in the spirit of Wizardry: each floor is a randomly generated maze seen in a 2.5D corridor view. Tap Forward to auto-walk to the next junction or object, use the automap, open chests (some trapped, some Mimics), pray at shrines, rest at campfires, trade with a wandering merchant, and decide whether to take the stairs down or keep exploring. Floors roll their own prefixes and suffixes (Dark, Infested, Haunted, Flooded, of Riches, of Spinners, of Traps, of Fog, and more).

- **104 monsters** across ants, spiders, flying insects, crawlers, rats, snakes, bears, humanoids (goblinoids, orcs, outlaws, warriors, spellcasters, beastfolk, archers, clerics), undead and dragons. Each has a species trait and an ability pool for its family.
- **Monster affixes:** 29 prefixes and 21 suffixes, good and bad, including humanoid-only prefixes (Dark, Evil, Hideous, Bulked, Avenged, Holy).
- **Gear in 8 slots** (weapon, shield, head, body, hands, feet, neck, ring), with cloth, light and heavy armor builds, two-handed weapons, and dozens of positive, negative and mixed item affixes.
- **Five attributes** (Strength, Dexterity, Vitality, Intelligence, Luck) with points to spend each level, and a Character screen that shows exactly what's affecting every stat.
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
  objects.py        Dungeon objects: chest, stairs, shrine, campfire, merchant
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

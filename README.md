# The World in One Day — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/aikbani/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/aikbani/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-image front page summing up the world's news of Friday 20 November 2026:
**36 stories from 7 regions** — North America, Latin America, Europe, Africa,
the Middle East, Asia-Pacific and Global — led by Russia's biggest barrage of
the year on Kyiv, Cyclone Akvan's landfall in Odisha, and the ICJ ruling that
Myanmar committed genocide against the Rohingya.

The poster also carries a drawn world map with numbered story locations, a
"day in numbers" panel, a UTC timeline of the day, and a DATE CHECK box:
every story happened or was first reported on 20 November 2026.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (byte-identical to entry.png in this repo)
```

`main.py` is Python 3.13 standard library only and needs no network; it simply
copies the pre-rendered `entry.png` (1024×1024 PNG, 866,633 bytes) to the
output directory. The poster itself is drawn by `render.py` from the story
data in `stories.py` (Pillow is only needed to re-render, not to run the
entry — the entry ships the finished PNG). Re-running `render.py` reproduces
the same bytes: the grain overlay uses a fixed seed and no timestamps are
drawn.

## How the poster is laid out

- **Masthead** — the day, the story count and the region count.
- **Lead** — the three stories that defined the day: Kyiv, Akvan, the ICJ.
- **Map** — every story numbered 1–36 on a drawn world map, with a
  "day in numbers" panel beside it (400+ missiles, 300,000+ evacuated,
  S&P −3.7%, $2bn+ GTA VI, 100,000 youth-mobility places, 72 hours).
- **Regions** — all 36 stories in two columns, grouped by region.
- **Timeline** — eight moments from 00:40 to 21:00 UTC.
- **Date check** — every story is dated 20 November 2026.

## Sources

See [SOURCES.md](SOURCES.md) for all 36 stories with their source and
verification date (21 November 2026, covering 20 November 2026).

## License

MIT — see [LICENSE](LICENSE).

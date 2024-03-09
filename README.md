# unique unicode runes

use stdin to generate a unique list of runes to stdout.

# usage

```sh
> echo "日本語にほんご\u243\uf254\u463\u462\udasdvds" | poetry run unique_unicode_runes
ÚɃѢѣごにほん日本語
```

## testing

use `pytest` for running tests

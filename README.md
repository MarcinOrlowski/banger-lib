```ascii
▙▄▄                ▗▟█▙  ▟█▙    ▐▄▄              ▄▄▄▄▄▄▄▄▄█             ▗█    ▙▄▖
▜██████████▄▖        ▀    ▀ ▗█  ▝█████████▙▄ ▗▟██████████▀▚▖   ▗▄█████████▛   ▜█████████▙▄
█▙▄▀▀▀▀▀▀█████▖  ▗▄███████████  █▄▄▀▀▀▀▜█████ ████▀     ▗███▌ ▟██████▀▀▀▀▄▄█▌ █▙▄▛▀▀▀▀▜████▌
████      ▟███▌ ▟████▀   ▀▀▀▀▄▌ ████     ████ ████▖     ▐███▌ ████▀    ▄████▌ ████     ▐███▌
██████████████  ████      ▐███▌ ████     ████ ▝█████████████▌ ██████████████▌ ████▄▄▄▄▄▟███▌
████     ▝▜███▌ ████      ▐███▌ ████     ████    ▀▀▘    ▀███▌ ████▙▖     ▄▄▄  ████████████▀
████      ▟███▌ ████▖     ▟███▌ ████     ████  ▄▄        ███▘ ▝▜████████████  ████  ▝███▙
██████████████  ▝█████████████▌ ▄▄▄▄     ▄▄▄▄   ▜▄▄▄▟███████    ▝▀▀▀▀▀▀▀▀▀▀▘  ████    ▜███▖
▀▀▀▀▀▀▀▀▀▀▀▀▀     ▀▀▀▀▀▀▀▀▝▀▀▀▘ ▝▘▝▘     ▝▘▝▘  ▐█▀▀▀▀▀▀▀▀▀▀                   ▀▀▀▀     ▝▀▀▀▘
                                               ▝              *** LUBRARY ***
```

![PyPI - Version](https://img.shields.io/pypi/v/banger-lib?style=flat)
[![PyPI Downloads](https://static.pepy.tech/badge/banger-lib)](https://pepy.tech/projects/banger-lib)
![MIT License](https://img.shields.io/github/license/MarcinOrlowski/banger-lib)

---

# What it is?

`Bänger` (pronounced just `banger`) is a modern tribute to the classic Unix `banner` command line
utility that produces text banners, with additional features added a top:  multiple built-in ASCII
character set and support for rendering any TTF/OTF font with Unicode! This package contains
the main functionality of the tool in form of a Python library, which can be used to create banners
in your own Python code.

# Command line tool (`banger`)

If you are looking for the command line tool instead, see
the [banger](https://github.com/MarcinOrlowski/banger) project.

# Examples

```python
from banger_lib import Banger

banger = Banger(font="fire")
banger.add_text("Hello World")
output = banger.render()
```

## License

- Written and copyrighted &copy;2025-2026 by Marcin Orlowski <https://marcinOrlowski.com>
- Bänger is the open-sourced software licensed under
  the [MIT license](http://opensource.org/licenses/MIT)

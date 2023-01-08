# My QTile Config

The python config for my daily driver WM


## Why a WM

I feel very confortable being a keyboard user, and a WM provides that functionality out of the box


## Why QTile

Well basically I'm in the path of learn python, so use QTile to play with python code seems to me a good excuse


# My Configuration

My `config.py` is pretty much the default QTile's config, but I tried to put my custom stuffs in a modular approach


### Basic Python and libqtile libs

``` python
import subprocess

from libqtile import bar, widget, hook
from libqtile.config import Group, Match, Screen
from libqtile.layout import floating

```


### `userconfigs` module

The `userconfigs` local module will store the custom configuration to run QTile
``` python
# local imports
from userconfigs.keybinds import Keybinds
from userconfigs.layouts import Layouts
from userconfigs.userVariables import UserVars

keybinds = Keybinds()
screen = Layouts()

```

### Keys config

``` python
keys = keybinds.load_keys()
```


### Layouts config

``` python
layouts = screen.init_layouts()
```

### Main config

#### Groups definition

``` python
groups = [Group(i) for i in "123456789"]

```


#### Bar and it's widgets definition

``` python
widget_defaults = dict(
  font="sans",
  fontsize=12,
  padding=3
)

extension_defaults = widget_defaults.copy()

screens = [
  Screen(
    bottom=bar.Bar(
      [
        widget.CurrentLayout(),
        widget.GroupBox(),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
          chords_colors={
            "launch": ("#ff0000", "#ffffff"),
          },
          name_transform=lambda name: name.upper(),
        ),
        widget.TextBox("default config", name="default"),
        widget.TextBox(
          "Press &lt;M-r&gt; to spawn",
          foreground="#d75f5f"
        ),
        widget.Systray(),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(),
      ],
      24,
    ),
  ),
]

```


#### Miscellaneus configs

Multiple QTile configs
``` python
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = floating.Floating(
    float_rules=[
        *floating.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None
wmname = "LG3D"


```

#### Startup Once configuration

All apps that should start once (at startup), should be defined in the `autostart` script 
``` python
@hook.subscribe.startup_once
def start_once():
    subprocess.call([f"{UserVars.home}/.config/qtile/autostart"])

```

import os
import subprocess

from libqtile import bar, widget, hook
from libqtile.config import Group, Match, Screen
from libqtile.layout import floating

# local imports
from userconfigs.keybinds import Keybinds
from userconfigs.layouts import Layouts

keybinds = Keybinds()
screen = Layouts()

groups = [Group(i) for i in "123456789"]

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


@hook.subscribe.client_new
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([f"{home}/.config/qtile/autostart"])

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from keys import keys, mod

# GROUPS
# groups = [Group(i) for i in "123456789"]

groups = [
    Group(name="1",label=""),
    Group(name="2",label="󰈹"),
    #Group(name="8",label=""),
    Group(name="3",label="󰇮"),
    Group(name="4",label=""),
    #Group(name="7",label=""),
    #Group(name="8",label="p"),
    #Group(name="9",label="o"),
]

for i in groups:
    keys.append(
        # mod1 + group number = switch to group
        Key(
            [mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name),
        ),
    )
    keys.append(
        # mod1 + shift + group number = switch to & move focused window to group
        Key(
            [mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name),
        ),
            # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            # desc="move focused window to group {}".format(i.name)),
    )


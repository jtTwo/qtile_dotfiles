from libqtile import bar#, widget
from libqtile.config import Screen

from qtile_extras import widget 
from qtile_extras.widget.decorations import RectDecoration

#CONFIG VARS
bar_margin_gaps = 15
window_external_margin_gaps = 10

widget_defaults = dict(
    font="JetBrainsMonoNL Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

symbol_defaults = dict(
    font="JetBrainsMonoNL Nerd Font",
    fontsize=18,
)

widget_separator = widget.TextBox (
    **symbol_defaults,
    foreground="#444444",
    padding = 4,
    text="󰇙",
)

def widget_spacer(width):
    return widget.TextBox (
        padding = width,
    )

class MouseOverClock(widget.Clock):
    defaults = [
        (
            "long_format",
            "%A %d %B %Y | %H:%M",
            "Format to show when mouse is over widget."
        )
    ]

    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        self.add_defaults(MouseOverClock.defaults)
        self.short_format = self.format

    def mouse_enter(self, *args, **kwargs):
        self.format = self.long_format
        self.bar.draw()

    def mouse_leave(self, *args, **kwargs):
        self.format = self.short_format
        self.bar.draw()

screens = [
    Screen(
        bottom=bar.Gap(window_external_margin_gaps),
        left=bar.Gap(window_external_margin_gaps),
        right=bar.Gap(window_external_margin_gaps),

        top=bar.Bar(
            [
                #widget.Spacer(length=5),
                widget.TextBox(
                    **symbol_defaults,
                    #background = "#444444",
                    text="",
                    padding=25,
                    decorations = [RectDecoration(
                        filled=True,
                        padding_x=0,
                        radius=10,
                        colour="#777777",
                    )],
                ),
                widget.Spacer(length=8),
                widget_separator,
                widget.GroupBox(
                    **symbol_defaults,
                    highlight_method='text',
                    #block_highlight_text_color='ffffff',
                    active='#68DD21',
                    #foreground='ffffff',
                    this_screen_border='#FFFFFF',
                    this_current_screen_border='#FFFFFF',
                    borderwidth=1,
                    margin=2,
                    padding_x=8,
                    #urgent_border='ffffff',
                ),
                widget_separator,
                #widget.CurrentLayout(**widget_defaults),
                widget.CurrentLayoutIcon(scale=0.85),

                widget.Prompt(),
                widget.WindowName(),
                #widget.TextBox("default onfig", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                #widget.Systray(),
                #widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                #widget.QuickExit(),

                widget.Spacer(length=bar.STRETCH),
                MouseOverClock(),
                widget.Spacer(length=bar.STRETCH),

                widget.Clock(
                    **widget_defaults,
                    foreground = "#f0ffff",
                    format = "%a, %b %d - %H:%M",
                ),
                widget.Spacer(length=5),
            ],
            size=25,
            border_width=7,
            margin = [bar_margin_gaps, bar_margin_gaps, window_external_margin_gaps, bar_margin_gaps],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

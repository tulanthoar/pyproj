'''menu to interface with xmonad'''
from time import sleep
from click import echo, getchar, command
from sh import Command
from ewmh import EWMH


def active_class(ewmh_obj):
    '''returns the focused window class after 200ms'''
    sleep(0.3)
    win = ewmh_obj.getActiveWindow()
    win_class = win.get_wm_class()
    return win_class


def class_is_mapped(hinter, class_name):
    '''use ewmh to see if a window with class name is mapped'''
    for win in hinter.getClientListStacking():
        classnames = win.get_wm_class()
        if class_name in classnames:
            return True
    return False


def class_is_visible(hinter, class_name):
    '''check if a window with class_name is currently visible'''
    for win in hinter.getClientListStacking():
        if class_name in win.get_wm_class():
            attrs = win.get_attributes()
            if attrs._data['map_state'] == 2:
                return True
    return False


def print_menu(persist):
    '''print menu of available keys'''
    echo('Spc: next empty ws')
    echo('Tab: toggle persist')
    echo('  c: clipmenu')
    echo('  q: qutebrowser')
    echo('  j: j4-app-menu')
    echo('  n: neovim')
    echo('  i: ipython')
    echo('  p: perl repl')
    echo('  r: ranger')
    echo('  a: all pads')
    echo('  b: byobu')
    echo('  P: pomodoro')
    echo('  h: htop')
    echo('  u: urxvt')
    if persist:
        echo('Persistence on')
    else:
        echo('Persistence off')


@command()
def xdomenu():
    """interacts with a simple menu."""
    xmc = Command('xmctl')
    char_to_bin = {'q': (xmc, 'srmenu'),
                   'c': (xmc, 'clipmenu'),
                   'j': (xmc, 'jmenu'),
                   'n': (xmc, 'nvim'),
                   'h': (xmc, 'htop'),
                   'u': (xmc, 'myterm'),
                   'i': (xmc, 'ipython'),
                   'p': (xmc, 'perl'),
                   'r': (xmc, 'ranger'),
                   'a': (xmc, 'allpads'),
                   'b': (xmc, 'byobu'),
                   'P': (xmc, 'pomodoro')}
    xdo = Command('xdotool')
    hinter = EWMH()
    persistent = False
    print_menu(persistent)
    while True:
        char = getchar()
        if char == '\x1b':
            raise KeyboardInterrupt
        elif char == '\t':
            if not persistent:
                persistent = True
                echo('Persistence on')
            else:
                persistent = False
                echo('Persistence off')
            continue
        elif char == ' ':
            xdo(['key', 'Menu'])
            xmc('nextempty')
            xdo(['key', 'Menu'])
            continue
        elif char == 'b':
            if persistent:
                xmc('minone')
            else:
                xmc('suicide')
            if not class_is_mapped(hinter, 'urxv'):
                xmc('byobu')
                sleep(1)
            else:
                if class_is_visible(hinter, 'urxv'):
                    xmc('sendbyo')
                else:
                    xmc('bringbyo')
        else:
            try:
                (cmd, opts) = char_to_bin[char]
                if persistent:
                    xmc('minone')
                else:
                    xmc('suicide')
                cmd(opts)
            except KeyError:
                echo('key ' + char + ' not recognized')
                continue
        if persistent:
            xdo(['key', 'Menu'])
        else:
            raise KeyboardInterrupt

'''menu to interface with xmonad'''
from time import sleep
from click import echo, getchar, command
from sh import Command
from ewmh import EWMH


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
    char_to_bin = {'q': ('srmenu'),
                   'c': ('clipmenu'),
                   'j': ('jmenu'),
                   'n': ('nvim'),
                   'h': ('htop'),
                   'u': ('myterm'),
                   'i': ('ipython'),
                   'p': ('perl'),
                   'r': ('ranger'),
                   'a': ('allpads'),
                   'b': ('byobu'),
                   'P': ('pomodoro')}
    xdo = Command('xdotool')
    hinter = EWMH()
    persistent = False
    print_menu(persistent)
    while True:
        char = getchar()
        if char == '\t':
            persistent = not persistent
            echo("\n")
            print_menu(persistent)
            continue
        elif char == ' ':
            xdo(['key', 'Menu'])
            xmc('nextempty')
            xdo(['key', 'Menu'])
            continue
        if persistent:
            xmc('minone')
        else:
            xmc('suicide')
        if char == 'b':
            if not class_is_mapped(hinter, 'urxv'):
                xmc('byobu')
                sleep(1)
            else:
                if class_is_visible(hinter, 'urxv'):
                    xmc('sendbyo')
                else:
                    xmc('bringbyo')
        else:
            (opts) = char_to_bin[char]
            xmc(opts)
        if persistent:
            xdo(['key', 'Menu'])
            continue
        raise KeyboardInterrupt

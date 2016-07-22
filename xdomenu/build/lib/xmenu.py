'''menu to interface with xmonad'''
from click import echo, getchar, command
from sh import Command


@command()
def xdomenu():
    """Shows a simple menu."""
    char_to_bin = {'q': ('xmctl', 'srmenu'),
                   'j': ('xmctl', 'jmenu'),
                   'n': ('xmctl', 'nvim'),
                   'h': ('urxvt', ['-e', 'htop']),
                   'u': ('urxvt', ['-name', 'urxvt', '-n', 'urxvt']),
                   'i': ('xmctl', 'ipython'),
                   'p': ('xmctl', 'perl'),
                   'r': ('xmctl', 'ranger'),
                   'a': ('xmctl', 'allpads'),
                   'b': ('xmctl', 'byobu'),
                   'P': ('xmctl', 'pomodoro')}
    echo('Main menu:')
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
    char = getchar()
    cmd = Command(char_to_bin[char][0])
    cmd(char_to_bin[char][1])

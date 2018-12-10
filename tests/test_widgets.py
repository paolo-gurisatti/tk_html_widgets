import json
import sys
import pytest
import tkinter as tk

sys.path.insert(0, '..')
from tk_html_widgets import HTMLText, HTMLScrolledText, HTMLLabel
from tk_html_widgets.html_parser import *


@pytest.mark.parametrize("f", ('tags', 'styles', 'images'))
@pytest.mark.parametrize("Widget", (HTMLText, HTMLScrolledText, HTMLLabel))
def test_tags(Widget, f):
    #----------------------------------------------------------------------------------------------
    for _ in range(10):
        try:
            root = tk.Tk()
            break
        except Exception as e:
            exception = e
    else:
        raise exception
    text = Widget(root)
    text.pack(fill="both", expand=True)
    text.set_html(open("../examples/%s.html" % f, 'r').read(), strip=True)
    text.fit_height()
    tags_json = json.dumps(text.html_parser._w_tags, sort_keys=True, indent=4)
    #open(Widget.__name__ + '_%s.json' % f, 'w').write(tags_json)
    assert open(Widget.__name__ + '_%s.json' % f, 'r').read() == tags_json

    # check stack lenght
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.BACKGROUND]) == 1
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.FOREGROUND]) == 1
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.JUSTIFY]) == 1
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.TABS]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.FAMILY]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.SIZE]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.WEIGHT]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.SLANT]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.UNDERLINE]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.OVERSTRIKE]) == 1
    assert len(text.html_parser.stack[Bind.KEY][Bind.LINK]) == 1
    root.destroy()


@pytest.mark.parametrize("Widget", (HTMLText, HTMLScrolledText, HTMLLabel))
def test_untagged(Widget):
    #----------------------------------------------------------------------------------------------
    for _ in range(10):
        try:
            root = tk.Tk()
            break
        except Exception as e:
            exception = e
    else:
        raise exception
    text = Widget(root)
    text.pack(fill="both", expand=True)
    text.set_html("untagged")
    text.fit_height()
    tags_json = json.dumps(text.html_parser._w_tags, sort_keys=True, indent=4)
    #open(Widget.__name__ + '_untagged.json', 'w').write(tags_json)
    assert open(Widget.__name__ + '_untagged.json', 'r').read() == tags_json

    # check stack lenght
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.BACKGROUND]) == 1
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.FOREGROUND]) == 1
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.JUSTIFY]) == 1
    assert len(text.html_parser.stack[WCfg.KEY][WCfg.TABS]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.FAMILY]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.SIZE]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.WEIGHT]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.SLANT]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.UNDERLINE]) == 1
    assert len(text.html_parser.stack[Fnt.KEY][Fnt.OVERSTRIKE]) == 1
    assert len(text.html_parser.stack[Bind.KEY][Bind.LINK]) == 1
    root.destroy()


def test_html_format():
    #----------------------------------------------------------------------------------------------
    TEXT = '<code style="color: #%06x; background-color: #%06x; text-align: center; font-size:30px"> text color #%06x</code>'
    for _ in range(10):
        try:
            root = tk.Tk()
            break
        except Exception as e:
            exception = e
    else:
        raise exception
    text = HTMLLabel(root, height=10)
    text.pack(fill="both", expand=True)
    for increment in (0x010000, 0x000100, 0x000001):
        for i in range(0, increment*256, increment):
            text.set_html(TEXT % (i,  increment*255, i))
            root.update()
    root.destroy()

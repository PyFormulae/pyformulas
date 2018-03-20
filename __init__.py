class object:
    pass

def screen(canvas=None, title='Display'):
    from _formulas.screen import screen
    globals()['screen'] = screen

    return screen(canvas, title)

audio = object()
def _play(wavedata, bitrate=None, duration=None, block=False):
    from _formulas.audio.play import play
    globals()['audio'].play = play

    return play(wavedata, bitrate, duration, block)
audio.play = _play


def download(url, out_path=None, get_headers=False, get_body=None):
    from _formulas.download import download
    globals()['download'] = download

    return download(url, out_path, get_headers, get_body)

def thread(function, args=(), kwargs={}):
    from _formulas.thread import thread
    globals()['thread'] = thread

    return thread(function, args, kwargs)

def settimeout(function, delay, repeat=False, args=(), kwargs={}):
    from _formulas.settimeout import settimeout
    globals()['settimeout'] = settimeout

    return settimeout(function, delay, repeat, args, kwargs)
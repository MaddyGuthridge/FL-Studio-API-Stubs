

import transport


def testPlaybackToggle():
    playing = transport.isPlaying()
    transport.start()
    assert playing != transport.isPlaying()
    transport.start()
    assert playing == transport.isPlaying()

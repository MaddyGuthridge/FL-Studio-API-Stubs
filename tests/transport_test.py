

import transport


def testPlaybackToggle():
    playing = transport.isPlaying()
    transport.start()
    assert playing != transport.isPlaying()
    transport.start()
    assert playing == transport.isPlaying()


def testRecordToggle():
    rec = transport.isRecording()
    transport.record()
    assert rec != transport.isRecording()
    transport.record()
    assert rec == transport.isRecording()

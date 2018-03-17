class screen:
    import numpy as np
    import cv2

    def __init__(self, canvas=None, title='Display'):
        self.title = title

        if canvas is None:
            self.canvas = self.np.zeros((480,640), dtype=self.np.uint8)
        else:
            self.canvas = canvas

        self.cv2.imshow(self.title, self.canvas)

        self._closed = False

        #cv2.destroyAllWindows() #TODO

    def update(self, canvas=None):
        if self.cv2.getWindowProperty(self.title, 0) < 0:
            #cv2.destroyAllWindows()
            self._closed = True
            return

        if canvas is not None:
            self.canvas = canvas

        self.cv2.imshow(self.title, self.canvas)

        # keycode = cv2.waitKey(1) & 0xFF
        self.cv2.waitKey(1)

    def exists(self):
        return not self._closed

class audio:
    class play:
        def __init__(self, wavedata, bitrate=2.56e5, duration=None):  # TODO: restrict bitrate based on pyaudio limits
            self.wavedata = wavedata
            self.bitrate = bitrate
            self.duration = duration

            # if block:TODO
            self._play()

        def _play(self):
            import pyaudio

            pa = pyaudio.PyAudio()

            # if hasattr(wavedata, 'shape'):TODO

            wavedata = bytes(self.wavedata)

            bitrate = round(self.bitrate)
            if self.duration is not None:
                bits = len(wavedata) * 8
                bitrate = round(bits / self.duration)

            sample_rate = round(bitrate / 8)

            stream = pa.open(format=pa.get_format_from_width(1),
                             channels=1,
                             rate=sample_rate,
                             output=True)

            stream.write(wavedata)
            stream.stop_stream()
            stream.close()
            pa.terminate()
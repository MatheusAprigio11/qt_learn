from PyQt5 import QtWidgets, uic, QtMultimedia
from PyQt5.QtCore import QUrl

class test:
    def __init__(self):
        app = QtWidgets.QApplication([])

        self.som = None

        self.tl_exemplo = uic.loadUi("./Exemplo.ui")
        self.tl_exemplo.okBtn.clicked.connect(lambda: self.test())
        self.tl_exemplo.show()

        self.tl_2 = uic.loadUi("./2.ui")
        self.tl_2.nextBtn.clicked.connect(self.test2)

        self.player = QtMultimedia.QMediaPlayer()
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./scream.mp3")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.setPlaylist(self.playlist)
        self.player.play()

        app.exec()

    def test(self):
        self.tl_exemplo.close()
        self.tl_2.show()
        self.sound()
        self.som.play()

    def test2(self):
        self.tl_2.close()
        self.tl_exemplo.show()
        self.chng_sound("parabens")

    def sound(self):
        self.som = QtMultimedia.QMediaPlayer()
        self.som.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./parabens.wav")))

    def chng_sound(self, msc):
        self.player.stop()

        self.playlist.clear()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile(f"./{msc}.wav")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.play()


if __name__ == '__main__':
    c = test()

from PyQt5 import QtWidgets, uic, QtMultimedia
from PyQt5.QtCore import QUrl

class test:
    def __init__(self):
        app = QtWidgets.QApplication([])

        self.som = None

        self.tl_exemplo = uic.loadUi("./Exemplo.ui") #loadui para carregar a tela
        self.tl_exemplo.okBtn.clicked.connect(lambda: self.test())    #lambda é quando voce quer utilizar uma função e precisa parar parametro     -   okBtn é o nome do botao, clicked connect a função do qt
        self.tl_exemplo.show()   #arquivo show serve para abrir a tela

        self.tl_2 = uic.loadUi("./2.ui")
        self.tl_2.nextBtn.clicked.connect(self.test2)

        self.player = QtMultimedia.QMediaPlayer()      #aditivos para musica
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./scream.mp3")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.setPlaylist(self.playlist)
        self.player.play()

        app.exec()    #executar a classe

    def test(self):     #metodo feito para fechar uma tela e abrir a outra    -    daqui para baixo são funções
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

from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer

app = QApplication([])

player = QMediaPlayer()
media = QMediaContent(QUrl.fromLocalFile("music.wav"))
player.setMedia(media)
player.play()

# 10 saniye sonra sesin durmasını sağlayacak bir zamanlayıcı (timer) oluşturuyoruz
timer = QTimer()
timer.setSingleShot(True)
timer.timeout.connect(player.stop)
timer.start(20000)  # 10 saniye (10000 milisaniye) süresince bekletiyoruz
app.exec_()



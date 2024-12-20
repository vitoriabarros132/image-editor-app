import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PySide6.QtGui import QPixmap
from ui_main_window import Ui_MainWindow
from PIL import Image, ImageFilter


class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        'Lista para armazenamento das imagens selecionadas'
        self.selected_images = []

        'Dicionário para armazenamento de imagens com filtros'
        self.filtered_images = {}

        'Conexão dos botões às funções'
        self.ui.selectImagesButton.clicked.connect(self.select_images)
        self.ui.applyFilterButton.clicked.connect(self.apply_filter)
        self.ui.saveButton.clicked.connect(self.save_images)
        self.ui.imageList.itemClicked.connect(self.preview_image)

        'Ajuste de tamanho'
        self.ui.imagePreview.setFixedSize(600,600)

    def select_images(self):
        'Abre uma janela para selecionar imagem e exibe na lista'
        files, _ = QFileDialog.getOpenFileNames(self, "Selecionar Imagens", "",
                                                "Imagens (*.png *.jpg *.jpeg *.bpm")
        if files:
            self.selected_images = files
            'Limpar lista antes de adicionar novas imagens'
            self.ui.imageList.clear()
            for file in files:
                item = QListWidgetItem(file)
                self.ui.imageList.addItem(item)

    def apply_filter(self):
        'Aplica um filtro às imagens selecionadas'
        for image_path in self.selected_images:
            'Carrega a imagem com Pillow'
            image = Image.open(image_path)
            'Aplica o filtro'
            filtered_image = image.filter(ImageFilter.CONTOUR)
            self.filtered_images[image_path] = filtered_image

            'Atualiza a pré visualizção da primeira imagem'
            if self.selected_images:
                pixmap = QPixmap(self.selected_images[0])
                self.ui.imagePreview.setPixmap(pixmap)

    def save_images(self):
        'Salva as imagens com filtro numa pasta escolhida'
        if not self.filtered_images:
            self.ui.statusbar.showMessage("Nenhuma imagem filtrada para salvar", 5000)
            return

        save_dir = QFileDialog.getExistingDirectory(self, "Selecione o local para salvar as imagens")
        if save_dir:
            for image_path, filtered_image in self.filtered_images.items():
                output_path = f"{save_dir}/{image_path.split('/')[-1]}"
                filtered_image.save(output_path)
            self.ui.statusbar.showMessage("Imagens salvas com sucesso!", 5000)

    def preview_image(self, item):
        'Visualização da imagem clicada'

        'Pegar o caminho da imagem clicada'
        image_path = item.text()
        'Carregar a imagem'
        pixmap = QPixmap(image_path)
        'Define no QLabel'
        self.ui.imagePreview.setPixmap(pixmap)
        'Ajusta o tamanho ao QLabel'
        self.ui.imagePreview.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec())

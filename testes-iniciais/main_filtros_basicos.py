import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PySide6.QtGui import QPixmap
from ui_filtrosbasicos_window import Ui_MainWindow
from PIL import Image, ImageFilter, ImageEnhance


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
        self.ui.applyContourButton.clicked.connect(self.apply_contour)
        self.ui.applyContrastButton.clicked.connect(self.apply_contrast)
        self.ui.applyNoiseButton.clicked.connect(self.apply_noise)
        self.ui.saveButton.clicked.connect(self.save_images)
        self.ui.imageList.itemClicked.connect(self.preview_image)

        'Ajuste de tamanho'
        self.ui.imagePreview.setFixedSize(500, 500)

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

        'Atualiza a pré visualização da primeira imagem'
        if self.selected_images:
            pixmap = QPixmap(self.selected_images[0])
            self.ui.imagePreview.setPixmap(pixmap)

    def apply_contour(self):
        'Aplica o filtro de CONTORNO às imagens selecionadas'
        for image_path in self.selected_images:
            'Carrega a imagem com Pillow'
            image = Image.open(image_path)
            'Aplica o filtro'
            filtered_image = image.filter(ImageFilter.CONTOUR)
            self.filtered_images[image_path] = filtered_image
            self.preview_filtered_image()

    def apply_contrast(self):
        'Aplica o filtro de CONTRASTE às imagens selecionadas'
        for image_path in self.selected_images:
            'Carrega a imagem com Pillow'
            image = Image.open(image_path)
            'Objeto para ajustar o contraste'
            enhancer = ImageEnhance.Contrast(image)
            '''1.0 → mantém o contraste original. 
            maior que 1.0 → aumenta o contraste. 
            menor que 1.0 → reduz o contraste.'''
            contrast_image = enhancer.enhance(1.5)
            self.filtered_images[image_path] = contrast_image
            self.preview_filtered_image()

    def apply_noise(self):
        'Aplica o filtro de REDUÇÃO DE RUIDO às imagens selecionadas'
        for image_path in self.selected_images:
            image = Image.open(image_path)
            noise_reduced_image = image.filter(ImageFilter.SMOOTH)
            self.filtered_images[image_path] = noise_reduced_image
            self.preview_filtered_image()

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

    def preview_filtered_image(self):
        'Se não houver nenhuma imagem filtrada, ele não dá retorno.'
        if not self.filtered_images:
            return

        'Pega o caminho e a imagem filtrada mais recente'
        last_image_path, last_filtered_image = list(self.filtered_images.items())[-1]

        'Salva a imagem filtrada em um arquivo temporário para exibição'
        temp_path = "../temp_preview.png"
        last_filtered_image.save(temp_path)

        'Cria um QPixmap da imagem salva e ajusta para o tamanho da pré-visualização'
        pixmap = QPixmap(temp_path).scaled(600, 600)
        self.ui.imagePreview.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec())

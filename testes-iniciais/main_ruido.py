import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PySide6.QtGui import QPixmap
from ui_ruido_window import Ui_MainWindow
from skimage import io, restoration, filters, metrics
from PIL import Image


class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """Lista para armazenamento das imagens selecionadas"""
        self.selected_images = []

        """Dicionário para armazenamento de imagens com filtros"""
        self.filtered_images = {}

        """Conexão dos botões às funções"""
        self.ui.selectImagesButton.clicked.connect(self.select_images)
        self.ui.applyWaveletButton.clicked.connect(self.apply_wavelet)
        self.ui.applyWienerButton.clicked.connect(self.apply_wiener)
        self.ui.applyMedianButton.clicked.connect(self.apply_median)
        self.ui.saveButton.clicked.connect(self.save_images)
        self.ui.imageList.itemClicked.connect(self.preview_image)

        """Ajuste de tamanho"""
        self.ui.imagePreview.setFixedSize(500, 500)

    def select_images(self):
        """Abre uma janela para selecionar imagem e exibe na lista"""
        files, _ = QFileDialog.getOpenFileNames(self, "Selecionar Imagens", "",
                                                "Imagens (*.png *.jpg *.jpeg *.bpm")
        if files:
            self.selected_images = files
            """Limpar lista antes de adicionar novas imagens"""
            self.ui.imageList.clear()
            for file in files:
                item = QListWidgetItem(file)
                self.ui.imageList.addItem(item)

        """Atualiza a pré visualização da primeira imagem"""
        if self.selected_images:
            pixmap = QPixmap(self.selected_images[0])
            self.ui.imagePreview.setPixmap(pixmap)

    def apply_filter(self, filter_function):
        """Função genérica que recebe um filtro como argumento
         e o aplica a todas as imagens selecionadas. Isso evita
         a repetição de código nas funções específicas de cada filtro."""

        for image_path in self.selected_images:
            """Precisa carregar a imagem em escala de cinza"""
            image = io.imread(image_path, as_gray=True)

            """O filter_function será substituído pelos outros três filtros"""
            filtered_image = filter_function(image)
            psnr_value = metrics.peak_signal_noise_ratio(image, filtered_image)
            self.ui.labelPSNR.setText(f"PSNR: {psnr_value:.2f} dB")

            """As imagens processadas pela scikit-image são representadas como arrays de float entre 0 e 1.
            Para converter para valores de pixel, multiplica por 255. O astype converte para imagem tradicional."""
            filtered_pil = Image.fromarray((filtered_image * 255).astype(np.uint8))
            self.filtered_images[image_path] = filtered_pil

        self.preview_filtered_image()

    def apply_wavelet(self):
        """Aplica o filtro de WAVELET às imagens selecionadas"""
        self.apply_filter(lambda img: restoration.denoise_wavelet(img, channel_axis=None))

    def apply_wiener(self):
        """Aplica o filtro de WIENER às imagens selecionadas"""
        self.apply_filter(lambda img: restoration.wiener(img, np.ones((5, 5)) / 25, balance=0.1))

    def apply_median(self):
        """Aplica o filtro de MEDIANA às imagens selecionadas"""
        self.apply_filter(lambda img: filters.median(img))

    def save_images(self):
        """Salva as imagens com filtro numa pasta escolhida"""
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
        """Visualização da imagem clicada"""

        """Pegar o caminho da imagem clicada"""
        image_path = item.text()
        """Carregar a imagem"""
        pixmap = QPixmap(image_path)
        """Define no QLabel"""
        self.ui.imagePreview.setPixmap(pixmap)
        """Ajusta o tamanho ao QLabel"""
        self.ui.imagePreview.setScaledContents(True)

    def preview_filtered_image(self):
        """Se não houver nenhuma imagem filtrada, ele não dá retorno."""
        if not self.filtered_images:
            return

        """Pega o caminho e a imagem filtrada mais recente"""
        last_image_path, last_filtered_image = list(self.filtered_images.items())[-1]

        """Salva a imagem filtrada em um arquivo temporário para exibição"""
        temp_path = "../temp_preview.png"
        last_filtered_image.save(temp_path)

        """Cria um QPixmap da imagem salva e ajusta para o tamanho da pré-visualização"""
        pixmap = QPixmap(temp_path).scaled(600, 600)
        self.ui.imagePreview.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec())

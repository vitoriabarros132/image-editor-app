import os
import sys
import cv2 as cv
import numpy as np
from PySide6.QtGui import QPixmap, QImage, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_main_window import Ui_mainWindow
import cv2.ximgproc as xip
from skimage import io, restoration, filters, exposure
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtGui import QIcon

if sys.platform == 'win32':
    import ctypes
    myappid = "editor.de.imagens.final"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    full_path = os.path.join(base_path, relative_path)

    return full_path

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        icon_path = get_resource_path("icone.ico")
        self.setWindowIcon(QIcon(icon_path))

        """Lista para armazenamento das imagens selecionadas"""
        self.selected_images = []
        self.filtered_images = {}
        self.equalized_images = {}

        """Conexão dos botões às funções"""
        self.ui.selectButton.clicked.connect(self.select_images)
        self.ui.applyButton.clicked.connect(self.apply_filters)
        self.ui.saveButton.clicked.connect(self.save_images)
        self.ui.imageList.clicked.connect(self.preview_original)

    def select_images(self):
        """Abre uma janela para selecionar imagens"""
        files, _ = QFileDialog.getOpenFileNames(self, "Selecionar Imagens", "", "Imagens (*.png *.jpg *.jpeg)")

        if files:
            self.selected_images = files

            # Criar um modelo para o QListView
            model = QStandardItemModel()

            for file in files:
                item = QStandardItem(file)
                model.appendRow(item)

            # Definir o modelo no QListView
            self.ui.imageList.setModel(model)

            # Atualiza a visualização da primeira imagem
            self.preview_original()

    def apply_filters(self):
        """Aplica o filtro e a equalização escolhidos pelo usuário"""
        if not self.selected_images:
            self.ui.statusbar.showMessage("Nenhuma imagem selecionada", 3000)
            return

        filtro_index = self.ui.filterBox.currentIndex()
        equalizacao_index = self.ui.equalizationBox.currentIndex()

        self.filtered_images = {}
        self.equalized_images = {}

        for image_path in self.selected_images:
            img = io.imread(image_path, as_gray=True)

            # Aplicando o filtro escolhido
            if filtro_index == 0:
                filtered = restoration.denoise_wavelet(img, channel_axis=None)
            elif filtro_index == 1:
                filtered = restoration.wiener(img, np.ones((5, 5)) / 25, balance=0.1)
            elif filtro_index == 2:
                filtered = filters.median(img)
            elif filtro_index == 3:
                # Esse filtro exige imagem BGR uint8, então converte a imagem grayscale para BGR
                img_bgr = cv.cvtColor((img * 255).astype(np.uint8), cv.COLOR_GRAY2BGR)
                # Aplica difusão anisotrópica diretamente em BGR uint8
                filtered_bgr = xip.anisotropicDiffusion(img_bgr, alpha=0.05, K=70, niters=5)
                # Converte o resultado BGR de volta para escala de cinza
                filtered = cv.cvtColor(filtered_bgr, cv.COLOR_BGR2GRAY)
                # Converte para float32 em escala [0, 1] para manter compatibilidade com equalização
                filtered = filtered.astype(np.float32) / 255.0
            else:
                filtered = img  # Sem filtro

            # Aplicando a equalização escolhida
            if equalizacao_index == 0:
                equalized = exposure.equalize_hist(filtered)
            elif equalizacao_index == 1:
                clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
                equalized = clahe.apply((filtered * 255).astype(np.uint8))
            else:
                equalized = filtered  # Sem equalização

            # Convertendo para formato correto antes de salvar
            self.filtered_images[image_path] = (filtered * 255).astype(np.uint8)
            self.equalized_images[image_path] = (equalized * 255).astype(np.uint8)

        # Chama a função de exibição
        self.preview_processed_images()

    def preview_original(self):
        """Exibe a primeira imagem original na label imgOriginal redimensionada para visualização"""
        if self.selected_images:
            img_path = self.selected_images[0]
            pixmap = QPixmap(img_path)

            # Redimensiona a imagem apenas para exibição, mantendo a proporção
            max_size = 250
            pixmap = pixmap.scaled(max_size, max_size, Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)

            self.ui.imgOriginal.setPixmap(pixmap)
            self.ui.imgOriginal.setScaledContents(True)

    def preview_processed_images(self):
        """Exibe as imagens filtradas e equalizadas"""
        if not self.filtered_images:
            return

        # Obtém a primeira imagem processada
        first_image_path = self.selected_images[0]
        
        filtered_image = self.filtered_images.get(first_image_path)        
        if filtered_image is None:
            return
        # Criando QImage para QLabel - FILTRADA
        height, width = filtered_image.shape
        bytes_per_line = width
        q_image_filtered = QImage(filtered_image.data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)

        # Criar um QPixmap e redimensionar para exibição - FILTRADA
        pixmap_filtered = QPixmap.fromImage(q_image_filtered).scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio,
                                                                     Qt.TransformationMode.SmoothTransformation)
        # Atualizar QLabel de imgFiltrada
        self.ui.imgFiltrada.setPixmap(pixmap_filtered)
        self.ui.imgFiltrada.setScaledContents(True)

        
        equalized_image = self.equalized_images.get(first_image_path)
        if equalized_image is None:
            return
        # Criando QImage para QLabel - EQUALIZADA
        height, width = equalized_image.shape
        bytes_per_line = width
        q_image_equalized = QImage(equalized_image.data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)

        # Criar um QPixmap e redimensionar para exibição - EQUALIZADA
        pixmap_equalized = QPixmap.fromImage(q_image_equalized).scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio,
                                                                       Qt.TransformationMode.SmoothTransformation)
        # Atualizar QLabel de imgEqualizada
        self.ui.imgEqualizada.setPixmap(pixmap_equalized)
        self.ui.imgEqualizada.setScaledContents(True)

    def save_images(self):
        """Salva as imagens com filtros e equalização"""
        if not self.filtered_images:
            self.ui.statusbar.showMessage("Nenhuma imagem processada para salvar", 3000)
            return

        save_dir = QFileDialog.getExistingDirectory(self, "Selecione o local para salvar as imagens")
        if save_dir:
            for image_path, processed_image in self.equalized_images.items():
                output_path = f"{save_dir}/{image_path.split('/')[-1]}"
                cv.imwrite(output_path, processed_image)

            self.ui.statusbar.showMessage("Imagens salvas com sucesso!", 3000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec_())


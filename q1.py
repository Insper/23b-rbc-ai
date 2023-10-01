import numpy as np
import cv2

class DetectorFormas():
    def __init__(self):
        self.formas = {
            'quadrado': [],
            'triangulo': [],
            'circulo': [],
            'estrela': [],
            'flecha': [],
        }

        self.centros = []

    def run(self, bgr: np.ndarray) -> np.ndarray:
        """ Realiza a detecção de formas geométricas na imagem.
        Retorna a imagem com as formas detectadas.
        Salva as formas detectadas no atributo self.formas no formato:
        {
            'quadrado': [(x1, y1), (x2, y2), ...],
            'triangulo': [(x1, y1), (x2, y2), ...],
            ...

        Args:
            bgr (np.ndarray): Imagem BGR

        Returns:
            bgr (np.ndarray): Imagem com o nome das formas detectadas
        """
        
        return bgr

def rodar_frame():
    RodaAtividade = DetectorFormas()
    
    bgr = cv2.imread("img/q1/base-formas1.png") # Escolha aqui a imagem que deseja usar para testar

    bgr = RodaAtividade.run(bgr)

    cv2.imshow("Imagem", bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    rodar_frame()

if __name__ == "__main__":
    main()
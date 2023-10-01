import numpy as np
import cv2

class CowMonitor():
    def __init__(self):
        self.animais = {
            'vacas':[],
            'cavalos':[],
        }
        self.right = []
        self.left = []

        self.total_animais_da_Direita = 0
        self.total_animais_da_Esquerda = 0
        self.vacas_intrusas_na_Direita = 0
        self.vacas_intrusas_na_Esquerda = 0

        self.vacas_solitarias_na_Direita = 0
        self.vacas_solitarias_na_Esquerda = 0

        self.fence = None

    def run(self, bgr: np.ndarray) -> np.ndarray:
        """Esta função deve receber uma imagem e processar o 
            numero de animais de cada fazenda, 
            o numero de vacas que estão na fazenda errada 
            e o numero de vacas solitarias.
        Salva os anumais detectados no atributo self.animais no formato:
            {
                'vacas': [(x1, y1), (x2, y2), ...],
                'cavalos': [(x1, y1), (x2, y2), ...],
            }
        Tambem salva o centro do tag de cada fazenda no atributo self.right e self.left no formato:
            [(x1, y1), (x2, y2), ...]
        
        Args:
            bgr (np.ndarray): Imagem BGR

        Returns:
            bgr (np.ndarray): Imagem de saida
        """

        return bgr



def rodar_frame():
    RodaAtividade = CowMonitor()
    
    bgr = cv2.imread("img/q2/base-cows1.png") # Escolha aqui a imagem que deseja usar para testar

    bgr = RodaAtividade.run(bgr)

    print(f"Total de animais que pertencem a fazenda Direita: {RodaAtividade.total_animais_da_Direita}")
    print(f"Total de animais que pertencem a fazenda Esquerda: {RodaAtividade.total_animais_da_Esquerda}")
    print(f"Total de vacas intrusas na fazenda Direita: {RodaAtividade.vacas_intrusas_na_Direita}")
    print(f"Total de vacas intrusas na fazenda Esquerda: {RodaAtividade.vacas_intrusas_na_Esquerda}")
    print(f"Total de vacas solitarias na fazenda Direita: {RodaAtividade.vacas_solitarias_na_Direita}")
    print(f"Total de vacas solitarias na fazenda Esquerda: {RodaAtividade.vacas_solitarias_na_Esquerda}")

    cv2.imshow("Imagem", bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    rodar_frame()

if __name__ == "__main__":
    main()
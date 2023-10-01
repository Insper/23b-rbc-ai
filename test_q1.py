import pytest
import cv2
from unittest.mock import patch
import numpy as np
import traceback

from q1 import DetectorFormas

formas_expected = {
    'base-formas1.png': {'quadrado': [], 'triangulo': [(671, 62)], 'circulo': [(888, 526), (422, 462)], 'estrela': [], 'flecha': []},
    'base-formas2.png': {'quadrado': [(373, 336), (141, 120)], 'triangulo': [(103, 420), (889, 384)], 'circulo': [(948, 184)], 'estrela': [], 'flecha': []},
    'base-formas3.png': {'quadrado': [(180, 447), (570, 340)], 'triangulo': [(916, 155)], 'circulo': [(310, 178)], 'estrela': [], 'flecha': []},
    'des-formas4.png': {'quadrado': [(613, 347)], 'triangulo': [(337, 146), (865, 113)], 'circulo': [(312, 178), (444, 556)], 'estrela': [(825, 455)], 'flecha': [(137, 360)]},
    'des-formas5.png': {'quadrado': [(586, 389)], 'triangulo': [(444, 86)], 'circulo': [(312, 178), (488, 436)], 'estrela': [(850, 352), (128, 267)], 'flecha': [(148, 451), (743, 120)]}
}

centros_expected = {
    'base-formas1.png': 3,
    'base-formas2.png': 5,
    'base-formas3.png': 4,
    'des-formas4.png': 7,
    'des-formas5.png': 8
}

def run(fname):
    RodaAtividade = DetectorFormas()
    bgr = cv2.imread(fname)
    with patch('cv2.imshow'):
        bgr = RodaAtividade.run(bgr)
    
    result = {}
    result['formas'] = formas_check(RodaAtividade.formas, formas_expected[fname.split('/')[-1]])
    result['centros'] = len(RodaAtividade.centros) == centros_expected[fname.split('/')[-1]]
    return result

def distance(p1, p2):
     return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
def formas_check(formas,expected):
    res = {}
    # loop through both dicts
    for k in formas.keys():
        if len(formas[k]) != len(expected[k]):
            res[k] = False
        elif len(formas[k]) == 0:
            res[k] = True
        else:
            res[k] = np.any([distance(p1,p2) < 10 for p1 in formas[k] for p2 in expected[k]])
    return res
             
def check_base(result):
        nota = 0
        centros = np.all([result[k]['centros'] for k in result.keys()])
        if centros:
            nota += 1
            print('[+1,0] Encontra o contorno e centro de todas as forma')
        quadrado = np.all([result[k]['formas']['quadrado'] for k in result.keys()])
        triangulo = np.all([result[k]['formas']['triangulo'] for k in result.keys()])
        circulo = np.all([result[k]['formas']['circulo'] for k in result.keys()])
        resultado = np.sum(np.array([quadrado, triangulo, circulo], dtype=np.uint8))
        if resultado == 1:
            nota += 0.5
            print('[+0,5] Encontra uma forma corretamente')
        elif resultado == 2:
            nota += 1
            print('[+1,0] Encontra duas formas corretamente')
        elif resultado == 3:
            nota += 2.
            print('[+2,0] Encontra todas as formas corretamente para as imagens base')
        return nota

def check_des(result):
    estrela = np.all([result[k]['formas']['estrela'] for k in result.keys()])
    flecha = np.all([result[k]['formas']['flecha'] for k in result.keys()])
    resultado = np.sum(np.array([estrela, flecha], dtype=np.uint8))
    nota = 0
    if resultado == 2:
        nota += 1
        print('[+1,0] Identifica corretamente todas as formas, em todas as imagens - parabens!')
    return nota

def test():
    result = {
        'base-formas1.png': run('img/q1/base-formas1.png'),
        'base-formas2.png': run('img/q1/base-formas2.png'),
        'base-formas3.png': run('img/q1/base-formas3.png'),
    }
    result_des = {
        'des-formas4.png': run('img/q1/des-formas4.png'),
        'des-formas5.png': run('img/q1/des-formas5.png')
    }
    nota = check_base(result)
    if nota < 3:
        print(f'Nota estimada da questao: {nota} - não qualifica para o desafio')
    else:
        nota += check_des(result_des)
        print(f'Nota estimada da questao: {nota}')
    
    try:
        assert False, ''
    except:
        pass
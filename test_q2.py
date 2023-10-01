import pytest
import cv2
from unittest.mock import patch
import numpy as np
import traceback

from q2 import CowMonitor

animais_expected = {
    'base-cows1.png': {'vacas': [(841, 374), (1105, 547), (474, 196), (1074, 241), (203, 189), (153, 513)], 'cavalos': [(410, 471)]},
    'base-cows2.png': {'vacas': [(778, 204), (1009, 132), (514, 205), (343, 392), (142, 198)], 'cavalos': [(871, 517), (238, 563)]},
    'base-cows3.png': {'vacas': [(168, 432), (492, 341), (771, 428), (748, 606), (271, 198), (386, 506)], 'cavalos': [(973, 280)]},
    'des-cows4.png': {'vacas': [(370, 200), (232, 616), (990, 564), (780, 185), (1083, 121), (148, 235), (1092, 311), (231, 430), (781, 404)], 'cavalos': [(698, 595)]},
    'des-cows5.png': {'vacas': [(1132, 309), (727, 427), (1125, 622), (732, 215), (515, 273), (214, 242), (486, 570), (1008, 459), (1118, 117)], 'cavalos': [(186, 519)]}
}

fence_expected = {
    'base-cows1.png': 705,
    'base-cows2.png': 640,
    'base-cows3.png': 619,
    'des-cows4.png': 521,
    'des-cows5.png': 871,
}
baselist = ['total_animais_da_Direita', 'total_animais_da_Esquerda', 'vacas_intrusas_na_Direita', 'vacas_intrusas_na_Esquerda']
deslist = ['vacas_solitarias_na_Direita', 'vacas_solitarias_na_Esquerda']
values_expected = {
    'base-cows1.png': [4, 3, 1, 2, 0, 0],
    'base-cows2.png': [4, 3, 1, 1, 0, 0],
    'base-cows3.png': [3, 4, 1, 2, 0, 0],
    'des-cows4.png': [3, 5, 3, 2, 1, 1],
    'des-cows5.png': [4, 4, 2, 3, 0, 2],
}

def run(fname):
    RodaAtividade = CowMonitor()
    bgr = cv2.imread(fname)
    with patch('cv2.imshow'):
        bgr = RodaAtividade.run(bgr)
    
    result = {}
    result['animais'] = animais_check(RodaAtividade.animais, animais_expected[fname.split('/')[-1]])
    result['values'] = values_check(RodaAtividade, values_expected[fname.split('/')[-1]])
    result['fence'] = RodaAtividade.fence == fence_expected[fname.split('/')[-1]]
    return result

def distance(p1, p2):
     return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
def animais_check(animais,expected):
    res = {}
    # loop through both dicts
    for k in animais.keys():
        if len(animais[k]) != len(expected[k]):
            res[k] = False
        elif len(animais[k]) == 0:
            res[k] = True
        else:
            res[k] = np.any([distance(p1,p2) < 10 for p1 in animais[k] for p2 in expected[k]])
    return res

def values_check(RodaAtividade, expected):
    result = []
    for k in baselist:
        comp = getattr(RodaAtividade, k) == expected.pop(0)
        result.append(comp)
        
    for k in deslist:
        comp = getattr(RodaAtividade, k) == expected.pop(0)
        result.append(comp)
    return result

def check_base(results):
    nota = 0
    animais = np.all([np.all(list(x['animais'].values())) for x in results.values()])
    if animais:
        nota += 0.5
        print('[+0,5] Identifica corretamente os animais e salva no dicionário self.animais')

    fence = np.all([x['fence'] for x in results.values()])
    if fence:
        nota += 0.5
        print('[+0,5] Identifica corretamente a cerca e salva no atributo self.fence')

    total_animais = np.all([np.all(x['values'][:2]) for x in results.values()])
    if total_animais:
        nota += 1.0
        print('[+1,0] Identifica corretamente o total de animais de cada fazenda')
    
    vacas_intrusas = np.all([np.all(x['values'][2:4]) for x in results.values()])
    if vacas_intrusas:
        nota += 1.0
        print('[+1,0] Identifica corretamente o total de vacas intrusas de cada fazenda')
    return nota

def check_des(results):
    animais = np.all([np.all(list(x['animais'].values())) for x in results.values()])
    fence = np.all([x['fence'] for x in results.values()])
    total_animais = np.all([np.all(x['values'][:2]) for x in results.values()])
    vacas_intrusas = np.all([np.all(x['values'][2:4]) for x in results.values()])
    vacas_solitarias = np.all([np.all(x['values'][4:]) for x in results.values()])

    nota = 0
    if not animais:
        print('falha ao identificar os animais nas imagens desafio')
    if not fence:
        print('falha ao identificar a cerca nas imagens desafio')
    if not total_animais:
        print('falha ao identificar o total de animais nas imagens desafio')
    if not vacas_intrusas:
        print('falha ao identificar o total de vacas intrusas nas imagens desafio')
    if not vacas_solitarias:
        print('falha ao identificar o total de vacas solitarias nas imagens desafio')
    if animais and fence and total_animais and vacas_intrusas and vacas_solitarias:
        nota += 1.0
        print('[+1,0] Calcula corretamente os número de animais que não pertencem a nenhuma fazenda - parabens!')
    return nota

def test():
    result = {
        'base-cows1.png': run('img/q2/base-cows1.png'),
        'base-cows2.png': run('img/q2/base-cows2.png'),
        'base-cows3.png': run('img/q2/base-cows3.png'),
    }
    result_des = {
        'des-cows4.png': run('img/q2/des-cows4.png'),
        'des-cows5.png': run('img/q2/des-cows5.png'),
    }
    print(result)
    nota = check_base(result)
    if nota < 3:
        print(f'Nota estimada da questao: {nota} - não qualifica para o desafio')
    else:
        nota += check_des(result_des)
        print(f'Nota estimada da questao: {nota}')


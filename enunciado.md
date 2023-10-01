# Robótica Computacional 2023.2

Observações de avaliações nesta disciplina:

* A prova tem duração de **2 horas**.
* Inicie a prova no Blackboard para a ferramenta de Proctoring iniciar. Só finalize o Blackboard quando enviar a prova via Github classroom.
* Durante esta prova vamos registrar somente a tela, não a câmera nem microfone.
* Coloque seu nome e email no README.md do seu repositório.
* Você pode consultar a internet ou qualquer material que usamos no curso, mas não pode se comunicar com pessoas ou colegas a respeito da prova. Também não pode usar ferramentas de **IA** como chatGPT ou Github Copilot durante a prova.
* Faça commits e pushes frequentes no seu repositório.
* Avisos importantes serão dados na sala da prova.
* Permite-se consultar qualquer material online ou próprio. Não se pode compartilhar informações com colegas durante a prova.
* Faça commits frequentes. O primeiro a enviar alguma ideia será considerado autor original.
* A responsabilidade por ter o *setup* funcionando é de cada estudante.
* Questões de esclarecimento geral podem ser perguntadas.
* É vedado colaborar ou pedir ajuda a colegas ou qualquer pessoa que conheça os assuntos avaliados nesta prova.
* Para fazer uma avaliação estimada do seu código, execute o comando `pytest test_q1.py` ou `pytest test_q2.py` no terminal. O resultado será exibido no terminal. Se tiver problemas com o `pytest`, de commit e push no seu repositório e visualize o resultado na aba `Actions` do seu repositório no Github.
* Manter o formato de saída e variáveis é parte da avaliação.

# Exercício 1 [3 + 1]

Neste exercício você deve implementar um código que identifica as formas geométricas nas imagens. As formas geométricas são: `quadrado`, `triangulo` e `circulo`. 

Para a avaliação, você deve salvar na lista `self.centros` o centro de cada forma, no formato `(x, y)`, e no dicionário `self.formas` o nome da forma, no formato `{'quadrado': [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], ...}`. Manter o formato de saída é parte da avaliação.

Seu código deve ser robusto para identificar as formas geométricas em qualquer imagem, independentemente de sua orientação, tamanho, cor e etc. Incluindo na ausência de alguma forma.

- Imagens com prefixo `base-`: são as imagens que serão utilizadas para avaliar seu código. Contendo as formas geométricas `quadrado`, `triangulo` e `circulo`. 
- Imagens com prefixo `des-`: são imagens consideradas **DESAFIO**, nelas existem formas que não foram apresentadas no conjunto das imagens `base-`, são elas: estrela e flecha e o triângulo é equilátero e não isósceles.

**Atenção:** Só serão avaliados códigos dentro da classe `DetectorFormas`. Não mudem a entrada e a saída da classe `DetectorFormas` e da função `run`, pois elas serão utilizadas para avaliar seu código. Fora isso, é permitido criar quantas funções auxiliares forem necessárias. Manter o formato descrito é parte da avaliação.

1. [+1,0] Encontra o contorno e centro de todas as formas e salva na lista `self.centros`
2. [+0,5] Identifica corretamente uma das formas nas imagens com prefixo `base-` e salva os centros na chave correspondente no dicionário `self.formas`
3. [+0,5] Identifica corretamente duas das formas nas imagens com prefixo `base-` e salva os centros na chave correspondente no dicionário `self.formas`
4. [+1,0] Identifica corretamente todas as formas nas imagens com prefixo `base-`, salva os centros na chave correspondente no dicionário `self.formas` **e escreve o nome da forma na imagem.**
5. [+1,0] **DESAFIO**: Identifica corretamente todos as formas, em todas as imagens (prefixos `base-` e `des-`), salva os centros na chave correspondente no dicionário `self.formas` e escreve o nome da forma na imagem.

# Exercício 2 [3 + 1]

Neste exercício você está implementando um sistema de monitoramento de vacas que tem o costume de invadir a fazenda vizinha. A esquerda da cerca é a fazenda `Esquerda` e à direita da cerca está a fazenda `Direita`. A fazenda `Esquerda` coloca uma `tag vermelha` em todos os animais e a fazenda `Direita` coloca uma `tag roxa` em todos os animais. A cerca é representada pela linha vertical tracejada. **Vacas que não pertencem a fazenda onde estão são consideradas `intrusas`.**

Além das vacas, existem cavalos que o sistema deve contar na hora de estimar o número de animais em cada fazenda, mas não tem problema se eles invadirem a fazenda vizinha.

- Imagens com prefixo `base-`: são as imagens que serão utilizadas para avaliar seu código.
- Imagens com prefixo `des-`: são imagens consideradas **DESAFIO**, nelas alguns animais não identificados `sem tag`, ou seja, que não pertencem a nenhuma das duas fazendas aparecem nas imagens e devem ser considerados como `solitárias`, você deve contar os animais `sem tag` nas variáveis `self.vacas_solitarias_na_Direita` e `self.vacas_solitarias_na_Esquerda`, mas elas **também** devem ser consideradas como `intrusas`.

Para a avaliação, você deve salvar no dicionário `self.animais` o nome do animal, no formato `{'vaca': [(x1, y1), (x2, y2)], ...}`. O centro dos tags devem ser armazenados corretamente nas listas `self.right` e `self.left`, no formato `[(x1, y1),(x2, y2)]`. Manter o formato de saída é parte da avaliação.

**Atenção:** Só serão avaliados códigos dentro da classe `CowMonitor`. Não mudem a entrada e a saída da classe `CowMonitor` e da função `run`, pois elas serão utilizadas para avaliar seu código. Fora isso, é permitido criar quantas funções auxiliares forem necessárias. Manter o formato descrito é parte da avaliação.

1. [+0,5] Identifica corretamente os animais e salva no dicionário `self.animais`
3. [+0,5] Calcula corretamente a posição da cerca divisória na imagem e salva na variável `self.fence`
3. [+1,0] Calcula corretamente o total de animais (vacas e cavalos) que pertencem a cada fazenda e salva nas variáveis `self.total_animais_da_Direita` e `self.total_animais_da_Esquerda`
4. [+1,0] Calcula corretamente o número de **vacas** intrusas em cada fazenda e salva nas variáveis `self.vacas_intrusas_na_Direita` e `self.vacas_intrusas_na_Esquerda`
5. [+1,0] **DESAFIO**: Calcula corretamente o número de animais que não pertencem a nenhuma fazenda (sem tag) e salva nas variáveis `self.vacas_solitarias_na_Direita` e `self.vacas_solitarias_na_Esquerda`

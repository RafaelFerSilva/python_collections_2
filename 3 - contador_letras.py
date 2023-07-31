from collections import Counter

texto1 = """
Fazer seu próprio horário, ter liberdade geográfica e um pouco de flexibilidade na rotina é o sonho de muita gente que escolhe trabalhar como autônoma, não é mesmo? Com o avanço das tecnologias da internet, o desejo de desfrutar das vantagens dessa modalidade de trabalho tornou-se ainda mais acessível para muitos.

É comum rolar os stories do Instagram e se deparar com anúncios que prometem mudar vidas, com garantias de faturamento infinito e um mínimo de esforço no trabalho autônomo. A verdade é que existem inúmeros discursos sobre como obter sucesso e lucro na carreira freelancer, mas, independentemente do caminho que você escolherá para isso, ter uma gestão financeira organizada é um dos pilares fundamentais para ter sucesso em seu projeto autônomo, uma vez que a saúde financeira do seu negócio é o que ditará o ritmo do seu crescimento.

Se você quer aprender mais sobre como fazer uma gestão financeira eficiente, continue a leitura deste artigo. Nele você conhecerá:

Os primeiros passos para uma gestão financeira eficiente;
As principais dicas para uma boa organização financeira para freelancers;
Como lidar com a imprevisibilidade inerente ao trabalho autônomo e como se precaver para os diferentes cenários.
"""

texto2 = """
Com a crescente necessidade de lidar com grandes quantidades de dados, a engenharia de dados tem ganhado cada vez mais relevância no mercado. A cada dia novas tecnologias surgem, e aumentamos a quantidade de dispositivos e sensores conectados, gerando uma quantidade considerável de dados. Empresas e organizações têm acesso a uma quantidade exponencial de informações provenientes de fontes diversas. No entanto, lidar com esses dados de maneira eficiente e eficaz requer uma abordagem estruturada. Nesse contexto, surge o conceito de pipeline de dados, uma solução estratégica para gerenciar o fluxo de informações em todas as áreas relacionadas aos dados.

Componentes de um pipeline de dados
Um pipeline de dados é uma sequência de etapas interconectadas que permitem a coleta, armazenamento, transformação, análise e visualização de dados, com a intenção de facilitar o fluxo contínuo e automatizado de informações, desde a sua origem até o destino final, a fim de obter insights valiosos e tomar decisões informadas.

O principal objetivo de um pipeline de dados é fornecer uma estrutura eficiente e confiável para lidar com grandes volumes de dados, garantindo sua integridade, segurança e acessibilidade. Mas, independente da ordem do fluxo que escolhemos, um pipeline de dados conta com alguns componentes principais como fontes de dados, transformações e destinos.
"""


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    print(aparicoes)
    total_caracteres = sum(aparicoes.values())
    print(total_caracteres)

    proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, propocao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, propocao * 100))


analisa_frequencia_de_letras(texto1)

analisa_frequencia_de_letras(texto2)


'''
Sript para rodar no terminal PyQgis
Este Script pega a tabela vinda do acervo fundiário, SNCI ou SIGEF onde os 
códigos do imóvel rural estão sem formatação e coloca os pontos e traços no 
formato 000.000.000.000-0.

## INSTRUÇÕES ##
- Selecione a camada que será editada no painel de camadas;
- Criar um campo na tabela de atributos chamado "cod_sncr" tipo string com tamanho
17;
- Informar o nome da coluna que contém os valores a serem formatados

autor:  Israel Ely de Almeida Oliveira
e-mail: israel.oliveira@incra.gov.br
'''
camada = qgis.utils.iface.activeLayer()

#nome da coluna na tabela de entrada com os valores do código do imóvel
# Tabela SIGEF = codigo_imo
# Tabela SNCR  = cod_imovel
cod_tabela = 'codigo_imo'
# formata o código do imóvel com 17 digitos 000.000.000.000-0
def format_cod(codigo):
    if codigo == '':
        return '000.000.000.000-0'
    else:
        codigo = '{:0>13}'.format(str(codigo).split('.')[0])
        t1 = codigo[0:3]
        t2 = codigo[3:6]
        t3 = codigo[6:9]
        t4 = codigo[9:12]
        t5 = codigo[12:]
        codigo = f'{t1}.{t2}.{t3}.{t4}-{t5}'
        return codigo
        
cont = camada.featureCount()

for i in range(1,cont+1):
    print(i)
    prov = camada.dataProvider()
    linha = camada.getFeature(i)
    cod = linha[cod_tabela]
    cod = format_cod(cod)
    codigo = camada.fields().lookupField('cod_sncr')
    atts = {codigo: cod}
    prov.changeAttributeValues({linha.id(): atts})
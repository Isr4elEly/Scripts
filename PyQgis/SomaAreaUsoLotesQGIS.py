'''
Sript para rodar no terminal PyQgis
Este Script analisa um shape de parcelamento de lotes do INCRA gerando dados 
para o relatório técnico.

## REQUERIMENTOS ##
- Pandas

## INSTRUÇÕES ##
- Selecione a camada que será editada no painel de camadas;
- preparar a tabela de atributos conforme está no código de carregamento do 
    pandas;
- Informar o nome da coluna que contém os valores a serem formatados

autor:  Israel Ely de Almeida Oliveira
e-mail: israel.oliveira@incra.gov.br
'''
import pandas as pd


camada = qgis.utils.iface.activeLayer()
nome_do_pa = 'PA xxxx'


print(camada.id())
print(camada.featureCount())
#imprimir o nome dos campos da tabela de atributos
print('-*-'*30)
for fild in camada.fields():
    print('Campo de Tabela -> ',fild.name())
# carregando os dados da tabela de atributos da camada selecionada
dados = camada.getFeatures()
#transformando a tabela de atributos em um dataframe pandas
df = pd.DataFrame(dados, columns=['FID', 'tipo', 'area', 'nome'])

# Cálculos
print('-*-'*30)
print('Área Total das Parcelas')
print(round(df['area'].sum(),4))
print('-*-'*30)
print(f'Tipos de Parcelas encontradas no PA {nome_do_pa} com a Totalização de Áreas em ha')
print(df.groupby(['tipo']).sum())
print('-*-'*30)
print('Área total dos Lotes Individuais por Beneficiário')
print(df[df['tipo'] == 'Lote'].groupby(['nome']).sum())
df2 = df.groupby(['nome']).sum()

import matplotlib.pyplot as plt
import pandas as pd

raw=pd.read_excel(r'caminhodoarqiovcompleto')


def tratamento():
    return raw[(raw['colunafiltro1'] != 'filtro1') & (raw['colunafiltro2'] != 'filtro2')]
curated=tratamento()


def pivot():#pivot table
    pivot1=pd.pivot_table(curated,
                          values='nomedacolunavalor',
                          index='nome da coluna linha',
                          columns='nomedacoluna',
                          aggfunc='nomedafuncao de agregacao')
    print(pivot1)
    return pivot1

def agrupado():
    pivot2=curated.groupby('nomedacolunalinha')['nomedacolunavalor'].sum()
    pivot2=pivot2.sort_values()
    print(pivot2)
    return pivot2

def colunasempihadas(pivot1): 
    pivot1.plot(kind='bar',stacked=True,color=['#f5bf42', 'orange', '#693202','#232326'])

    for i , valor in enumerate(pivot1.sum(axis=1)):
        plt.text(i,valor,f'R${valor:.0f}',ha='center')
    plt.title('TITULODOB GRAFICO')
    plt.xlabel("nomedoindex")
    plt.ylabel("nomedoeixoy")
    plt.xticks(rotation=45,ha='right')
    plt.show()
pivot1 = pivot()
colunasempihadas(pivot1)


def grafcolunas(pivot2):
    plt.bar(pivot2.index,pivot2.values,color='orange')

    for i , valor in enumerate(pivot2.values):
        plt.text(i,valor,f'{valor:.0f}',ha='center')

    plt.title('TITULODOB GRAFICO')
    plt.xlabel("index")
    plt.ylabel("Valor")
    plt.xticks(rotation=45,ha='right')
    plt.show()
pivot2=agrupado()
grafcolunas(pivot2)

def grafcolunaspercent(pivot2):
    
    total = pivot2.sum()  
    
    plt.bar(pivot2.index, pivot2.values, color='orange')

    for i, valor in enumerate(pivot2.values):
        percentual = (valor / total) * 100  
        plt.text(i, valor + 0.5, f'R${valor:.0f}\n({percentual:.1f}%)', ha='center')

    plt.title('NOME DO GRAFICO DE PORCENTAGENS')
    plt.xlabel("Categoria")
    plt.ylabel("Valor")
    plt.xticks(rotation=45, ha='right')
    plt.show()
pivot2=agrupado()
grafcolunaspercent(pivot2)


def mostrar_tabela(pivot2):
    
   
    total = pivot2.sum()
    table_data = pivot2.reset_index()
    table_data['Percentual'] = (table_data['colunavalor'] / total) * 100
    
    
    table_data['colunavalor'] = table_data['colunavalor'].round(2)
    table_data['Percentual'] = table_data['Percentual'].round(2)
    
   
    total_row = pd.DataFrame({'nomedacoluna': ['Total'], 'nomedacolunavalor': [total], 'Percentual': [100]})
    table_data = pd.concat([table_data, total_row], ignore_index=True)
    
    
    fig, ax = plt.subplots(figsize=(8, 4))  # Cria uma figura e eixo, ajustando o tamanho da figura
    table = ax.table(cellText=table_data.values,
                    colLabels=table_data.columns,
                    cellLoc='center', loc='center')

    
    ax.axis('off')

    plt.show()
pivot2=agrupado()
mostrar_tabela(pivot2)
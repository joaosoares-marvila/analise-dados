import pandas as pd
import os
from loguru import logger

def obtem_dados_arquivo_csv(caminho_arquivo: str, delimitador: str)-> list[dict]:
    
    df = pd.read_csv(
            filepath_or_buffer=caminho_arquivo,
            delimiter=delimitador,
            header=None
        )

    dados_retorno = []

    for linha in df.iloc:
        
        id = linha[0]
        placa = linha[1]
        marca = linha[2]
        modelo = linha[3]

        dados_retorno.append({
            'id':id,
            'placa':placa,
            'marca':marca,
            'modelo':modelo
        })

        logger.info(f"Id:{id}\tPlaca:{placa}\tMarca:{marca}\tModelo:{modelo}")

    """    if coluna4 == 'Braund, Mr. Owen Harris':
            df.at[indice, 12] = 'TEstandoa'
        df.to_csv(path_or_buf=arquivo_titanic, index=False, header=False)"""

def adiciona_retorno(caminho_arquivo: str, delimitador: str, id: str, retorno:str, indice_coluna_retorno)-> None:
    
    df = pd.read_csv(
        filepath_or_buffer=caminho_arquivo,
        delimiter=delimitador,
        header=None
    )

    condicao = df.iloc[:, 0] == id

    df.loc[condicao, indice_coluna_retorno] = retorno
    df.to_csv(path_or_buf=caminho_arquivo, index=False, header=False)


if __name__ == '__main__':
    arquivo_titanic = os.path.join(os.getcwd(),'assets', 'titanic_treino.csv')
    
    obtem_dados_arquivo_csv(
        caminho_arquivo=arquivo_titanic, 
        delimitador=','
    )
    
    adiciona_retorno(
        caminho_arquivo=arquivo_titanic,
        delimitador=',',
        id=3,
        indice_coluna_retorno=2,
        retorno='Chevrolet'
    )

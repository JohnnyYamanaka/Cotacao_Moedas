import pandas as pd


def transform_data(dicionary: dict):
    df_cotacao = pd.DataFrame.from_dict(dicionary["value"])

    df_cotacao["dataHoraCotacao"] = pd.to_datetime(
        df_cotacao["dataHoraCotacao"], format="%Y-%m-%d %H:%M:%S.%f"
    )

    df_cotacao["moeda"] = "USD"
    df_cotacao["dataCotacao"] = pd.to_datetime(df_cotacao["dataHoraCotacao"].dt.date)
    df_cotacao["horaCotacao"] = df_cotacao["dataHoraCotacao"].dt.time
    # df_cotacao['dataConsulta'] = dt_consulta

    return df_cotacao

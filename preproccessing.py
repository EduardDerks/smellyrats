import numpy as np
import pandas as pd


def pareto_scaling(series: pd.Series) -> pd.Series:
    """
    Pareto scale the series. According to the paper (see src) pareto scaling is
    dividing the series by the square root of the standard deviation of the
    values of the series.

    Parameters
    ----------
    series : pd.Series
        The series to be scaled.

    Returns
    -------
    pd.Series : Pareto scaled column.

    TODO
    ----
    Make a `sklearn` transfromer from this function.

    Src:
    H. Winning, E. Roldan-Marin, L.O. Dragsted, An exploratory NMR
    nutri-metabonomic investigation reveals dimethyl sulfone as a dietary
    biomarker for onion intake.  September 2009
    """
    return series / np.sqrt(np.std(series))

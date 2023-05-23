import datetime
import logging
from typing import Iterable
from io import BytesIO

import pandas as pd
import numpy as np
from matplotlib import pyplot, dates as mdates


def generate_time_scatter_plot(
    labels_array: Iterable[str],
    timestamps_array: Iterable[datetime.datetime],
    timestamp_now: datetime.datetime,
    period_seconds: int,
) -> BytesIO:
    """
    Функция генерации графиков отметок запросов.
    :param labels_array:
    :param timestamps_array:
    :param timestamp_now:
    :param period_seconds:
    :return:
    """

    # Для удобной работы с группировкой данных был использован pandas.
    timestamps_dataframe = pd.DataFrame(
        dict(label=labels_array, timestamps=timestamps_array)
    ).groupby("label")

    figure, ax = pyplot.subplots(figsize=(12, 4), layout="constrained")

    ax.plot(
        (timestamp_now - datetime.timedelta(seconds=period_seconds), timestamp_now),
        (0, 0),
        marker=".",
        linestyle="",
        color="white",
    )
    for label, label_timestamps in timestamps_dataframe:
        logging.warning(label_timestamps.timestamps.values)
        logging.warning(tuple(np.zeros(label_timestamps.timestamps.shape[0])))
        ax.plot(
            label_timestamps.timestamps.values,
            list(np.zeros(label_timestamps.timestamps.shape[0])),
            marker="o",
            linestyle="",
            ms=6,
            label=label,
        )

    ax.set(title="Запросы агентов за последние {} секунд.".format(period_seconds))
    ax.margins(0.05)
    ax.xaxis.set_major_locator(mdates.SecondLocator(interval=period_seconds // 24))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))

    pyplot.setp(ax.get_xticklabels(), rotation=30, ha="right")
    ax.yaxis.set_visible(False)
    ax.spines[["left", "top", "right"]].set_visible(False)
    ax.legend()

    buffer = BytesIO()
    pyplot.savefig(buffer)
    buffer.seek(0)
    return buffer

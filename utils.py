"""This module contains functionality for querying flights from Modlin Airport,
hotels from TUI, and attractions from DbPedia."""

import json
import os
import tempfile
from datetime import datetime, timedelta

import pandas as pd
import pysparql_anything as sa
from jinja2 import Template

engine = sa.SparqlAnything()

def get_attractions_for_flights(flights: pd.DataFrame) -> pd.DataFrame:
    dfs = []
    for ix, row in get_flights().iterrows():
        dest = row["destText"].split()[0].lower().capitalize()
        dfs.append(get_attractions_for_city(dest))
    return pd.concat(dfs)


def get_flights() -> pd.DataFrame:
    """Get flights from Modlin Airport."""
    query_file = "queries/modlin.rq"

    df = engine.select(
        query=query_file,
        values={"location": "https://www.modlinairport.pl/pasazer/rozklad-lotow"},
        output_type=pd.DataFrame,
    )

    return df

def get_attractions_for_city(city, limit=1000):
    with open("query_templates/attractions.rq.j2", "r") as file:
        template_str = file.read()
    template = Template(template_str)
    query = template.render(city=city, limit=limit)
    print(query)
    df = engine.select(
        query=query,
        output_type=pd.DataFrame
    )
    return df


def get_hotels() -> pd.DataFrame:
    """Get hotels from TUI."""
    query_file = "queries/tui_hotels.rq"

    df = engine.select(query=query_file, output_type=pd.DataFrame)

    return df


def get_flights_with_hotels() -> pd.DataFrame:
    """Get flights and hotels from Modlin Airport and TUI."""
    query_file = "queries/flights_hotels.rq"

    df = engine.select(
        query=query_file,
        values={"location": "https://www.modlinairport.pl/pasazer/rozklad-lotow"},
        output_type=pd.DataFrame,
    )

    return df


def get_flights_with_hotels_params(
    max_price_per_day: int, duration: int, min_standard: float
) -> pd.DataFrame:
    """Get flights and hotels from Modlin Airport and TUI.

    The output is filtered by the given parameters.

    Args:
        max_price_per_day (int): Maximum price per day for hotel.
        duration (int): Duration of the stay.
        min_standard (float): Minimum standard of the hotel."""
    today = datetime.today()
    one_month_later = today + timedelta(days=30)
    departureDateFrom = today.strftime("%Y-%m-%d")
    departureDateTo = one_month_later.strftime("%Y-%m-%d")

    payload_dict = {
        "childrenBirthdays": [],
        "departureDateFrom": departureDateFrom,
        "departureDateTo": departureDateTo,
        "departuresCodes": [],
        "destinationsCodes": [],
        "durationFrom": 6,
        "durationTo": 10,
        "filters": [
            {"filterId": "priceSelector", "selectedValues": []},
            {"filterId": "board", "selectedValues": []},
            {"filterId": "amountRange", "selectedValues": []},
            {
                "filterId": "minHotelCategory",
                "selectedValues": ["defaultHotelCategory"],
            },
            {
                "filterId": "tripAdvisorRating",
                "selectedValues": ["defaultTripAdvisorRating"],
            },
            {"filterId": "beach_distance", "selectedValues": ["defaultBeachDistance"]},
        ],
        "metaData": {"page": 1, "pageSize": 1000, "sorting": "price"},
        "numberOfAdults": 2,
        "occupancies": [],
        "offerType": "BY_CAR",
        "site": "wypoczynek/wyniki-wyszukiwania-nocleg",
    }
    payload = json.dumps(payload_dict).replace('"', '"')
    params = {
        "payload": payload,
        "max_price_per_day": max_price_per_day,
        "duration": duration,
        "min_standard": min_standard,
    }

    with open("query_templates/flights_hotels_with_filtering.rq.j2", "r") as file:
        template_content = file.read()

    template = Template(template_content)
    rendered_query = template.render(**params)

    with tempfile.TemporaryDirectory() as temp_dir:
        query_file = os.path.join(temp_dir, "flights_hotels_with_filtering.rq")

        with open(query_file, "w") as file:
            file.write(rendered_query)

        df = engine.select(
            query=query_file,
            values={"location": "https://www.modlinairport.pl/pasazer/rozklad-lotow"},
            output_type=pd.DataFrame,
        )

    return df

import i18n
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from src.data.loader import DataSchema
from src.data.manager import DataManager

from . import ids


def render(app: Dash, data_manager: DataManager) -> html.Div:
    @app.callback(
        Output(ids.CATEGORY_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks"),
        ],
    )
    def select_all_categories(
        year: list[int], month: list[int], _: list[int]
    ) -> list[str]:
        query_string = (
            f"({DataSchema.YEAR.value} == {year})"
            f" & ({DataSchema.MONTH.value} == {month})"
        )
        categories: set[str] = set(
            data_manager._data.query(query_string)[DataSchema.CATEGORY.value]
        )
        return sorted(list(categories))

    return html.Div(
        children=[
            html.H6(i18n.t("general.category")),
            dcc.Dropdown(
                id=ids.CATEGORY_DROPDOWN,
                options=data_manager.category_options,
                value=data_manager.category_values,
                multi=True,
                placeholder=i18n.t("general.select"),
            ),
            html.Button(
                className="dropdown-button",
                children=[i18n.t("general.select_all")],
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                n_clicks=0,
            ),
        ],
    )

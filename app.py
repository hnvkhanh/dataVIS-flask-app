from flask import Flask, flash, redirect, render_template, request, session
import pandas as pd
import numpy as np
from plot_life_expectancy import *

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/life_expectancy_data", methods=["GET", "POST"])
def life_expectancy_vis():
    df = pd.read_csv('datasets/Life Expectancy Data.csv')
    if request.method == "POST":
        if not request.form.get("meta"):
            meta = 'Status'
        else:
            meta = request.form.get("meta")

        if not request.form.get("year"):
            year = 2015
        else:
            year = int(request.form.get("year"))

        if not request.form.get("selected_country"):
            country = 'Spain'
        else:
            country = request.form.get("selected_country")
    else:
        country = 'Viet Nam'
        meta = 'Status'
        year = 2015

    map_fig = plot_on_map(df, meta, year)
    fig = basic_plot(df, country)
    countries = df.Country.unique()
    heatmap = plot_heatmap(df.drop(columns=['Year', 'Country', 'Status']))

    return render_template("life_expectancy_vis.html",  MAP=map_fig, METAS=df.columns[2:], YEARS=df.Year.unique(),
                           chosen_year=year, chosen_meta=meta, FIG=fig, COUNTRIES=countries, chosen_country=country,
                           HEATMAP=heatmap)


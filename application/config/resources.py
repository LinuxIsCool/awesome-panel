"""In this module we define all Resources (except apps in the gallery) and exposes
them via the RESOURCES list.
"""
from application.config import authors, tags
from application.config.settings import THUMBNAILS_ROOT

# pylint: disable=line-too-long
from awesome_panel.application.models import Resource

# panel FILE ROOTS

RESOURCES = [
    Resource(
        name="Colormap Distorsions",
        url="https://github.com/mycarta/Colormap-distorsions-Panel-app",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.CODE, tags.APP],
        author=authors.MATTEO_NICOLI,
    ),
    Resource(
        name="Elvis - Golden Layout",
        url="https://github.com/LeonvanKouwen/elvis",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.CODE],
        author=authors.LEON_VAN_KOUWEN,
    ),
    Resource(
        name="Color Dropper App",
        url="http://colordropper.herokuapp.com/colordropper",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP],
        author=authors.ANDREW_HUANG,
    ),
    Resource(
        name="A tour (of a small part) of the Python visualization landscape",
        url="https://indico.cern.ch/event/833895/contributions/3577846/attachments/1928191/3205023/PyHEP2019_slides.pdf",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ARTICLE],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Building Dashboards. Introduction to Data Analysis in Biological Sciences.",
        url="https://xavartley.github.io/#panel/vtk_examples/Gallery_VTK.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP, tags.INSPIRATION],
        author=authors.JUSTIN_BOIS,
    ),
    Resource(
        name="VTK Examples by xavArtley",
        url="http://bebi103.caltech.edu.s3-website-us-east-1.amazonaws.com/2019a/content/recitations/recitation_05/dashboards.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL, tags.INSPIRATION, tags.VTK],
        author=authors.XAVARTLEY,
    ),
    Resource(
        name="XrViz",
        url="https://github.com/intake/xrviz",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP, tags.CODE, tags.INSPIRATION,],
        author=authors.INTAKE,
    ),
    Resource(
        name="Information is Beautiful",
        url=(
            "https://towardsdatascience.com/how-to-build-a-time-series-dashboard-in-python-with-"
            "panel-altair-and-a-jupyter-notebook-c0ed40f02289"
        ),
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL, tags.ARTICLE,],
        author=authors.BENJAMIN_COOLEY,
    ),
    Resource(
        name="Information is Beautiful",
        url="https://informationisbeautiful.net/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.INSPIRATION],
        author=authors.INFORMATIONISBEUTIFULL,
    ),
    Resource(
        name="Open Source Directions ep. 29: Panel",
        url="https://www.youtube.com/watch?v=hZOsxmM_wyg",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.VIDEO],
        author=authors.QUANSIGHT,
    ),
    Resource(
        name="Our World in Data",
        url="https://ourworldindata.org/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.INSPIRATION],
        author=authors.OURWORLDINDATA,
    ),
    Resource(
        name="Panel",
        url="https://panel.pyviz.org/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Discourse",
        url="https://discourse.holoviz.org/c/panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Getting Started",
        url="https://panel.pyviz.org/getting_started/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="User Guide",
        url="https://panel.pyviz.org/user_guide/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Gallery",
        url="https://panel.pyviz.org/gallery/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Reference Gallery",
        url="https://panel.pyviz.org/reference/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="GitHub",
        url="https://github.com/holoviz/panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Announcing Article",
        url="https://medium.com/@philipp.jfr/panel-announcement-2107c2b15f52",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Awesome-panel.org",
        url="https://awesome-panel.org",
        thumbnail_png_path=THUMBNAILS_ROOT + "awesome-panel-org.png?raw=true",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Github",
        url="https://github.com/marcskovmadsen/awesome-panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docs",
        url="https://awesome-panel.readthedocs.io/en/latest/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docker",
        url="https://hub.docker.com/r/marcskovmadsen/awesome-panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="PyPi",
        url="https://pypi.org/project/awesome-panel/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Dashboards with PyViz Panel for interactive web apps",
        url="https://dmnfarrell.github.io/bioinformatics/pyviz-panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ARTICLE],
        author=authors.DAMIAN_FARRELL,
    ),
    Resource(
        name="Turn any Notebook into a Deployable Dashboard | SciPy 2019 | James Bednar",
        url="https://www.youtube.com/watch?v=L91rd1D6XTA&t=274s",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.VIDEO, tags.TUTORIAL,],
        author=authors.JAMES_BEDNAR,
    ),
    Resource(
        name="Turn any notebook into a deployable dashboard|PyData Berlin 2019",
        url="https://www.youtube.com/watch?v=Ohr29FJjBi0&list=PLGVZCDnMOq0pNHTYo3i56zYU-Tdw5Uguw",
        thumbnail_png_path=THUMBNAILS_ROOT + "pydataberlin2019.png?raw=true",
        is_awesome=True,
        tags=[tags.VIDEO, tags.TUTORIAL,],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Visualize any Data Easily, from Notebooks to Dashboards",
        url="https://www.youtube.com/watch?v=7deGS4IPAQ0&t=1326s",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.VIDEO, tags.TUTORIAL,],
        author=authors.JAMES_BEDNAR,
    ),
    Resource(
        name="HoloViz.org - Awesome Resources and Tutorials",
        url="http://holoviz.org/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL],
        author=authors.HOLOVIZ,
    ),
    Resource(
        name="awesome-streamlit.org",
        url="https://awesome-streamlit.org",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.SISTER_SITES],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Bokeh",
        url="https://bokeh.pydata.org/en/latest/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.BOKEH,
    ),
    Resource(
        name="Jupyter Voila",
        url="https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.VOILA,
    ),
    Resource(
        name="Plotly Dash",
        url="https://plot.ly/dash/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.PLOTLY,
    ),
    Resource(
        name="Streamlit",
        url="https://streamlit.io",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.STREAMLIT,
    ),
]

TAGS = sorted(list({tag for resource in RESOURCES for tag in resource.tags}))

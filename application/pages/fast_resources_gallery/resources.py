"""In this modue we define the FAST Gallery Resources"""
# pylint: disable=line-too-long
from awesome_panel_extensions.site import Resource

from application.pages.fast_resources_gallery import authors

RESOURCES = [
    Resource(
        name="PANOPTES Explorer App",
        url="https://www.panoptes-data.net/",
        description="",
        tags=["App"],
        author=authors.PANOPTES,
    ),
    Resource(
        name="PANOPTES Explorer Repo",
        url="https://github.com/panoptes/panoptes-network/blob/develop/data-explorer/README.md",
        description="",
        tags=["Code"],
        author=authors.PANOPTES,
    ),
    Resource(
        name="World Glaciers Explorer",
        url="https://edu.oggm.org/en/latest/explorer.html",
        description="",
        tags=["App", "Video"],
        author=authors.OGGM_EDU,
    ),
    Resource(
        name="Experimental Machine Learning with HoloViz and PyTorch in Jupyterlab ",
        url="https://pyvideo.org/pydata-la-2019/experimental-machine-learning-with-holoviz-and-pytorch-in-jupyterlab.html",
        description="",
        tags=["Tutorial", "Video"],
        author=authors.HAYLEY_SONG,
    ),
    Resource(
        name="Panel Tutorial by vda-lab",
        url="https://vda-lab.github.io/visualisation-tutorial/holoviz-what-is-panel.html#",
        description="",
        tags=["Tutorial", "Code", "App"],
        author=authors.VDA_LAB,
    ),
    Resource(
        name="Panel Dashboards by Nic Fox",
        url="https://foxnic.github.io/projects.html",
        description="",
        tags=["App", "Code"],
        author=authors.NIC_FOX,
    ),
    Resource(
        name="How to Create an Interactive Dashboard in Python Using HoloViz Panel",
        url="https://dev.to/nicfoxds/how-to-create-an-interactive-dashboard-in-python-using-holoviz-panel-5bhp",
        description="",
        tags=["Tutorial", "Code"],
        author=authors.NIC_FOX,
    ),
    Resource(
        name="Colormap Distorsions",
        url="https://github.com/mycarta/Colormap-distorsions-Panel-app",
        description="",
        tags=["Code", "App"],
        author=authors.MATTEO_NICCOLI,
    ),
    Resource(
        name="Elvis - Golden Layout",
        url="https://github.com/LeonvanKouwen/elvis",
        description="",
        tags=["Code"],
        author=authors.LEON_VAN_KOUWEN,
    ),
    Resource(
        name="Color Dropper App",
        url="http://colordropper.herokuapp.com/colordropper",
        description="",
        tags=["App"],
        author=authors.ANDREW_HUANG,
    ),
    Resource(
        name="A tour (of a small part) of the Python visualization landscape",
        url="https://indico.cern.ch/event/833895/contributions/3577846/attachments/1928191/3205023/PyHEP2019_slides.pdf",
        description="",
        tags=["Article"],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Building Dashboards. Introduction to Data Analysis in Biological Sciences.",
        url="https://xavartley.github.io/#panel/vtk_examples/Gallery_VTK.html",
        description="",
        tags=["App", "Inspiration"],
        author=authors.JUSTIN_BOIS,
    ),
    Resource(
        name="VTK Examples by xavArtley",
        url="http://bebi103.caltech.edu.s3-website-us-east-1.amazonaws.com/2019a/content/recitations/recitation_05/dashboards.html",
        description="",
        tags=["Tutorial", "Inspiration", "VTK"],
        author=authors.XAVARTELY,
    ),
    Resource(
        name="XrViz",
        url="https://github.com/intake/xrviz",
        description="",
        tags=["App", "Code", "Inspiration"],
        author=authors.INTAKE,
    ),
    Resource(
        name="Information is Beautiful",
        url="https://towardsdatascience.com/how-to-build-a-time-series-dashboard-in-python-with-panel-altair-and-a-jupyter-notebook-c0ed40f02289",
        description="",
        tags=["Tutorial", "Article"],
        author=authors.BOKEH,
    ),
    Resource(
        name="Information is Beautiful",
        url="https://informationisbeautiful.net/",
        description="",
        tags=["Inspiration"],
        author=authors.INFORMATION_IS_BEAUTIFUL,
    ),
    Resource(
        name="Open Source Directions ep. 29: Panel",
        url="https://www.youtube.com/watch?v=hZOsxmM_wyg",
        description="",
        tags=["Video"],
        author=authors.QUANSIGHT,
    ),
    Resource(
        name="Our World in Data",
        url="https://ourworldindata.org/",
        description="",
        tags=["Inspiration"],
        author=authors.OUR_WORLD_IN_DATA,
    ),
    Resource(
        name="Panel",
        url="https://panel.pyviz.org/",
        description="",
        tags=["Panel"],
        author=authors.PANEL,
    ),
    Resource(
        name="Discourse",
        url="https://discourse.holoviz.org/c/panel",
        description="",
        tags=["Panel"],
        author=authors.PANEL,
    ),
    Resource(
        name="Getting Started",
        url="https://panel.pyviz.org/getting_started/index.html",
        description="",
        tags=["Panel"],
        author=authors.PANEL,
    ),
    Resource(
        name="User Guide",
        url="https://panel.pyviz.org/user_guide/index.html",
        description="",
        tags=["Panel"],
        author=authors.PANEL,
    ),
    Resource(
        name="Gallery",
        url="https://panel.pyviz.org/gallery/index.html",
        description="",
        tags=["Panel"],
        author=authors.PANEL,
    ),
    Resource(
        name="Reference Gallery",
        url="https://panel.pyviz.org/reference/index.html",
        description="",
        tags=["Panel"],
        author=authors.PANEL,
    ),
    Resource(
        name="GitHub",
        url="https://github.com/holoviz/panel",
        description="",
        tags=["Panel"],
        author=authors.PANEL,
    ),
    Resource(
        name="Announcing Article",
        url="https://medium.com/@philipp.jfr/panel-announcement-2107c2b15f52",
        description="",
        tags=["Panel"],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Awesome-panel.org",
        url="https://awesome-panel.org",
        description="",
        tags=["Awesome-panel.org"],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Github",
        url="https://github.com/marcskovmadsen/awesome-panel",
        description="",
        tags=["Awesome-panel.org"],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docs",
        url="https://awesome-panel.readthedocs.io/en/latest/",
        description="",
        tags=["Awesome-panel.org"],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docker",
        url="https://hub.docker.com/r/marcskovmadsen/awesome-panel",
        description="",
        tags=["Awesome-panel.org"],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="PyPi",
        url="https://pypi.org/project/awesome-panel/",
        description="",
        tags=["Awesome-panel.org"],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Dashboards with PyViz Panel for interactive web apps",
        url="https://dmnfarrell.github.io/bioinformatics/pyviz-panel",
        description="",
        tags=["Article"],
        author=authors.DAMIEN_FARRELL,
    ),
    Resource(
        name="Turn any Notebook into a Deployable Dashboard | SciPy 2019 | James Bednar",
        url="https://www.youtube.com/watch?v=L91rd1D6XTA&t=274s",
        description="",
        tags=["Video", "Tutorial"],
        author=authors.JAMES_A_BEDNAR,
    ),
    Resource(
        name="Turn any notebook into a deployable dashboard|PyData Berlin 2019",
        url="https://www.youtube.com/watch?v=Ohr29FJjBi0&list=PLGVZCDnMOq0pNHTYo3i56zYU-Tdw5Uguw",
        description="",
        tags=["Video", "Tutorial"],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Visualize any Data Easily, from Notebooks to Dashboards",
        url="https://www.youtube.com/watch?v=7deGS4IPAQ0&t=1326s",
        description="",
        tags=["Video", "Tutorial"],
        author=authors.JAMES_A_BEDNAR,
    ),
    Resource(
        name="HoloViz.org - Awesome Resources and Tutorials",
        url="http://holoviz.org/index.html",
        description="",
        tags=["Tutorial"],
        author=authors.HOLOVIZ,
    ),
    Resource(
        name="awesome-streamlit.org",
        url="https://awesome-streamlit.org",
        description="",
        tags=["Sister Sites"],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Bokeh",
        url="https://bokeh.pydata.org/en/latest/index.html",
        description="",
        tags=["Alternatives"],
        author=authors.BOKEH,
    ),
    Resource(
        name="Jupyter Voila",
        url="https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93",
        description="",
        tags=["Alternatives"],
        author=authors.VOILA,
    ),
    Resource(
        name="Plotly Dash",
        url="https://plot.ly/dash/",
        description="",
        tags=["Alternatives"],
        author=authors.PLOTLY,
    ),
    Resource(
        name="Streamlit",
        url="https://streamlit.io",
        description="",
        tags=["Alternatives"],
        author=authors.STREAMLIT,
    ),
]

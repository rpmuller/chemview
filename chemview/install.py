import os
import warnings
from IPython.display import display, Javascript
from IPython.html.nbextensions import install_nbextension
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from pkg_resources import resource_filename

__all__ = ['enable_notebook']

_REQUIRE_CONFIG = Javascript('''
require.config({
    paths: {
        'three': '/nbextensions/three.min',
        'exporter' : '/nbextensions/objexporter',
        'filesaver' : '/nbextensions/filesaver',
        'base64-arraybuffer': '/nbextensions/base64-arraybuffer',
        'jqueryui': '/nbextensions/jquery-ui.min',
        'contextmenu': '/nbextensions/context',
        'TrackballControls' : '/nbextensions/TrackballControls',
        'chemview': '/nbextensions/chemview',
        'marchingcubes': '/nbextensions/MarchingCubes',
    },
    shim: {
        three: {
            exports: 'THREE'
        },

        chemview: {
            deps: ['three', 'TrackballControls', 'marchingcubes'],
            exports: 'MolecularViewer'
        },

        exporter: {
            deps: ['three'],
            exports: 'THREE.OBJExporter'
        },

        TrackballControls: {
            deps: ['three'],
            exports: 'THREE.TrackballControls',
        },

        jqueryui: {
            exports: "$"
        },

        marchingcubes: {
            deps: ['three'],
            exports: "THREE.MarchingCubes",
        },
    },
});
''',
css  = ['/nbextensions/context.standalone.css']
)

def enable_notebook():
    """Enable IPython notebook widgets to be displayed.

    This function should be called before using TrajectoryWidget.
    """
    libs = ['objexporter.js', 'MarchingCubes.js',
            'TrackballControls.js', 'filesaver.js',
            'base64-arraybuffer.js', 'context.js', 
            'chemview.js', 'three.min.js', 'jquery-ui.min.js',
            'context.standalone.css']
    fns = [resource_filename('chemview', os.path.join('static', f)) for f in libs]
    install_nbextension(fns, verbose=0, overwrite=True)
    display(_REQUIRE_CONFIG)

    widgets = ['chemview_widget.js']
    for fn in widgets:
        fn = resource_filename('chemview', os.path.join('static', fn))
        display(Javascript(filename=fn))

from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1}},
    windows = [{'script': "eyes.py"}],
    zipfile = None,
    data_files = [('', ['centerball.png', 'clock.png', 'cover.png', 'end1.png', 'end2.png', 'eyeclosed.png', 'eyedroopy.png', 'eyeopen.png', 'eyetired.png', 'floor0.png', 'floor1.png', 'floor2.png', 'floor3.png', 'floor4.png', 'floor5.png', 'floor6.png', 'floor7.png', 'floor8.png', 'floor9.png', 'floor10.png', 'floor11.png', 'floor12.png', 'floor13.png', 'floor14.png', 'legball.png', 'life.png', 'rules.png', 'rulestext.png', 'spikeball.png', 'titletext.png', 'title0.png', 'title1.png', 'title2.png', 'title3.png'])],
)

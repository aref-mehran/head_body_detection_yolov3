import pip


def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])
        import FastAPI


import_or_install('FastAPI')

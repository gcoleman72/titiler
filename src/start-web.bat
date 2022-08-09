pip uninstall titiler-core
pip install -e titiler/core
pip install -e titiler/mosaic
pip install -e titiler/application
uvicorn titiler.application.main:app

import os
import tempfile
import adsk.core  # type: ignore
from ... import dxf


def execute(output_dxf_path):
    app = adsk.core.Application.get()
    design = app.activeProduct
    rootComp = design.rootComponent
    sketches = rootComp.sketches

    with tempfile.TemporaryDirectory() as tmp_dir:
        dxf_paths = []

        for i in range(sketches.count):
            dxf_path = os.path.join(tmp_dir, f"{i}.dxf")
            sketches.item(i).saveAsDXF(dxf_path)
            dxf_paths.append(dxf_path)

        dxf.merge(dxf_paths, output_dxf_path)

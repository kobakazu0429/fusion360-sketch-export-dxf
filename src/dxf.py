import sys
from .lib import fusion360utils as futil


try:
    import ezdxf
    from ezdxf.addons import Importer
except ImportError:
    try:
        import pathlib

        site_packages_path = str(
            pathlib.Path(__file__).parent.parent.joinpath("site-packages")
        )
        futil.log(site_packages_path)

        if not site_packages_path in sys.path:
            sys.path.append(site_packages_path)
            import ezdxf
            from ezdxf.addons import Importer
    except:
        futil.handle_error("install ezdxf !")


def merge(dxf_files, output_dxf_path):
    merged_doc = ezdxf.new("R2018")

    for i, file in enumerate(dxf_files):
        source_doc = ezdxf.readfile(file)

        importer = Importer(source_doc, merged_doc)

        layer_name = f"layer_{i}"
        layer = merged_doc.layers.add(layer_name)
        layer.color = i

        source_doc.layers.add(layer_name)

        # TODO: consider the use of query('*[layer=="0"]'):
        for e in source_doc.modelspace():
            if e.get_dxf_attrib("layer") == "0":
                e.dxf.layer = layer_name

        importer.import_modelspace()

        importer.finalize()

    merged_doc.saveas(output_dxf_path)

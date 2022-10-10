import ezdxf
from ezdxf.addons import Importer


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

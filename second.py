import yaml
from pprint import pprint

from dicttoxml import dicttoxml


def with_libs(n):
    yaml_f = "data/tt.yaml"
    xml_f = f"out/2{n}.xml"

    with open(yaml_f) as f:
        d1ct = yaml.load(f, Loader=yaml.FullLoader)

    xml = dicttoxml(d1ct, root=None, attr_type=False)
    xml = str(xml).replace('</item>', '').replace('<item>', '')
    with open(xml_f, 'w') as f:
        f.write(str(xml)[2:-1])

with_libs('')
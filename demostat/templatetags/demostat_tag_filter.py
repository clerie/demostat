from django import template
from ..utils import Querystring

register = template.Library()

def tag_dict_to_array(dict):
    if "org" in dict:
        if dict["org"] == {}:
            dict.pop("org")
        else:
            dict["org"] = [dict["org"]]
    out = {}
    for tag, values in dict.items():
        out[tag] = []
        for v in values:
            out[tag].append(v.slug)

    print(out)

    return out

@register.simple_tag
def tf_generate_qs(**dict):
    qs = Querystring(tag_dict_to_array(dict))
    return qs.get()

@register.simple_tag
def tf_generate_qs_without_tag(value, **dict):
    qs = Querystring(tag_dict_to_array(dict))
    return qs.get_without("tag", value)

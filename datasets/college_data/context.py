from typing import Dict, Any
import squirrels as sq


def main(prms: sq.ParameterSet, proj: Dict[str, str], *args, **kwargs) -> Dict[str, Any]:
    region_param: sq.MultiSelectParameter = prms['region']
    view_param: sq.MultiSelectParameter = prms['select']
    selected_region = region_param.get_selected_labels_quoted_joined()
    selected_selects = ",".join(view_param.get_selected_labels_as_list())
    #limit: str = limit_parameter.get_selected_value()
    sq.Parameter
    return {'regions': selected_region, 'selections': selected_selects}
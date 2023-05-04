from typing import Dict, Any
import squirrels as sq


def main(prms: sq.ParameterSet, proj: Dict[str, str], *args, **kwargs) -> Dict[str, Any]:
    region_param: sq.MultiSelectParameter = prms['region']
    selected_region = region_param.get_selected_labels_quoted_joined()
    #limit: str = limit_parameter.get_selected_value()
    return {'regions': selected_region}

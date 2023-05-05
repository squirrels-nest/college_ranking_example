import squirrels as sq


def main(*args, **kwargs) -> sq.ParameterSet:
    region_ds = sq.SelectionDataSource("my_db","select distinct region, region as reg_id from colleges", "reg_id", "Region")
    region_param = sq.DataSourceParameter(sq.WidgetType.MultiSelect, "region", "Region(s)", region_ds)
    view_param = sq.MultiSelectParameter("select", "Selection(s)", [sq.SelectParameterOption("1","region"), sq.SelectParameterOption("2","name"), 
                                                                    sq.SelectParameterOption("3", "category"),sq.SelectParameterOption("4", "url")])

    return sq.ParameterSet([
        region_param,
        view_param
    ])

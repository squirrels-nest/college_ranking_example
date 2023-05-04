import squirrels as sq


def main(*args, **kwargs) -> sq.ParameterSet:
    # select_options = (
    #     sq.SelectParameterOption('x0', 'Red'),
    #     sq.SelectParameterOption('x1', 'Green'),
    #     sq.SelectParameterOption('x2', 'Blue')
    # )
    region_ds = sq.SelectionDataSource("my_db","select distinct region, region as reg_id from colleges", "reg_id", "Region")
    region_param = sq.DataSourceParameter(sq.WidgetType.MultiSelect, "region", "Region(s)", region_ds)
    #sq.MultiSelectParameter()
    return sq.ParameterSet([
        region_param
    ])

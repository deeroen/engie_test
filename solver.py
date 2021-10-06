

def solver(input_info):
    def price(dct, fuel, input_info):
        if "wind(%)" == fuel:
            dct['cost_min'] = 0
            dct['cost_max'] = 0
            dct['prod_min'] = dct['pmin'] * dct['efficiency'] * input_info["fuels"][fuel] / 100
            dct['prod_max'] = dct['pmax'] * dct['efficiency'] * input_info["fuels"][fuel] / 100
            dct['eff_cost'] = 100000
        else:
            dct['cost_min'] = dct['pmin'] * input_info["fuels"][fuel]
            dct['cost_max'] = dct['pmax'] * input_info["fuels"][fuel]
            dct['prod_min'] = dct['pmin'] * dct['efficiency']
            dct['prod_max'] = dct['pmax'] * dct['efficiency']
            dct['eff_cost'] = input_info["fuels"][fuel] * dct['efficiency']
        return 1

    process = {}
    for keys, values in input_info.items():
        if keys == 'powerplants':
            # Create the out file

            for dict in values:
                # Fill the out file

                if dict['type'] == 'gasfired':
                    price(dict, "gas(euro/MWh)", input_info)
                elif dict['type'] == 'turbojet':
                    price(dict, "kerosine(euro/MWh)", input_info)
                else:
                    price(dict, "wind(%)", input_info)
                dict["p"] = 0
                process[dict['name']] = dict

    load = input_info['load']

    item_cost = {keys: [values['eff_cost'], values["pmin"]] for keys, values in process.items()}
    best_items = sorted(item_cost.items(), key=lambda item: (-item[1][0], -item[1][1]))

    while load > 0:
        name = best_items[0][0]
        data = process[name]

        if data["prod_min"] > load:
            pass
        elif data["prod_max"] <= load:
            load = load - data["prod_max"]
            process[name]['p'] = data["pmax"]
        else:
            process[name]['p'] = round(load / data['efficiency'],1)
            load = 0

        del best_items[0]

    out = []

    for i, j in process.items():
        out.append({"name": j["name"], "p": j["p"]})
    return out

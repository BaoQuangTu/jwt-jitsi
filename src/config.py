from jproperties import Properties

def get(key):
    configs = Properties()
    value = None

    with open('./app-config.properties', 'rb') as config_file:
        configs.load(config_file)
        try:
            value = configs[key]
            print(value)
        except KeyError as ke:
            print(f'{ke}, lookup key was ', key)

    return value.data
def calc_cost(area):
    y = process(area, "")
    return y


# TODO: Переписать предобработку под свою задачу
def preprocess(param):
    try:
        param = float(param)
    except Exception as e:
        param = 0
    return param


def process(x, path):
    # TODO: загрузить модель по пути path
    model = load_model(path)

    # TODO: добавить предобработку x перед использованием
    x = preprocess(x)
    y = model.predict(x)
    return y


# TODO: написать код загрузки модели 
# Это может быть модель sklearn, tf и т.д.
def load_model(path):
    pass
class State:

    country = 'Us State'

    def __init__(self, name, abv):
        self.name = name
        self.abv = abv


class StateCapital(State):
    def __init__(self, name, abv, capital):
        super().__init__(name, abv)
        self.capital = capital


if __name__ == '__main__':

    states = [
        {'name': 'Alabama', 'abv': 'AL', 'capital': 'Montgomery'},
        {'name': 'Alaska', 'abv': 'AK', 'capital': 'Juneau'}
    ]

    for d in states:
        state = StateCapital(
            name=d['name'], abv=d['abv'], capital=d['capital'])
        print(state.name + ',', state.capital + ',', state.abv)

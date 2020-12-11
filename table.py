from tabulate import tabulate

class Table():
    def __init__(self):
        pass

    def render_table(self, data, headers):
        return tabulate(data, headers=headers, tablefmt="psql")

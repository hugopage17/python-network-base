import click
from scanner import Scanner
from table import Table
import os
import time
from progress.bar import ChargingBar
table = Table()
scan = Scanner()

class Functions():
    def __init__(self):
        pass

    @click.command()
    @click.option('--nodes')
    def view_status(nodes):
        while True:
            data = scan.run_scan(nodes)
            os.system('cls')
            tbl = table.render_table(data, headers=["Address","Status", "Time (ms)"])
            print(tbl)

    @click.command()
    @click.option('--nodes')
    def ip_scan(nodes):
        data = scan.get_range(nodes)
        bar = ChargingBar('Scanning', max=len(data))
        discovered = []
        for ip in data:
            s = scan.poll(ip)
            if s[1] == 'online':
                mac = scan.mac_scan(ip)
                s.append(mac['mac'])
                s.append(mac['vendor'])
                arr = [s[0],s[3],s[4]]
                discovered.append(arr)
            bar.next()
        print('\n')
        tbl = table.render_table(discovered, headers=["Address","Status", "Time (ms)"])
        print(tbl)

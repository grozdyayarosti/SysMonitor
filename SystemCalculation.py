import psutil

class SystemCalculation:

    def __init__(self):
        pass

    def get_cpu(self):
        info = psutil.cpu_percent(interval=1, percpu=False)
        # text = '\n'.join([(f'ЦП{i+1}: {v}%') for i, v in enumerate(info)])
        res = f'{info}%'
        return res

    def get_ram(self):
        info = psutil.virtual_memory()
        calc = round(100 * info.used / info.total, 2)
        res = f'{calc}%'
        return res
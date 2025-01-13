import shutil

import psutil


class SystemCalculation:

    def __init__(self):
        pass

    def get_cpu(self):
        info = psutil.cpu_percent(interval=1, percpu=False)
        # text = '\n'.join([(f'ЦП{i+1}: {v}%') for i, v in enumerate(psutil.cpu_percent(interval=1, percpu=True))])
        res = f'{info}%'
        return res

    def get_ram(self):
        info = psutil.virtual_memory()
        # calc = round(100 * info.used / info.total, 2)
        res = f'{(info.used // (2**30))}/{(info.total // (2**30))} GiB({info.percent}%)'
        return res

    def get_rom(self):
        total, used, free = shutil.disk_usage('/')
        res = f'{(used // (2**30))}/{(total // (2**30))} GiB'
        # disks = dict()
        # if partitions := psutil.disk_partitions():
        #     for partition in partitions:
        #         device = partition.device
        #         mountpoint = partition.mountpoint
        #         disk_us = psutil.disk_usage(mountpoint)
        #         disk = {'Drive': device,
        #                 'Mountpoint': mountpoint,
        #                 'TotalSpace': disk_us.total,
        #                 'UsedSpace': disk_us.used,
        #                 'FreeSpace': disk_us.free,
        #                 'PercentUsed': disk_us.percent
        #         }
        #         disks[device] = disk
        #     return disks if disks else False
        # return False
        return res

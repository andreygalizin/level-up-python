from pathlib import Path
import platform

print('OS:',*platform.version())
q=Path('/proc/cpuinfo').read_text().splitlines()
cpu=[j for j in q if j.startswith('model name')]
print('CPU',cpu[0].replace('model name',''))
r = Path('/proc/meminfo').read_text().splitlines()
mem = [k for k in r if k.startswith('MemTotal')]
print('Memory Size:',round(int(mem[0].split()[1])/1024/1024), 'GB')
s = Path('/sys/block/sda/size').read_text().splitlines()
print('Hard Disk:',round(int(s[0])*512/1000/1000/1000), 'GB')
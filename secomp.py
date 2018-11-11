from typing import List
import json

src_data = open('host1.json').read()

data = json.loads(src_data)
print("begin")
print(data['whoami'])
print("end")
src1: str = "hostnew1.oc.prod.au.in.cba"
dst1: str = "hostold2.oc.prod.au.in.cba"
src_part1: List[str] = src1.split(".")
dst_part1: List[str] = dst1.split(".")

# source host file
src_json = '{"segment":"internal", "geo":"au", "env":"prod", "zone":"azure", "application":"payments" }'
src_attr = json.loads(src_json)
print(src_attr)

# destination host file
dst_json = '{"segment":"internal", "geo":"au", "env":"prod", "zone":"azure", "application":"hr" }'
dst_attr = json.loads(dst_json)
print(dst_attr)

# { I allow geo:[au, nz], env:prod, zone:oc, application: web, port [345,567] ]
# { I access segment:internal, geo:au, env:prod, zone:oc, application: hr_db, ports [345,456] }

for s in src_attr:
    for d in dst_attr:
        if s == d:
            if src_attr[s] == dst_attr[d]:
                print("source-" + s + ":" + src_attr[s] + " = " + "dest-" + d + ":" + dst_attr[d] + " ->allow")
            elif src_attr[s] != dst_attr[d]:
                print("source-" + s + ":" + src_attr[s] + " != " + "dest-" + d + ":" + dst_attr[d] + " ->deny")

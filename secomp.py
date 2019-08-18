from typing import List
import json

src_data = open('host1.json').read()

data = json.loads(src_data)
print("whoami")
print(data['whoami'])
print("allow")
print(data['allow'])
print("access")
print(data['access'])

# source host file
src_json = json.dumps(data['whoami'])
src_attr = json.loads(src_json)

# destination host file
dst_json = '{"segment":"internal", "geo":"au", "env":"prod", "zone":"azure", "application":"hr" }'
dst_attr = json.loads(dst_json)
print("dest attribs: ")
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

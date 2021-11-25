#!/usr/bin/env python
# coding: utf-8

# In[14]:


rack_struc = {
 "rack": [
      { "device": { "dev_id": "D1" , 
                    "dev_name": "R1" , 
                    "role": "router"  ,      
                    "interfaces": [   
                      {"interface": "GigabitEhternet1" , "ipaddress": "172.18.1.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEhternet2" , "ipaddress": "172.18.3.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEhternet3" , "ipaddress": "172.18.4.1", "subnet_mask": "255.255.255.0"} 
                     ]
                 }
      },
      { "device": { "dev_id": "D2" , "dev_name": "C1" , "role": "core"  ,   
                   "interfaces": [   
                     {"interface": "VLAN1"  ,"ipaddress": "172.18.1.2" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN2"  ,"ipaddress": "172.18.2.1" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN20" ,"ipaddress": "172.18.1", "subnet_mask": "255.255.255.0"} 
                   ]     
                 }
      },
      { "device": { "dev_id": "D3" , "dev_name": "AC" ,  "role": "access"  ,
                   "interfaces": [   
                     {"interface": "VLAN2" ,"ipaddress": "172.18.2.2", "subnet_mask": "255.255.255.0"}
                   ] 
                 }
      }
   ]
}


# In[ ]:


rack_struc = {
 "rack": [
      { "server": { "dev_id": "D1" , 
                    "dev_name": "R1" , 
                    "role": "router"  ,      
                    "services": [   
                      {"interface": "GigabitEhternet1" , "ipaddress": "172.18.1.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEhternet2" , "ipaddress": "172.18.3.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEhternet3" , "ipaddress": "172.18.4.1", "subnet_mask": "255.255.255.0"} 
                     ]
                 }
      },
      { "device": { "dev_id": "D2" , "dev_name": "C1" , "role": "core"  ,   
                   "interfaces": [   
                     {"interface": "VLAN1"  ,"ipaddress": "172.18.1.2" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN2"  ,"ipaddress": "172.18.2.1" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN20" ,"ipaddress": "172.18.1", "subnet_mask": "255.255.255.0"} 
                   ]     
                 }
      },
      { "device": { "dev_id": "D3" , "dev_name": "AC" ,  "role": "access"  ,
                   "interfaces": [   
                     {"interface": "VLAN2" ,"ipaddress": "172.18.2.2", "subnet_mask": "255.255.255.0"}
                   ] 
                 }
      }
   ]
}


# In[3]:


import yaml
yaml_data = yaml.dump(rack_struc)
print(yaml_data)


# In[4]:


#!pip install dicttoxml


# In[15]:


#import json
print('-----1-----')
print(type(rack_struc))
print(rack_struc)
#print('-----1A-----')
js_struc = json.dumps(rack_struc)
#print(type(js_struc))
#print(js_struc)
#print(json.dumps(rack_struc,indent=8))

print('-----1B-----')
g = rack_struc["rack"][0]
print(type(g))
print(g["device"].keys())

print('-----2-----')
for g in rack_struc["rack"]:
    print('----2A----')
    print(type(g))
    print(g)
    print(g["device"]["dev_name"])
    for p in g["device"]["interfaces"]:
        print(p["ipaddress"])
        
print('----3----')
print("Keys device")
print(g["device"].keys())
print('----3A----')
print("Keys interfaces")
print(g["device"]["interfaces"][0].keys())


# In[17]:


###All devices + interfaces + IP address
print('--ALL-DEVICES-INTERFACES-IP-ADDRESSES--')
for gig in rack_struc["rack"]:
    print(gig["device"]["dev_name"])
    for vlan in gig["device"]["interfaces"]:
        print(vlan["interface"]+" => "+p["ipaddress"])


# In[37]:


rack_struc = {
 "rack": [
      { "server": { "dev_id": "S1" , 
                    "dev_name": "Nmap" , 
                    "role": "server"  ,
                    "ip address" : "127.0.0.1",
                    "services": [   
                      {"port": "22/tcp" , "version": "6.40", "service": "ssh"},
                      {"port": "25/tcp" , "version": "6.40", "service": "smtp"},
                      {"port": "80/tcp" , "version": "6.40", "service": "http"},
                      {"port": "111/tcp" , "version": "6.40", "service": "rpcbind"},
                      {"port": "631/tcp" , "version": "6.40", "service": "ipp"},
                      {"port": "3000/tcp" , "version": "6.40", "service": "ppp"},
                      {"port": "4000/tcp" , "version": "6.40", "service": "remoteanything"},
                      {"port": "8080/tcp" , "version": "6.40", "service": "http-proxy"},
                      {"port": "8090/tcp" , "version": "6.40", "service": "zeus-admin"}
                     ]
                 }
      }
 ]
}
 


# In[ ]:





# In[38]:


import yaml
yaml_data = yaml.dump(rack_struc)
print(yaml_data)


# In[40]:


#import json
print('-----1-----')
print(type(rack_struc))
print(rack_struc)
#print('-----1A-----')
js_struc = json.dumps(rack_struc)
#print(type(js_struc))
#print(js_struc)
#print(json.dumps(rack_struc,indent=8))

print('-----1B-----')
g = rack_struc["rack"][0]
print(type(g))
print(g["server"].keys())

print('-----2-----')
for g in rack_struc["rack"]:
    print('----2A----')
    print(type(g))
    print(g)
    print(g["server"]["dev_name"])
    for p in g["server"]["port"]:
        print(p["version"])
        
print('----3----')
print("Keys server")
print(g["server"].keys())
print('----3A----')
print("Keys services")
print(g["server"]["services"][0].keys())


from ciscoconfparse import CiscoConfParse

config_file = CiscoConfParse("cisco_config.txt")

crypto_map = config_file.find_objects(r"^crypto map CRYPTO")

pfs_group2 = config_file.find_objects_w_child(parentspec = r"^crypto map CRYPTO", childspec = "set pfs group2")

for i in pfs_group2:
    print i.text
    print i.children[2].text

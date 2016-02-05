from snmp_helper import snmp_get_oid,snmp_extract


snmp_device = ('50.76.53.27', 'galileo', 7961)
sys_descr = '.1.3.6.1.2.1.1.1.0'
sys_name = '.1.3.6.1.2.1.1.5.0'

snmp_data = snmp_get_oid(snmp_device, oid=sys_descr , display_errors=True)
output = snmp_extract(snmp_data)
print('the system des is %s' % output)

snmp_data = snmp_get_oid(snmp_device, oid=sys_name, display_errors=True)
output = snmp_extract(snmp_data)
print("the system name is {0}".format(output))


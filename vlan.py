# vlan.py
def determinar_rango_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN del rango normal"
    elif 1006 <= vlan_id <= 4094:
        return "VLAN del rango extendido"
    else:
        return "VLAN fuera de rango"

if __name__ == "__main__":
    vlan_id = int(input("Ingrese el número de VLAN: "))
    rango = determinar_rango_vlan(vlan_id)
    print(rango)

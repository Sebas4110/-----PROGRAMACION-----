"""
Diagnóstico de WiFi para Windows (pensado para portátiles viejos que
de repente dejaron de ver redes).

Cómo usarlo:
    1. Abre cmd o PowerShell COMO ADMINISTRADOR
       (clic derecho -> "Ejecutar como administrador")
    2. python diagnostico_wifi.py

Sin permisos de administrador el script igual diagnostica, pero no
podrá reiniciar servicios ni habilitar el adaptador.
"""

import subprocess


def run(cmd):
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, shell=True, timeout=15
        )
        salida = (result.stdout or "").strip()
        error = (result.stderr or "").strip()
        return salida if salida else error
    except Exception as e:
        return f"[Error ejecutando '{cmd}': {e}]"


def check_wlan_service():
    print("=== 1) Servicio WLAN AutoConfig ===")
    out = run("sc query WlanSvc")
    print(out)
    if "RUNNING" not in out.upper():
        print("\n⚠️  El servicio WLAN no está corriendo. Intentando iniciarlo...")
        print(run("net start WlanSvc"))
    print()


def check_wlan_interfaces():
    print("=== 2) ¿Windows ve alguna tarjeta WiFi? ===")
    out = run("netsh wlan show interfaces")
    print(out)
    bajo = out.lower()
    if "no wireless interface" in bajo or "no hay ninguna interfaz" in bajo:
        print("\n⚠️  Windows NO detecta ninguna tarjeta WiFi. Las causas más")
        print("   comunes en portátiles viejos, de más a menos probable:")
        print("   1) Adaptador deshabilitado en Windows (revisa el paso 4)")
        print("   2) Driver no cargado / corrupto (revisa el paso 3)")
        print("   3) Interruptor físico o Fn+tecla de WiFi apagado")
        print("   4) Falla de hardware de la tarjeta WiFi (la menos común)")
    print()


def check_wlan_driver():
    print("=== 3) Info del driver WiFi ===")
    print(run("netsh wlan show drivers"))
    print()


def check_adapter_status():
    print("=== 4) Estado de adaptadores de red ===")
    out = run(
        'wmic path win32_networkadapter where "NetConnectionID is not null" '
        "get Name,NetEnabled,NetConnectionStatus"
    )
    print(out)
    print("(NetEnabled=FALSE significa que está deshabilitado)")
    print()


def try_enable_adapter():
    print("=== Intentando habilitar el/los adaptador(es) WiFi ===")
    cmd = (
        'powershell -Command "Get-NetAdapter | '
        "Where-Object {$_.InterfaceDescription -like '*Wireless*' -or "
        "$_.InterfaceDescription -like '*Wi-Fi*' -or "
        "$_.InterfaceDescription -like '*WLAN*'} | "
        'Enable-NetAdapter -Confirm:$false"'
    )
    out = run(cmd)
    print(out if out else "(sin salida — revisa el paso 4 de nuevo para confirmar)")
    print()


if __name__ == "__main__":
    print("Diagnóstico de WiFi — ejecútalo como Administrador para mejores resultados\n")
    check_wlan_service()
    check_wlan_interfaces()
    check_wlan_driver()
    check_adapter_status()

    respuesta = input(
        "¿Intento habilitar el adaptador WiFi si aparece deshabilitado? (s/n): "
    )
    if respuesta.strip().lower() == "s":
        try_enable_adapter()
        check_adapter_status()

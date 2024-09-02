import segno

ssid = "ssid"  # Replace with your actual Wi-Fi SSID
password = "password"  # Replace with your Wi-Fi password
security_type = "WPA"  # Use "WEP" for WEP encryption or "" for no password


wifi_config = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
qr = segno.make(wifi_config)

qr.save("wifi_qr_code.png")

qr.show()

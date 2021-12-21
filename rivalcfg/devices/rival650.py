from .. import usbhid


profile = {
    "name": "SteelSeries Rival 650 Wireless",
    "models": [
        {
            "name": "SteelSeries Rival 650 Wireless (wired mode)",
            "vendor_id": 0x1038,
            "product_id": 0x172B,
            "endpoint": 0,
        },
        {
            "name": "SteelSeries Rival 650 Wireless (2.4 GHz wireless mode)",
            "vendor_id": 0x1038,
            "product_id": 0x1726,
            "endpoint": 0,
        },
    ],
    "settings": {
        "sensitivity1": {
            "label": "Sensitivity preset 1",
            "description": "Set sensitivity preset 1 (DPI)",
            "cli": ["-s", "--sensitivity1"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x15, 0x01],
            "value_type": "range",
            "input_range": [100, 12000, 100],
            "output_range": [0x00, 0x77, 1],
            "default": 800,
        },
        "sensitivity2": {
            "label": "Sensitivity preset 2",
            "description": "Set sensitivity preset 2 (DPI)",
            "cli": ["-S", "--sensitivity2"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x15, 0x02],
            "value_type": "range",
            "input_range": [100, 12000, 100],
            "output_range": [0x00, 0x77, 1],
            "default": 1600,
        },
        "polling_rate": {
            "label": "Polling rate",
            "description": "Set the polling rate (Hz)",
            "cli": ["-p", "--polling-rate"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x17],
            "value_type": "choice",
            "choices": {
                125: 0x04,
                250: 0x03,
                500: 0x02,
                1000: 0x01,
            },
            "default": 1000,
        },
    },
    "battery_level": {
        "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
        "command": [0xAA, 0x01],
        "response_length": 3,
        "is_charging": lambda data: bool(data[2]),
        "level": lambda data: int(data[0]),
    },
    "save_command": {
        "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
        "command": [0x09],
    },
}

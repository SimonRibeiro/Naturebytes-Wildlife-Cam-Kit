# Naturebytes Wildlife Cam Kit - Powered by Raspberry Pi and Python
![Cover image]()

[Naturebytes](https://naturebytes.org/about/) define themselves as a “community of conservation, education and technology”. They created this Wildlife Camera Kit to help people reconnect with Nature, through technology and digital skills learning accessible to all.
This project allows to automatically take pictures or videos when detecting movement (change in infrared heat).

## Components
- IP55 weatherproof Case
  - Print with STL files from Naturebytes [resources page]( https://naturebytes.org/2020/09/03/wildlife-cam-kit-resources/)
  - Or buy from the community’s [shop](https://shop.naturebytes.org/products/wildlife-cam-case-by-naturebytes)
- Raspberry Pi (any will do, A+ model recommended for power efficiency)
- Raspberry Pi Camera Module
- PIR Motion Sensor Module
- 8GB+ Micro SD card for OS (and optionally for storage)
	- Download the OS image corresponding to your Pi model from Naturebytes [resources page]( https://naturebytes.org/2020/09/03/wildlife-cam-kit-resources/)
- Optionally: 2.0 USB thumb-drive for storage (Micro SD card still needed for OS)
- Optionally: Mini RTC Module for Raspberry Pi (for timestamping)
- Power supply (max recommended dimension: 70 mm (w) x 100 mm (l) x 22 mm (d)):
  - USB Power Bank 
  - Or rechargeable Li-ion battery (needs a Seeed studio Lipo rider)

## Assembly
Check out Assembly guide file (downloaded from the Naturebytes [resources page]( https://naturebytes.org/2020/09/03/wildlife-cam-kit-resources/))

## How to run
OS images from the community’s website comes with the files in the *Desktop* and the *Naturesbytes* folders, both in /home/pi/

To start camera:
1.	Plug fully charged power supply in the Raspberry Pi’s micro-USB *PWR* port
2.	Plug in screen and HID
3.	Launch the *launch_nbcamera.sh* file from the *Naturebytes/Scripts* folder
4.	Unplug peripherals
5.	Close case and set in selected area
6.	When the PIR detects a change in heat, it will trigger capture and by default save the created file in the */usb0* folder (with or without a usb storage actually plugged in)

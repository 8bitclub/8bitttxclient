import spidev

spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0 (/dev/spidev0.0)
spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz

# Send READ STATUS REGISTER (RDSR) command
response = spi.xfer2([0x05, 0x00])  # 0x05 = RDSR, second byte is dummy

print("Status register response:", response)

spi.close()

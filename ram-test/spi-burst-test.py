import spidev
import time

CMD_READ  = 0x03
CMD_WRITE = 0x02
CMD_WRSR  = 0x01

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# Set SEQUENTIAL mode
spi.xfer2([CMD_WRSR, 0x40])
time.sleep(0.01)

start_addr = 0x0100
test_data = [i & 0xFF for i in range(32)]  # 32 bytes: 0x00 to 0x1F

# Burst write
addr_hi = (start_addr >> 8) & 0xFF
addr_lo = start_addr & 0xFF
spi.xfer2([CMD_WRITE, addr_hi, addr_lo] + test_data)

# Burst read
read_back = spi.xfer2([CMD_READ, addr_hi, addr_lo] + [0x00]*len(test_data))[3:]

# Verify
if read_back == test_data:
    print("Burst test passed.")
else:
    print("Data mismatch!")
    print("Written:", test_data)
    print("Read:   ", read_back)

spi.close()

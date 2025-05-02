import spidev
import time

CMD_READ = 0x03
CMD_WRITE = 0x02
CMD_WRSR = 0x01

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# Set SEQUENTIAL mode (bit 6 = 1)
spi.xfer2([CMD_WRSR, 0x40])
time.sleep(0.01)

def write_byte(address, data_byte):
    hi = (address >> 8) & 0xFF
    lo = address & 0xFF
    spi.xfer2([CMD_WRITE, hi, lo, data_byte])

def read_byte(address):
    hi = (address >> 8) & 0xFF
    lo = address & 0xFF
    return spi.xfer2([CMD_READ, hi, lo, 0x00])[3]

test_addr = 0x0123
test_data = 0xAB

write_byte(test_addr, test_data)
time.sleep(0.01)
print(f"Read back: 0x{read_byte(test_addr):02X}")

spi.close()

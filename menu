#!/bin/bash

TITLE="8BitClub Teletext Services - CLIENT (version 1.0)"

run_sram_test() {
  RESULT=""
  PASS=true

  RESULT+="\n\Z4Step 1:\Zn Checking for SPI devices...\n"
  if ls /dev/spidev0.0 &>/dev/null && ls /dev/spidev0.1 &>/dev/null; then
    RESULT+="-> Devices found: \Z2OK\Zn\n\n"
  else
    RESULT+="-> Devices not found: \Z1FAIL\Zn\n\n"
    PASS=false
  fi

  RESULT+="\Z4Step 2:\Zn Running spi-test.py...\n"
  TEST_OUT=$(python3 ram-test/spi-test.py 2>/dev/null)
  if echo "$TEST_OUT" | grep -q "Status register response: \[0, 64\]"; then
    RESULT+="-> Response correct: \Z2OK\Zn\n\n"
  else
    RESULT+="-> Unexpected response: \Z1FAIL\Zn\n$TEST_OUT\n\n"
    PASS=false
  fi

  RESULT+="\Z4Step 3:\Zn Running spi-write.py...\n"
  WRITE_OUT=$(python3 ram-test/spi-write.py 2>/dev/null)
  if echo "$WRITE_OUT" | grep -q "Read back: 0xAB"; then
    RESULT+="-> Read back correct: \Z2OK\Zn\n\n"
  else
    RESULT+="-> Unexpected response: \Z1FAIL\Zn\n$WRITE_OUT\n\n"
    PASS=false
  fi

  RESULT+="\Z4Step 4:\Zn Running spi-burst-test.py...\n"
  BURST_OUT=$(python3 ram-test/spi-burst-test.py 2>/dev/null)
  if echo "$BURST_OUT" | grep -q "Burst test passed."; then
    RESULT+="-> Burst test passed: \Z2OK\Zn\n\n"
  else
    RESULT+="-> Unexpected response: \Z1FAIL\Zn\n$BURST_OUT\n\n"
    PASS=false
  fi

  if $PASS; then
    RESULT+="\n\Z2All diagnostics completed successfully.\Zn\n"
  else
    RESULT+="\n\Z1One or more tests failed.\Zn\n"
  fi

  dialog --colors --title "SPI SRAM TEST Result" --msgbox "$RESULT" 30 90
}

diagnostics_menu() {
  while true; do
    CHOICE=$(dialog --clear \
      --backtitle "$TITLE" \
      --title "Diagnostics Menu" \
      --menu "Select an option:" \
      15 50 2 \
      1 "SPI SRAM TEST" \
      2 "Back to Main Menu" \
      2>&1 >/dev/tty)

    clear

    case $CHOICE in
      1) run_sram_test ;;
      2) break ;;
    esac
  done
}

show_ip_address() {
  IP_INFO=$(ip -4 a | grep -v '127.0.0.1' | grep inet | head -n 1 | awk '{print $2 " on " $NF}')
  dialog --title "IP Address Info" --msgbox "$IP_INFO" 7 50
}

show_information() {
  dialog --title "Information" --msgbox "8BitClub Teletext Services - CLIENT (Version 1.0)\n\n8BitClub - 2025" 10 60
}

main_menu() {
  while true; do
    CHOICE=$(dialog --clear \
      --backtitle "$TITLE" \
      --title "$TITLE" \
      --menu "Select an option:" \
      15 60 6 \
      1 "Diagnostics" \
      2 "Show IP Address" \
      3 "Information" \
      4 "Exit" \
      2>&1 >/dev/tty)

    clear

    case $CHOICE in
      1) diagnostics_menu ;;
      2) show_ip_address ;;
      3) show_information ;;
      4) break ;;
    esac
  done
}

main_menu

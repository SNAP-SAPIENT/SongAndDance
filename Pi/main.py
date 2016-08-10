import beaconScaner
import uart
import sys
import time
import logging

import bluetooth._bluetooth as bluez

beacon1 = '18660'
beacon2 = '18637'
beacon3 = '18627'
beacon4 = '18620'
logging.basicConfig(filename = '/home/pi/logs/song_dance/app.log', level= logging.DEBUG)

logging.info('Starting app..')
try:
        dev_id = 0
        try:
                sock = bluez.hci_open_dev(dev_id)
                print "Beacon Scaner started..."
                logging.info('Beacon Scaner started.....')

        except:
                print "Error scanning for beacons!!!"
                logging.info('Error scanning for beacons!!!')
                sys.exit(1)

        beaconScaner.hci_le_set_scan_parameters(sock)
        beaconScaner.hci_enable_le_scan(sock)



        avgCounter = 0
        totalRssi = 0
        while True:
                valueMap = beaconScaner.parse_events(sock, 10)
                print valueMap
                logging.info("valueMap; %s" %valueMap)
                b1 = 0
                b2 = 0
                b3 = 0
                b4 = 0
                if valueMap:
                        b1 = valueMap.get(beacon1)
                        b2 = valueMap.get(beacon2)
                        b3 = valueMap.get(beacon3)
                        b4 = valueMap.get(beacon4)
                        send = False
                        if b1:
                                data = '1' + ":%d" %abs(b1)
                                send = True
                        if b2:
                                data =  '2' + ":%d" %abs(b2)
                                send = True
                        if b3:
                                data =  '3' + ":%d" %abs(b3)
                                send = True
                        if b4:
                                data = '4' + ":%d" %abs(b4)
                                send = True
                        if send:
                                uart.sendData(data)       
                # rssi = valueMap.get(beaconMinorId)
                # if rssi:
                #       getBeaconValues(valueMap, rssi)
                #       if(avgCounter == 5):
                #               avgRssi = totalRssi/avgCounter
                #               print "avgRssi: %d" %avgRssi
                #               avgCounter = 0
                #               totalRssi = 0                   
                avgCounter += 1

except KeyboardInterrupt:
    print 'closing due to Keyboard Interrupt'
    logging.info('closing due to Keyboard Interrupt..')

uart.closeport()
logging.info('stopping app..')

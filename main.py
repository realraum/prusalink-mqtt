# multiple processes
from multiprocessing import Process

# parse config.ini file
from config_handler import ConfigHandler

# prusa link
from printer_handler import PrinterHandler

# mqtt
import paho.mqtt.client as mqtt

config_handler = ConfigHandler()
printer_handler = PrinterHandler()


def main():
    if config_handler.check_any_empty():
        raise Exception('config.ini file has empty fields')

    # mqtt
    mqtt_client = mqtt.Client()

    # PrusaLink
    prusa_link = printer_handler.connect(mqtt_client, config_handler)

    # start processes
    processes = []

    # start mqtt process
    mqtt_process = Process(target=mqtt_client.loop_forever)
    mqtt_process.start()
    processes.append(mqtt_process)

    # start prusa link process
    prusa_link_process = Process(target=prusa_link.loop_forever)
    prusa_link_process.start()
    processes.append(prusa_link_process)

    # wait for processes to finish
    for process in processes:
        process.join()

    # close mqtt connection
    mqtt_client.disconnect()

    # stop prusa link
    prusa_link.stop()


if __name__ == '__main__':
    main()

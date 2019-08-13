# Azure IoT - Getting Started with Raspberry Pi
The Raspberry Pi is a low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python. It’s capable of doing everything you’d expect a desktop computer to do, from browsing the internet and playing high-definition video, to making spreadsheets, word-processing, and playing games.  As a dev board it is also very handy for quickly connecting to various sensors for flexible prototyping.

If you were looking for Azure Sphere, go [here](https://github.com/jasonerrett/AzureIoT_HelloSphere)

## Using Github
- [Download Github Desktop](https://desktop.github.com/)
- Click on the green **'Clone or download'** button, and copy the url.  *Note: if you download the ZIP file, you will miss out on any notifications of updates to the project.  But, if you don't want the additional software on your machine, this option is will work fine.*
- Open Github Desktop, click File -> Clone Repository -> Url tab -> Paste the url into the box -> specify the local folder to clone into -> hit **'Clone'**
- If you'd like more information... [Github Tutorial](https://lab.github.com/githubtraining/paths/first-day-on-github)

## Tools
These are not all required.  I will show some of them in the video, but if you have tools you prefer that work just fine, by all means use what you like.  All of these are freely available.
- [Azure Device Explorer](https://github.com/Azure/azure-iot-sdk-csharp/releases/download/2019-1-4/SetupDeviceExplorer.msi) (Helpful if using IoT Hub)
- [Visual Studio Community Edition](https://visualstudio.microsoft.com/vs/community/)
- [VSCode](https://code.visualstudio.com/Download) is a cross-platform IDE
- [SD Card Formatter](https://www.sdcard.org/downloads/formatter/)
- [Etcher](https://www.balena.io/etcher/)

## Getting Started with Raspberry Pi
If you want to follow an end-to-end guide on Azure Docs, feel free to skip this section.  This is provided for those of you who want to work with Raspberry Pi on other things.  It's a simple guide on getting up and running with Pi.
- Hardware Overview
    - GPIO pins are your gateway to interacting with the "real" world.  This site, [Learn Robotics](https://www.learnrobotics.org/blog/raspberry-pi-gpio/
), has a good explanation of the hardware layout and pins
- Common starter dev/test Peripheral
    - [Sense Hat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) - One "hat" with multiple sensors built in
- Software / Setup
    1. Read the [Easy SD Card Setup](https://elinux.org/RPi_Easy_SD_Card_Setup) process to prepare your SD Card for installation
    2. Go to [RaspberryPi.org](https://www.raspberrypi.org/downloads/raspbian/) and download the Raspbian OS image (zip file).  Including an image labeled **'with Desktop'** will provide a more familiar experience for those of you who enjoy graphical UI's
    3. Use [Etcher](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to flash the OS image to the SD Card
    4. Connect a usb keyboard/mouse, and a monitor, then connect a micro-usb cable to the Pi for power
        - *Note: If you want to use a remote viewer after the initial install, Raspberry Pi's come installed with VNC Viewer.  There just a little bit of [configuration](https://www.realvnc.com/en/connect/docs/raspberry-pi.html#raspberry-pi-setup) that has to be done first. Oh yeah, and you'll need a wifi or wired network connection ;)*
    5. Done.  Ready for sensors and coding fun!

## Connecting the Raspberry Pi *Simulator* to Azure IoT Hub
The fastest way to get started with streaming data into Azure is using a simulator.  Simulators give you a way to see what a test stream of data will look like as it passes through back end services.
- [Getting Started with the Raspberry Pi Simulator](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-web-simulator-get-started)


## Connecting the Real-world Raspberry Pi to Azure IoT Hub
The Raspberry Pi is now running a version of Linux.  What this means for you is that you can now do basically whatever you want.

Here are a couple of guides you may be intersted in:
- [Connect Raspberry Pi to Azure IoT Hub (Node.js)](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-kit-node-get-started)
- [Connect Raspberry Pi to Azure IoT Hub (C)](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-kit-c-get-started)
- For Python, you will need the RPi.GPIO library mentioned [here](https://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/)
    - [DHT22 Temp Sensor Example](https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/)
    - [Sending data to IoT Hub with Python](https://github.com/Azure-Samples/azure-iot-samples-python/archive/master.zip )
- [Azure IoT Hub get started with physical devices tutorials](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-get-started-physical)

## What Now?
Now that your device is sending data to Azure IoT Hub and/or IoT Central, you have an enormous amount of capabilities to add and explorer.  Below are just a few of the most common data services typically used in IoT architectures.

Azure Portal: **https://portal.azure.com**

## Azure Services Common in IoT Architectures
- [Example Architecture Diagram](images/AzureIoTArchitecture.png
)
- Device Registration / Ingestion
    - [IoT Hub](https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub)
    - [IoT Central](https://docs.microsoft.com/en-us/azure/iot-central/overview-iot-central) *Note: also has visualization, analytics, etc.*
    - [Device Provisioning Service](https://docs.microsoft.com/en-us/azure/iot-dps/about-iot-dps)
    - [Event Hubs](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about)
- Storage
    - [Azure Storage](https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction)
    - [Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction)
- Analytics
    - [Stream Analytics](https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction)
    - [Time Series Insights](https://docs.microsoft.com/en-us/azure/time-series-insights/time-series-insights-update-overview)
    - [Server-less Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview)
- Integration & Visualization
    - [Logic Apps](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-overview)
    - [Power BI](https://docs.microsoft.com/en-us/power-bi/power-bi-overview)
- Disconnected Scenarios (Very cool stuff)
    - [IoT Edge](https://docs.microsoft.com/en-us/azure/iot-edge/about-iot-edge)
    - [Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-intro)
- Artification Intelligence
    - [Cognitive Services](https://docs.microsoft.com/en-us/azure/cognitive-services/)
- 3rd-Party and Open source
    - [SendGrid](https://docs.microsoft.com/en-us/azure/sendgrid-dotnet-how-to-send-email)
    - [Kafka](https://docs.microsoft.com/en-us/azure/hdinsight/kafka/apache-kafka-introduction)
    - [Spark](https://docs.microsoft.com/en-us/azure/hdinsight/spark/apache-spark-overview)
    - [Storm](https://docs.microsoft.com/en-us/azure/hdinsight/storm/apache-storm-overview)
    - [Notebooks](https://docs.microsoft.com/en-us/azure/notebooks/azure-notebooks-overview)
    - Bring-your-Own on [Virtual Machines](https://azure.microsoft.com/en-us/services/virtual-machines/)

## Azure Solution Accelerators
- [IoT Solution Accelerators](https://azure.microsoft.com/en-us/features/iot-accelerators/)
    - Remote Monitoring
    - Device Simulation
    - Connected Factory
    - Predictive Maintenance

## Free Supplemental Learning Materials
- [Microsoft Learn](https://docs.microsoft.com/en-us/learn/)
- [IoT School](https://iotschool.microsoft.com/)
- [AI School](https://aischool.microsoft.com/)
- [IoT & AI Workshop](https://github.com/kenhausman/ADSWorkshop)
- [Microsoft Professional Certification Programs](https://www.edx.org/course/?type=Professional%20Certificate&school=Microsoft%3A%20Microsoft) *Note: free if just learning, but there is a fee to receive certification upon completion*
- [Other edX Courses](https://www.edx.org/course?search_query=Azure)

## Other Useful Stuff
- [Anomaly Detection in Azure Stream Analytics](https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-machine-learning-anomaly-detection)
- [Custom Vision at the Edge Walkthrough](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-deploy-custom-vision)
- [Container Support in Azure Cognitive Services](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-container-support)
- [Using the MXChip IoT DevKit](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-arduino-iot-devkit-az3166-door-monitor)
- [Azure IoT Security](https://azure.microsoft.com/en-us/overview/iot/security/)
- [Azure Security Center for IoT](https://docs.microsoft.com/en-us/azure/asc-for-iot/overview)
- [IoT Security Architecture](https://docs.microsoft.com/en-us/azure/iot-fundamentals/iot-security-architecture)
- [IoT Security Best Practices](https://docs.microsoft.com/en-us/azure/iot-fundamentals/iot-security-best-practices)
- [Secure Deployment of IoT](https://docs.microsoft.com/en-us/azure/iot-fundamentals/iot-security-deployment)





 
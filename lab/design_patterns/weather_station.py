class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass
    
    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        pass
    
# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and 
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):
    
    def __init__(self):        
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    
    def registerObserver(self, observer):
        # When an observer registers, we just 
        # add it to the end of the list.
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)
    
    def notifyObservers(self):
        # We notify the observers when we get updated measurements 
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        """Notifies other parts of the program that the measurements have been updated."""
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        
        self.measurementsChanged()
    
    # other WeatherData methods here.


class CurrentConditionsDisplay(Observer):
    
    def __init__(self, weatherData):        
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
        
    def display(self):
        print("Current conditions:", self.temerature, 
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)
        
# TODO: implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay:
    """Keeps track of the min/average/max measurements and displays them."""

    def __init__(self, weatherData):
        self.temperatures = []
        self.humidities = []
        self.pressures = []
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer so it gets data updates.
                                           
    def update(self, temperature, humidity, pressure):
        self.temperatures.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)
        self.display()

    def display(self):
        print("Minimum temperature: ", min(self.temperatures), 
        "\nMaximum temperature: ", max(self.temperatures),
        "\nAverage temperature: ", sum(self.temperatures)/len(self.temperatures))

        print("Min Humidity: ", min(self.humidities), 
        "\nMax Humidity: ", max(self.humidities),
        "\nAverage Humidity: ", sum(self.humidities)/len(self.humidities))

        print("Min pressure: ", min(self.pressures), 
        "\nMax pressure: ", max(self.pressures), 
        "\nAverage pressure: ", sum(self.pressures)/len(self.pressures))

class ForecastDisplay:
    """The ForecastDisplay class shows the weather forcast based on the current
        temperature, humidity and pressure. Use the following formulas :
        forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        forcast_humadity = humidity - 0.9 * humidity
        forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure """

    def __init__(self, weatherData):
        self.temperature = 0
        self.forcast_humidity = 0
        self.forcast_pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forcast_humidity = humidity - 0.9 * humidity
        self.forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()
    
    def display(self):
        print("The temperature forecast is: ", self.temperature, 
        "\nThe humidity forecast is: ", self.forcast_humidity,
        "\nThe pressure forecast is: ", self.forcast_pressure)
    
    
class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forcast_display = ForecastDisplay(weather_data)
        
        # TODO: Create two objects from StatisticsDisplay class and 
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.

        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.

        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)
        weather_data.removeObserver(forcast_display)
        
        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)
        weather_data.removeObserver(statistics_display)
    
        

if __name__ == "__main__":
    w = WeatherStation()
    w.main()
from abc import ABC, abstractmethod

# interfas producto
class Smartphone(ABC):
    @abstractmethod
    def specifications(self):
        pass

class Tablet(ABC):
    @abstractmethod
    def specifications(self):
        pass

# apple
class IPhone(Smartphone):
    def specifications(self):
        return "iPhone iOS-17 con Face ID"

class IPad(Tablet):
    def specifications(self):
        return "iPad  M2 Chip con Apple Pencil Support"

# Samwung
class GalaxyPhone(Smartphone):
    def specifications(self):
        return "Galaxy Phone con Fingerprint Sensor"

class GalaxyTab(Tablet):
    def specifications(self):
        return "Galaxy Tablet con S Pen"

# intrefas fabricas
class DeviceFactory(ABC):
    @abstractmethod
    def create_smartphone(self):
        pass
    
    @abstractmethod
    def create_tablet(self):
        pass

# fabricas
class AppleFactory(DeviceFactory):
    def create_smartphone(self):
        return IPhone()
    
    def create_tablet(self):
        return IPad()

class SamsungFactory(DeviceFactory):
    def create_smartphone(self):
        return GalaxyPhone()
    
    def create_tablet(self):
        return GalaxyTab()

def client_code(factory: DeviceFactory):
    smartphone = factory.create_smartphone()
    tablet = factory.create_tablet()
    
    print(smartphone.specifications())
    print(tablet.specifications())

print("Apple Factory Products:")
client_code(AppleFactory())

print("Samsung Factory Products:")
client_code(SamsungFactory())

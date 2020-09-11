from . import geom


class Area:
    def __get__(self, instance, owner):
        if owner == geom.Rectangle or owner == geom.Square:
            return instance.width * instance.height
        elif owner == geom.Circle:
            return instance.radius * instance.radius * 3.14


class Perimeter:
    def __get__(self, instance, owner):
        if owner == geom.Rectangle or owner == geom.Square:
            return (instance.width + instance.height) * 2
        elif owner == geom.Circle:
            return 2 * instance.radius * 3.14
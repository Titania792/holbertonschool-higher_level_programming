#!/usr/bin/python3
""" base.py """
import json


class Base:
    """Creating Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing Class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation of a list of dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string representation of a list of objects to a file"""
        if list_objs is None or len(list_objs) == 0:
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(None))
        else:
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**d) for d in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        from turtle import Turtle, Screen
        screen = Screen()
        t = Turtle()
        list_rectangles.extend(list_squares)
        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.color("blue")
            t.begin_fill()
            t.forward(rectangle.width)
            t.left(90)
            t.forward(rectangle.height)
            t.left(90)
            t.forward(rectangle.width)
            t.left(90)
            t.forward(rectangle.height)
            t.end_fill()
        t.hideturtle()
        screen.exitonclick()

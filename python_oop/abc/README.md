Introduction and Context
In object-oriented programming, some classes are used to define a common contract for other classes.

Sometimes a class should define what behavior must exist, but not provide the full implementation itself. In Python, this can be modeled using abstract classes.

An abstract class allows you to define methods that subclasses are expected to implement. This helps create consistent designs where different objects share the same interface while keeping their own specific behavior.

A related concept is the idea of an interface. Python does not have a dedicated interface keyword, but similar results can be achieved using abstract methods or by relying on duck typing: if an object provides the required behavior, it can be used.

In this project, you will work with:

abstract base classes
abstract methods
interface-like design
duck typing
subclassing built-in classes
multiple inheritance
mixins
These tools are useful when building flexible and reusable software designs.

Learning Objectives
By completing this project, you should be able to:

explain the purpose of an abstract class
use ABC and @abstractmethod
implement subclasses that satisfy an abstract contract
understand how Python can model interfaces
explain and apply duck typing
extend built-in classes while preserving their behavior
understand the role of multiple inheritance
use mixins to add reusable behavior to a class
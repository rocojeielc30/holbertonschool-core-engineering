#!/usr/bin/env python3
"""A list that announces every time something is added or removed."""


class VerboseList(list):
    """A normal list that also prints a message for each change."""

    def append(self, item):
        """Add one item to the end, then say what was added."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Add several items to the end, then say how many were added."""
        # turn it into a list first so we can count it safely
        new_items = list(items)
        super().extend(new_items)
        print("Extended the list with [{}] items.".format(len(new_items)))

    def remove(self, item):
        """Say what is being removed, then remove it."""
        # only announce it if it's really there; otherwise list raises
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Say which item is being taken out, then take it out."""
        # look at the item first so the message can name it
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)


if __name__ == "__main__":
    verbose_list = VerboseList([1, 2, 3])

    verbose_list.append(4)
    verbose_list.extend([5, 6])
    verbose_list.remove(2)
    verbose_list.pop()
    verbose_list.pop(0)
    print(verbose_list)

    # removing something that isn't there still raises an error
    try:
        verbose_list.remove(99)
    except ValueError as error:
        print("[ValueError] {}".format(error))

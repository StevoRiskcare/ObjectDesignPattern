import abc


class AbsAdapter(metaclass=abc.ABCMeta):
    def __init__(self, adaptee):
        self._adptee = adaptee

    @property
    def adaptee(self):
        return self._adptee

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def address(self):
        pass


class VendAdpater(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return '{} {}'.format(self.adaptee.name, self.adaptee.street)


class Vendor(object):
    def __init__(self, name, number, street):
        self._name = name
        self._number = number
        self._street = street

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def street(self):
        return self._street


MOCKVENDOR = (VendAdpater(Vendor('steve', 46, 'Pendle')),)
CUSTOMER = MOCKVENDOR

def main():
    for cust in CUSTOMER:
        print(cust.name, cust.address)


if __name__ == '__main__':
    main()

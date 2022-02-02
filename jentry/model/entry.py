from hbutils.model import hasheq, asitems, get_repr_info


@hasheq()
@asitems(['package', 'clazz', 'filename'])
class JavaEntry:
    """
    Entry model of java source code.
    """

    def __init__(self, filename, package, clazz):
        """
        Constructor of :class:`jentry.model`

        :param filename:
        :param package:
        :param clazz:
        """
        self.__filename = filename if filename else None
        self.__package = package if package else None
        self.__clazz = clazz

    @property
    def filename(self):
        return self.__filename

    @property
    def package(self):
        return self.__package

    @property
    def clazz(self):
        return self.__clazz

    @property
    def full_name(self):
        if self.__package:
            return f'{self.__package}.{self.__clazz}'
        else:
            return f'{self.__clazz}'

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return get_repr_info(
            cls=self.__class__,
            args=[
                ('class', lambda: self.full_name),
                ('filename', lambda: repr(self.filename), lambda: self.filename),
            ]
        )

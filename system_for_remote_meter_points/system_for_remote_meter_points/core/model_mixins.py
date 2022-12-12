class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

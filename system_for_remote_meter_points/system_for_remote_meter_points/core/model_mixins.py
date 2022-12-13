# mixin for choice fields, show value to value
class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.value, x.value) for x in cls]

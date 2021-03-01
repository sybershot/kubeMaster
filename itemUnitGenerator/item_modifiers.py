from typing import Dict


class ModifierBase:
    def __init__(self, name="Err#228", description="This item might have unexpected behaviour.",
                 effect_tip="Hm, looks like something went wrong.", effects=None):
        self._name = name
        self._description = description
        self._effect_tip = effect_tip
        if effects is None:
            raise Exception("Error during modifier effects creation!")
        self._effects = effects  # type: Dict

    @property
    def name(self):
        return self._name

    @property
    def effects(self):
        return self._effects

    @property
    def parsed_effects(self):
        ret = {}
        for effect_name, effect_value in self.effects.items():
            applies_to, field1, field2 = effect_name.split('_')
            ret[applies_to] = ret.get(applies_to, {})
            ret[applies_to][field1] = ret[applies_to].get(field1, {})
            ret[applies_to][field1][field2] = effect_value
        return ret

    def __repr__(self):
        return f'<Modifier name:"{self.name}" ' \
               f'description:"{self._description}" ' \
               f'tip:"{self._effect_tip}" '


class ModifierMajor(ModifierBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ModifierMinor(ModifierBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

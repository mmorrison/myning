from unittest import mock

from myning.config import SPECIES
from myning.objects.character import Character, CharacterSpecies, SpeciesEmoji
from myning.utils.generators import generate_character


class TestCharacter:
    """Test Character instantiation"""

    def test_alien_species_attributes(self):
        """Test that alien species attributes are correct"""
        char = generate_character(level_range=[1, 2])
        assert char.name.isalpha
        assert " " in char.name
        for attr in ("damage", "armor", "critical_chance", "dodge_chance"):
            assert isinstance(char.stats[attr], int)
        assert isinstance(char.icon, SpeciesEmoji)

    def test_companion_classes(self):
        """Test that companion classes are correctly typed"""
        char = generate_character(level_range=[1, 2])
        assert isinstance(char.companion_species, list)
        for attr in char.companion_species:
            assert isinstance(attr, CharacterSpecies)

    def test_character_intros(self):
        """test that character intros work with species intros"""
        char = generate_character(level_range=[1, 2])
        assert isinstance(char.intros, list)
        assert len(char.intros) > 0
        assert char.get_introduction().isalpha

    def test_species_attributes(self):
        """Test that species attributes are correct"""
        for species in Character.companion_species:
            species = SPECIES[species.value]
            char = generate_character(level_range=[1, 2], species=species)
            assert char.health_mod == species.health_mod
            assert char.name.isalpha
            assert " " in char.name
            for attr in ("damage", "armor", "critical_chance", "dodge_chance"):
                assert isinstance(char.stats[attr], int)
            assert isinstance(char.icon, SpeciesEmoji)

"""Tests for the data model."""

from pytest import mark

from animal_db.models import Taxonomy, Subject


@mark.parametrize(
    'taxonomy, expected_scientific_name',
    (
        (Taxonomy(), None),
        (Taxonomy(genus='Brachypelma'), None),
        (Taxonomy(species='Hamorii'), None),
        (
            Taxonomy(species='Hamorii', common_name='Mexican Red-Knee'),
            'Mexican Red-Knee',
        ),
        (
            Taxonomy(genus='Brachypelma', common_name='Mexican Red-Knee'),
            'Mexican Red-Knee',
        ),
        (Taxonomy(common_name='Mexican Red-Knee'), 'Mexican Red-Knee'),
        (
            Taxonomy(genus='Brachypelma', species='Hamorii'),
            'Brachypelma Hamorii',
        ),
    ),
)
def test_taxonomy_scientific_name(
    taxonomy: Taxonomy, expected_scientific_name: str | None
) -> None:
    """Test the `secientific_name` method for `Taxonomy`."""
    assert taxonomy.scientific_name == expected_scientific_name


@mark.parametrize(
    'subject, expected_repr',
    ((Subject(name='Grace Hopper'), 'Grace Hopper (Unknown spieces)'),),
)
def test_subject_repr(subject: Subject, expected_repr: str) -> None:
    """Test the `__repr__` method for subjects."""
    assert repr(subject) == expected_repr

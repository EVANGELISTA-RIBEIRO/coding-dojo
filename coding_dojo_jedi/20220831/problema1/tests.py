import pytest
from dojo import conceito


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ((10, 10), 'Média 10, "A", APROVADO'),
        ((1, 1), 'Média 1, "E", REPROVADO'),
        ((10, 5), 'Média 7.5, "B", APROVADO'),
        ((9, 5), 'Média 7, "C", APROVADO'),
        ((6, 4), 'Média 5, "D", REPROVADO'),
    )
)
def test_conceito(entrance, expected):
    assert conceito(*entrance) == expected

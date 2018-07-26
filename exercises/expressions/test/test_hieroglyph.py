from exercises.expressions.src.hieroglyph import Hieroglyph


def test_sacred_cat():
    # all cats are sacred!
    assert not Hieroglyph.worship_sacred_cats('dog dog dog')
    assert Hieroglyph.worship_sacred_cats('cat')
    assert Hieroglyph.worship_sacred_cats('dog cat dog dog')
    assert Hieroglyph.worship_sacred_cats('scarab cat scarab cat')
    assert Hieroglyph.worship_sacred_cats('cat cat ')


def test_alphanumeric_glyph():
    assert Hieroglyph.alphanumeric_glyph('wxyd67891')
    assert not Hieroglyph.alphanumeric_glyph('ad143')
    assert not Hieroglyph.alphanumeric_glyph('34561')
    assert not Hieroglyph.alphanumeric_glyph('sand pyramid')
    assert Hieroglyph.alphanumeric_glyph('gold2134598')
    assert Hieroglyph.alphanumeric_glyph('sand104923')
    assert not Hieroglyph.alphanumeric_glyph('143sand')


def test_avoid_nile_crocodile():
    assert Hieroglyph.avoid_nile_crocodile('nile')
    assert Hieroglyph.avoid_nile_crocodile('nile nile')
    assert not Hieroglyph.avoid_nile_crocodile('crocodile nile nile')
    assert not Hieroglyph.avoid_nile_crocodile('nile crocodile nile')
    assert not Hieroglyph.avoid_nile_crocodile('nile nile crocodile')


def test_find_gold_scarab():
    assert not Hieroglyph.find_gold_scarab('gold')
    assert not Hieroglyph.find_gold_scarab('scarab')
    assert not Hieroglyph.find_gold_scarab('scarab gold')
    assert Hieroglyph.find_gold_scarab('gold scarab') == 'gold'


def test_raid_tuts_tomb():
    assert Hieroglyph.raid_tuts_tomb('tomb')
    assert Hieroglyph.raid_tuts_tomb('tomb ')
    assert Hieroglyph.raid_tuts_tomb('tomb tomb tomb')
    assert not Hieroglyph.raid_tuts_tomb('tomb tut tomb tomb')
    assert not Hieroglyph.raid_tuts_tomb('tut tomb tomb')
    assert not Hieroglyph.raid_tuts_tomb('tomb tomb Tut tomb')
    assert not Hieroglyph.raid_tuts_tomb('TUT tomb tomb tomb')
    assert not Hieroglyph.raid_tuts_tomb('TOMB TOMB tUt TOMB TOMB')


def test_steal_crystal_skull():
    assert Hieroglyph.steal_crystal_skull('crystal skull') == 'crystal idol'
    assert Hieroglyph.steal_crystal_skull('skull crystal skull') == 'idol crystal idol'
    assert Hieroglyph.steal_crystal_skull('crystal boulder') == 'crystal boulder'
    assert Hieroglyph.steal_crystal_skull('skull skull boulder skull') == 'idol idol boulder idol'


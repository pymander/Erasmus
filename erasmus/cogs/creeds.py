from __future__ import annotations

from typing import TYPE_CHECKING, Final, TypedDict

from botus_receptus import utils
from botus_receptus.cog import GroupCog
from discord import app_commands

if TYPE_CHECKING:
    import discord

    from ..erasmus import Erasmus


class CreedDict(TypedDict):
    title: str
    description: str


_apostles_creed: Final[CreedDict] = {
    'title': "The Apostles' Creed",
    'description': '''
I believe in God, the Father Almighty,
    the Maker of heaven and earth,
    and in Jesus Christ, His only Son, our Lord:

Who was conceived by the Holy Ghost,
    born of the virgin Mary,
    suffered under Pontius Pilate,
    was crucified, dead, and buried;

He descended into hell.

The third day He arose again from the dead;

He ascended into heaven,
    and sitteth on the right hand of God the Father Almighty;
    from thence he shall come to judge the quick and the dead.

I believe in the Holy Ghost;
    the holy catholic church;
    the communion of saints;
    the forgiveness of sins;
    the resurrection of the body;
    and the life everlasting.

Amen.
''',
}

_athanasian_creed: Final[CreedDict] = {
    'title': 'The Athanasian Creed',
    'description': (
        'Whosoever will be saved, before all things it is necessary that he hold the '
        'catholic faith; Which faith except every one do keep whole and undefiled, '
        'without doubt he shall perish everlastingly.\n\n'
        'And the catholic faith is this: That we worship one God in Trinity, and '
        'Trinity in Unity; '
        'Neither confounding the persons, nor dividing the substance. '
        'For there is one Person of the Father, another of the Son and another of the '
        'Holy Spirit. '
        'But the Godhead of the Father, of the Son, and of the Holy Spirit is all one, '
        'the glory equal, the majesty co-eternal. '
        'Such as the Father is, such is the Son and such is the Holy Spirit. '
        'The Father uncreated, the Son uncreated, and the Holy Spirit uncreated. '
        'The Father incomprehensible, the Son incomprehensible, and the Holy Spirit '
        'incomprehensible. '
        'The Father eternal, the Son eternal, and the Holy Spirit eternal. '
        'And yet they are not three eternals, but one eternal. '
        'As also there are not three uncreated nor three incomprehensibles, but one '
        'uncreated and one incomprehensible. '
        'So likewise the Father is almighty, the Son almighty, and the Holy Spirit '
        'almighty; '
        'And yet they are not three almighties, but one almighty. '
        'So the Father is God, the Son is God, and the Holy Spirit is God; '
        'And yet they are not three Gods, but one God. '
        'So likewise the Father is Lord, the Son Lord, and the Holy Spirit Lord; '
        'And yet they are not three Lords, but one Lord. '
        'For like as we are compelled by the Christian verity to acknowledge every '
        'person by himself to be God and Lord; '
        'so are we forbidden by the catholic religion to say: There are three Gods or '
        'three Lords.\n\n'
        'The Father is made of none, neither created nor begotten. '
        'The Son is of the Father alone; not made nor created, but begotten. '
        'The Holy Spirit is of the Father and of the Son; neither made, nor created, '
        'nor begotten, but proceeding. '
        'So there is one Father, not three Fathers; one Son, not three Sons; one Holy '
        'Spirit, not three Holy Spirits.'
        'And in this Trinity none is afore, nor after another; none is greater, or '
        'less than another. '
        'But the whole three persons are co-eternal, and co-equal. '
        'So that in all things, as aforesaid, the Unity in Trinity and the Trinity in '
        'Unity is to be worshipped. '
        'He therefore that will be saved must thus think of the Trinity.\n\n'
        'Furthermore it is necessary to everlasting salvation that he also believe '
        'rightly the incarnation of our Lord Jesus Christ. '
        'For the right faith is that we believe and confess that our Lord Jesus '
        'Christ, the Son of God, is God and man. '
        'God of the substance of the Father, begotten before the worlds; and made of '
        'the substance of His mother, born in the world. '
        'Perfect God and perfect man, of a reasonable soul and human flesh subsisting. '
        'Equal to the Father as touching His Godhead, and inferior to the Father as '
        'touching His manhood. '
        'Who, although He is God and man, yet He is not two, but one Christ. '
        'One, not by conversion of the Godhead into flesh, but by taking of the '
        'manhood into God. '
        'One altogether, not by the confusion of substance, but by unity of person. '
        'For as the reasonable soul and flesh is one man, so God and man is one '
        'Christ; '
        'Who suffered for our salvation, descended into hell, rose again the third day '
        'from the dead; '
        'He ascended into heaven, He sitteth on the right hand of the Father, God '
        'Almighty; '
        'From thence He shall come to judge the living and the dead. '
        'At whose coming all men shall rise again with their bodies; '
        'And shall give account of their own works. '
        'And they that have done good shall go into life everlasting, and they that '
        'have done evil into everlasting fire.\n\n'
        'This is the catholic faith, which except a man believe faithfully, he cannot '
        'be saved.'
    ),
}


_chalcedon: Final[CreedDict] = {
    'title': 'The Chalcedonian Definition',
    'description': (
        'Therefore, following the holy fathers, we all with one accord teach '
        'men to acknowledge one and the same Son, our Lord Jesus Christ, at once '
        'complete in Godhead and complete in manhood, truly God and truly man, '
        'consisting also of a reasonable soul and body; of one substance with the '
        'Father as regards his Godhead, and at the same time of one substance with us '
        'as regards his manhood; like us in all respects, apart from sin; as regards '
        'his Godhead, begotten of the Father before the ages, but yet as regards his '
        'manhood begotten, for us men and for our salvation, of Mary the Virgin, the '
        'God-bearer; one and the same Christ, Son, Lord, Only-begotten, recognized in '
        'two natures, without confusion, without change, without division, without '
        'separation; the distinction of natures being in no way annulled by the union, '
        'but rather the characteristics of each nature being preserved and coming '
        'together to form one person and subsistence, not as parted or separated into '
        'two persons, but one and the same Son and Only-begotten God the Word, Lord '
        'Jesus Christ; even as the prophets from earliest times spoke of him, and our '
        'Lord Jesus Christ himself taught us, and the creed of the fathers has '
        'handed down to us.'
    ),
}


_nicene_325: Final[CreedDict] = {
    'title': 'The Nicene Creed (325 AD)',
    'description': (
        'We believe in one God, the Father Almighty, Maker of all things visible and '
        'invisible.\n\n'
        'And in one Lord Jesus Christ, the Son of God, begotten of the Father the '
        'only-begotten; that is, of the essence of the Father, God of God, Light of '
        'Light, very God of very God, begotten, not made, being of one substance with '
        'the Father; by whom all things were made both in heaven and on earth; who for '
        'us men, and for our salvation, came down and was incarnate and was made man; '
        'he suffered, and the third day he rose again, ascended into heaven; from '
        'thence he shall come to judge the quick and the dead.\n\n'
        'And in the Holy Ghost.\n\n'
        'But those who say: "There was a time when he was not;" and "He was not before '
        'he was made;" and "He was made out of nothing," or "He is of another '
        'substance" or "essence," or "The Son of God is created," or "changeable," or '
        '"alterable"—they are condemned by the holy catholic and apostolic Church.'
    ),
}


_nicene_381: Final[CreedDict] = {
    'title': 'The Nicene Creed (381 AD)',
    'description': (
        'We believe in one God, the Father Almighty, Maker of heaven and earth, and of '
        'all things visible and invisible.\n\n'
        'And in one Lord Jesus Christ, the only-begotten Son of God, begotten of the '
        'Father before all worlds (æons), Light of Light, very God of very God, '
        'begotten, not made, being of one substance with the Father; by whom all '
        'things were made; who for us men, and for our salvation, came down from '
        'heaven, and was incarnate by the Holy Ghost of the Virgin Mary, and was made '
        'man; he was crucified for us under Pontius Pilate, and suffered, and was '
        'buried, and the third day he rose again, according to the Scriptures, and '
        'ascended into heaven, and sitteth on the right hand of the Father; from '
        'thence he shall come again, with glory, to judge the quick and the dead; '
        'whose kingdom shall have no end.\n\n'
        'And in the Holy Ghost, the Lord and Giver of life, who proceedeth from the '
        'Father, who with the Father and the Son together is worshiped and glorified, '
        'who spake by the prophets. In one holy catholic and apostolic Church; we '
        'acknowledge one baptism for the remission of sins; we look for the '
        'resurrection of the dead, and the life of the world to come. Amen.'
    ),
}


_nicene_381_filioque: Final[CreedDict] = {
    'title': 'The Nicene Creed',
    'description': (
        'We believe in one God, the Father Almighty, Maker of heaven and earth, and of '
        'all things visible and invisible.\n\n'
        'And in one Lord Jesus Christ, the only-begotten Son of God, begotten of the '
        'Father before all worlds (æons), Light of Light, very God of very God, '
        'begotten, not made, being of one substance with the Father; by whom all '
        'things were made; who for us men, and for our salvation, came down from '
        'heaven, and was incarnate by the Holy Ghost of the Virgin Mary, and was made '
        'man; he was crucified for us under Pontius Pilate, and suffered, and was '
        'buried, and the third day he rose again, according to the Scriptures, and '
        'ascended into heaven, and sitteth on the right hand of the Father; from '
        'thence he shall come again, with glory, to judge '
        'the quick and the dead; whose kingdom shall have no end.\n\n'
        'And in the Holy Ghost, the Lord and Giver of life, who proceedeth from the '
        'Father and the Son, who with the Father and the Son together is worshiped and '
        'glorified, who spake by the prophets. In one holy catholic and apostolic '
        'Church; we acknowledge one baptism for the remission of sins; we look for the '
        'resurrection of the dead, and the life of the world to come. Amen.'
    ),
}


_shared_cooldown: Final = app_commands.checks.cooldown(
    2, 60.0, key=lambda itx: itx.user.id
)


class Creeds(
    GroupCog['Erasmus'], group_name='creed', group_description='Historic creeds'
):
    @app_commands.command()
    @_shared_cooldown
    async def apostles(self, itx: discord.Interaction, /) -> None:
        '''The Apostles' Creed'''

        await utils.send_embed(itx, **_apostles_creed)

    @app_commands.command()
    @_shared_cooldown
    async def athanasian(self, itx: discord.Interaction, /) -> None:
        '''The Athanasian Creed'''

        await utils.send_embed(itx, **_athanasian_creed)

    @app_commands.command()
    @_shared_cooldown
    async def chalcedon(self, itx: discord.Interaction, /) -> None:
        '''The Chalcedonian Definition'''

        await utils.send_embed(itx, **_chalcedon)

    @app_commands.command()
    @_shared_cooldown
    async def nicene(self, itx: discord.Interaction, /) -> None:
        '''The Nicene Creed'''

        await utils.send_embed(itx, **_nicene_381_filioque)

    @app_commands.command()
    @_shared_cooldown
    async def nicene325(self, itx: discord.Interaction, /) -> None:
        '''The Nicene Creed (325 AD)'''

        await utils.send_embed(itx, **_nicene_325)

    @app_commands.command()
    @_shared_cooldown
    async def nicene381(self, itx: discord.Interaction, /) -> None:
        '''The Nicene Creed (381 AD)'''

        await utils.send_embed(itx, **_nicene_381)


async def setup(bot: Erasmus, /) -> None:
    await bot.add_cog(Creeds(bot))
